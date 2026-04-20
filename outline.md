# Outline

Survey on Game benchmark for LLMs and VLMs

high-level narrative stages, all sections follow or recall:
- Level 1: Rule understanding — Can it make legal moves? (SmartPlay, GTBench)
- Level 2: Strategic Reasoning — Can it think effectively? (PokerBench, DSGBench. BeyondScaling)
- Level 3: Social Intelligence — Can it cooperate and deceive? (Werewolf Arena, WOLF)
- Level 4: Visual Agency — Can it play like a human? (BALROG, StarBench)
- Level 5: Cross-Game Generalization — Can it play anything? (GameVerse, AI GAMESTORE)

## 0. Lead in: Why Games as Benchmarks
Goal:
- Open with the benchmark mismatch rather than with the taxonomy. First explain why static QA-style and one-shot multimodal tests are weak proxies for continuous agent behavior such as long-horizon planning, adaptive recovery, and state tracking.
- Reframe games as human-calibrated capability probes rather than as a loose genre collection. Their value comes from explicit rules, sequential interaction, delayed consequences, and auditable progress across diverse human game structures.
- Make the benchmark-design tension explicit: raw pixels, GUI layouts, and native controls are closer to human play, while textified states or semantic APIs make evaluation tractable but alter the capability demands.
- Introduce the emerging front-end/back-end split in benchmark design: preserve human-like interaction on the front end when possible, while exploiting evaluator-only game-state access or other verifiable signals on the back end for robust scoring.
- Preview the survey's four follow-up dimensions in a way that cleanly hands off to taxonomy, capability mapping, paradigm analysis, and final synthesis.

Need evidence from:
- foundational framing papers and P0 anchors on why static evaluation misses interactive agency
- representative benchmark papers showing games as capability probes across formal, social, and visual settings
- platform and methodology papers on interface trade-offs, human-relative breadth, and verifiable evaluation

Subsections:
0.1 Why static QA-style benchmarks and one-shot multimodal tests are not enough
0.2 Why games: human-calibrated capability probes instead of a genre taxonomy
0.3 Front-end interaction versus back-end evaluation in game benchmark design
0.4 Contribution preview and roadmap

Contribution preview:
- Introduce a five-level narrative taxonomy together with an orthogonal design-space view, organizing benchmarks by game structure, world structure, benchmark scope, modality, interface, and evaluation intent rather than by surface genre alone.
- Map different game environments to the specific cognitive and agentic capabilities they expose, from rule grounding and strategic reasoning to visual control and cross-game transfer.
- Analyze the interaction-evaluation pipeline, especially the trade-off between human-like interfaces, privileged abstractions, calibration quality, and protocol comparability.
- Synthesize recurring model bottlenecks together with unresolved benchmark-design flaws to motivate more scalable next-generation game evaluation.

## 1. Taxonomy: The Evolutionary Levels of Game Environments
Goal:
- Trace how game benchmarks evolved from formal, rule-bounded evaluation environments into broader capability probes and finally into open-ended, ecologically grounded agent benchmarks. Connect that evolution to the survey’s high-level narrative from rule-grounded interaction to cross-game generalization.

A giant table showing: detailed cols showing a clear design-space view of game benchmarks by organizing papers along multiple benchmark axes, including game structure, world structure, benchmark scope, modality, and evaluation intent.

A detailed overview of the various forms and directions of the table content code:
1. Game structure: perfect vs imperfect information, deterministic vs stochastic, single-agent vs multi-agent, cooperative vs competitive, turn-based vs real-time
2. World structure: board/card/puzzle/social deduction/RTS/adventure/open-world/sandbox
3. Benchmark scope: single game, single family, curated suite, genre-diverse suite, procedural/infinite/open-ended game space
4. Modality: text-only, symbolic state, GUI, raw image/video, first-person multi-video
5. Evaluation intent: diagnostic evaluation, ecological evaluation, train-and-eval foundation, or lifelong/open-ended task

## 2. Purpose: Core Capabilities Evaluated by Games
Goal:
- Classify game benchmarks by their primary capability targets, follow the 5 level structure and explain why games are a suitable medium for that capability, and identify which benchmark innovations make the measurement credible.

Subsections:
2.1 Level 1: Rule Following:
  - Games as rule-grounded formal containers
  - Understand the game rulea and make legal moves
2.2 Level 2: Reasoning
  - Game as interactive reasoning environment
  - Diagnostic probes for various abilities：
  - Spatial Reasoning
2.3 Level 3: Social Intelligence:
  - Multi-agent cooperation,
  - deception and network dynamics.
2.4 Level 4: Visual Agency:
  - Visual grounding，Perception
  - Real-Time Interaction
  - Agentic skills (Long-horizon autonomy and story/task completion with memory. )
2.5 Level 5: Cross-Game Generalization — Open-ended transfer and generalist agents
  - open-worlds tasks
  - multi-game universe(AI Gamestore)
  - zero-shot generalization

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

Knowing-Doing gap(Barlog),
