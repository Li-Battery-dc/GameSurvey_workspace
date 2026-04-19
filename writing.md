# Writing

This file is the active drafting workspace for the survey on game benchmarks for LLMs and VLM agents. `outline.md` is the canonical section map. `paper_cards/` and `corpus/registry/benchmark_registry.csv` remain the evidence layer. Use this file to track section status, claim plans, draft prose direction, and evidence gaps.

## Working Rules

- Draft only from `card-reviewed` or `finalized` cards unless a sentence is explicitly marked as a placeholder or open question.
- Keep comparative synthesis separate from raw evidence extraction. If a claim cannot be traced to reviewed cards, do not smooth it over.
- When drafting exposes a gap, record it here and send the work back to the registry or paper-card workflow instead of guessing.
- Update this file when a section changes status, gains enough evidence, or becomes blocked.

## Section Status Vocabulary

- `not-started`: no active drafting work yet
- `planning`: section claim plan exists but prose is still thin
- `drafting`: prose direction and evidence plan are both clear
- `needs-evidence`: blocked by missing reviewed cards or unresolved conflicts
- `ready-for-revision`: a coherent draft exists and should be tightened
- `stable`: section is reusable with only light future edits expected

## Narrative Spine

- Level 1: Rule Following — Can it make legal moves? (`SmartPlay`, `GTBench`)
- Level 2: Strategic Reasoning — Can it think effectively? (`PokerBench`, `DSGBench`)
- Level 3: Social Intelligence — Can it cooperate and deceive? (`WerewolfArena`, `Wolf`)
- Level 4: Visual Agency — Can it play like a human? (`Balrog`, `StarBench`)
- Level 5: Cross-Game Generalization — Can it play anything? (`Orak`, `GameVerse`, `AIGameStore`)

## Section Tracker

| Section | Status | Current evidence base | Next move |
| :--- | :--- | :--- | :--- |
| 0. Lead in: Why Games as Benchmarks | drafting | B01, B03, B04, B05, B06, B07 | Keep the lead-in short: static benchmark limits -> games as human-calibrated capability probes -> front-end/back-end benchmark design trade-off -> survey roadmap. |
| 1. Taxonomy: The Evolutionary Levels of Game Environments | drafting | B01, B02, B03, B04, B05, B06, B08, B09 | Build the five-level taxonomy table and use the level anchors as the running narrative rather than keeping history and taxonomy as separate top-level sections. |
| 2. Purpose: Core Capabilities Evaluated by Games | drafting | B01, B02, B03, B04, B05, B06, B08, B09 | Draft the capability-target subsections with one clear benchmark innovation per capability family so this section does not collapse into a paper list. |
| 3. Paradigm: From Interaction to Evaluation | drafting | B01, B04, B05, B06, B07, B09 | Separate interaction design from evaluation design, then make the privileged-interface versus ecological-validity trade-off the main through-line. |
| 4. Synthesis: Model Bottlenecks and Future Benchmark Design | drafting | B01, B02, B03, B04, B05, B06, B07, B08, B09 | Merge old failure-mode and future-work material into one synthesis section that pairs recurring model failures with benchmark-design weaknesses. |

## 0. Lead in: Why Games as Benchmarks

- Draft goal: align this lead-in with `script.md` and keep it short. The section should move from the limits of static evaluation to why games are a stronger substrate for agentic benchmarking, then briefly hand off to the rest of the survey.
- Core framing:
  Static QA-style and one-shot multimodal benchmarks still measure useful local skills, but they under-measure continuous agent behavior such as long-horizon planning, adaptive recovery, state tracking, and delayed consequences. The opening should start from this mismatch.
- Why games:
  Present games as capability probes rather than as a genre list. Their value is that they combine explicit rules, sequential interaction, auditable progress, and behaviorally meaningful outcomes across formal, social, and visual settings.
- Human-calibrated angle:
  Sync with the script's stronger claim that the space of human games is a culturally evolved and human-calibrated source of capability coverage. The point is not that games are automatically realistic, but that their structural diversity exposes different agentic demands inside repeatable interactive loops.
- Semantic privilege vs. ecological interaction:
  Bring in the script's main benchmark-design line. Human-like front ends use pixels, complex GUI layouts, and native controls, while many practical benchmarks grant **semantic privilege** by textifying states or exposing structured APIs to make agents tractable (StarBench). This abstraction masks the grounding complexity required for genuine agency.
- Front-end/back-end split:
  State explicitly that recent work increasingly separates ecological interaction from robust evaluation: keep the observation-action loop as human-like as possible on the front end, while using evaluator-only state access, verifiable progress signals, or other backend instrumentation for scoring.
- Section handoff:
  End with a short roadmap to the later sections: a five-level narrative taxonomy plus orthogonal design-space view, a capability-centered reading of what different games reveal, an interaction/evaluation paradigm analysis, and a synthesis of model bottlenecks plus benchmark-design flaws.
- Evidence anchors:
  Formal motivation: `SmartPlay`, `GTBench`, `BotzoneBench`, `Clembench`, `ThirdParadigm`.
  Social and visual consequence: `WerewolfArena`, `HumanLevelDiplomacy`, `Balrog`, `VideoGameBench`, `StarBench`.
  Platform and methodology: `GameWorld`, `Orak`, `TextArena`, `AIGameStore`, `ARCAGI3`.
- Keep explicit caution:
  Do not write this section as a mini taxonomy. Do not claim that all game benchmarks are equally ecological or contamination-resistant. Keep `HumanLevelDiplomacy` as a milestone bridge, and use `GameWorld` or similar papers when making verifiable-evaluation claims.

## 1. Taxonomy: The Evolutionary Levels of Game Environments

- Draft goal: trace how game benchmarks expand from formal rule-grounded containers to social, visual, and open-ended benchmark platforms, while still keeping a usable design-space taxonomy.
- Table schema to lock in:
  game structure; world structure; benchmark scope; modality; evaluation intent.
- Global framing claim:
  The five levels are a narrative taxonomy, not a strict chronology. Many strong papers straddle adjacent levels, and the survey should say that directly.

### 1.1 Level 1: Rule Following

- Core anchors: `SmartPlay`, `GTBench`, `BotzoneBench`.
- Draft angle:
  These benchmarks emphasize legal moves, state tracking, and explicit rule compliance under strongly normalized interfaces. Their main strength is diagnostic control; their main weakness is privileged interaction.

### 1.2 Level 2: Strategic Reasoning

- Core anchors: `PokerBench`, `DSGBench`, `GameBench`, `BeyondScaling`, `OpenGuanDan`.
- Draft angle:
  The focus shifts from merely acting legally to planning under uncertainty, opponent modeling, and time-sensitive choice. `PokerBench` is the specialist imperfect-information contrast; `DSGBench` is the comparative multi-game platform; `BeyondScaling` adds the strategy-versus-execution split.

### 1.3 Level 3: Social Intelligence

- Core anchors: `WerewolfArena`, `Wolf`, `LLMHanabi`, `StrategicHanabi`, `LLMCoordination`, `CollabOvercooked`.
- Draft angle:
  Social benchmarks matter because success depends on belief tracking, persuasion, deception, or partner modeling, not only on task-state optimization. Keep deduction, negotiation, and cooperation as separate sub-branches.
  Keep `HumanLevelDiplomacy` as a historical and ecological bridge rather than treating it as a reusable standardized benchmark.

### 1.4 Level 4: Visual Agency

- Core anchors: `Balrog`, `StarBench`, `FlashAdventure`, `GameplayQA`, `MCU`.
- Supporting comparison case: `VideoGameBench` for raw-screen control, walkthrough-frame checkpoint scoring, and the pause-versus-real-time trade-off.
- Draft angle:
  This level preserves more of the human play loop: pixels, GUI control, raw timing pressure, and richer world dynamics. The section should stress that visual agency is not one thing; passive gameplay understanding (`GameplayQA`) is different from end-to-end control (`VideoGameBench`, `FlashAdventure`, `MCU`). `StarBench` serves as the diagnostic anchor here by quantifying the performance drop when semantic privilege (TA mode) is removed in favor of direct GUI control (DC mode).

### 1.5 Level 5: Cross-Game Generalization

- Core anchors: `Crafter`, `Orak`, `GameVerse`, `AIGameStore`, `GVGAILLM`, `TextArena`.
- Draft angle:
  The benchmark question becomes whether one model or scaffold can remain competent across genres, interfaces, and evolving challenge spaces. `Crafter` is the single-world precursor, `Orak` the explicit cross-genre benchmark-plus-platform, `GameVerse` the reflection-heavy VLM branch, and `AIGameStore` the open-ended platform vision.

- Open synthesis caution:
  Avoid treating Level 5 as simply "more games." The real distinction is whether the benchmark is designed around transfer, scalability, or open-ended challenge growth rather than one fixed environment family.

## 2. Purpose: Core Capabilities Evaluated by Games

- Draft goal: organize the survey by capability target without losing the benchmark-design details that make each capability claim credible.

### 2.1 Rule grounding, legal action generation, and state tracking

- Primary anchors: `SmartPlay`, `LLMChess`, `BotzoneBench`, `GTBench`.
- Draft claim:
  Formal and board-game settings are strongest when the benchmark can distinguish illegal-action failure, weak state tracking, and strategic weakness instead of collapsing them into one score.

### 2.2 Strategic planning under uncertainty

- Primary anchors: `GTBench`, `PokerBench`, `DSGBench`, `BeyondScaling`, `OpenGuanDan`.
- Draft claim:
  Games are credible here because hidden information, mixed strategies, and adversarial adaptation are part of the environment rather than added after the fact as judge prompts.

### 2.3 Social intelligence: cooperation, negotiation, deception

- Primary anchors: `WerewolfArena`, `Wolf`, `LLMHanabi`, `StrategicHanabi`, `LLMCoordination`, `CollabOvercooked`.
- Draft claim:
  Keep three distinct targets visible: deception and suspicion (`WerewolfArena`, `Wolf`), cooperation and partner modeling (`LLMHanabi`, `LLMCoordination`, `CollabOvercooked`), and open-ended negotiation with strategic intent (`HumanLevelDiplomacy`, a reviewed ecological milestone rather than a standardized benchmark).

### 2.4 Visual grounding and spatial reasoning

- Primary anchors: `Balrog`, `GameplayQA`, `VLMPlayStarCraftII`, `StarBench`.
- Supporting comparison cases: `VideoGameBench` for raw-frame control failures and very low-score qualitative analysis; `AtariGPT` for the gap between visual understanding and spatially grounded low-level action.
- Draft claim:
  Game benchmarks are particularly useful here because perception errors immediately propagate into bad control, missed affordances, or false event attribution. `StarBench` explicitly identifies the "grounding gap" by showing models failing to locate UI targets despite potentially possessing the task logic.

### 2.5 Long-horizon autonomy and story or task completion with memory

- Primary anchors: `FlashAdventure`, `MineNPCTask`, `EMemBench`, `TextQuests`, `MCU`, `StarDojo`.
- Draft claim:
  The benchmark value comes from persistent dependencies across long trajectories: forgotten clues, broken inventories, failed repair, and weak return-to-go reasoning.

### 2.6 Time-sensitive decision-making and execution efficiency

- Primary anchors: `BeyondScaling`, `StarCraftIIArena`, `TowerMind`, `TextAtari`.
- Supporting comparison case: `VideoGameBench` for the gap between strict real-time play and its paused `Lite` variant.
- Draft claim:
  This subsection should separate reasoning quality from execution latency. `BeyondScaling` and `StarCraftIIArena` are the cleaner time-pressure comparisons. `VideoGameBench` is still useful as a raw-visual case because its paused `Lite` setting shows that some failures persist after reaction deadlines are relaxed, but that ablation is not directly equivalent to the original real-time task. `AtariGPT` can appear here only as a secondary caveat on systems feasibility, since its stronger contribution is the decomposition of low-level visual-action failure rather than a clean latency study.

### 2.7 Cross-game transfer and open-ended generalization

- Primary anchors: `Orak`, `GameVerse`, `AIGameStore`, `GVGAILLM`, `TextArena`, `Crafter`.
- Draft claim:
  The strongest papers here do not merely add titles; they test whether competence transfers across changing rules, genres, and interfaces, or whether scaffolding is doing most of the work.

- Open synthesis caution:
  This section should keep benchmark innovation and capability target coupled. For example, `Wolf` is not just about deception; it matters because it instruments deception at statement level. `MineNPCTask` is not just about memory; it matters because validators and repair traces make the claim auditable.

## 3. Paradigm: From Interaction to Evaluation

- Draft goal: compare how benchmarks let models play and how they turn trajectories into scores, then show why those two choices jointly determine benchmark validity.

### 3.1 Interaction: transfer to human-like play

- Observation-channel ladder:
  text manuals and summarized state (`SmartPlay`, `GTBench`, `BotzoneBench`);
  structured or API-mediated state (**Semantic Privilege**: `BeyondScaling`, `DSGBench`, `MineNPCTask`, `Orak`);
  GUI and raw visual control (**Ecological**: `StarBench`, `FlashAdventure`, `MCU`, `VideoGameBench`);
  video-only perceptual proxy (`GameplayQA`).
- Action-channel ladder:
  discrete legal moves;
  natural-language commands;
  semantic action tuples or tool/API calls (**Semantic Privilege**: `StarBench` TA, `Orak`, `MineNPCTask`);
  low-level GUI or controller-like actions (**Ecological**: `StarBench` DC, `VideoGameBench`, `FlashAdventure`).
- Main synthesis claim:
  Benchmark results are not comparable unless the paper discloses how much state abstraction, legal-action exposure, planning scaffolding, memory support, and tool mediation the agent receives. `StarBench` is the cleanest matched example because it keeps tasks and metrics fixed while shifting from screenshot-to-primitive control (DC) to semantic tuples plus OCR / detection aids (TA), revealing the catastrophic cost of removing semantic privilege.
- Core contrast set:
  `SmartPlay` and `BotzoneBench` for privileged rule-clean play;
  `Orak` and `MineNPCTask` for scaffolded API play;
  `StarBench` for matched low-level GUI versus semantic-action control on identical tasks;
  `FlashAdventure`, `MCU`, and `VideoGameBench` for more human-like control;
  `GameplayQA` as a boundary case that keeps perception but drops action.

### 3.2 Evaluation: from result metrics to diagnostic instrumentation

- Result-based metrics:
  win rate, reward, native score, completion, milestone progress, family-native combat metrics with different task objectives (`StarBench`), human-normalized reward in fixed-horizon Atari rollouts (`AtariGPT`), and walkthrough-frame checkpoint coverage (`VideoGameBench`).
- Process-level metrics:
  paired visual / spatial / acceptable-strategy / identification diagnostics (`AtariGPT`);
  ask-rate, per-ask effect, and normalized ask efficiency (`StarBench`);
  regret and equilibrium distance (`GTBench`);
  statement-level deception and suspicion trajectories (`Wolf`);
  collaboration or coordination submetrics (`LLMCoordination`, `CollabOvercooked`);
  reasoning-trace or subproblem diagnostics (`GAMEBoT`).
- Calibration families:
  fixed AI anchors (`BotzoneBench`, `GTOWizardBenchmark`);
  live arenas and TrueSkill or Elo (`TextArena`, `BeyondScaling`);
  human-relative comparison (`AIGameStore`);
  judge-based or validator-based evaluation (`MCU`, `FlashAdventure`, `MineNPCTask`).
- Main synthesis claim:
  Evaluation design is now a benchmark contribution in its own right. The survey should explicitly compare stable anchors, live leaderboards, human-vs-model comparison, and automatic judges instead of treating them as interchangeable scoring layers.
- Cross-paper caution:
  The survey should not compare a solver-grounded specialist accuracy score (`PokerBench`), a live leaderboard (`TextArena`), `StarBench`'s family-specific native RPG metrics, heuristic walkthrough-frame checkpoint matching (`VideoGameBench`), or an automatic VLM judge (`MCU`) as if they lie on one common scale.

## 4. Synthesis: Model Bottlenecks and Future Benchmark Design

- Draft goal: merge empirical failure analysis with benchmark-design critique so the ending section says both what current models lack and what current benchmarks still fail to measure cleanly.

### 4.1 Recurring model bottlenecks

- Rule compliance is no longer the whole problem:
  `SmartPlay`, `LLMChess`, and `BotzoneBench` show that legal play can coexist with shallow strategy.
- Strategic depth remains brittle under uncertainty:
  `GTBench`, `PokerBench`, `DSGBench`, and `BeyondScaling` show weak opponent modeling, poor mixed-strategy play, and a strategy-execution gap.
- Social belief modeling is still fragile:
  `WerewolfArena`, `Wolf`, `LLMHanabi`, and `LLMCoordination` show that fluent language does not imply robust deception detection or partner reasoning; `HumanLevelDiplomacy` adds a reviewed ecological milestone showing that stronger negotiation performance depended on a language-plus-planning stack rather than raw dialogue fluency.
- Perception and control remain major blockers:
  `Balrog`, `VideoGameBench`, `GameplayQA`, and `StarBench` show failures in temporal grounding, affordance detection, and latency-sensitive action; `StarBench` is especially useful because its direct-vs-tool-assisted split shows how much failure comes from grounding rather than task logic.
- Long-horizon memory and repair are still unstable:
  `FlashAdventure`, `MineNPCTask`, `EMemBench`, `TextQuests`, and `MCU` repeatedly surface clue forgetting, inventory misuse, and weak recovery after mistakes.

### 4.2 Benchmark-design bottlenecks

- Interface privilege distorts comparability:
  symbolic or API-heavy benchmarks can diagnose reasoning well, but they should not be presented as direct evidence of human-like play; `StarBench` is a useful anchor because it demonstrates this distortion inside one matched task suite.
- Evaluation protocols are fragmented:
  anchor ladders, arena ratings, human baselines, judge models, and validator pipelines each answer different questions.
- Process metrics help, but they also introduce new assumptions:
  `Wolf`, `GAMEBoT`, `MCU`, and `MineNPCTask` are strong here, but the survey should note the dependence on instrumented labels or judge quality.
- Open-endedness creates a comparability problem:
  `TextArena` and `AIGameStore` are compelling because they resist saturation, but living benchmarks and human-game platforms complicate stable year-to-year comparison.

### 4.3 Forward design agenda for the final section

- Prefer explicit interface disclosure:
  every benchmark comparison should state observation privilege, action abstraction, scaffold allowance, and judge dependence.
- Push toward dual-track evaluation:
  one controlled diagnostic track plus one ecological track is often better than forcing one protocol to do both.
- Use calibration deliberately:
  fixed anchors, hidden content, and human-relative comparisons solve different problems and should be combined rather than treated as substitutes.
- Expand multimodal social and open-world coverage:
  the corpus is now stronger on text-only social play than on benchmarks that combine raw perception with negotiation or collaboration.
- Keep future-work claims grounded:
  `Orak`, `GameVerse`, `MCU`, `TextArena`, and `AIGameStore` are the strongest basis for proposing more unified, scalable, and less saturable benchmark ecosystems.

## Active Drafting Cautions

- Do not flatten `GameplayQA`, `EMemBench`, `DeepPHY`, or similar diagnostic papers into full-agent benchmarks.
- Do not overstate anti-contamination claims for classic formal games such as `GTBench`; keep those claims benchmark-specific.
- Keep `HumanLevelDiplomacy` framed as a historical milestone and ecological bridge, not as a standardized reusable benchmark in the same sense as the later papers; it is now reviewed evidence, but protocol and ranking claims should still stay close to what the Science paper directly reports.
- Keep specialist benchmarks such as `PokerBench` and `GTOWizardBenchmark` as contrasts on calibration and uncertainty, not as the center of the general-game narrative.
