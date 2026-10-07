---
title: "Mistral releases Mistral Large 4, a 1-trillion-parameter multimodal model"
description: "French lab Mistral AI has launched Mistral Large 4, a roughly 1T-parameter multimodal model it says is designed to compete with leading American and Chinese rivals."
pubDate: 2026-10-07T04:40:58+00:00
sourceUrl: "https://techcrunch.com/2026/10/06/mistrals-new-1t-model-aims-to-leapfrog-closed-and-open-rivals/"
sourceName: "TechCrunch"
tags: ["industry", "models"]
aiGenerated: true
---

On Tuesday, French AI lab Mistral AI released Mistral Large 4 (ML4), a multimodal model with 1 trillion parameters. Mistral pitches it as an alternative both to closed U.S. models and to open-weight models that mostly come from China. For now, though, only a gated public endpoint can access it. Mistral says it will release the weights in about three weeks, once safety testing is finished.

## What's new

ML4's size has earned it the nickname "Le Chonk." TechCrunch reports that Mistral wants the model to jump ahead of both American and Chinese competitors. That fits a framing French President Emmanuel Macron has used, calling Europe's approach a "third way" in AI.

At launch, ML4 is not an open-weight model. Mistral describes the current endpoint as having guardrails. Pierre Stock, Mistral's VP of Science, told TechCrunch that before the weights come out, the company will work with trusted partners and governments. The goal is to make sure the open weights can help defenders without enabling malicious attacks.

Stock also said Mistral trained the model entirely on its own compute, using 4,000 Nvidia GPUs. He called that "two to three times less than our Chinese competitors," and said it was well below what closed-model developers use. These figures come from Mistral and have not been independently checked.

Mistral says it tuned ML4 for a few specific areas:

- **Cybersecurity**
- **Finance**
- **Chip design**, a field central to two of its biggest backers. Dutch lithography company ASML led Mistral's Series C. Samsung led its Series D last month, at a valuation of €21 billion (about $24.39 billion).

## Why it matters

The release comes as the industry splits into two camps. One is closed models, whose providers can restrict or shut off access. TechCrunch points to a recent dispute over a U.S. government ban on some of Anthropic's most powerful models as an example. The other camp is open-weight models, and many of the most capable ones currently come from Chinese labs. A trillion-parameter open-weight model from a European company would give enterprises and governments another option, especially those concerned about sovereignty or vendor lock-in.

The model also matters for how Mistral is seen. The company recently began hosting Chinese models, which led some observers to ask whether it was turning into a plain inference provider. Mistral had already said that was not a pivot. With ML4, it is arguing that it still belongs among frontier labs that train their own top-tier models.

The staged release also says something about security. Stock said open weights are easier to audit, which matters to Mistral's core enterprise and institutional customers. Those customers are also increasingly worried that powerful models could be misused. The three-week delay is Mistral's attempt to address both concerns.

## Caveats

There is still a lot we don't know:

- **No benchmarks yet.** Mistral says it hopes ML4 will be the best open-weight model, especially outside China. It also thinks focused training could let ML4 beat closed models in some areas that matter to its customers. Neither claim can be tested until benchmark results come out.
- **Architecture details are missing.** The reporting gives the total parameter count but doesn't say whether ML4 uses a mixture-of-experts design or how many parameters are active per token. It also doesn't list which modalities the model handles, its context length, its pricing, or the license for the upcoming weights.
- **The release timeline could change.** The weights are tied to finishing safety testing and to work with partners and governments. It isn't clear what would happen if that testing turned up problems.
- **Running it won't be easy.** Even with open weights, a model this large will need serious infrastructure. Most organizations would likely use hosted versions rather than run it themselves.

The model's actual strength and openness will become clearer once independent evaluations appear and the weights are released.
