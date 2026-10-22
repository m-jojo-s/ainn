---
title: "China-aligned hackers used AI agents to breach thousands of ConnectWise customers"
description: "Microsoft attributes the ConnectWise breach to a China-aligned group that used AI agents to rapidly compromise thousands of the IT firm's customers."
pubDate: 2026-10-22T17:53:15+00:00
sourceUrl: "https://techcrunch.com/2026/10/22/chinese-hackers-spied-on-thousands-of-companies-after-breaching-it-giant-connectwise/"
sourceName: "TechCrunch"
tags: ["security", "technology", "world"]
aiGenerated: true
---

Microsoft says hackers aligned with the Chinese state broke into ConnectWise's cloud backup service, an IT management and remote-access company. They stole application credentials and used them to get into the Microsoft-hosted email and files of about 2,250 of ConnectWise's corporate customers. Microsoft's researchers say AI agents made the attack unusually fast: almost 3,000 attempted sign-ins per minute. They warn that this pace leaves defenders very little time to react.

## What happened

TechCrunch reported the findings on October 22, 2026. They come from a Microsoft security research post published a day earlier. Microsoft says the attackers first got into ConnectWise's cloud backup product. Corporate customers use this service to back up their company data. Inside it, the intruders found application credentials, the machine-to-machine secrets that let ConnectWise's service connect to each customer's environment.

With those credentials, the hackers could sign in to customers' Microsoft-hosted tenants as if they were an authorized user. A tenant is an organization's own space within Microsoft's cloud. From there, they could read emails and other files. Because the stolen credentials belonged to a trusted connection, the access probably looked legitimate.

ConnectWise has paused access to its cloud backup system while it investigates. As of Thursday, the company said it was working to restore the service.

## The AI angle

Microsoft linked the speed of the attack to AI agents, meaning software that can carry out multi-step tasks with little human direction. Specifically, it pointed to ARTEX, which TechCrunch describes as an open-source framework that pairs with AI models to stress-test cyber defenses. Like many offensive security tools, it was built for defenders but can also be used by attackers.

ARTEX has appeared in a real attack before. TechCrunch notes it was used in a recent compromise of South Korean financial systems. CrowdStrike researched that incident, and the title of its report credits the attack to an unknown threat actor. Local reporting said many of the targeted Korean institutions had weak security and lacked multi-factor authentication.

Microsoft summed up the risk of this kind of automation by saying it gives defenders "little time to detect and respond."

## Why it matters

This is a supply-chain attack: instead of targeting each victim directly, the attackers broke into one vendor and used its trusted connections to reach that vendor's customers. ConnectWise sells remote-access and IT management software, much of it to managed service providers (MSPs), which run IT for many other businesses. That makes it a valuable target, because one breach can open doors to thousands of organizations.

The incident also suggests that AI-driven automation is starting to matter in real state-linked operations, not just in theory. Stolen credentials have always been dangerous. AI agents appear to shorten the time between getting credentials and using them across a whole customer base. Security teams that rely on spotting and stopping suspicious logins by hand may struggle at that speed.

## What's still unclear

The TechCrunch report is short and leaves many questions open:

- **Initial access:** It doesn't explain how the hackers first got into ConnectWise's backup service, or when.
- **Scope:** It says about 2,250 organizations were hacked. It's unclear whether that counts confirmed data access or broader compromise, and how many backup customers were exposed in total.
- **Data taken:** It doesn't say what information was actually stolen, or which sectors and countries the victims are in.
- **Attribution details:** Microsoft calls the group China state-aligned. The web address of Microsoft's post appears to refer to the group by its tracking name, Storm-0940. Neither ConnectWise nor Chinese authorities have publicly commented on the attribution, according to the report.
- **Customer guidance:** It doesn't say whether ConnectWise has rotated, or told customers to rotate, the affected credentials, or when the backup service will come back.

The breach comes during what TechCrunch called an already bad week for cybersecurity. More details are likely as ConnectWise's investigation continues and affected organizations review their logs.
