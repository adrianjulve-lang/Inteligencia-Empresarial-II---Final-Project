# Agentic Intelligence for Strategic Decision-Making
## Oral Presentation — Final Project, Corporate Intelligence II
**50 Doctors México · Spanish Market Expansion · UFV 2026**

> Premium edition · 10 slides · ~15–18 min + Q&A
> Style: minimalist editorial, white canvas, obsidian black + cobalt blue + silver gray, Inter/Helvetica Neue
> Author: Pablo Cerezal & Adrián Julve · Prof. César Moreno Pascual, PhD

---

## Visual System (apply across all slides)

| Element | Specification |
|---|---|
| Background | Pure white `#FFFFFF` (or near-white `#FAFAFA` for body slides) |
| Primary text | Obsidian black `#0B0B0F` |
| Accent 1 | Deep Cobalt Blue `#0F3460` (titles, key numbers, line strokes) |
| Accent 2 | Silver Gray `#9AA0A6` (supporting text, captions, secondary lines) |
| Highlight | Use cobalt **only** to spotlight the single most important metric per slide |
| Typography | Inter or Helvetica Neue · titles 36–44 pt · body 18–22 pt · line-height 1.45 |
| Diagrams | Hairline strokes (1–1.5 pt), pure geometric shapes, generous negative space (≥40%) |
| Density rule | Maximum 6 visual elements per slide. If you need a 7th, split the slide. |
| Slide numbering | Bottom right, silver gray, 10 pt, format `01 / 10` |

---

# SLIDE 01 — COVER

**Executive Title:** *From Information to Action: An Agentic Intelligence System for Cross-Border Market Entry*

**Content**
- 50 Doctors México — Expansion Decision into Spain
- Multi-agent architecture replacing 6 weeks of analyst work with a 90-second pipeline
- Verdict produced by the system: **CONDITIONAL GO** · Confidence 72%
- Pablo Cerezal · Adrián Julve · UFV · 2026

**Design Suggestion**
Full-bleed white canvas. Title set in 44 pt Inter Light, left-aligned, occupying the upper third. A single thin cobalt horizontal rule (1.5 pt, 280 px wide) below the title. Bottom-left: a 3-line block in silver gray with the four content bullets, 18 pt. Bottom-right: a small geometric mark — three concentric circles (perception → reasoning → action) in cobalt hairlines, no fill. No logos. No images. Negative space dominates the right two thirds.

**Speaker Notes**
Good morning. Over the next fifteen minutes I will walk you through how we built an agentic intelligence system to support a real strategic decision: whether 50 Doctors México should enter the Spanish private healthcare market. The output you will see — a Conditional Go with 72% confidence and a quantified Net Present Value — was not produced by us writing a memo. It was produced by four cooperating AI agents that perceive, reason, and act on real evidence. The point of this presentation is not to demo a chatbot; it is to show you the architectural shift from generative AI to agentic AI, and why that shift changes what executive decision-making looks like.

---

# SLIDE 02 — THESIS

**Executive Title:** *Generative AI Answers Questions. Agentic AI Closes Decisions.*

**Content**
- Generative AI: a single-turn oracle — produces text on demand, no state, no goals
- Agentic AI: a goal-directed system — plans, acts, observes, replans until a decision is closed
- The leap is not model size; it is the **control loop** wrapped around the model
- For executives, this changes the unit of value from *answers* to *resolved decisions*

**Design Suggestion**
Two-column layout, separated by a single vertical hairline (1 pt, silver gray) running from top to bottom. Left column: the word "GENERATIVE" in 28 pt cobalt, followed by a stylised speech bubble icon (hairline only) and the bullet "Stateless · Reactive · Single-shot". Right column: the word "AGENTIC" in 28 pt cobalt, followed by a closed-loop arrow icon (hairline only) and the bullet "Stateful · Proactive · Multi-step". At the bottom, centred across both columns: a single sentence in 22 pt black — *"The model is the engine. The agent is the vehicle."*

**Speaker Notes**
The first thing to understand is what we mean by agentic. A generative model — GPT, Claude, any of them — answers a single question and forgets. It is brilliant, but it is a one-shot oracle. An agentic system wraps that same model inside a control loop: it sets a goal, it plans the steps to reach it, it executes those steps using tools, it observes the result, and it decides whether to continue or stop. The intelligence is not in the model alone; it is in the loop. For an executive, the consequence is concrete: instead of receiving an answer that you then have to operationalise, you receive a decision that has already been operationalised. That is a different category of artefact.

---

# SLIDE 03 — CORE ARCHITECTURE

**Executive Title:** *Three Capabilities, One Closed System: Perception · Reasoning · Action*

**Content**
- **Perception** — ingests structured and unstructured signals (filings, BOE, LinkedIn, alt-data)
- **Reasoning** — frames the problem, applies domain frameworks (AMC, Shell, ECOMO), weighs evidence
- **Action** — writes outputs, triggers tools, escalates alerts, updates the decision record
- All three loop back: every action produces new perception that refines reasoning

**Design Suggestion**
Centred composition. Three perfect circles arranged horizontally, each 120 px wide, hairline cobalt outline, no fill. Inside each circle, a single word in 18 pt black: PERCEPTION · REASONING · ACTION. Connect the circles with two short cobalt arrows (1.5 pt) running left-to-right, plus a third long arrow at the bottom curving from ACTION back to PERCEPTION to close the loop. Below the diagram, a single 16 pt silver gray caption: *"Each loop iteration narrows uncertainty."* Title at top, left-aligned, 36 pt.

**Speaker Notes**
Every agentic system, regardless of domain, decomposes into the same three capabilities. Perception is the system's senses — it must be able to read the world, not just respond to a prompt. Reasoning is where the domain frameworks live; in our case the agents apply Chen and Miller's AMC, the Shell scenario method, and the ECOMO valuation logic — the same frameworks an analyst would use, but executed at machine speed. Action is the part most people forget: a system that only thinks is not agentic. It must change something — produce a document, trigger an alert, escalate to a human. And critically, the loop closes: every action generates fresh perception, which feeds back into the next reasoning cycle. That is what makes the system improve itself over time.

---

# SLIDE 04 — THE THINKING LOOP

**Executive Title:** *Decomposition Is the Hidden Multiplier of Agent Quality*

**Content**
- Top-level goal: *"Decide whether to enter Spain"* — too coarse for any single model call
- The agent decomposes into sub-goals: identify competitors → score reactions → simulate scenarios → value the decision
- Each sub-goal becomes its own plan-execute-observe cycle, with explicit success criteria
- Failure of one sub-goal triggers replanning, not failure of the system

**Design Suggestion**
Vertical tree diagram, hairline strokes only. At the top, a single rounded rectangle (cobalt outline, no fill) containing the goal *"Decide market entry"*. Below it, four child rectangles connected by thin vertical lines: *"Map competitors"*, *"Score AMC"*, *"Simulate scenarios"*, *"Value options"*. Below each child, three small grey dots (•••) representing further decomposition that we do not need to expand. Right-hand margin: a 14 pt cobalt callout — *"Plan → Act → Observe → Replan"* — vertically stacked, one verb per line, with hairline arrows between them.

**Speaker Notes**
A model is only as good as the question you ask it. The hardest engineering work in an agentic system is not prompting — it is decomposition. Our top-level goal, *decide whether to enter Spain*, is far too coarse for any single language-model call. The agent has to break it down recursively until each leaf is small enough to be solved with high confidence. We end up with a tree of sub-goals, each with its own plan-act-observe-replan cycle. The benefit, beyond reliability, is that when one branch fails — say, a data source returns nothing — the system replans only that branch instead of collapsing the whole decision. That is what gives agentic systems their robustness.

---

# SLIDE 05 — TOOLS AND THE EXTERNAL WORLD

**Executive Title:** *An Agent Without Tools Is a Brain in a Jar*

**Content**
- Web fetch and search — official registries (CNMC, BOE, Sanitas IR), news, regulatory filings
- Structured APIs — financial data, employment signals, alternative data
- Internal artefacts — JSON evidence files, decision records, the project repo itself
- The agent chooses *which* tool to invoke based on the sub-goal — tool selection is itself a reasoning step

**Design Suggestion**
Centred hexagon with the word AGENT in 22 pt cobalt at the centre. Six hairline lines radiate outward at 60-degree intervals to six small labelled boxes (each 80 × 30 px, hairline outline): *Web*, *News API*, *Filings*, *LinkedIn*, *Repo*, *JSON store*. Use silver gray for the radiating lines, cobalt for the central hexagon outline. Bottom-right corner: a single 14 pt italic line in silver — *"In our system: 12 verified sources across 4 tool categories."* Maintain ≥45% white space.

**Speaker Notes**
A frequent misconception is that agents reason in a vacuum. They do not. Their power comes from the tools they can invoke — and choosing the right tool is itself a reasoning step. In our system the agent has access to four categories of tools: open-web fetching for news and competitor pages, structured APIs for financial and employment data, alternative-data feeds for weak signals, and the project's own repository as a memory store. Twelve verified sources, all traceable. When the agent decides to score Sanitas's likelihood of reaction, it does not invent the answer — it pulls the relevant filings, the recent news, and the LinkedIn hiring patterns, and only then runs the AMC framework. Evidence first, judgement second.

---

# SLIDE 06 — MEMORY

**Executive Title:** *Short-Term for Reasoning. Long-Term for Compounding Intelligence.*

**Content**
- **Short-term memory** — the working context inside a single decision cycle (sub-goals, intermediate results, tool outputs)
- **Long-term memory** — the persisted artefacts (JSON evidence, decision records, KIIs, signposts) that survive across runs
- Long-term memory is what turns a one-shot analysis into an Early Warning System that improves weekly
- Without persistence, every executive question starts from zero — the analyst's curse

**Design Suggestion**
Two-panel layout. Left panel — labelled SHORT-TERM in 16 pt cobalt — contains a small clock icon (hairline) and a stack of three light-grey rectangles representing transient context. Right panel — labelled LONG-TERM in 16 pt cobalt — contains a vault icon (hairline only, no fill) and a dense grid of 6 × 4 small dots representing accumulated facts. A horizontal hairline cobalt arrow points from the left panel to the right panel, labelled *"Distillation"* in 12 pt italic. Single bold line at the bottom in 22 pt black: *"In our project: weekly EWS run + persistent KII state = compounding intelligence."*

**Speaker Notes**
Memory is what most demonstrations skip — and it is what separates a toy from a system. Short-term memory holds the agent's working context within a single decision cycle: the current sub-goal, the partial results, the tools it has already called. That memory dissolves when the cycle ends. Long-term memory is different: it persists across runs. In our project, the long-term store is the repository itself — the JSON evidence files, the decision records, the nine KIIs of the Early Warning System. This is what allows our system to do something an analyst cannot: it runs every Monday morning via GitHub Actions, compares the world today against what it knew last week, and only escalates when something has actually changed. The intelligence compounds.

---

# SLIDE 07 — USE CASE I · OPERATIONAL OPTIMISATION

**Executive Title:** *Six Weeks of Analyst Work, Compressed into Ninety Seconds*

**Content**
- Task: full competitive intelligence sweep on Sanitas, Adeslas, Asisa — AMC scoring, sources, P(response)
- Manual baseline: ≈ 240 analyst-hours, 6 weeks, single point-in-time snapshot
- Agentic execution: 90 seconds per run, fully reproducible, weekly refresh — *audit trail included*
- Result: **Sanitas P(response) = 87%** in 3–6 months — drove the alliance recommendation

**Design Suggestion**
Horizontal timeline, hairline cobalt baseline running across the slide. Two markers on the timeline: a long bar (40% of width) on the left labelled *"6 weeks · manual"* in silver gray, and a single dot on the right labelled *"90 s · agentic"* in cobalt. Below the timeline, a small 3-row table with hairline borders showing: *Hours · Cost · Refresh frequency* for each approach. Top-right corner: the hero metric **87%** in 56 pt cobalt with a 14 pt caption *"Sanitas P(response), validated against 12 sources"*.

**Speaker Notes**
This is the first concrete use case, and it is the easiest one for a board to grasp. We asked the system to do what a junior analyst typically does: build a competitive intelligence file on the three Spanish private health insurers, score them with the Awareness-Motivation-Capability framework, and estimate the probability and timeline of their reaction to 50 Doctors's entry. A manual version of this work, done properly, takes around six weeks and gives you a snapshot that is already stale by the time it lands on the desk. Our agent does it in ninety seconds, with the same twelve sources cited, and — this is the key — it can be rerun every Monday. The output is not a report; it is a living instrument. The headline number on the right, 87%, is the probability that Sanitas will respond within three to six months. That single number changed the entire entry strategy from confrontation to alliance.

---

# SLIDE 08 — USE CASE II · AUTONOMOUS DECISION SUPPORT

**Executive Title:** *From Indicators to Actions, Without a Human in Between*

**Content**
- Early Warning System: 9 KIIs, 3 KITs, four-tier escalation protocol
- The agent classifies each KII as 🟢 / 🟡 / 🔴 against pre-agreed thresholds — no judgement call needed
- ≥ 2 reds → automatic strategic-review trigger; ≥ 3 reds → CapEx suspension recommendation
- Verdict produced by the system: **CONDITIONAL GO**, E[NPV] = **+€14.2M**, Confidence **72%**

**Design Suggestion**
Centre stage: a 4-step staircase rising left-to-right, hairline cobalt strokes, each step labelled with the alert level (🟢 nominal · 🟡 alert · 🔴 escalate · 🔴🔴 strategic review). A small dot indicating *current state* sits on the first step (🟢), with a hairline arrow pointing forward to suggest movement. Right edge, vertically: three stacked metrics in 36 pt cobalt with 12 pt silver labels — **+€14.2M** *E[NPV]* · **72%** *Confidence* · **9/9** *KIIs green*. Title at top, left-aligned. No other content.

**Speaker Notes**
The second use case is more ambitious because it removes the human from the routine loop. The Early Warning System monitors nine indicators across three Key Intelligence Topics — competitor receptivity, regulation, and Latin-American movements. Each indicator has a pre-agreed threshold, defined in the strategy document and signed off by the team. The agent runs every Monday, checks each indicator against its threshold, and assigns a colour. If two or more turn red, it does not ask for permission — it triggers a strategic review automatically. If three turn red, it recommends suspending capital expenditure. Today, all nine are green, and the system's verdict is a Conditional Go with an expected NPV of plus fourteen point two million euros and a confidence level of seventy-two percent. The numbers are the system's, not ours.

---

# SLIDE 09 — GOVERNANCE AND SAFETY

**Executive Title:** *Autonomy Without Alignment Is Just Faster Failure*

**Content**
- **Human-in-the-loop** — the agent recommends, executives ratify; CapEx and contractual moves remain human-signed
- **Auditability** — every decision step is logged: source → reasoning → output, traceable line by line
- **Alignment** — explicit success criteria and pre-agreed thresholds; the agent does not redefine the goal
- **Boundaries** — read-only on production data, no autonomous spend, escalation paths defined

**Design Suggestion**
Two columns separated by a hairline vertical rule. Left column titled *AGENT AUTONOMY* with three small filled cobalt squares (40 × 40 px) representing tasks the agent owns: *Monitor · Score · Alert*. Right column titled *HUMAN AUTHORITY* with three hollow cobalt squares (hairline outline only) representing tasks reserved for humans: *Ratify · Sign · Override*. Bottom band, full width, in silver gray 14 pt: *"Every system action is logged. Every override is logged. Logs are version-controlled in the project repository."* Small lock icon (hairline) bottom-left.

**Speaker Notes**
Any executive who has worked with autonomous systems will ask the same question: what stops it from being wrong at scale? The answer has three parts. First, human-in-the-loop is not a slogan — it is a contract. The agent recommends; human executives ratify. Capital expenditure decisions and contractual commitments are never executed by the agent. Second, every step is auditable: the source, the reasoning step, the output, all version-controlled in the same repository as the code. If a decision turns out to be wrong, we can reconstruct exactly why. Third, alignment is enforced by structure, not hope: the success criteria and the alert thresholds were agreed in writing before the system ran, and the agent cannot redefine them mid-flight. Speed without these three guardrails is not an asset — it is a liability.

---

# SLIDE 10 — ROADMAP AND CLOSE

**Executive Title:** *The Decision Is Made. The Discipline Is Permanent.*

**Content**
- **Now (T0–T3 months):** Sanitas/BUPA CEO-to-CEO; weekly EWS runs; track Confidence 72% → target 85%
- **Mid-term (T3–T12):** GO conditions C1–C4 verified; signpost monitoring; first JV milestone
- **Long-term (T12–T36):** Hospital openings tracked against Roadmap KPIs; system extended to Latin-American expansion
- **Closing thesis:** Agentic systems do not replace strategic judgement. They institutionalise it.

**Design Suggestion**
Horizontal timeline, hairline cobalt, three milestones marked as small filled cobalt circles at 0, 12, and 36 months. Above each milestone, a 16 pt label: *Decision · First Hospital · Full Network*. Below the timeline, three short text blocks (one per phase) in 14 pt silver gray, ≤ 12 words each. At the very bottom, centred, the closing line in 28 pt black: *"They institutionalise it."* — with the word *institutionalise* in cobalt. Right corner: small QR code linking to the GitHub repository. Slide number `10 / 10` bottom-right in silver.

**Speaker Notes**
The decision in front of us — entering Spain through an alliance with Sanitas/BUPA — is a one-time act. But the discipline that produced this decision is permanent. The same agentic architecture that gave us a Conditional Go today will run every Monday for the next thirty-six months, comparing reality against the assumptions we signed off on, and warning us the moment one of them breaks. In twelve months we will know whether the first hospital is on track. In thirty-six months we will know whether the full network has been built or whether we should have stopped at hospital number two. None of that requires a new system. It only requires that we let this one keep running. Agentic systems do not replace strategic judgement; they institutionalise it. Thank you. I am happy to take your questions.

---

## Q&A CHEATSHEET (anchor numbers, English)

| Question | One-line answer |
|---|---|
| *Why Spain and not another EU market?* | Highest unmet premium-private supply gap + BUPA already operates in Mexico (information asymmetry collapses). |
| *Why an alliance and not a direct entry?* | E[NPV] direct = **−€3.5M** vs alliance = **+€14.2M**; Sanitas AMC P(response) = 87%. |
| *Why only 72% confidence?* | Three load-bearing assumptions (regulation 35%, insurer cooperation 40%, patient volume 45%); confidence reflects the joint hazard. |
| *What stops the agent from hallucinating?* | Twelve verified sources cited per output; every claim is traceable; human ratification gates all spend. |
| *What if Sanitas refuses?* | Hedging Action H2: parallel track with Adeslas (E[NPV] = +€4.6M); falls to defensive entry scenario. |
| *Why not just hire more analysts?* | 6 weeks → 90 s is a 1,400× speedup; the value is not cost — it is the weekly refresh that no analyst team can sustain. |
| *Could the system be wrong?* | Yes. That is why ≥ 2 red KIIs trigger automatic strategic review; the system is designed to detect its own errors. |

---

## DELIVERY NOTES

- **Total time target:** 15–18 minutes for the deck, leaving 5–7 minutes for Q&A.
- **Pacing:** Slides 1–2 fast (90 s each). Slides 3–6 are the technical heart (2 min each). Slides 7–8 are the demo handover (2 min each, plus optional live Streamlit demo). Slides 9–10 close (90 s each).
- **Live demo cue:** at the end of Slide 8, switch to the Streamlit app — module *Early Warning System* — and click the **🔴 KIT2 in RED** button. Watch the audience as the strategic-review banner appears in real time. That is the moment.
- **Three numbers you must say without notes:** **+€14.2M** (E[NPV] alliance) · **87%** (Sanitas P-response) · **72%** (Confidence). If you only remember three things on stage, remember these.
- **What never to say:** "AI-powered", "revolutionary", "next-generation". The deck earns its credibility through restraint.

---

*Document version: 2026-04-25 · Maintained by Pablo Cerezal · For UFV Corporate Intelligence II final defence.*
