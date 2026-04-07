# Outline

Survey on Game benchmark for LLMs and VLMs

high-level narrative stages, all sections follow or recall:
- Level 1: Rule Following — Can it make legal moves? (SmartPlay, GTBench)
- Level 2: Strategic Reasoning — Can it think effectively? (PokerBench, DSGBench)
- Level 3: Social Intelligence — Can it cooperate and deceive? (Werewolf Arena, WOLF)
- Level 4: Visual Agency — Can it play like a human? (BALROG, VideoGameBench)
- Level 5: Cross-Game Generalization — Can it play anything? (Orak, GameVerse, AI GAMESTORE)

## 0. Why game as benchmark
Goal:
- Establish why games are a uniquely valuable benchmark environment for LLMs and VLMs by synthesizing:

1. evidence that games provide dynamic, multi-step, interactive, strategic, and relatively contamination-resistant evaluation settings. This section should clarify what gaps in static QA-style benchmarks games can fill. 
2. Foundation models change from formal reasoning with text to embodied and social agency

Need evidence from:
- foundational framing papers, P0
- benchmark papers with explicit motivation
- examples spanning text to embodied-like interaction

## 1. Historical evolution of game benchmarks
Goal:
- Trace how game benchmarks evolved from formal, rule-bounded evaluation environments into broader capability probes and finally into open-ended, ecologically grounded agent benchmarks.This section should identify the major shifts in benchmark philosophy and connect that evolution to the survey’s high-level narrative from rule-grounded interaction to cross-game generalization.

Subsections:
1.1 Games as formal containers for rule-grounded and strategic reasoning
1.2 Games as diagnostic capability probes
1.3 Games as ecologically grounded agent benchmarks
1.4 Toward open-ended and general-game evaluation

## 2. Taxonomy of game benchmarks
Goal:
- Construct a clear design-space view of game benchmarks by organizing papers along multiple benchmark axes, including game structure, world structure, benchmark scope, modality, and evaluation intent. Show our own taxonomy which is actually the high-level narrative stages. 

A giant table showing: 5 level stages as taxonomy as Rows and detailed cols showing: 
1. Environment structure: perfect vs imperfect information, deterministic vs stochastic, single-agent vs multi-agent, cooperative vs competitive, turn-based vs real-time
2. World structure: board/card/puzzle/social deduction/RTS/adventure/open-world/sandbox
3. Benchmark scope: single game, single family, curated suite, genre-diverse suite, procedural/infinite/open-ended game space
4. Modality and embodiment: text-only, symbolic state, GUI, raw image/video, first-person multi-video
5. Benchmark intent: diagnostic evaluation, ecological evaluation, train-and-eval foundation, or lifelong/open-ended evaluation

## 3. Purpose: What game benchmarks actually measure
Goal:
- Classify game benchmarks by their primary capability targets, Explian why games are a suitable medium for that capability and what specific benchmark innovations make the measurement credible.

Subsections:
3.1 Rule grounding, legal action generation, and state tracking
3.2 Strategic planning under uncertainty
3.3 Social intelligence: cooperation, negotiation, deception
3.4 Visual grounding, spatial reasoning.
3.5 Long-horizon autonomy and story/task completion with memory. 
3.6 Time-sensitive decision-making and execution efficiency
3.7 Cross-game transfer and open-ended generalization

## 4. Paradigm: how models are allowed to play
Goal:
- Compare how different benchmarks operationalize model interaction with games. What different benchmark interfaces affect the benchmark mearsurement. 

Subsections:
4.1 Observation channel: language description, structured states, GUI, pixels, video
4.2 Action channel: discrete action set, natural language action, tool/API calls, hybrid control
4.3 Agent scaffolds: memory, reflection, retrieval, planners, tool use, MCP modules
4.4 Trade-off: Privileged interface vs ecological validity

## 5. Evaluation protocols
Goal:
- Analyze how game benchmarks define success, assign scores, calibrate difficulty, and instrument the gameplay process for evaluation. Compare how evaluation design affects benchmark validity, comparability, and robustness.

Subsections:
5.1 Native score, win rate, completion rate, 
5.2 Diagnostic / process-level / milestone completion evaluation
5.3 Elo, arena, and adversarial evaluation
5.4 Human baselines, AI anchors, and calibration
5.5 Robustness to contamination, prompt variance, and model-pool drift

## 6. Synthesis: what current models still fail at
Goal:
- Synthesize recurring empirical failure modes across game benchmarks and explain which challenges remain unsolved for current LLMs and VLMs. Dive deep into bottlenecks such as brittle rule tracking, poor long-horizon consistency, weak partial-observability reasoning, limited social modeling, fragile visual grounding, and the gap between slow reasoning and timely action.

Subsections:
6.1 Formal success does not imply ecological competence
6.2 Partial observability, deception, and belief tracking remain hard (social reasoning)
6.3 Visual grounding and spatial/temporal reasoning remain brittle
6.4 Long horizons break memory and planning consistency
6.5 Strategy–execution gap

## 7. Open problems for next-generation game benchmarks
Goal:
- Identify the major unresolved questions in benchmark design and propose directions for building more unified, scalable, ecologically valid, and diagnostically useful game benchmarks. especially around generalization, interface standardization, calibration, and integration across social, visual, and open-ended settings.

7.1 Unified and non-overly-privileged interfaces
7.2 Better human difficulty calibration and cross-benchmark comparability
7.3 Social, real-time, and multimodal evaluation under one framework
7.4 Toward general, lifelong, open-ended game intelligence evaluation