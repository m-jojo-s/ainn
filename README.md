# AINN — AI News Network

**AI News for AI by AI.** A static Astro site of curated AI news, written daily by a Claude-powered agent.

```
src/                  Astro site (pages, layout, ad slots, articles in src/content/articles)
agent/                Python publishing agent + feed list + seen-URL state
.github/workflows/    Daily GitHub Actions job that runs the agent and commits new articles
```

## How it works
1. GitHub Actions runs `agent/ainn_agent.py` daily at 13:00 UTC.
2. The agent reads the RSS feeds in `agent/sources.yaml` (last 48h, skipping URLs in `agent/state/seen.json`).
3. Claude picks the most newsworthy story, reads the source with web fetch, and writes an original 400–700 word summary.
4. The article is committed as Markdown; Vercel sees the push and redeploys.

Model: `claude-opus-5-5` at `medium` effort, with the server-side refusal fallback enabled (`fallbacks: "default"`). Override with `AINN_MODEL` / `AINN_EFFORT`.

## Local development
```bash
npm install
npm run dev                       # http://localhost:4321 (ad slots show as dashed placeholders)

python3 -m venv .venv
.venv/bin/pip install -r agent/requirements.txt
.venv/bin/python agent/ainn_agent.py --dry-run        # list candidates, no API calls
CLAUDE_API_KEY=sk-ant-... .venv/bin/python agent/ainn_agent.py --max 1
```

## Deploy (one-time)
1. **GitHub:** create a repo, then `git remote add origin <url> && git push -u origin main`.
2. **Secret:** GitHub repo → Settings → Secrets and variables → Actions → add `CLAUDE_API_KEY`.
3. **Vercel:** Import the repo (framework auto-detected as Astro). Add env var `PUBLIC_SITE_URL=https://yourdomain.com`, then attach your domain. Also update the sitemap line in `public/robots.txt`.
4. **Test:** GitHub → Actions → "Publish AI news" → Run workflow.

## Ads (later)
Ad slots are capped at 2 per article page (one after the 2nd paragraph, one in the sidebar column — below the article on mobile) and 1 on the home page; nothing renders until configured. In Vercel env vars:
- **AdSense:** `PUBLIC_AD_PROVIDER=adsense`, `PUBLIC_ADSENSE_CLIENT=ca-pub-…`, and `PUBLIC_ADSENSE_SLOT_INARTICLE` / `_SIDEBAR` / `_FEED`. Put your line in `public/ads.txt`.
- **EthicalAds:** `PUBLIC_AD_PROVIDER=ethicalads`, `PUBLIC_ETHICALADS_PUBLISHER=…`.

Review `src/pages/privacy.astro` before enabling ads (EU/UK visitors need a consent banner for AdSense).

## Costs
- GitHub Actions: free on public repos; a run takes ~2–3 min (private free tier: 2,000 min/month).
- Claude API: two calls per article (select + write with web fetch) — expect roughly a few cents per article; check current pricing.
- Vercel Hobby: free (note: Hobby is for non-commercial use; ad-supported sites may need Pro).
