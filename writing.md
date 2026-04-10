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
- Level 4: Visual Agency — Can it play like a human? (`Balrog`, `VideoGameBench`)
- Level 5: Cross-Game Generalization — Can it play anything? (`Orak`, `GameVerse`, `AIGameStore`)

## Section Tracker

| Section | Status | Current evidence base | Next move |
| :--- | :--- | :--- | :--- |
| 0. Lead in: Summary and why Game as Benchmark | drafting | B01, B03, B04, B05, B06 | Open with `SmartPlay`, `GTBench`, and `Crafter` on dynamic rule-grounded evaluation, then bridge to `HumanLevelDiplomacy`, `Balrog`, `VideoGameBench`, and `AIGameStore` for social and embodied agency. |
| 1. Taxonomy: The Evolutionary Levels of Game Environments | drafting | B01, B02, B03, B04, B05, B06, B08, B09 | Build the five-level taxonomy table and use the level anchors as the running narrative rather than keeping history and taxonomy as separate top-level sections. |
| 2. Purpose: Core Capabilities Evaluated by Games | drafting | B01, B02, B03, B04, B05, B06, B08, B09 | Draft the capability-target subsections with one clear benchmark innovation per capability family so this section does not collapse into a paper list. |
| 3. Paradigm: From Interaction to Evaluation | drafting | B01, B04, B05, B06, B07, B09 | Separate interaction design from evaluation design, then make the privileged-interface versus ecological-validity trade-off the main through-line. |
| 4. Synthesis: Model Bottlenecks and Future Benchmark Design | drafting | B01, B02, B03, B04, B05, B06, B07, B08, B09 | Merge old failure-mode and future-work material into one synthesis section that pairs recurring model failures with benchmark-design weaknesses. |

## 0. Lead in: Summary and why Game as Benchmark

- Draft goal: establish why games are a uniquely valuable benchmark substrate for LLM and VLM agents, especially compared with static QA and one-shot multimodal tests.
- Core synthesis claim:
  Games combine explicit rules, sequential action, delayed consequences, hidden state, and automatic verification in a way that makes agent behavior observable rather than purely inferential.
- Revised opening thesis:
  Compared with static benchmarks that mainly test recognition or one-step response quality, game benchmarks place models inside interactive systems where perception, action, feedback, adaptation, and failure are coupled. This is the opening contrast, and it should be framed with the stronger "why games" logic visible in `GameVerse` and `AI GAMESTORE`: games are useful not only because they are challenging, but because they let us test closed-loop behavior, learning from failure, and broad human-evolved challenge spaces inside environments that still permit scoring and replay.
- Reviewed anchors:
  `SmartPlay`, `GTBench`, `BotzoneBench`, `Crafter`, `Balrog`, `VideoGameBench`, `Orak`, `GameWorld`, `MCU`, `AIGameStore`.
- Introduction shape to draft:
  Write this section as a compact introduction to the whole survey, not as a mini-related-work catalog. It should move from the benchmark problem, to the developmental storyline, to the paper's contribution preview.
- Paragraph architecture:
  Paragraph 1 should open with the benchmark problem. Use `SmartPlay`, `GTBench`, and `BotzoneBench` to argue that games recover closed-loop interaction, legal action constraints, strategic incentives, repeated trials, and calibrated scoring that static prompt benchmarks flatten away. The tone should stay methodological rather than celebratory.
  Paragraph 2 should transition from controlled formal settings to richer agents. Use `Crafter`, `Balrog`, `MCU`, and `VideoGameBench` to show that once benchmark designers preserve longer horizons, richer observations, and more ecological control loops, game benchmarks begin to expose perception, memory, exploration, and recovery failures that are hard to see in static tests.
  Paragraph 3 should expand the same argument into social and language-mediated agency. Use `WerewolfArena`, `HumanLevelDiplomacy`, and `TextArena` to show that games can make negotiation, deception, cooperation, and partner modeling behaviorally consequential rather than purely judged after the fact.
  Paragraph 4 should incorporate the stronger "why games" framing from `GameVerse` and `AI GAMESTORE`. `GameVerse` should support the claim that games uniquely permit act-fail-reflect-retry evaluation loops that static video understanding benchmarks cannot reproduce. `AI GAMESTORE` should support the claim that the space of human games is broad, culturally evolved, and harder to saturate than fixed benchmark sets. `AIGameStore`, `Orak`, and `GameVerse` should also bridge into the survey's Level 5 generalization story.
  Paragraph 5 should preview the rest of the survey and state the contribution logic explicitly. It should say that the paper is not only a paper list; it offers a five-level narrative taxonomy, a capability-and-design-space comparison, a benchmark-paradigm analysis, and a synthesis of both model bottlenecks and benchmark-design bottlenecks.
- Contribution preview to foreshadow in the introduction:
  Contribution 1: a five-level narrative taxonomy from rule following to cross-game generalization, with the levels used as a narrative scaffold rather than a rigid chronology.
  Contribution 2: a cross-benchmark comparison framework that jointly tracks game structure, world structure, benchmark scope, modality, and evaluation intent.
  Contribution 3: a benchmark-methodology argument that interface privilege, calibration strategy, and evaluation protocol matter as much as raw task difficulty when interpreting results.
  Contribution 4: a synthesis section that pairs recurring model failures with unresolved benchmark-design failures and turns that pairing into a forward design agenda.
- Core insights to plant early so the later sections feel earned:
  Insight 1: games matter because they bind outputs to state transitions and delayed consequences, not simply because they are entertaining or realistic.
  Insight 2: the field evolves from rule-bounded formal containers toward social, visual, and open-ended environments, but stronger ecological validity usually reduces control and comparability.
  Insight 3: benchmark breadth alone is not generalization; the real shift at the high end is toward transfer, challenge growth, and less saturable evaluation ecosystems.
  Insight 4: the main comparability problem in the literature is interface and evaluation design, not only heterogeneity of game genres.
- Evidence map for the final paragraph:
  Section 1 preview should point to `SmartPlay`, `GTBench`, `WerewolfArena`, `Balrog`, `Orak`, and `AIGameStore` as representative level anchors.
  Section 2 preview should emphasize that games can target rule grounding, strategic reasoning, social intelligence, visual grounding, long-horizon autonomy, real-time execution, and cross-game transfer under one survey frame.
  Section 3 preview should foreground the interaction-versus-evaluation split, especially the gap between privileged symbolic interfaces and more human-like play loops.
  Section 4 preview should make the ending claim explicit: current models still fail on strategy, social belief tracking, perception, and long-horizon repair, while benchmark design still fails on calibration, comparability, and sustainable openness.
- Keep explicit caution:
  Do not claim that all game benchmarks are inherently realistic or leakage-resistant. `SmartPlay`, `BotzoneBench`, and `PokerBench` are strong because they are structured and checkable, not because they are human-like.
- Additional caution for this draft:
  `GameplayQA` can appear only as a boundary example for dynamic gameplay perception, not as evidence of full interactive agency. `HumanLevelDiplomacy` should be framed as a historical and ecological milestone, not as a reusable benchmark platform. `AIGameStore` should support the anti-saturation argument carefully: the point is benchmark openness and human-game breadth, not a blanket claim that all game benchmarks resist contamination.

## 1. Taxonomy: The Evolutionary Levels of Game Environments

- Draft goal: trace how game benchmarks expand from formal rule-grounded containers to social, visual, and open-ended benchmark platforms, while still keeping a usable design-space taxonomy.
- Table schema to lock in:
  game structure; world structure; benchmark scope; modality; evaluation intent.
- Global framing claim:
  The five levels are a narrative taxonomy, not a strict chronology. Many strong papers straddle adjacent levels, and the survey should say that directly.

### 1.1 Level 1: Rule Following

- Core anchors: `SmartPlay`, `LLMChess`, `GTBench`, `BotzoneBench`.
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

- Core anchors: `Balrog`, `VideoGameBench`, `StarBench`, `FlashAdventure`, `GameplayQA`, `MCU`.
- Draft angle:
  This level preserves more of the human play loop: pixels, GUI control, raw timing pressure, and richer world dynamics. The section should stress that visual agency is not one thing; passive gameplay understanding (`GameplayQA`) is different from end-to-end control (`VideoGameBench`, `FlashAdventure`, `MCU`).

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

- Primary anchors: `Balrog`, `VideoGameBench`, `GameplayQA`, `VLMPlayStarCraftII`, `StarBench`.
- Draft claim:
  Game benchmarks are particularly useful here because perception errors immediately propagate into bad control, missed affordances, or false event attribution.

### 2.5 Long-horizon autonomy and story or task completion with memory

- Primary anchors: `FlashAdventure`, `MineNPCTask`, `EMemBench`, `TextQuests`, `MCU`, `StarDojo`.
- Draft claim:
  The benchmark value comes from persistent dependencies across long trajectories: forgotten clues, broken inventories, failed repair, and weak return-to-go reasoning.

### 2.6 Time-sensitive decision-making and execution efficiency

- Primary anchors: `BeyondScaling`, `StarCraftIIArena`, `VideoGameBench`, `TowerMind`, `AtariGPT`, `TextAtari`.
- Draft claim:
  This subsection should separate reasoning quality from execution latency. `BeyondScaling`, `StarCraftIIArena`, and `VideoGameBench` are especially important because they expose how agent quality changes when time pressure is preserved versus factored out, even within otherwise strong strategic systems.

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
  structured or API-mediated state (`BeyondScaling`, `DSGBench`, `MineNPCTask`, `Orak`);
  GUI and raw visual control (`StarBench`, `FlashAdventure`, `MCU`, `VideoGameBench`);
  video-only perceptual proxy (`GameplayQA`).
- Action-channel ladder:
  discrete legal moves;
  natural-language commands;
  tool or API calls;
  low-level GUI or controller-like actions.
- Main synthesis claim:
  Benchmark results are not comparable unless the paper discloses how much state abstraction, legal-action exposure, planning scaffolding, memory support, and tool mediation the agent receives.
- Core contrast set:
  `SmartPlay` and `BotzoneBench` for privileged rule-clean play;
  `Orak` and `MineNPCTask` for scaffolded API play;
  `FlashAdventure`, `MCU`, and `VideoGameBench` for more human-like control;
  `GameplayQA` as a boundary case that keeps perception but drops action.

### 3.2 Evaluation: from result metrics to diagnostic instrumentation

- Result-based metrics:
  win rate, reward, native score, completion, milestone progress, and checkpoint coverage.
- Process-level metrics:
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
  The survey should not compare a solver-grounded specialist accuracy score (`PokerBench`) to a live leaderboard (`TextArena`) or an automatic VLM judge (`MCU`) as if they lie on one common scale.

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
  `Balrog`, `VideoGameBench`, `GameplayQA`, and `StarBench` show failures in temporal grounding, affordance detection, and latency-sensitive action.
- Long-horizon memory and repair are still unstable:
  `FlashAdventure`, `MineNPCTask`, `EMemBench`, `TextQuests`, and `MCU` repeatedly surface clue forgetting, inventory misuse, and weak recovery after mistakes.

### 4.2 Benchmark-design bottlenecks

- Interface privilege distorts comparability:
  symbolic or API-heavy benchmarks can diagnose reasoning well, but they should not be presented as direct evidence of human-like play.
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
