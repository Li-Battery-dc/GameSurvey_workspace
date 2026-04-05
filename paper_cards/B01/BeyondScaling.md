# BeyondScaling Beyond Scaling: Assessing Strategic Reasoning and Rapid Decision-Making Capability of LLMs in Zero-sum Environments

## 0. Metadata
- Date: 2026/03
- Venue: arXiv
- Authors: Yang Li, Xing Chen, Yutao Liu, Gege Qi, Yanxian Bi, Zizhe Wang, Yunjian Zhang, Yao Zhu
- Paper link: https://arxiv.org/pdf/2603.09337v1
- Code link: https://github.com/star-nexus/star
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: medium
- Review gate label: usable

## 1. One-paragraph benchmark summary
- Beyond Scaling introduces the STAR benchmark, a controlled zero-sum multi-agent environment designed to separate deep strategy from fast tactical execution. The framework supports both turn-based and real-time play in a partially observable wargame-style setting, and evaluates models with round-robin competition rather than isolated tasks. Its main contribution is a protocol that exposes the strategy-execution gap: models that reason well with unlimited time can underperform once latency matters. For this survey, it is a useful contrast case showing how time pressure changes what a strong game agent means.

## 2. Position in our survey
- Why-games relevance: It uses adversarial games to expose dynamic decision quality and latency trade-offs that static reasoning tests miss.
- Historical stage: diagnostic capability probe
- Narrative level(s): L2 strategic reasoning
- Most relevant outline section(s): 2,3,5,6
- Role in corpus: contrast

## 3. Design-space coding
### 3.1 Environment structure
- Information structure: imperfect
- Transition structure: stochastic
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
- Primary modality: mixed
- Perception burden retained: partial observability, spatial positioning, action timing, tactical coordination
- Perception burden removed: direct low-level control, because structured environment state is summarized into prompts

## 4. What this benchmark measures
- Primary capability target: strategic planning under uncertainty versus time-bounded tactical execution
- Secondary capability target(s): opponent-aware adaptation, spatial reasoning, latency-sensitive decision making
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? yes
- Does it test social reasoning / deception / cooperation? no
- Does it test visual grounding / spatial-temporal reasoning? yes
- Does it test long-horizon autonomy / task completion? yes
- Does it test real-time efficiency? yes
- Does it test cross-game transfer / open-ended generalization? no
- Why is a game environment especially suitable here? A zero-sum game naturally couples planning quality, adversarial adaptation, and timely action in a way single-shot tasks cannot.

## 5. Interaction paradigm
- Observation channel: promptified environment state under fog-of-war
- Action channel: protocol directives emitted back into the game engine
- Interface type: hybrid
- Agent scaffold allowed: none
- Is there privileged API access? yes
- How close is the setup to human play? medium; the benchmark preserves adversarial spatial play but still abstracts raw control and perception
- Main ecological-validity trade-off: It preserves uncertainty and time pressure, but converts the environment into summarized prompt context.

## 6. Evaluation protocol
- Main score: Performance-Weighted Elo Rating (PWER)
- Auxiliary score(s): win rate, Standard Elo Rating (SER)
- Evaluation style: Elo / tournament / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: round-robin model-vs-model evaluation
- Automatic verifiability: high
- Calibration method: shared round-robin protocol across turn-based and real-time modes
- Anti-contamination argument: not central
- Reliability or comparability concerns: results depend on one designed environment family rather than broad cross-game coverage

## 7. Main contributions
- Contribution 1: Builds a modular zero-sum benchmark with both turn-based and real-time modes.
- Contribution 2: Adds PWER so decisive efficient wins count differently from narrow wins.
- Contribution 3: Empirically isolates a strategy-execution gap between slow reasoning models and faster instruction-tuned systems.

## 8. Main findings and failure modes
- Core empirical takeaway: Reasoning-enhanced models lead in turn-based play, but faster models often overtake them in real-time mode because inference latency becomes decisive.
- Notable model failure mode 1: slow reasoning pipelines miss real-time opportunities despite strong plans
- Notable model failure mode 2: text-only fast models incur more spatial errors than better-grounded variants
- Notable model failure mode 3: victories that look similar by win rate differ substantially in execution quality and resource efficiency
- Does this paper reveal a benchmark-design limitation as well? yes; the benchmark is narrow in world diversity even if rich in protocol design

## 9. Why this paper matters for our survey
- Best use in Section 0 (why games): Good example of how games reveal timing-sensitive agent failures.
- Best use in Section 1 (historical evolution): Represents newer benchmark designs that focus on interaction regimes rather than only task suites.
- Best use in Section 2 (design space): Strong case for hybrid turn-based / real-time taxonomy placement.
- Best use in Section 3 (capability targets): Direct evidence for strategic planning, spatial reasoning, and real-time efficiency.
- Best use in Section 4 (interaction paradigm): Useful example of promptified state plus protocol mediation.
- Best use in Section 5 (evaluation protocol): Important for PWER and strategy-quality-sensitive tournament scoring.
- Best use in Section 6/7 (limitations and future): Strong support for the strategy-execution gap theme.

## 10. Relation to nearby papers
- Closest predecessor(s): strategic arena benchmarks and RTS-inspired LLM agent evaluations
- Closest follow-up(s): PillagerBench, StarCraft-style real-time benchmarks
- Best comparison targets inside our corpus: BotzoneBench, OpenGuanDan, PillagerBench, WhoIsABetterPlayer
- What this paper uniquely adds relative to neighbors: It turns latency into a first-class evaluation variable instead of treating it as an implementation detail.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- STAR formalizes evaluation as a finite-horizon partially observable zero-sum stochastic game.
- It evaluates models in both turn-based and real-time modes using win rate, SER, and PWER in round-robin play.
- The paper reports that reasoning models dominate turn-based play but lose ground in real-time settings due to latency.

### 11.2 Our synthesis / interpretation
- This is a strong contrast card for Section 5 because it shows that better reasoning is not enough if inference speed collapses execution quality.
- The benchmark is more valuable as a protocol paper than as a broad survey anchor on game diversity.

### 11.3 Uncertain or needs re-check
- Recheck Appendix A or B if we later need exact terrain, unit, or action-space details for the STAR environment.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? No immediate reread; key protocol and findings are already clear.
- Which section to read next if needed: 4.1 / 4.3 / Appendix A
- Follow-up question(s): If we compare real-time benchmarks across papers, which latency assumptions are directly comparable?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P1
- Reading depth: deep
- Batch ID: B01
- Outline sections: 2,3,5,6
- Survey role: contrast
- Paper card path: `paper_cards/B01/BeyondScaling.md`
- Next action: draft-section
- Last updated: 2026-04-05
