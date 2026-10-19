---
title: "AI-generated proof of the quasi-Riemann hypothesis verified and unpacked by mathematicians"
description: "Human experts have worked through an AI-produced proof of the quasi-Riemann hypothesis, with one mathematician calling the implications \"staggering.\""
pubDate: 2026-10-19T19:05:35+00:00
sourceUrl: "https://www.quantamagazine.org/ai-proved-the-quasi-riemann-hypothesis-what-happens-now-20261019/"
sourceName: "Quanta Magazine"
tags: ["ai", "mathematics", "science"]
aiGenerated: true
---

Number theorists say a proof produced by an OpenAI model has settled the "quasi-Riemann hypothesis," a weaker version of what may be the most famous open problem in mathematics. According to Quanta Magazine, experts have spent the past two weeks taking the proof apart, and they largely agree that it holds up. If it does, a large body of results that until now depended on the unproven Riemann hypothesis would be established in one stroke.

## What happened

On October 6, 2026, OpenAI published a large batch of AI-generated mathematical results. The source gives two different figures for the batch: it calls it 377 results in one place and 722 papers in another, without explaining the difference. One of them claimed to prove the quasi-Riemann hypothesis. Stanford mathematician Jared Duker Lichtman called it "the most significant AI-for-math achievement so far, by quite a margin."

Some background helps. The Riemann zeta function is built from the infinite sum 1 + 1/2^s + 1/3^s + …, where s is a complex number, meaning a point on a plane. In 1859 Bernhard Riemann linked the points where this function equals zero to how the prime numbers thin out along the number line. His hypothesis says that all the "nontrivial" zeros lie on one vertical line, where the real part of s equals 1/2. It is the only problem on both David Hilbert's 1900 list and the Clay Mathematics Institute's Millennium Prize Problems. The first 12 trillion nontrivial zeros have been checked numerically, but nobody has proved that all of them sit on the line.

It has long been known that the zeros lie in a strip between 0 and 1. The quasi version asks for a proof that they fit inside a narrower strip. OpenAI released two versions:

- **September 30 version:** 199 pages. It puts all nontrivial zeros between 1/8 and 7/8, and it was formally verified in Lean, a programming language that machine-checks every step of a proof.
- **October 5 version:** 49 pages. It proves a weaker bound, between 1/12 and 11/12, and has not been formally verified.

Mathematicians have mostly studied the shorter paper. It appears to use similar techniques and has similar consequences. According to Quanta, it is the only paper in the batch that a human edited. OpenAI did not say who the editor was, and told the magazine only that the paper came from "everyone at OpenAI."

## Why it matters

NYU's Maksym Radziwiłł told Quanta that most consequences of the full hypothesis already follow from the quasi version. Those consequences reach into geometry and theoretical computer science as well as number theory.

What surprised experts was how the proof works. Princeton's Peter Sarnak has argued for decades that the zeta function should be studied as one member of a larger family of functions. The AI found a suitable family that people had missed. Rutgers mathematician Henryk Iwaniec came close to it in 2002. Building the family required metaplectic forms, a fairly obscure kind of object studied by Alexander Dunn of Georgia Tech. A formula Dunn and Radziwiłł proved in 2021 turned out to be a key ingredient.

Dunn described the proof as a synthesis of well-known ideas rather than something requiring new concepts. That runs against long-held expectations. Radziwiłł said specialists had assumed their tools were too weak and that the problem would need methods from a different branch of number theory. In his view, the model's apparent willingness to try the existing tools was the crucial step.

## What's uncertain

- **Readability:** Radziwiłł said both papers are so poorly written that a mathematical journal would reject them immediately.
- **Peer review:** Radziwiłł says he can now sketch the argument in half a page. Other experts' write-ups run 7 to 13 pages but are circulating privately and have not been published. Sarnak is devoting a course he teaches this semester to the proof. He said he won't consider it a theorem until humans have checked and understood every detail.
- **Verification is split:** The Lean-checked paper is the long 7/8 version. The shorter paper that people are actually reading has not been machine-checked. A headline saying the result was "verified" covers both versions, so it needs that caveat.
- **The full hypothesis:** Will Sawin of Princeton doubts the new methods can narrow the bound all the way to 1/2, though he said he isn't certain. Thomas Bloom of the University of Manchester noted that experts would have said the quasi version was out of reach only weeks ago.
