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
| 0. Why game as benchmark | planning | B01, B03, and B05 reviewed | Draft the core motivation paragraph from `SmartPlay`, `GTBench`, `BALROG`, `AIGameStore`, `MCU`, and `Crafter`, then use `HumanLevelDiplomacy` as a high-ecology bridge example. |
| 1. Historical evolution of game benchmarks | planning | B01, B05, B07, B10, and B12 reviewed | Build the historical skeleton using `Crafter`, `InteractiveFictionGames`, `NetHackLearningEnvironment`, and `HumanLevelDiplomacy` as reviewed bridge papers. |
| 2. Taxonomy of game benchmarks | planning | Broad reviewed coverage across core and edge-case batches | Draft the table schema and five-level narrative mapping, then use `GridBasedGameCompetitions`, `clembench`, and `GTOWizardBenchmark` as edge-case contrasts. |
| 3. Purpose: What game benchmarks actually measure | planning | B01, B02, B03, B10, and B12 reviewed | Draft capability-target subsections using the newly reviewed social, memory, and collaboration cards alongside the existing anchors. |
| 4. Paradigm: how models are allowed to play | planning | B03, B08, B09, B10, and B13 reviewed | Draft the interface taxonomy and privileged-vs-ecological trade-off using the dialogue-game, open-world, and specialist-interface contrasts now in reviewed state. |
| 5. Evaluation protocols | planning | B01, B03, B04, B08, and B13 reviewed | Draft the score and calibration comparison using `TextArena`, the `clembench` line, `CollabOvercooked`, and `GTOWizardBenchmark` as methodology anchors. |
| 6. Synthesis: what current models still fail at | planning | B01, B02, B03, B10, B12, and B13 reviewed | Build the failure-mode skeleton from reviewed anchors spanning social, memory, collaboration, and specialist-calibration settings. |
| 7. Open problems for next-generation game benchmarks | planning | B03, B05, B08, B10, and B12 reviewed | Draft the agenda from the reviewed generalization, dialogue-game, open-world, and collaboration branches. |

## 0. Why game as benchmark

- Draft goal: explain why games provide dynamic, multi-step, interactive, strategically rich, and comparatively contamination-resistant benchmark settings.
- Likely reviewed anchors: `SmartPlay`, `GTBench`, `BALROG`, `AIGameStore`, `MCU`, `Crafter`, `HumanLevelDiplomacy`.
- Open synthesis focus: use the early precursor cards to bridge from formal containers to later ecological and open-ended benchmark claims without overstating direct comparability.

## 1. Historical evolution of game benchmarks

- Draft goal: trace the shift from formal rule-grounded containers to diagnostic probes, ecological agent benchmarks, and open-ended challenge spaces.
- Likely reviewed anchors: `SmartPlay`, `GTBench`, `GameBench`, `BALROG`, `Orak`, `AIGameStore`, `Crafter`, `InteractiveFictionGames`, `NetHackLearningEnvironment`, `HumanLevelDiplomacy`.
- Open synthesis focus: keep single-environment precursors, live-play milestones, and later benchmark suites distinct as the lineage broadens.

## 2. Taxonomy of game benchmarks

- Draft goal: define the design-space axes and map the five narrative levels onto environment structure, world structure, scope, modality, and intent.
- Likely reviewed anchors: `SmartPlay`, `BotzoneBench`, `BALROG`, `GameVerse`, `Orak`, `GVGAI-LLM`, `DSGBench`, `KORGym`, `GridBasedGameCompetitions`, `clembench`, `GTOWizardBenchmark`.
- Open synthesis focus: explain where dialogue-game frameworks, narrow prompt-format probes, and specialist anchor benchmarks sit relative to the main taxonomy.

## 3. Purpose: What game benchmarks actually measure

- Draft goal: classify benchmarks by capability target and explain why games are a credible medium for each capability.
- Likely reviewed anchors: `SmartPlay`, `GTBench`, `WerewolfArena`, `LLMHanabi`, `MulticulturalSpyfall`, `StrategicHanabi`, `BALROG`, `EMemBench`, `MineNPCTask`, `CollabOvercooked`, `LLMCoordination`, `TextQuests`, `StarDojo`.
- Open synthesis focus: separate cooperation, negotiation, memory, and mixed-initiative task execution rather than collapsing them into one generic social-intelligence bucket.

## 4. Paradigm: how models are allowed to play

- Draft goal: compare observation channels, action channels, scaffolds, and ecological-validity trade-offs.
- Likely reviewed anchors: `BALROG`, `GameplayQA`, `StarBench`, `VideoGameBench`, `V-MAGE`, `LLMPlayStarCraftII`, `Orak`, `TextArena`, `Clembench`, `Clembench2024`, `ThirdParadigm`, `MineNPCTask`, `GTOWizardBenchmark`.
- Open synthesis focus: contrast pure natural-language dialogue games, structured API interfaces, and open-world scaffolded play without flattening them into one interface family.

## 5. Evaluation protocols

- Draft goal: compare win rate, completion rate, milestone scoring, Elo or arena setups, human baselines, AI anchors, and contamination arguments.
- Likely reviewed anchors: `BotzoneBench`, `BoardGameArena`, `BALROG`, `GAMEBoT`, `KORGym`, `VMage`, `StarCraftIIArena`, `TextArena`, `Clembench`, `Clembench2024`, `ThirdParadigm`, `CollabOvercooked`, `GTOWizardBenchmark`.
- Open synthesis focus: separate living leaderboards, dialogue-game protocol design, process-level collaboration metrics, and fixed-anchor calibration into distinct evaluation families.

## 6. Synthesis: what current models still fail at

- Draft goal: synthesize recurring failure modes across rule tracking, partial observability, social reasoning, visual grounding, long-horizon consistency, and execution under time pressure.
- Likely reviewed anchors: `GTBench`, `BeyondScaling`, `WerewolfArena`, `BALROG`, `GameplayQA`, `FlashAdventure`, `EMemBench`, `MineNPCTask`, `CollabOvercooked`, `LLMCoordination`, `TextAtari`, `StarDojo`.
- Open synthesis focus: compare collaboration failures, memory failures, and long-horizon execution failures without reducing them to a single generic capability gap.

## 7. Open problems for next-generation game benchmarks

- Draft goal: propose benchmark-design directions around unified interfaces, calibration, multimodal social play, and open-ended generalization.
- Likely reviewed anchors: `AIGameStore`, `Orak`, `BALROG`, `GameVerse`, `KORGym`, `MCU`, `TeamCraft`, `TextArena`, `Clembench2024`, `MineNPCTask`, `CollabOvercooked`, `HumanLevelDiplomacy`.
- Open synthesis focus: connect benchmark maintenance, open-world validators, collaboration protocols, and calibration design into one forward-looking agenda.
