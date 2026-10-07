"""AINN publishing agent.

Scans news feeds, asks Claude to pick the most newsworthy unseen stories,
has Claude read each source (web_fetch) and write an original summary, then
saves it as a Markdown article for the Astro site.

Usage:
    python agent/ainn_agent.py             # publish up to AINN_MAX_ARTICLES (default 1)
    python agent/ainn_agent.py --max 3     # publish up to 3
    python agent/ainn_agent.py --dry-run   # list candidates only, no API calls
"""

from __future__ import annotations

import argparse
import calendar
import html
import json
import os
import re
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

import anthropic
import feedparser
import yaml

ROOT = Path(__file__).resolve().parent.parent
SOURCES_FILE = ROOT / "agent" / "sources.yaml"
SEEN_FILE = ROOT / "agent" / "state" / "seen.json"
ARTICLES_DIR = ROOT / "src" / "content" / "articles"

MODEL = os.environ.get("AINN_MODEL", "claude-opus-5-5")
EFFORT = os.environ.get("AINN_EFFORT", "medium")
LOOKBACK_HOURS = int(os.environ.get("AINN_LOOKBACK_HOURS", "48"))
MAX_CANDIDATES = 200
SEEN_LIMIT = 2000
# Server-side refusal fallback: if a safety classifier declines, the API
# re-runs the request on Anthropic's recommended fallback model.
FALLBACK_BETA = "server-side-fallback-2026-07-01"

SELECT_SYSTEM = """You are the editor of AINN (AI News Network): "AI News for AI by AI". \
AINN publishes short, accurate summaries of the news an AI would find worth knowing, \
for AI readers and curious humans. Coverage spans all domains, not just AI.

From the candidate list, choose the stories most worth covering today. Prefer stories \
with lasting informational value that change the state of the world or of knowledge:
- science and research results, discoveries, medical and health advances
- technology, computing and AI developments
- economics, markets and major business decisions
- geopolitics, policy, law and regulation with real consequences
- energy, climate, space and infrastructure

Prefer new facts, data and decisions over commentary, and global significance over local \
interest. Aim for variety: avoid picking several stories on the same topic unless they \
are exceptional.

Avoid: celebrity and entertainment gossip, sports results, lifestyle, routine crime, \
listicles, opinion pieces, promotional posts, minor updates, paywalled-looking items, \
and any story that duplicates one already published (see the recent titles) or another \
candidate. If nothing is worth covering, return an empty list.

For each pick, write a fresh, factual headline (no clickbait, max ~90 characters), a \
one-sentence description (max ~200 characters), a short lowercase-hyphenated slug, \
and 1-4 lowercase tags (e.g. world, science, technology, ai, economy, policy, health, climate, energy, space, security)."""

WRITE_SYSTEM = """You are a staff writer at AINN (AI News Network). You write clear, \
accurate, original news summaries for AI readers and curious humans. Be precise and \
information-dense: include the key facts, numbers, dates and named entities, define \
specialist terms briefly, and keep facts separate from claims and speculation.

First use the web_fetch tool to read the source URL you are given. Base the article \
only on what the source says plus widely known background context; never invent \
facts, numbers, quotes or dates.

Write 400-700 words of Markdown body text:
- Open with a 2-3 sentence lede stating what happened and why it matters.
- Then use 2-4 short sections with `##` headings (e.g. What happened, Why it matters, What's uncertain).
- Write in your own words. Do not copy sentences from the source; at most one short \
quotation (under 25 words), attributed.
- Note uncertainty or missing details honestly.
- Do not include the headline, front matter, a byline, or a source link; those are added separately.

If you cannot read the source (fetch error, paywall, empty page), reply with exactly \
`SKIP: <reason>` and nothing else."""

SELECT_SCHEMA = {
    "type": "object",
    "properties": {
        "picks": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "candidate_id": {"type": "integer"},
                    "title": {"type": "string"},
                    "description": {"type": "string"},
                    "slug": {"type": "string"},
                    "tags": {"type": "array", "items": {"type": "string"}},
                    "reason": {"type": "string"},
                },
                "required": ["candidate_id", "title", "description", "slug", "tags", "reason"],
                "additionalProperties": False,
            },
        }
    },
    "required": ["picks"],
    "additionalProperties": False,
}


class RefusalError(Exception):
    pass


# ---------- feeds ----------

def strip_html(text: str) -> str:
    text = re.sub(r"<[^>]+>", " ", text or "")
    return re.sub(r"\s+", " ", html.unescape(text)).strip()


def entry_time(entry) -> datetime | None:
    for key in ("published_parsed", "updated_parsed"):
        parsed = entry.get(key)
        if parsed:
            return datetime.fromtimestamp(calendar.timegm(parsed), tz=timezone.utc)
    return None


def collect_candidates(seen: set[str]) -> list[dict]:
    feeds = yaml.safe_load(SOURCES_FILE.read_text())["feeds"]
    cutoff = datetime.now(timezone.utc) - timedelta(hours=LOOKBACK_HOURS)
    candidates, urls = [], set()
    for feed in feeds:
        parsed = feedparser.parse(feed["url"], agent="AINN-bot/0.1 (+https://github.com)")
        if parsed.bozo and not parsed.entries:
            print(f"  ! {feed['name']}: could not parse feed ({parsed.get('bozo_exception')})")
            continue
        taken = 0
        for entry in parsed.entries:
            if taken >= feed.get("max_items", 8):
                break
            url = (entry.get("link") or "").strip()
            published = entry_time(entry)
            if not url or url in seen or url in urls:
                continue
            if published and published < cutoff:
                continue
            urls.add(url)
            taken += 1
            candidates.append({
                "source": feed["name"],
                "title": strip_html(entry.get("title", "")),
                "url": url,
                "published": published.isoformat() if published else None,
                "snippet": strip_html(entry.get("summary", ""))[:400],
            })
        print(f"  {feed['name']}: {taken} new")
    candidates.sort(key=lambda c: c["published"] or "", reverse=True)
    return candidates[:MAX_CANDIDATES]


# ---------- Claude ----------

def call_claude(client: anthropic.Anthropic, **kwargs):
    response = client.beta.messages.create(
        model=MODEL,
        betas=[FALLBACK_BETA],
        fallbacks="default",
        **kwargs,
    )
    if response.stop_reason == "refusal":
        category = response.stop_details.category if response.stop_details else None
        raise RefusalError(f"request declined (category={category})")
    return response


def select_stories(client, candidates: list[dict], recent_titles: list[str], max_picks: int) -> list[dict]:
    listing = "\n".join(
        f"[{i}] ({c['source']}, {c['published'] or 'date unknown'}) {c['title']}\n    {c['snippet']}"
        for i, c in enumerate(candidates)
    )
    recent = "\n".join(f"- {t}" for t in recent_titles) or "(none yet)"
    prompt = (
        f"Pick at most {max_picks} stories.\n\n"
        f"Recently published on AINN:\n{recent}\n\n"
        f"Candidates:\n{listing}"
    )
    response = call_claude(
        client,
        max_tokens=16000,
        system=SELECT_SYSTEM,
        output_config={"effort": EFFORT, "format": {"type": "json_schema", "schema": SELECT_SCHEMA}},
        messages=[{"role": "user", "content": prompt}],
    )
    text = next(b.text for b in response.content if b.type == "text")
    picks = json.loads(text)["picks"][:max_picks]
    valid = []
    for pick in picks:
        idx = pick["candidate_id"]
        if 0 <= idx < len(candidates):
            valid.append({**pick, "candidate": candidates[idx]})
    return valid


def write_article(client, pick: dict) -> str | None:
    c = pick["candidate"]
    prompt = (
        f"Headline: {pick['title']}\n"
        f"Source: {c['source']}\n"
        f"URL: {c['url']}\n\n"
        "Read the URL above with web_fetch, then write the article body."
    )
    messages = [{"role": "user", "content": prompt}]
    tools = [{"type": "web_fetch_20260209", "name": "web_fetch", "max_uses": 3}]
    for _ in range(4):  # resume server-tool loop on pause_turn
        response = call_claude(
            client,
            max_tokens=16000,
            system=WRITE_SYSTEM,
            output_config={"effort": EFFORT},
            tools=tools,
            messages=messages,
        )
        if response.stop_reason != "pause_turn":
            break
        messages = [messages[0], {"role": "assistant", "content": response.content}]
    if response.stop_reason == "max_tokens":
        print("    ! hit max_tokens, skipping")
        return None
    # Final text after the last tool result.
    texts, after_tools = [], False
    for block in response.content:
        if block.type in ("server_tool_use", "web_fetch_tool_result"):
            texts, after_tools = [], True
        elif block.type == "text":
            texts.append(block.text)
    body = "".join(texts).strip()
    if not after_tools:
        print("    ! source was not fetched, skipping")
        return None
    if not body or body.startswith("SKIP:"):
        print(f"    ! {body or 'empty response'}")
        return None
    return body


# ---------- output ----------

def slugify(text: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return slug[:60].rstrip("-") or "story"


def yaml_str(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)  # JSON strings are valid YAML


def save_article(pick: dict, body: str) -> Path:
    c = pick["candidate"]
    today = datetime.now(timezone.utc)
    base = f"{today:%Y-%m-%d}-{slugify(pick['slug'] or pick['title'])}"
    path = ARTICLES_DIR / f"{base}.md"
    n = 2
    while path.exists():
        path = ARTICLES_DIR / f"{base}-{n}.md"
        n += 1
    tags = sorted({slugify(t) for t in pick["tags"] if t.strip()})[:4]
    front = "\n".join([
        "---",
        f"title: {yaml_str(pick['title'])}",
        f"description: {yaml_str(pick['description'])}",
        f"pubDate: {today.isoformat(timespec='seconds')}",
        f"sourceUrl: {yaml_str(c['url'])}",
        f"sourceName: {yaml_str(c['source'])}",
        f"tags: [{', '.join(yaml_str(t) for t in tags)}]",
        "aiGenerated: true",
        "---",
    ])
    path.write_text(f"{front}\n\n{body}\n")
    return path


def recent_titles(limit: int = 30) -> list[str]:
    titles = []
    for path in sorted(ARTICLES_DIR.glob("*.md"), reverse=True)[:limit]:
        match = re.search(r'^title:\s*"?(.*?)"?\s*$', path.read_text(), re.M)
        if match:
            titles.append(match.group(1))
    return titles


def load_seen() -> list[str]:
    if SEEN_FILE.exists():
        return json.loads(SEEN_FILE.read_text()).get("urls", [])
    return []


def save_seen(urls: list[str]) -> None:
    SEEN_FILE.parent.mkdir(parents=True, exist_ok=True)
    SEEN_FILE.write_text(json.dumps({"urls": urls[-SEEN_LIMIT:]}, indent=2) + "\n")


# ---------- main ----------

def main() -> int:
    parser = argparse.ArgumentParser(description="AINN publishing agent")
    parser.add_argument("--max", type=int, default=int(os.environ.get("AINN_MAX_ARTICLES", "1")))
    parser.add_argument("--dry-run", action="store_true", help="list candidates only; no API calls")
    args = parser.parse_args()

    seen = load_seen()
    print("Scanning feeds...")
    candidates = collect_candidates(set(seen))
    print(f"{len(candidates)} candidate(s) in the last {LOOKBACK_HOURS}h.")
    if args.dry_run:
        for c in candidates:
            print(f"- [{c['source']}] {c['title']}\n  {c['url']}")
        return 0
    if not candidates:
        return 0

    api_key = os.environ.get("CLAUDE_API_KEY")
    if not api_key:
        print("CLAUDE_API_KEY is not set.")
        return 1
    client = anthropic.Anthropic(api_key=api_key)
    try:
        picks = select_stories(client, candidates, recent_titles(), args.max)
    except RefusalError as e:
        print(f"Selection declined: {e}")
        return 1
    print(f"Selected {len(picks)} stor{'y' if len(picks) == 1 else 'ies'}.")

    published = 0
    for pick in picks:
        url = pick["candidate"]["url"]
        print(f"- Writing: {pick['title']}\n    {url}")
        try:
            body = write_article(client, pick)
        except RefusalError as e:
            print(f"    ! declined: {e}")
            body = None
        except anthropic.APIStatusError as e:
            print(f"    ! API error {e.status_code}: {e.message}")
            continue  # leave unseen so it can be retried next run
        seen.append(url)  # don't retry stories we deliberately skipped
        if body:
            path = save_article(pick, body)
            published += 1
            print(f"    saved {path.relative_to(ROOT)}")
        time.sleep(1)

    save_seen(seen)
    print(f"Done. Published {published} article(s).")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except anthropic.AuthenticationError:
        print("Authentication failed: check CLAUDE_API_KEY.")
        sys.exit(1)
    except anthropic.RateLimitError:
        print("Rate limited by the API; try again later.")
        sys.exit(1)
    except anthropic.APIConnectionError:
        print("Network error talking to the Claude API.")
        sys.exit(1)
