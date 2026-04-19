# BeyondScaling Beyond Scaling: Assessing Strategic Reasoning and Rapid Decision-Making Capability of LLMs in Zero-sum Environments

## 0. Metadata
- Date: 2026/03
- Venue: arXiv
- Authors: Yang Li, Xing Chen, Yutao Liu, Gege Qi, Yanxian Bi, Zizhe Wang, Yunjian Zhang, Yao Zhu
- Paper link: https://arxiv.org/pdf/2603.09337v1
- Code link: https://github.com/star-nexus/star
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: high
- Review gate label: usable

## 1. One-paragraph benchmark summary
- Beyond Scaling introduces STAR, a controlled 1v1 zero-sum benchmark for iterative, opponent-aware decision making under partial observability and explicit time pressure. The same wargame-style environment is evaluated in matched turn-based and real-time modes, letting the paper compare unconstrained deliberation against latency-bounded execution inside one protocol. Its strongest survey value is a clean strategy-execution contrast rather than ecological gameplay: the standard setup uses structured JSON observations and tool-mediated actions instead of raw human-like control. For this survey, it is best used as evidence that strong strategic reasoning can still fail operationally once real-time actuation and inference latency enter the loop.

## 2. Position in our survey
- Why-games relevance: It uses a zero-sum adversarial game to force reasoning to unfold over repeated, evolving states under latency pressure, while also making clear how much of that difficulty is retained after interface abstraction.
- Historical stage: diagnostic capability probe
- Narrative level(s): L2 strategic reasoning
- Most relevant outline section(s): 1,2,3,4
- Role in corpus: contrast

## 3. Design-space coding
### 3.1 Environment structure
- Information structure: imperfect
- Transition structure: mixed
- Agent structure: multi-agent
- Social structure: competitive
- Time structure: hybrid

### 3.2 World structure
- World type(s): RTS / strategy / other
- Real game / simulated game / designed task-game hybrid: designed wargame-style task-game
- Benchmark unit: full match

### 3.3 Benchmark scope
- Scope: single game
- Number of games / tasks: one benchmark environment with turn-based and real-time modes
- Benchmark intent: diagnostic evaluation

### 3.4 Modality
- Primary modality: symbolic state
- Perception burden retained: partial observability, spatial state tracking, opponent updates over time, and action timing within an evolving battlefield
- Perception burden removed: raw pixels, native GUI control, and low-level motor execution, because the standard setting feeds faction-level JSON state through a protocol layer

## 4. What this benchmark measures
- Primary capability target: opponent-aware sequential planning under uncertainty plus time-bounded execution
- Secondary capability target(s): spatial state tracking, adversarial adaptation, latency-sensitive decision making
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? yes
- Does it test social reasoning / deception / cooperation? no
- Does it test visual grounding / spatial-temporal reasoning? partially; map-based spatial reasoning is central, but native visual grounding is only probed in the separate VLM ablation
- Does it test long-horizon autonomy / task completion? partially; it measures multi-turn planning within a match, not open-ended task completion or memory-heavy long-horizon agency
- Does it test real-time efficiency? yes
- Does it test cross-game transfer / open-ended generalization? no
- Why is a game environment especially suitable here? A partially observable zero-sum game makes reasoning iterative and adversarial, so the benchmark can test whether a model keeps adapting across evolving states and still acts in time.

## 5. Interaction paradigm
- Observation channel: faction-level structured JSON observations under fog-of-war; in real-time mode the agent continuously polls updated state rather than waiting for discrete turns
- Action channel: structured protocol actions or tool calls sent over WebSocket and translated into engine-executable directives; real-time mode can batch multiple actions in one step
- Interface type: API / structured action space
- Agent scaffold allowed: tool use / prompt-level OODA guidance
- Is there privileged API access? yes
- How close is the setup to human play? low to medium; it preserves adversarial dynamics and timing pressure, but abstracts most human perception and control burden
- Main ecological-validity trade-off: STAR captures iterative adversarial reasoning under time pressure, but its standard protocol removes raw-screen grounding and low-level actuation, so it is better as a controlled real-time contrast than as evidence of human-like continuous play.

## 6. Evaluation protocol
- Main score: Performance-Weighted Elo Rating (PWER)
- Auxiliary score(s): win rate, Standard Elo Rating (SER)
- Evaluation style: Elo / tournament / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: round-robin model-vs-model evaluation
- Automatic verifiability: high
- Calibration method: shared round-robin protocol across matched turn-based and real-time modes
- Anti-contamination argument: not central
- Reliability or comparability concerns: results come from one designed environment family, and the real-time rankings partly depend on serving latency, batching, and inference infrastructure rather than reasoning quality alone

## 7. Main contributions
- Contribution 1: Builds a modular 1v1 zero-sum benchmark with matched turn-based and real-time modes.
- Contribution 2: Adds PWER so decisive efficient wins count differently from narrow wins.
- Contribution 3: Empirically isolates a strategy-execution gap between high-deliberation models and faster systems under latency pressure.

## 8. Main findings and failure modes
- Core empirical takeaway: Reasoning-enhanced models lead in turn-based play, but faster systems often overtake them in real-time mode once latency and action frequency become decisive.
- Notable model failure mode 1: slow reasoning pipelines cannot convert strong plans into timely actions under continuous-polling real-time constraints
- Notable model failure mode 2: VLM variants reduce spatial and tool-call errors, but visual encoding latency sharply lowers action throughput
- Notable model failure mode 3: victories that look similar by win rate differ substantially in execution quality and resource efficiency
- Does this paper reveal a benchmark-design limitation as well? yes; its strongest insight comes from a protocol-mediated single environment, so it should not be overread as ecological real-world control evidence

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Limited contrast only: use it to show that time pressure changes agent evaluation, not as the main evidence for human-like continuous play.
- Best use in Section 1 (taxonomy and evolutionary levels): Level 2 strategic-reasoning contrast that introduces matched turn-based versus real-time interaction regimes inside one designed environment.
- Best use in Section 2 (core capabilities evaluated by games): Direct evidence for adversarial sequential planning, partial observability, and time-sensitive execution; avoid citing it for open-ended long-horizon autonomy.
- Best use in Section 3 (interaction and evaluation paradigm): Strong example of structured-state prompting, protocol mediation, continuous polling in real-time mode, and efficiency-aware rating.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Strong support for the strategy-execution gap, with the caveat that deployment latency is part of what the benchmark is measuring.

## 10. Relation to nearby papers
- Closest predecessor(s): GameBench, GAMABench, and other structured strategic-game evaluations
- Closest follow-up(s): StarCraftIIArena, PillagerBench
- Best comparison targets inside our corpus: DSGBench, GameBench, OpenGuanDan, StarCraftIIArena
- What this paper uniquely adds relative to neighbors: It keeps one designed environment fixed while varying turn-based versus real-time regimes, making latency and execution efficiency first-class evaluation variables.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- STAR formalizes evaluation as a finite-horizon partially observable zero-sum stochastic game.
- The concrete RoTK benchmark instance uses deterministic combat resolution even though the broader STAR formalization allows potentially stochastic dynamics.
- The standard benchmark exposes faction-level structured JSON observations under fog-of-war and supports unit-control, observation, faction-control, and system actions.
- The turn-based agent uses strict synchronization gating, while the real-time agent runs a continuous-polling loop and can batch actions within one inference step.
- It evaluates models in both turn-based and real-time modes using win rate, SER, and PWER in round-robin play.
- The system prompt explicitly enforces tool calls and an OODA-style perception-planning-action loop.
- The paper reports that reasoning models dominate turn-based play but lose ground in real-time settings due to latency.
- The paper explicitly notes that real-time performance is shaped not only by model architecture but also by deployment conditions such as optimized inference infrastructure.

### 11.2 Our synthesis / interpretation
- This is a strong contrast card for Sections 2.6, 3, and 4 because it shows that better reasoning is not enough if inference speed collapses execution quality.
- The benchmark is more valuable as controlled evidence for dynamic adversarial reasoning under interface abstraction than as a broad anchor on ecological gameplay or game diversity.

### 11.3 Uncertain or needs re-check
- Real-time performance partly entangles model quality with serving stack efficiency and batching policy; cross-paper comparison should keep that caveat explicit.
- Recheck Appendix B or C if we later need exact latency budgets, batching assumptions, or the full action schema for cross-benchmark comparison.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? Completed in this audit; the benchmark formalization, protocol layer, action schema, and latency findings are now clear enough for survey use.
- Which section to read next if needed: 4.1 / 4.3 / Appendix B-C
- Follow-up question(s): If we compare real-time benchmarks across papers, which latency budgets, batching rules, and serving stacks are directly comparable?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P1
- Reading depth: deep
- Batch ID: B02
- Outline sections: 1,2,3,4
- Survey role: contrast
- Paper card path: `paper_cards/B02/BeyondScaling.md`
- Check status: unchecked
- Next action: draft-section
- Last updated: 2026-04-19
