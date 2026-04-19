# DeepPHY DeepPHY: Benchmarking Agentic VLMs on Physical Reasoning

## 0. Metadata
- Date: 2025/08
- Venue: arXiv
- Authors: Xinrun Xu, Pi Bu, Ye Wang, Borje F. Karlsson, Ziming Wang, Tengtao Song, Qi Zhu, Jun Song, Zhiming Ding, Bo Zheng
- Paper link: https://arxiv.org/pdf/2508.05405v1
- Code link: https://github.com/XinrunXu/DeepPHY
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: high
- Review gate label: usable

## 1. One-paragraph benchmark summary
- DeepPHY is a six-environment benchmark suite for testing whether agentic VLMs can turn visual observations into successful physics-grounded actions across PHYRE, I-PHYRE, Kinetix, Pooltool, Angry Birds, and Cut the Rope. Rather than preserve native human play, the benchmark deliberately re-engineers each environment with annotated images, discretized or structured action formats, and sometimes transformed views so that current models can be compared on physical reasoning itself. It evaluates both in-advance and on-the-fly planning, compares direct Vision-Language-Action prompting against an added World-Model prediction prompt, and reports success rate, Pass@K, and average attempts. For this survey, DeepPHY is best used as a contrast paper on physical reasoning and interface redesign, not as evidence of ecological game-agent competence.

## 2. Position in our survey
- Why-games relevance: Physics-based games and simulators turn physical prediction into an interactive action-consequence loop rather than static QA, but DeepPHY makes that loop tractable through heavy benchmark-side interface redesign.
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
- Perception burden retained: rendered-scene parsing, spatial relations among objects, temporal prediction, and visual revision after failed trials
- Perception burden removed: object detection is eased by grids or IDs, Pooltool is converted from a 3D view to a 2D top-down view, and much of the continuous-control burden is replaced by discretized or constrained action formats

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
- Observation channel: rendered scene images, annotated overlays or indexed objects, transformed 2D views for Pooltool, textual rules, and failed-attempt history
- Action channel: environment-specific structured outputs such as grid-cell and radius choices, JSON timed-removal plans, integer control vectors, or constrained code commands like `shoot(angle, power)` and `cut_pin(id)`
- Interface type: structured action space / hybrid
- Agent scaffold allowed: other (failed-trial history and optional world-model prompting)
- Is there privileged API access? no direct hidden-state API, but strong benchmark-side semantic privilege through annotations, discretization, transformed views, and constrained command languages
- How close is the setup to human play? low; the underlying domains are game-like, but observation, action, and even camera/view formats are redesigned for model tractability
- Main ecological-validity trade-off: DeepPHY keeps interactive physical consequences and multi-attempt refinement, but removes much of the raw perception, continuous motor control, and native-interface difficulty that human play would involve

## 6. Evaluation protocol
- Main score: success rate
- Auxiliary score(s): Pass@K, average attempts, and star-based solution-quality summaries for Angry Birds and Cut the Rope
- Evaluation style: completion rate / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: 17 open and closed VLMs plus a MOCK random-action baseline are evaluated across the suite; human results are ballpark non-expert baselines and are reported only for Pooltool, Angry Birds, and Cut the Rope
- Automatic verifiability: mixed; PHYRE, I-PHYRE, Kinetix, and Pooltool use environment-native success checks, while Angry Birds and Cut the Rope use manual evaluation and star summaries
- Calibration method: common VLA versus WM prompt formats, per-environment attempt or step budgets, 3-run averages at temperature 0.1, and benchmark-side observation/action conversions tailored to each environment
- Anti-contamination argument: weak; the paper mainly argues that interactive physical environments are a more meaningful target than static physics QA, not that DeepPHY itself fully solves contamination
- Reliability or comparability concerns: environments differ substantially in planning mode and interface design, Angry Birds and Cut the Rope require manual evaluation, Pooltool contains a deterministic brute-force artifact, Cut the Rope excludes multi-screen-transition levels, and the human baselines are only ballpark non-expert references

## 7. Main contributions
- Contribution 1: Aggregates six previously separate physics simulators and physics-based games into a single benchmark for agentic VLMs.
- Contribution 2: Standardizes observation and action conversions so current VLMs can be compared on interactive physical reasoning.
- Contribution 3: Reveals a persistent gap between verbal or descriptive physical knowledge and precise predictive control.

## 8. Main findings and failure modes
- Core empirical takeaway: DeepPHY shows that current VLMs remain weak at turning descriptive physical understanding into reliable control: strong closed-source models still trail even non-expert humans in Angry Birds and Cut the Rope, and WM prompting helps only modestly in simpler settings.
- Notable model failure mode 1: in in-advance planning environments such as PHYRE, models rarely find correct full plans quickly and learn only slowly from failed attempts
- Notable model failure mode 2: in sequential environments such as Kinetix, Angry Birds, and Cut the Rope, models struggle with precise timing, multi-step chain reactions, and dynamic adaptation even when key objects are labeled
- Notable model failure mode 3: Pooltool can yield misleadingly high scores because deterministic setups reward repeated brute-force shots rather than genuine cue-ball control or spin reasoning
- Does this paper reveal a benchmark-design limitation as well? yes; DeepPHY itself shows how much current results depend on discretization, annotation, and mixed evaluation modes

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Limited. At most a brief contrast showing why interactive physics tasks probe action-grounded reasoning differently from static physics QA.
- Best use in Section 1 (taxonomy and evolutionary levels): Limited boundary mention only; useful if we need to mark where simulator-heavy physical diagnostics sit beside, rather than inside, the main game-benchmark lineage.
- Best use in Section 2 (core capabilities evaluated by games): Contrast evidence for visual and spatiotemporal physical reasoning under simplified but still interactive interfaces.
- Best use in Section 3 (interaction and evaluation paradigm): One of the clearest contrast cases for benchmark-side semantic privilege without giving models full symbolic-state APIs; also useful for the descriptive-versus-procedural gap between WM explanations and actual control.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Evidence that current multimodal agents still fail on timing, chain reactions, and action-grounded physical prediction, while benchmark designers often recover tractability by redesigning interfaces.

## 10. Relation to nearby papers
- Closest predecessor(s): static physics reasoning QA benchmarks, symbolic-input physical simulators, and game agents that sidestep low-level physics by operating at higher abstraction
- Closest follow-up(s): future physically grounded multimodal agent benchmarks with less observation/action simplification
- Best comparison targets inside our corpus: ReasoningViaVideo, EvoEmpirBench, MazeEval, VGRPBench
- What this paper uniquely adds relative to neighbors: It is the clearest physical-reasoning contrast paper in the corpus: a multi-environment suite that keeps interactive consequence loops while openly exposing how much tractability comes from interface redesign.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- DeepPHY integrates PHYRE, I-PHYRE, Kinetix, Pooltool, Angry Birds, and Cut the Rope into one benchmark suite.
- The benchmark explicitly rewrites observation spaces through grids, numerical labels, or transformed views, and rewrites action spaces through discretized selections, JSON outputs, integer control vectors, or constrained code commands.
- Evaluation compares two prompt formats - Vision-Language-Action and World Model - where WM additionally asks the model to predict the environmental changes caused by its chosen action.
- The core metrics are success rate, Pass@K, and average attempts, with star-based solution-quality summaries also reported for Angry Birds and Cut the Rope.
- Human results are reported only for Pooltool, Angry Birds, and Cut the Rope, and the paper states that these are ballpark non-expert baselines rather than expert upper bounds.
- Cut the Rope excludes multi-screen-transition levels because element positions could not be reliably obtained in real time.

### 11.2 Our synthesis / interpretation
- DeepPHY is safest to cite as a contrast paper on physical reasoning and interface design, not as direct evidence of human-like game play.
- Its main survey value is in showing that keeping visual input is not the same thing as preserving ecological interaction: benchmark-side annotation, action restructuring, and transformed views substantially change what is being measured.

### 11.3 Uncertain or needs re-check
- If we later need exact per-environment prompt templates, task splits, or ablation settings, re-check the appendices because implementation details vary sharply across the six environments.
- If we compare scoring pipelines across benchmarks, re-check exactly how manual evaluation and star accounting were operationalized for Angry Birds and Cut the Rope.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? No immediate reread is required unless we later need per-environment score tables or a tighter comparison of VLA versus WM prompting.
- Which section to read next if needed: 3.3 / 3.4 / 4 / 5 / appendices for individual environments
- Follow-up question(s): When Section 3 discusses semantic privilege, should DeepPHY sit next to StarBench as a contrast case where visual input is retained but observation and action channels are heavily redesigned?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P2
- Reading depth: deep
- Batch ID: B08
- Outline sections: 2,3,4
- Survey role: contrast
- Paper card path: `paper_cards/B08/DeepPHY.md`
- Check status: unchecked
- Last updated: 2026-04-19
