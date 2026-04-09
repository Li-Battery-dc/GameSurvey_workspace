# Outline

Survey on Game benchmark for LLMs and VLMs

high-level narrative stages, all sections follow or recall:
- Level 1: Rule Following — Can it make legal moves? (SmartPlay, GTBench)
- Level 2: Strategic Reasoning — Can it think effectively? (PokerBench, DSGBench)
- Level 3: Social Intelligence — Can it cooperate and deceive? (Werewolf Arena, WOLF)
- Level 4: Visual Agency — Can it play like a human? (BALROG, VideoGameBench)
- Level 5: Cross-Game Generalization — Can it play anything? (Orak, GameVerse, AI GAMESTORE)

## 0. Lead in: Summary and why Game as Benchmark
Goal:
- Establish why games are a uniquely valuable benchmark environment for LLMs and VLMs by synthesizing:

1. evidence that games provide dynamic, multi-step, interactive, strategic, and relatively contamination-resistant evaluation settings. This section should clarify what gaps in static QA-style benchmarks games can fill. 
2. Foundation models change from formal reasoning with text to embodied and social agency

Need evidence from:
- foundational framing papers, P0
- benchmark papers with explicit motivation
- examples spanning text to embodied-like interaction

## 1. Taxonomy: The Evolutionary Levels of Game Environments
Goal:
- Trace how game benchmarks evolved from formal, rule-bounded evaluation environments into broader capability probes and finally into open-ended, ecologically grounded agent benchmarks. Connect that evolution to the survey’s high-level narrative from rule-grounded interaction to cross-game generalization.

A giant table showing: 5 level stages as taxonomy as Rows and detailed cols showing a clear design-space view of game benchmarks by organizing papers along multiple benchmark axes, including game structure, world structure, benchmark scope, modality, and evaluation intent. 

table content code:
1. Game structure: perfect vs imperfect information, deterministic vs stochastic, single-agent vs multi-agent, cooperative vs competitive, turn-based vs real-time
2. World structure: board/card/puzzle/social deduction/RTS/adventure/open-world/sandbox
3. Benchmark scope: single game, single family, curated suite, genre-diverse suite, procedural/infinite/open-ended game space
4. Modality: text-only, symbolic state, GUI, raw image/video, first-person multi-video
5. Evaluation intent: diagnostic evaluation, ecological evaluation, train-and-eval foundation, or lifelong/open-ended task

Subsections:
1.1 Level 1: Rule Following - Games as rule-grounded formal containers 
1.2 Level 2: Strategic Reasoning — Planning and optimization under uncertainty through diagnostic game probes
1.3 Level 3: Social Intelligence — Multi-agent cooperation, deception, and network dynamics (`Werewolf Arena`, `WOLF`)
1.4 Level 4: Visual Agency — Real-Time Perception and Embodied Control
1.5 Level 5: Cross-Game Generalization — Open-ended transfer and generalist agents (`Orak`, `GameVerse`, `AI GAMESTORE`)

## 2. Purpose: Core Capabilities Evaluated by Games
Goal:
- Classify game benchmarks by their primary capability targets, explain why games are a suitable medium for that capability, and identify which benchmark innovations make the measurement credible.

Subsections:
2.1 Rule grounding, legal action generation, and state tracking
2.2 Strategic planning under uncertainty
2.3 Social intelligence: cooperation, negotiation, deception
2.4 Visual grounding, spatial reasoning.
2.5 Long-horizon autonomy and story/task completion with memory. 
2.6 Time-sensitive decision-making and execution efficiency
2.7 Cross-game transfer and open-ended generalization

## 3. Paradigm: From Interaction to Evaluation
Goal:
- Construct a comprehensive benchmark pipeline view. Compare how different benchmarks operationalize model interaction with games, how interface choices affect benchmark assessment, and how game benchmarks define success, assign scores, calibrate difficulty, and instrument gameplay for evaluation. Compare how evaluation design affects benchmark validity, comparability, and robustness.

Subsections:
3.1 Interaction: transfer to human-like play.
  - Observation channel: language description, structured states, GUI, pixels, video. Highlight the shift from structured text to high-dimensional, real-time multimodal streams.
  - Action channel: discrete action set, natural language action, tool/API calls, hybrid control. 
  - Trade-off: Privileged interface vs ecological validity. Explain how interface choices heavily skew benchmark results.
3.2 Evaluation: compare paradigms and how different metrics affect evaluation quality.
  -  Result-based metrics
  -  Process-level and Diagnostic Evaluation
  -  Adversarial evaluation
  -  Calibration and Robustness: how benchmarks anchor their difficulty and defend against evaluation noise, ensuring the scores remain meaningful as models rapidly evolve.


## 4. Synthesis: Model Bottlenecks and Future Benchmark Design
Goal:
- Synthesize recurring empirical failure modes across game benchmarks to explain what current LLMs and VLMs still lack, and juxtapose these model bottlenecks with the unresolved methodological flaws in current benchmark designs.
- Identify the major unresolved questions in benchmark design and propose directions for building more unified, scalable game benchmarks. Especially around generalization, interface standardization, calibration. 

subsections open for final analyse
