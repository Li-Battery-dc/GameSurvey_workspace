# DeepPHY DeepPHY: Benchmarking Agentic VLMs on Physical Reasoning

## 0. Metadata
- Date: 2025/08
- Venue: arXiv
- Authors: Xinrun Xu, Pi Bu, Ye Wang, Borje F. Karlsson, Ziming Wang, Tengtao Song, Qi Zhu, Jun Song, Zhiming Ding, Bo Zheng
- Paper link: https://arxiv.org/pdf/2508.05405v1
- Code link: https://github.com/XinrunXu/DeepPHY
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: medium
- Review gate label: usable

## 1. One-paragraph benchmark summary
- DeepPHY is a physics-centered benchmark suite for agentic VLMs operating in interactive simulated environments and physics-based games. It aggregates six environments, including PHYRE, I-PHYRE, Kinetix, Pooltool, Angry Birds, and Cut the Rope, and standardizes them into a common evaluation frame with simplified visual observations and structured action formats. The benchmark focuses on whether models can turn visual understanding plus verbalized physics knowledge into predictive control and iterative refinement. For this survey, DeepPHY is best treated as a useful contrast case: it uses game-like environments, but its primary contribution is diagnosis of physical reasoning rather than broad game-agent benchmarking.

## 2. Position in our survey
- Why-games relevance: Physics games and simulators provide controllable, outcome-verifiable settings where perceptual understanding must be converted into action plans rather than static answers.
- Historical stage: diagnostic capability probe
- Narrative level(s): L4 visual agency
- Most relevant outline section(s): 3,4,6
- Role in corpus: contrast

## 3. Design-space coding
### 3.1 Environment structure
- Information structure: mixed
- Transition structure: mixed
- Agent structure: single-agent
- Social structure: N/A
- Time structure: hybrid

### 3.2 World structure
- World type(s): puzzle / physics game / simulated control task
- Real game / simulated game / designed task-game hybrid: curated suite mixing simulated physics environments with physics-based games
- Benchmark unit: episode / attempt

### 3.3 Benchmark scope
- Scope: curated suite
- Number of games / tasks: 6 environments
- Benchmark intent: diagnostic evaluation

### 3.4 Modality
- Primary modality: image
- Perception burden retained: visual scene reading, object interaction reasoning, causal prediction, and plan refinement from failures
- Perception burden removed: observations are often annotated or simplified, and action spaces are discretized into structured commands

## 4. What this benchmark measures
- Primary capability target: interactive physical reasoning from visual observations
- Secondary capability target(s): causal-chain reasoning, sequential planning, adaptation across retries, and visually grounded control
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? partially
- Does it test social reasoning / deception / cooperation? no
- Does it test visual grounding / spatial-temporal reasoning? yes
- Does it test long-horizon autonomy / task completion? partially
- Does it test real-time efficiency? no
- Does it test cross-game transfer / open-ended generalization? partially
- Why is a game environment especially suitable here? Physics games make latent physical laws observable through action consequences, so success depends on prediction rather than only verbal explanation.

## 5. Interaction paradigm
- Observation channel: screenshots or transformed visual scenes from each environment
- Action channel: environment-specific structured commands, JSON actions, integer vectors, or simplified launch/control parameters
- Interface type: structured action space / hybrid
- Agent scaffold allowed: none
- Is there privileged API access? yes
- How close is the setup to human play? low to medium; the underlying tasks are game-like, but observations and actions are redesigned to make them tractable for current VLMs
- Main ecological-validity trade-off: DeepPHY preserves interactive physical consequences but simplifies perception and motor control enough that it becomes a diagnostic suite rather than a raw game-agent benchmark

## 6. Evaluation protocol
- Main score: success rate
- Auxiliary score(s): Pass@K and average attempts
- Evaluation style: completion rate / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: leading open- and closed-source VLM baselines, with comparisons against mock baselines and reported human gaps
- Automatic verifiability: high
- Calibration method: unified prompt settings, two prompt formats, and repeated evaluation across six environments
- Anti-contamination argument: the benchmark centers on interactive environments rather than static textbook physics questions
- Reliability or comparability concerns: action-space redesign and mixed evaluation setups across environments mean that cross-environment scores partly reflect interface engineering rather than only raw reasoning

## 7. Main contributions
- Contribution 1: Introduces the first benchmark suite dedicated to interactive physical reasoning for agentic VLMs.
- Contribution 2: Unifies six previously separate physics environments and games under common metrics and prompt formats.
- Contribution 3: Shows that current VLMs struggle to convert descriptive physical knowledge into accurate predictive control.

## 8. Main findings and failure modes
- Core empirical takeaway: even strong VLMs struggle across the suite and often fail to beat simple baselines consistently on interactive physical reasoning tasks.
- Notable model failure mode 1: weak in-advance planning for tasks that require a full causal plan before acting
- Notable model failure mode 2: poor on-the-fly adaptation after observing failed physical interactions
- Notable model failure mode 3: sensitivity to environment-specific action reformulations, suggesting shallow control understanding
- Does this paper reveal a benchmark-design limitation as well? yes; the benchmark’s necessary observation and action simplifications make performance partly dependent on interface design choices

## 9. Why this paper matters for our survey
- Best use in Section 0 (why games): Shows why interactive game-like settings can test reasoning more directly than static physics QA.
- Best use in Section 1 (historical evolution): Useful as a side branch where game environments are used for embodied or physical-reasoning diagnosis rather than for broad benchmark suites.
- Best use in Section 2 (design space): Helps distinguish game benchmarks from simulator-heavy physics diagnostics.
- Best use in Section 3 (capability targets): Strong contrast case for visual causal reasoning and predictive control.
- Best use in Section 4 (interaction paradigm): Useful for discussing how much perceptual and motor burden current benchmarks remove.
- Best use in Section 5 (evaluation protocol): Relevant when comparing pass@K-style task completion with broader gameplay metrics.
- Best use in Section 6/7 (limitations and future): Supports the claim that current multimodal agents still do not reliably operationalize physics knowledge in action loops.

## 10. Relation to nearby papers
- Closest predecessor(s): static physical reasoning benchmarks and symbolic embodied-control settings
- Closest follow-up(s): physics-grounded multimodal agent benchmarks with richer action loops
- Best comparison targets inside our corpus: [TowerMind](D:/research_root/GameSurvey/workspace/paper_cards/B06/TowerMind.md), [ReasoningViaVideo](D:/research_root/GameSurvey/workspace/paper_cards/B06/ReasoningViaVideo.md), [EvoEmpirBench](D:/research_root/GameSurvey/workspace/paper_cards/B06/EvoEmpirBench.md), [LMGameBench](D:/research_root/GameSurvey/workspace/paper_cards/B08/LMGameBench.md)
- What this paper uniquely adds relative to neighbors: It turns diverse physics environments into one common VLM benchmark and foregrounds the gap between verbal physics competence and executable control.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- DeepPHY integrates PHYRE, I-PHYRE, Kinetix, Pooltool, Angry Birds, and Cut the Rope into a shared benchmark.
- The paper distinguishes in-advance planning from on-the-fly planning environments and evaluates models with success rate, Pass@K, and average attempts.
- The benchmark simplifies action spaces into structured formats such as JSON actions, integer commands, or constrained launch/control commands to make the environments usable for current VLMs.

### 11.2 Our synthesis / interpretation
- DeepPHY is better used in this survey as a boundary case than as a core benchmark anchor, because it is about physical-control reasoning with game assets rather than about game benchmarking per se.
- It is still valuable because it makes the interface-simplification problem unusually explicit.

### 11.3 Uncertain or needs re-check
- Re-check Section 5 and the per-environment result figures if we later need exact best-model scores for each of the six environments.
- The benchmark’s fit to the survey should remain marked as partial, because several included tasks look more like simulator diagnostics than like game benchmarks.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? Only if we need tighter per-environment comparisons against later embodied or physics-oriented papers.
- Which section to read next if needed: 3.2 / 4 / 5
- Follow-up question(s): Should DeepPHY remain in the main comparison tables, or should it be cited mainly as evidence about the boundary between game benchmarks and physical-control diagnostics?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P2
- Reading depth: deep
- Batch ID: B06
- Outline sections: 3,4,6
- Survey role: contrast
- Paper card path: `paper_cards/B06/DeepPHY.md`
- Next action: draft-section
- Last updated: 2026-04-05
