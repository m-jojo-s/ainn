---
title: "Meta releases Muse Wonder, its first frontier AI model, behind a paid subscription"
description: "Meta launched Muse Wonder and Muse Wonder Full, larger models it says rival leading systems on coding and complex tasks, available only to paying subscribers of its Muse app."
pubDate: 2026-10-12T21:35:58+00:00
sourceUrl: "https://techcrunch.com/2026/10/12/meta-releases-its-first-frontier-model-muse-wonder/"
sourceName: "TechCrunch"
tags: ["ai", "technology"]
aiGenerated: true
---

Meta's Superintelligence Lab released two large language models on Monday, October 12, 2026: Muse Wonder and Muse Wonder Full. Meta calls them its first attempt at a frontier model, meaning a model built to compete with the most capable systems from rivals such as OpenAI and Anthropic. The launch makes Meta a direct competitor at the top tier of AI, and its pricing and access put it among the most expensive commercial models.

## What happened

The two Wonder models are bigger than Muse Spark, Meta's earlier model, which was designed to be lightweight and respond with little delay (low latency). Meta says the new models score higher on benchmarks and do better on complex tasks like coding.

The company's own testing, published in a model card (a technical document describing a model's abilities and limits), puts Wonder and Wonder Full roughly level with two competing models, Fable 5.1 and GPT-6 Astra. Meta's announcement calls the release "the next step on our scaling ladder and a major leap toward personal superintelligence."

The two models are sold in different ways:

- **Muse Wonder** is available through the Meta Model API, the paid service developers use to build the model into their own software. It costs $4.00 per million input tokens and $20.00 per million output tokens. Tokens are the small chunks of text that models read and write. TechCrunch says that makes Wonder about as expensive as GPT-6 Sol or Opus 5.5.
- **Muse Wonder Full** will not be offered through the API. Only people who subscribe to Muse Code can use it.

Both models will also run Meta's Muse agent, an AI assistant that can carry out tasks for users.

## A focus on memory

Meta is especially promoting what it calls "active memory": the models' ability to hold on to information users give them and combine it later. This fits Meta's goal of building personal assistants that work on tasks over long periods.

As evidence, Meta points to MemoryBench, a published benchmark that tests continual learning (whether a system can keep learning from new information over time) and how well it stores memories. Meta says Muse Wonder now beats Fable, Opus and Astra on MemoryBench. In a launch video, Meta research scientist Kavya Kopparapu said the team worked hard to make the model remember what matters to users over "days, weeks, months and beyond."

## Why it matters

This is the first frontier model from Meta since Scale AI founder Alexandr Wang reorganized the company's AI work in August 2025. Since then, Meta has released Muse Spark and the Muse agent but held back from the kind of top-end launches OpenAI and Anthropic are known for. Muse Wonder is Meta's first attempt to compete with them directly.

Access is also a notable change. Meta built its earlier AI reputation largely on its Llama models, whose weights (the trained parameters that make up a model) it released publicly for anyone to download and run. With Muse Wonder, the strongest model is only available through a subscription, and the other is sold through a paid API. TechCrunch does not say whether Meta plans to release the weights of either model.

Meta says it trained the models at Prometheus, its data center in central Ohio, which started operating earlier in 2026.

## What's uncertain

- **Benchmarks:** All performance claims, including the MemoryBench results and the comparisons with Fable 5.1, GPT-6 Astra and others, come from Meta's own testing. No independent results were reported.
- **Wonder Full:** TechCrunch gives no price for a Muse Code subscription. It also does not explain how Wonder Full differs from Wonder in size or ability, or why Meta is keeping it off the API.
- **Technical details:** The report does not include model size, context window (how much text the model can handle at once), training data or safety testing results. These may be in Meta's model card but were not covered by TechCrunch.
- **Active memory:** It is unclear how Meta stores and uses personal information remembered over long periods. Meta has not said what privacy controls apply.
