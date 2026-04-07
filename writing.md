# Writing

This file is the active drafting workspace for the survey on game benchmarks for LLMs and VLM agents. `outline.md` is the canonical section map. `paper_cards/` and `corpus/registry/benchmark_registry.csv` remain the evidence layer. Use this file to track section status, claim plans, draft prose, and evidence gaps.

## Working Rules

- Draft only from `card-reviewed` or `finalized` cards unless a sentence is explicitly marked as a placeholder or open question.
- Keep comparative synthesis separate from raw evidence extraction. If a claim cannot be traced to reviewed cards, do not smooth it over.
- When drafting exposes a gap, record it here and send the work back to the registry or paper-card workflow instead of guessing.
- Update this file when a section changes status, gains enough evidence, or becomes blocked.

## Section Status Vocabulary

- `not-started`: no active drafting work yet
- `planning`: section claim plan exists but prose is still thin
- `drafting`: prose is actively being written from reviewed cards
- `needs-evidence`: blocked by missing reviewed cards or unresolved conflicts
- `ready-for-revision`: a coherent draft exists and should be tightened
- `stable`: section is reusable with only light future edits expected

## Narrative Spine

- Level 1: Rule Following — Can it make legal moves? (SmartPlay, GTBench)
- Level 2: Strategic Reasoning — Can it think effectively? (PokerBench, DSGBench)
- Level 3: Social Intelligence — Can it cooperate and deceive? (Werewolf Arena, WOLF)
- Level 4: Visual Agency — Can it play like a human? (BALROG, VideoGameBench)
- Level 5: Cross-Game Generalization — Can it play anything? (Orak, GameVerse, AI GAMESTORE)

## Section Tracker

| Section | Status | Current evidence base | Next move |
| :--- | :--- | :--- | :--- |
| 0. Why game as benchmark | planning | B01 and B03 reviewed; B05 mixed | Draft the core motivation paragraph from `SmartPlay`, `GTBench`, `BALROG`, `AIGameStore`, and `MCU`, then patch historical bridges after more precursor reviews. |
| 1. Historical evolution of game benchmarks | planning | B01 and B07 reviewed; B05, B10, B12 mixed | Build the historical skeleton first, then tighten the early-to-open-ended transition after `Crafter`, `InteractiveFictionGames`, `NetHackLearningEnvironment`, and `HumanLevelDiplomacy` are fully reviewed. |
| 2. Taxonomy of game benchmarks | planning | Broad reviewed coverage plus a few mixed edge cases | Draft the table schema and the five-level narrative mapping, then fill edge-case contrasts from mixed batches. |
| 3. Purpose: What game benchmarks actually measure | planning | B01, B02, B03, B10, B12 reviewed or mixed | Draft capability-target subsections now, then patch social and memory gaps after pending B02, B10, and B12 reviews. |
| 4. Paradigm: how models are allowed to play | planning | B03, B08, B09, B10, B13 reviewed or mixed | Draft the interface taxonomy and privileged-vs-ecological trade-off, then sharpen methodology contrasts after B08 review. |
| 5. Evaluation protocols | planning | B01, B03, B04, B08, B13 reviewed or mixed | Draft the score and calibration comparison, then tighten the methodology section after `TextArena` and the `clembench` line are fully reviewed. |
| 6. Synthesis: what current models still fail at | planning | B01, B02, B03, B10, B13 reviewed or mixed | Build the failure-mode skeleton from reviewed anchors, then revisit once the open-world and social mixed batches are upgraded. |
| 7. Open problems for next-generation game benchmarks | planning | B03, B05, B08, B10, B12 reviewed or mixed | Draft the forward-looking agenda after the generalization, methodology, and collaboration batches have cleaner reviewed support. |

## 0. Why game as benchmark

- Draft goal: explain why games provide dynamic, multi-step, interactive, strategically rich, and comparatively contamination-resistant benchmark settings.
- Likely reviewed anchors: `SmartPlay`, `GTBench`, `BALROG`, `AIGameStore`, `MCU`.
- Open gaps: early historical precursors still need stronger reviewed support before the framing section can make a clean lineage claim.

## 1. Historical evolution of game benchmarks

- Draft goal: trace the shift from formal rule-grounded containers to diagnostic probes, ecological agent benchmarks, and open-ended challenge spaces.
- Likely reviewed anchors: `SmartPlay`, `GTBench`, `GameBench`, `BALROG`, `Orak`, `AIGameStore`.
- Open gaps: `InteractiveFictionGames`, `NetHackLearningEnvironment`, `Crafter`, and `HumanLevelDiplomacy` should be reviewed more cleanly before this section is treated as stable.

## 2. Taxonomy of game benchmarks

- Draft goal: define the design-space axes and map the five narrative levels onto environment structure, world structure, scope, modality, and intent.
- Likely reviewed anchors: `SmartPlay`, `BotzoneBench`, `BALROG`, `GameVerse`, `Orak`, `GVGAI-LLM`, `DSGBench`, `KORGym`.
- Open gaps: edge cases in mixed batches should be checked before locking the final table wording.

## 3. Purpose: What game benchmarks actually measure

- Draft goal: classify benchmarks by capability target and explain why games are a credible medium for each capability.
- Likely reviewed anchors: `SmartPlay`, `GTBench`, `WerewolfArena`, `LLMHanabi`, `BALROG`, `FlashAdventure`, `TextQuests`, `StarDojo`.
- Open gaps: pending B02, B10, and B12 cards still matter for cooperation, negotiation, and memory-heavy claims.

## 4. Paradigm: how models are allowed to play

- Draft goal: compare observation channels, action channels, scaffolds, and ecological-validity trade-offs.
- Likely reviewed anchors: `BALROG`, `GameplayQA`, `StarBench`, `VideoGameBench`, `V-MAGE`, `LLMPlayStarCraftII`, `Orak`.
- Open gaps: methodology-heavy reviews in B08 should be finished before freezing the interface comparison section.

## 5. Evaluation protocols

- Draft goal: compare win rate, completion rate, milestone scoring, Elo or arena setups, human baselines, AI anchors, and contamination arguments.
- Likely reviewed anchors: `BotzoneBench`, `BoardGameArena`, `BALROG`, `GAMEBoT`, `KORGym`, `VMage`, `StarCraftIIArena`.
- Open gaps: the `clembench` and `TextArena` line still needs cleaner reviewed support for the broader methodology argument.

## 6. Synthesis: what current models still fail at

- Draft goal: synthesize recurring failure modes across rule tracking, partial observability, social reasoning, visual grounding, long-horizon consistency, and execution under time pressure.
- Likely reviewed anchors: `GTBench`, `BeyondScaling`, `WerewolfArena`, `BALROG`, `GameplayQA`, `FlashAdventure`, `TextAtari`, `StarDojo`.
- Open gaps: mixed open-world and collaboration cards should be upgraded before this section is treated as stable.

## 7. Open problems for next-generation game benchmarks

- Draft goal: propose benchmark-design directions around unified interfaces, calibration, multimodal social play, and open-ended generalization.
- Likely reviewed anchors: `AIGameStore`, `Orak`, `BALROG`, `GameVerse`, `KORGym`, `MCU`, `TeamCraft`.
- Open gaps: the open-ended, collaboration, and dialogue-game branches still need a few more reviewed anchors before the agenda is complete.
