---
title: "OpenAI releases 722 manuscripts of math results from unreleased frontier model"
description: "OpenAI published solutions to long-standing math problems from an internal model, spanning 372 result families, with Lean formalizations shared on GitHub."
pubDate: 2026-10-07T05:54:51+00:00
sourceUrl: "https://openai.com/index/sharing-ai-progress-in-mathematics"
sourceName: "OpenAI"
tags: ["ai", "science", "technology"]
aiGenerated: true
---

OpenAI has published 722 mathematical manuscripts that it says were produced by an unreleased internal "frontier" model. The papers, which tackle open research problems, are posted in a public GitHub repository along with partial computer-checked proofs and some notes on how the work was done. If the results hold up, this is the largest single batch of AI-generated research mathematics released so far. OpenAI also says that not all of the work has been verified.

## What happened

In a short post titled "Sharing AI progress in mathematics," OpenAI announced what it called a broad range of new results from an internal model. The company did not name the model. The manuscripts are in a repository called openai/math, released under the Apache-2.0 open-source license. According to the repository's README, the 722 manuscripts are grouped into 372 "families." Each family collects related papers, such as a main result, companion arguments, consequences or alternative proofs, and is labelled by mathematical field.

Many proofs come with formalizations in Lean. Lean is a programming language in which a mathematical proof can be written so that a computer checks every logical step. OpenAI says many manuscripts have been formalized but not all, and that it will add more formal proofs over time. It also says some of the unformalized results "could have issues" and that it will try to fix any problems quickly.

The repository includes abridged summaries of the model's reasoning for 10 result families. Their titles point to well-known topics, including:

- the irrationality exponent of π
- the Mahler conjectures
- Kaplansky's direct-finiteness conjecture in characteristic two
- quasipolynomial bounds for arithmetic progressions
- the isomorphism problem for free group factors
- spontaneous magnetization in the quantum Heisenberg ferromagnet
- the three-dimensional relativistic Vlasov–Maxwell system

The titles name the topics. They do not say how much of each problem the model claims to have settled.

## How the results were produced

OpenAI says it began testing its models on open research problems because they had saturated, or maxed out, its existing math benchmarks. The model was given about 4,000 problems over the course of the evaluation. OpenAI then grouped the outputs into families and kept only work it judged significant enough. It has not published the exact criteria for that filter.

According to OpenAI, the average result took compute equal to about three hours of ChatGPT Pro "thinking." Most results came from the same fixed procedure, with two stated exceptions:

- work on a zero-free region for the Riemann zeta function
- a proof of the Hodge Conjecture for CM abelian varieties, a special class of geometric objects

Humans also edited the write-up of the zeta-function result, which concerns the region where the real part of s is greater than 11/12, to make it easier to read. Some outputs build on results the models produced earlier.

## Why it matters

OpenAI says it consulted the independent Advisory Group on Mathematics and Artificial Intelligence at the Institute for Advanced Study on how to release AI-generated results, and followed that group's public recommendations. The repository sets out rules for revisions and citations: corrections will appear as new versions, earlier versions will stay accessible, and each manuscript comes with its own BibTeX citation entry. OpenAI says it is still looking for community-hosted alternatives to GitHub that meet the advisory group's guidelines.

The company also says it will fund workshops, conferences and special programs to help mathematicians understand major AI-produced results, with details to come. It says it is working to "responsibly release" the model behind the work but gave no timeline.

## What's uncertain

The main open question is how many of the results are correct and new. OpenAI itself says the collection mixes results at different stages of verification. Without Lean proofs, papers on deep open problems will need expert human review, and 722 manuscripts is a lot to review. OpenAI has not said how many manuscripts are fully formalized. It has also not said whether independent mathematicians have checked the most striking claims, such as the Hodge Conjecture case.

The roughly 4,000 problems attempted give some sense of the selection rate. Because significance was judged internally, though, outsiders can't yet tell how often the model failed or produced flawed work. Other details are also missing: the model's name and capabilities, and how the compute figures translate into actual cost.
