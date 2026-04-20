# PuzzlePlex PuzzlePlex: Benchmarking Foundation Models on Reasoning and Planning with Puzzles

## 0. Metadata
- Date: 2025/10
- Venue: arXiv
- Authors: Yitao Long, Yuru Jiang, Hongjun Liu, Yilun Zhao, Jingchen Sun, Yiqiu Shen, Chen Zhao, Arman Cohan, Dennis Shasha
- Paper link: https://arxiv.org/pdf/2510.06475v1
- Code link:
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: medium
- Review gate label: usable

## 1. One-paragraph benchmark summary
- PuzzlePlex is a broad puzzle benchmark designed to measure reasoning and planning in structured, multi-turn environments. It covers 15 novel rule-based puzzles spanning single-player and two-player settings, deterministic and stochastic dynamics, and both text-only and text-image instances. The benchmark evaluates models in instruction-based and code-based modes, reports normalized scores and Elo, and shows that reasoning models currently do much better in direct interaction than in code-based execution. For this survey, it is best used as a puzzle-heavy contrast case rather than a core agent-play anchor.

## 2. Position in our survey
- Why-games relevance: Puzzles retain explicit rules and strategic interaction while letting benchmark designers vary uncertainty, competition, and horizon length compactly.
- Historical stage: diagnostic capability probe
- Benchmark level(s): L2 strategic reasoning
- Most relevant outline section(s): 1,2,3,4
- Role in corpus: contrast

## 3. Design-space coding
### 3.1 Game structure
- Information structure: mixed
- Transition structure: mixed
- Agent structure: mixed
- Social structure: mixed
- Time structure: turn-based

### 3.2 World structure
- World type(s): puzzle
- Real game / simulated game / designed task-game hybrid: designed task-game hybrid
- Benchmark unit: puzzle instance

### 3.3 Benchmark scope
- Scope: curated suite
- Number of games / tasks: 15 puzzle types

### 3.4 Modality
- Observation modality: mixed
- Action modality: semantic
- Perception burden retained: rule interpretation, logical and spatial reasoning, long-horizon planning, legality handling
- Perception burden removed: richer ecological interaction beyond puzzle rules

## 4. What this benchmark measures
- Primary capability target: structured reasoning and planning across diverse puzzle formats
- Secondary capability target(s): code synthesis, multimodal puzzle understanding, scaling behavior
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? yes
- Does it test social reasoning / deception / cooperation? no
- Does it test visual grounding / spatial-temporal reasoning? partially
- Does it test long-horizon autonomy / task completion? yes
- Does it test real-time efficiency? no
- Does it test cross-game transfer / open-ended generalization? partially
- Why is a game environment especially suitable here? Puzzles provide controlled, automatically checkable settings where reasoning depth can be stressed without needing a full ecological world model.

## 5. Interaction paradigm
- Observation channel: puzzle state, rules, and prior moves in instruction-based mode; executable environment access in code-based mode
- Action channel: natural-language moves or generated code
- Interface type: natural language / code
- Agent scaffold allowed: none
- Is there privileged API access? yes
- How close is the setup to human play? low; PuzzlePlex is designed for controlled reasoning measurement rather than ecological play
- Main ecological-validity trade-off: The benchmark is precise and extensible, but much narrower than full game-agent environments.

## 6. Evaluation protocol
- Main score: normalized score and Elo-style comparison metrics
- Auxiliary score(s): legal play percentage, win probability matrices, and instruction-versus-code comparisons
- Evaluation style: hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: custom strategies and model-versus-model comparisons; no human baseline is used
- Automatic verifiability: high
- Calibration method: difficulty settings, legality checking, and custom strategy baselines
- Anti-contamination argument: partial; the paper emphasizes curated puzzle selection and the lack of public solving strategies rather than a hard contamination guarantee
- Reliability or comparability concerns: the benchmark is broad within puzzles, but puzzle reasoning does not cover all the burdens of agentic game play

## 7. Main contributions
- Contribution 1: Builds a 15-puzzle benchmark spanning single/two-player, deterministic/stochastic, and text/text-image settings.
- Contribution 2: Evaluates both instruction-based interaction and code-based execution.
- Contribution 3: Adds fine-grained metrics including Elo, legal-play statistics, and prompt-strategy analyses.

## 8. Main findings and failure modes
- Core empirical takeaway: reasoning models outperform non-reasoning models in instruction-based play, but performance drops substantially in the code-based setting
- Notable model failure mode 1: illegal moves and formatting failures remain common, showing that models still fail basic rule compliance
- Notable model failure mode 2: code generation is meaningfully harder than direct interactive play, even for strong models
- Notable model failure mode 3: multimodal gains are uneven, helping stronger models on some puzzles while weaker models can degrade
- Does this paper reveal a benchmark-design limitation as well? yes; PuzzlePlex is rigorous for puzzle reasoning, but puzzle-heavy benchmarks only partially overlap with broader agent evaluation

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Shows how compact game-like environments can still generate difficult reasoning tests.
- Best use in Section 1 (taxonomy and evolutionary levels): Later-stage example of reasoning-model benchmarking entering game-like domains. Useful contrast case for puzzle-focused suites.
- Best use in Section 2 (core capabilities evaluated by games): Supports claims about rule grounding, planning, and uncertainty handling.
- Best use in Section 3 (interaction and evaluation paradigm): Good example of comparing direct interaction with code-based execution. Useful Elo and legal-play metric comparison point.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Supports the argument that puzzle success and broader agent competence should not be conflated.

## 10. Relation to nearby papers
- Closest predecessor(s): PuzzleBench, VGRP-Bench, BoardgameQA, other puzzle-centered evaluations
- Closest follow-up(s): symbolic reasoning and multimodal puzzle suites
- Best comparison targets inside our corpus: GameTraversalBenchmark, CrossWordBench, VGRPBench, DeepPHY
- What this paper uniquely adds relative to neighbors: It joins interactive play and code execution inside one puzzle benchmark.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- PuzzlePlex contains 15 puzzle types with single-player and two-player, deterministic and stochastic, and text/text-image settings.
- The benchmark evaluates models in instruction-based and code-based modes and reports normalized scores, Elo, and legality-oriented statistics.
- The paper finds that reasoning models lead in instruction-based play and that performance drops notably in the code-based setting.

### 11.2 Our synthesis / interpretation
- This card is useful as a boundary case that is still game-like enough to belong in the survey but narrower than open-ended or embodied benchmarks.
- It is especially relevant when comparing direct play against code-mediated interaction.

### 11.3 Uncertain or needs re-check
- The instruction-based protocol excludes stochastic puzzles, so claims about uncertainty handling should be tied to the full benchmark rather than that specific protocol alone.
- Recheck Sections 3.4, 3.5, and C.4 if we later need the exact normalized-score formula or instruction-code conversion details.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? No immediate reread; the benchmark role is already clear.
- Which section to read next if needed: 3.4 / 3.5 / 4.2
- Follow-up question(s): Do we want PuzzlePlex in the main design taxonomy or as a contrast subsection on puzzle-heavy benchmarks?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P2
- Reading depth: deep
- Batch ID: B08
- Outline sections: 1,2,3,4
- Survey role: contrast
- Paper card path: `paper_cards/B08/PuzzlePlex.md`
- Check status: unchecked
- Next action: draft-section
- Last updated: 2026-04-10
