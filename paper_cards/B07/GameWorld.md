# GameWorld GameWorld: Towards Standardized and Verifiable Evaluation of Multimodal Game Agents

## 0. Metadata
- Date: 2026/04
- Venue: arXiv
- Authors: Mingyu Ouyang, Siyuan Hu, Kevin Qinghong Lin, Hwee Tou Ng, Mike Zheng Shou
- Paper link: https://arxiv.org/pdf/2604.07429v1.pdf
- Code link: https://gameworld-bench.github.io
- Reading depth: deep
- Card status: finalized
- Confidence in this card: high
- Review gate label: strong

## 1. One-paragraph benchmark summary
- GameWorld is a 34-game, 170-task browser-game benchmark for multimodal agents whose main contribution is to standardize interface and evaluation rather than to claim held-out transfer. It evaluates 18 model-interface pairs under one shared runtime, covering both computer-use agents that emit low-level mouse and keyboard controls and generalist multimodal agents that act through deterministic Semantic Action Parsing. A browser sandbox can pause execution during inference so that decision quality is separated from response latency, while a JavaScript bridge exposes serialized gameAPI state to a state-verifiable evaluator that computes deterministic progress and success signals. For this survey, GameWorld is strongest as an anchor for visual-agency evaluation design and for separating multi-game breadth from true cross-game generalization.

## 2. Position in our survey
- Why-games relevance: Browser games provide closed-loop visual interaction, broad mechanic diversity, and scalable resettable environments while still permitting deterministic outcome checks.
- Historical stage: ecological agent benchmark
- Benchmark level(s): L4 visual agency
- Most relevant outline section(s): 0,1,2,3,4
- Role in corpus: anchor

## 3. Design-space coding
### 3.1 Structure
- Form: Mixed
- Construction: Wrapped
- Construction note: curated suite of browser games under a shared sandbox runtime
- Benchmark unit: task episode

### 3.2 Mechanics profile
- State visibility: mixed
- Transition uncertainty: mixed
- Actor configuration: mixed
- Incentive structure: mixed
- Temporal regime: hybrid

### 3.3 Benchmark scope
- Scope: curated suite
- Number of games / tasks: 34 games, 170 tasks, 5 genres

### 3.4 Modality
- Observation modality: visual image
- Action modality: mixed
- Perception burden retained: raw screenshots, GUI layout interpretation, timing-sensitive control, and cross-game visual variability
- Perception burden removed: paused inference in the default setting factors out latency, and the Generalist interface abstracts low-level control into semantic actions

## 4. What this benchmark measures
- Primary capability target: visually grounded gameplay under standardized, interface-aware evaluation
- Secondary capability target(s): timing grounding, spatial navigation, long-horizon task completion, and reproducible benchmark diagnostics
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? partially; strategy matters mainly in the puzzle and simulation subsets rather than as a benchmark-wide hidden-information target
- Does it test social reasoning / deception / cooperation? no as a primary target
- Does it test visual grounding / spatial-temporal reasoning? yes
- Does it test long-horizon autonomy / task completion? yes
- Does it test real-time efficiency? yes, through the separate GameWorld-RT variant
- Does it test cross-game transfer / open-ended generalization? no; the suite is broad, but the paper does not study held-out transfer or benchmark growth
- Why is a game environment especially suitable here? Diverse games let the benchmark combine perception, timing, control, and delayed consequences while keeping success objectively measurable from environment state.

## 5. Interaction paradigm
- Observation channel: current game screenshot plus prompt blocks for rules, role, task instruction, and recent action history
- Action channel: either raw computer-use commands or semantic actions deterministically mapped into atomic mouse and keyboard events
- Interface type: hybrid
- Agent scaffold allowed: memory / reasoning / tool use
- Is there privileged API access? no for the agent; evaluator-only game state access is kept outside the prompt loop
- How close is the setup to human play? medium to high for CUA and medium for the semantic interface; the benchmark keeps visual interaction but also introduces standardized tool contracts and a paused runtime
- Main ecological-validity trade-off: GameWorld improves comparability through sandboxing and deterministic parsing, but the default paused setting removes real-time pressure and the semantic interface reduces low-level motor burden

## 6. Evaluation protocol
- Main score: normalized task progress (PG)
- Auxiliary score(s): success rate (SR), genre-level aggregates, repeated-run variance, GameWorld-RT scores, memory-round sensitivity, and invalid-action rates
- Evaluation style: milestone / outcome / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: 18 model-interface pairs are compared under the same runtime, and novice and expert human players are evaluated under the same action budget
- Automatic verifiability: high
- Calibration method: serialized gameAPI state, 233 task-relevant fields across 34 games, deterministic task targets, paused-inference standard runs, and repeated full-benchmark reruns on open models
- Anti-contamination argument: partial; the paper relies more on interactive execution and verifiable outcomes than on hidden holdouts or explicit contamination defenses
- Reliability or comparability concerns: the paused benchmark and GameWorld-RT answer different questions, semantic parsing changes control abstraction, and small performance gaps should not be over-read without reruns

## 7. Main contributions
- Contribution 1: Builds a 34-game, 170-task browser-game benchmark for multimodal agents with both computer-use and semantic-control interfaces.
- Contribution 2: Introduces outcome-based state-verifiable evaluation through a structured JavaScript bridge over game state.
- Contribution 3: Adds interface-aware robustness analyses, including repeated reruns, real-time evaluation, memory sensitivity, and invalid-action diagnostics.

## 8. Main findings and failure modes
- Core empirical takeaway: even the best GameWorld agents are far below novice human performance, and most models make partial progress much more often than they complete tasks.
- Notable model failure mode 1: both interfaces drop sharply on Level-1 basic control and timing grounding despite doing much better on reactive and symbolic-reasoning games
- Notable model failure mode 2: open-ended simulation tasks and Level-5 coordination or management tasks remain broadly difficult across both interfaces
- Notable model failure mode 3: longer action history helps semantic agents modestly but can hurt CUAs because low-level traces bloat context without preserving useful semantic structure
- Does this paper reveal a benchmark-design limitation as well? yes; it shows that benchmark conclusions depend strongly on whether latency is treated as part of the task, on how much control abstraction the interface allows, and on whether broad suite coverage is mistaken for transfer evidence

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Strong evidence that games can support interactive evaluation with deterministic, auditable outcome signals instead of heuristic judging.
- Best use in Section 1 (taxonomy and evolutionary levels): Helps position mature Level 4 benchmarks that preserve visual interaction while making protocol design itself a benchmark contribution. Also useful as a boundary case: a broad curated suite is not automatically a Level-5 transfer benchmark.
- Best use in Section 2 (core capabilities evaluated by games): Direct support for a capability-decomposition story inside visual gameplay: reactive control and symbolic reasoning are stronger than basic timing grounding and open-world coordination.
- Best use in Section 3 (interaction and evaluation paradigm): One of the corpus anchors for interface disclosure, semantic-versus-CUA trade-offs, paused-versus-real-time evaluation, and state-verifiable scoring.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Supports the forward-design claim that future benchmarks should separate decision quality from systems latency while still reporting both, and should say explicitly whether benchmark breadth means transfer, capability coverage, or instrumentation.

## 10. Relation to nearby papers
- Closest predecessor(s): BALROG, VideoGameBench, FlashAdventure, OSWorld
- Closest follow-up(s): GameVerse and future browser-game or computer-use benchmarks that combine ecological play with stronger verifiability or broader suite coverage
- Best comparison targets inside our corpus: Balrog, FlashAdventure, LMGameBench, Orak, AIGameStore
- What this paper uniquely adds relative to neighbors: It jointly standardizes dual agent interfaces, paused-versus-real-time browser execution, deterministic outcome verification, and rerun-based robustness analysis in one benchmark without claiming held-out transfer

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- GameWorld contains 34 browser games, 170 tasks, and 5 genres, and evaluates 18 model-interface pairs under one shared runtime.
- At each step, the agent observes a screenshot and outputs either computer-use function calls or game-specific semantic actions, both normalized into a unified atomic mouse/keyboard event space.
- The benchmark studies two interfaces: Computer-Use Agents that emit low-level mouse and keyboard controls and Generalist agents that act through deterministic Semantic Action Parsing.
- The evaluator reads serialized gameAPI state through a JavaScript bridge and instruments 233 task-relevant fields across the 34 games to compute deterministic progress and success.
- The best reported generalist result is Gemini-3-Flash-Preview at 21.2 SR and 41.9 PG, while the novice human reaches 55.3 SR and 64.1 PG under the same action budget.
- Ten repeated full-benchmark reruns on open Qwen models show only low single-digit variation in aggregate SR and PG, supporting benchmark-level robustness claims.
- The paper defines GameWorld-RT as an unpaused real-time variant and warns that default paused scores and RT scores should not be directly compared because latency becomes part of gameplay in RT.
- The paper's capability-aligned curriculum peaks at Level-4 reasoning or strategy and Level-2 reactive control, but drops sharply at Level-1 basic control or timing grounding and Level-5 open-world coordination or management.
- The limitations section states that scaling to new environments requires designing unique instruction sets and Semantic Action Parsing alignment for each game.

### 11.2 Our synthesis / interpretation
- GameWorld is one of the clearest recent papers for the survey's claim that interface privilege and evaluation protocol matter as much as raw game difficulty.
- It is better used as a visual-agency and evaluation-design anchor than as the main cross-game-generalization anchor, because its strongest contribution is making the benchmark itself more comparable and auditable.
- For Level-5 writing, treat it as a boundary case: multi-game breadth plus some open-ended tasks is not the same thing as explicit cross-game transfer or expandable benchmark growth.

### 11.3 Uncertain or needs re-check
- Re-check Appendix C or D if later drafting needs exact per-game state schemas, legality filters, prompt templates, or semantic-control registries.
- If we later cite individual games as Level-1 or Level-5 exemplars, re-check the paper's internal curriculum grouping rather than assuming it matches the survey's taxonomy one-to-one.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? No immediate reread; the current card already uses the full paper's setup, results, and analysis sections.
- Which section to read next if needed: 3.5 / 4.3 / 4.5 / Appendix C
- Follow-up question(s): Which Level-5 sentence, if any, should cite GameWorld only as a breadth-versus-transfer contrast alongside Orak or AI GameStore?

## 13. Registry sync
- Registry row synced: yes
- Registry status: finalized
- Priority: P0
- Reading depth: deep
- Batch ID: B07
- Outline sections: 0,1,2,3,4
- Survey role: anchor
- Paper card path: `paper_cards/B07/GameWorld.md`
- Check status: unchecked
- Last updated: 2026-04-28
