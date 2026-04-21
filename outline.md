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
- Open with the evaluation gap: static QA-style and one-shot tests are weak proxies for intelligence that must unfold over time through action, feedback, adaptation, and recovery.
- Reframe games as a uniquely suitable benchmark substrate because they are dynamic, interactive, and human-designed. Their rules, goals, and progress structures were built for human play, which makes them natural probes of human-relevant capability.
- Emphasize that game diversity should be understood as structured capability coverage rather than as a loose collection of genres. Different game structures expose different demands on reasoning, memory, planning and coordination.
- Preview the survey through three organizing questions that lead into taxonomy, capability mapping, and benchmark paradigm analysis.

Need evidence from:
- framing papers on why static evaluation misses sustained interactive intelligence
- representative benchmark papers showing how games operationalize dynamic, human-relevant capability demands
- benchmark papers and platform papers showing that the space of human games can support broad and extensible evaluation coverage

Paragraphs
0.1 The evaluation gap: from static answers to sustained interaction
0.2 Why games: dynamic, human-designed capability probes
0.3 Three questions for understanding game benchmarks

## 1. Taxonomy: The Evolutionary Levels of Game Environments
Goal:
- Use the five-level evolutionary spine as the primary historical organization of the literature. Then introduce structure, scope, and modality as secondary coding axes for reading the taxonomy table.


introduce the 5 level definition evolutionary spine, then add more information on a detailed overview of the table content code:
1. Structure:
  - Game Form: Match / Puzzle / Dialogue / Encounter / Arc / World / Mixed
  - Construction: Embedded / Wrapped / Adapted / Authored / Generated
  - Keep rule-level mechanics as supporting card annotations rather than as the main taxonomy axis.
2. Benchmark scope: single game, game family, curated suite, expandable suite, open-ended tasks
3. Modality: 
  - obs: text or symbolic, visual image, mixed
  - action: semantic, native control, mixed

Use the table to show each benchmark's dominant level at a glance. Keep cross-level nuance in the paper cards and unpack the capability meaning of each level later in Section 2 rather than inside the taxonomy table itself.

## 2. Purpose: Core Capabilities Evaluated by Games
Goal:
- Classify game benchmarks by their primary capability targets, follow the 5 level structure and explain why games are a suitable medium for that capability, and identify which benchmark innovations make the measurement credible.

Subsections:
2.1 Level 1: Rule Understanding:
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
3.1 Interaction: 
  - Observation channel: language description, structured states, raw images. Highlight the shift from structured text to high-dimensional, real-time multimodal streams.
  - Action channel: discrete action set, high-level semantic action, tool/API calls, native human-like-control, hybrid control.
  - Trade-off: Privileged interface vs ecological validity. Explain how interface choices heavily skew benchmark results.
3.2 Evaluation: Compare paradigms and how different metrics affect evaluation quality.
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
 
