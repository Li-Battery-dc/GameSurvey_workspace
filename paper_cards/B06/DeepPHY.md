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
- DeepPHY is a six-environment benchmark suite for testing whether agentic VLMs can turn visual observation into physically informed action. It aggregates PHYRE, I-PHYRE, Kinetix, Pooltool, Angry Birds, and Cut the Rope under a unified evaluation protocol, but it intentionally simplifies observation and action spaces through annotations, discretization, top-down views, and structured commands so that the benchmark stresses physical reasoning rather than raw perception or motor control. The benchmark mixes in-advance planning and on-the-fly planning settings, compares a direct Vision-Language-Action prompt against a World-Model prompt, and reports success rate, Pass@K, and average attempts. For this survey, DeepPHY is best treated as a carefully instrumented contrast case at the boundary between game benchmarks and physics-control diagnostics.

## 2. Position in our survey
- Why-games relevance: Physics-based games and simulators provide action-consequence loops that are automatically checkable, which makes them useful for testing whether visual understanding can drive executable control.
- Historical stage: diagnostic capability probe
- Narrative level(s): L4 visual agency
- Most relevant outline section(s): 2,3,4
- Role in corpus: contrast

## 3. Design-space coding
### 3.1 Environment structure
- Information structure: mixed
- Transition structure: mixed
- Agent structure: single-agent
- Social structure: N/A
- Time structure: hybrid

### 3.2 World structure
- World type(s): puzzle / physics game / simulation
- Real game / simulated game / designed task-game hybrid: curated suite mixing physics simulators with physics-based games
- Benchmark unit: attempt / trial

### 3.3 Benchmark scope
- Scope: curated suite
- Number of games / tasks: 6 environments, each with its own task distribution and attempt budget
- Benchmark intent: diagnostic evaluation

### 3.4 Modality
- Primary modality: image
- Perception burden retained: visual scene reading, causal prediction, temporal planning, and action refinement after failed trials
- Perception burden removed: many scenes are annotated, some action spaces are discretized or serialized, and Pooltool is converted to a 2D top-down view

## 4. What this benchmark measures
- Primary capability target: interactive physical reasoning from visual observations
- Secondary capability target(s): causal-chain reasoning, planning before action, adaptation after failure, and visually grounded control
- Does it test rule grounding / legal action generation? partially
- Does it test strategic planning under uncertainty? partially
- Does it test social reasoning / deception / cooperation? no
- Does it test visual grounding / spatial-temporal reasoning? yes
- Does it test long-horizon autonomy / task completion? partially
- Does it test real-time efficiency? no
- Does it test cross-game transfer / open-ended generalization? no
- Why is a game environment especially suitable here? Interactive physics tasks make action consequences observable over time, so the benchmark can test whether descriptive physical knowledge becomes predictive control.

## 5. Interaction paradigm
- Observation channel: annotated screenshots, gridded overlays, labeled interactive objects, or transformed visual scenes, plus environment rules and failed-attempt history
- Action channel: structured environment-specific commands such as grid-and-radius choices, JSON action lists, integer control vectors, or constrained function calls
- Interface type: structured action space / hybrid
- Agent scaffold allowed: other (failed-trial history and optional world-model prompting)
- Is there privileged API access? yes
- How close is the setup to human play? low; the underlying domains are game-like, but the benchmark intentionally reshapes observation and action spaces for current VLMs
- Main ecological-validity trade-off: DeepPHY preserves physical interaction loops but removes much of the raw perceptual and motor burden, making it a physics-reasoning diagnostic suite rather than a naturalistic game-agent benchmark

## 6. Evaluation protocol
- Main score: success rate
- Auxiliary score(s): Pass@K and average attempts
- Evaluation style: completion rate / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: 17 open and closed VLMs plus a MOCK random-action baseline are evaluated across the suite; non-expert human baselines are reported only for Pooltool, Angry Birds, and Cut the Rope
- Automatic verifiability: mixed
- Calibration method: standardized VLA versus WM prompt formats, fixed per-environment attempt budgets, unified observation/action conversions, and environment-specific difficulty settings
- Anti-contamination argument: weak; the paper mainly argues that interactive physical environments are a more meaningful target than static physics QA, not that DeepPHY itself fully solves contamination
- Reliability or comparability concerns: environments differ in planning mode, some evaluations are environment-native while Angry Birds and Cut the Rope require manual scoring, and part of the benchmark difficulty is introduced by action-space engineering rather than only by raw physical reasoning

## 7. Main contributions
- Contribution 1: Aggregates six previously separate physics simulators and physics-based games into a single benchmark for agentic VLMs.
- Contribution 2: Standardizes observation and action conversions so current VLMs can be compared on interactive physical reasoning.
- Contribution 3: Reveals a persistent gap between verbal or descriptive physical knowledge and precise predictive control.

## 8. Main findings and failure modes
- Core empirical takeaway: even strong VLMs struggle badly on interactive physical reasoning, and the optional World-Model prompt usually fails to convert descriptive prediction into better control.
- Notable model failure mode 1: in in-advance planning environments such as PHYRE, models rarely devise correct full plans from the start and improve only slowly across repeated attempts
- Notable model failure mode 2: in on-the-fly environments such as Kinetix, Angry Birds, and Cut the Rope, models make poor timing and control choices even when annotations reveal the interactive objects
- Notable model failure mode 3: some apparently strong results are brittle or misleading, such as repeated brute-force strategies in Pooltool that exploit deterministic settings without demonstrating robust strategy
- Does this paper reveal a benchmark-design limitation as well? yes; DeepPHY itself shows how much current results depend on discretization, annotation, and mixed evaluation modes

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Limited. Use only as a contrast case showing why interactive environments can test action-grounded physical reasoning better than static physics QA.
- Best use in Section 1 (taxonomy and evolutionary levels): Useful as a boundary marker separating game benchmarks from simulator-heavy physical-reasoning diagnostics.
- Best use in Section 2 (core capabilities evaluated by games): Strong contrast evidence for visual causal reasoning and action-grounded physical prediction.
- Best use in Section 3 (interaction and evaluation paradigm): Strong evidence that many multimodal benchmarks achieve tractability by redesigning observation and action spaces, and that even explicit world-model prompting may not help.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Supports the claim that current multimodal agents still struggle to turn physical understanding into executable plans, especially in richer dynamic environments.

## 10. Relation to nearby papers
- Closest predecessor(s): static physics reasoning QA benchmarks, symbolic-input physical simulators, and game agents that sidestep low-level physics by operating at higher abstraction
- Closest follow-up(s): future physically grounded multimodal agent benchmarks with less observation/action simplification
- Best comparison targets inside our corpus: `TowerMind`, `ReasoningViaVideo`, `EMemBench`, `AtariGPT`
- What this paper uniquely adds relative to neighbors: It foregrounds physical reasoning specifically, mixes in-advance and on-the-fly planning regimes, and makes the observation/action redesign problem explicit instead of hiding it.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- DeepPHY integrates PHYRE, I-PHYRE, Kinetix, Pooltool, Angry Birds, and Cut the Rope into one benchmark suite.
- The benchmark explicitly converts observation spaces through annotations, grids, or transformed views, and discretizes or structures actions to make the tasks tractable for current VLMs.
- Evaluation uses two prompt formats - Vision-Language-Action and World Model - and reports success rate, Pass@K, and average attempts.
- Human results are reported only for Pooltool, Angry Birds, and Cut the Rope, and the paper states that these are non-expert baselines rather than expert upper bounds.

### 11.2 Our synthesis / interpretation
- DeepPHY is valuable to the survey mainly as a scope boundary and methodology contrast: it is about interactive physical control, but it is not a general game benchmark in the same way as the survey's core game-agent papers.
- The paper is especially useful for Section 3 because it shows that benchmark interface design can dominate what "agentic" performance actually means.

### 11.3 Uncertain or needs re-check
- If we later need exact task counts, attempt budgets, or best-model numbers for each environment, re-check the appendix tables because these vary substantially across the six settings.
- If we compare human-relative performance in detail, re-check the paper's caveat that the reported human baselines are non-expert and only cover a subset of environments.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? No immediate reread is required unless we later need per-environment score tables or a tighter comparison of VLA versus WM prompting.
- Which section to read next if needed: 3.3 / 3.4 / 4 / 5 / appendices for individual environments
- Follow-up question(s): When we write the benchmark-interface subsection, should DeepPHY stay in the main contrast table or move into a boundary-case paragraph about simulator-heavy physical diagnostics?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P2
- Reading depth: deep
- Batch ID: B06
- Outline sections: 2,3,4
- Survey role: contrast
- Paper card path: `paper_cards/B06/DeepPHY.md`
- Check status: unchecked
- Last updated: 2026-04-09
