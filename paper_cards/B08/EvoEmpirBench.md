# EvoEmpirBench EvoEmpirBench: Dynamic Spatial Reasoning with Agent-ExpVer

## 0. Metadata
- Date: 2025/09
- Venue: arXiv
- Authors: Pukun Zhao, Longxiang Wang, Miaowei Wang, Chen Chen, Fanqing Zhou, Haojian Huang
- Paper link: https://arxiv.org/pdf/2509.12718v1
- Code link:
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: medium
- Review gate label: usable

## 1. One-paragraph benchmark summary
- EvoEmpirBench is a text-first dynamic reasoning benchmark built around two interactive tasks: a locally observable maze-navigation game and a match-2 elimination game. Both tasks are partially observable or dynamically changing, and the paper positions them as a harder alternative to static reasoning benchmarks by forcing agents to explore, adapt, and manage trade-offs over multi-step episodes. The paper's empirical story is inseparable from Agent-ExpVer, a three-agent online-learning scaffold that summarizes experience into reusable "truths" and feeds them back into future play. For this survey, EvoEmpirBench is most useful as a narrow dynamic-reasoning contrast paper and as evidence that benchmark difficulty and scaffold engineering are often entangled.

## 2. Position in our survey
- Why-games relevance: Dynamic games make exploration, adaptation, and score-versus-completion trade-offs observable and automatically measurable under partial observability.
- Historical stage: diagnostic capability probe
- Benchmark level(s): L2 strategic reasoning
- Most relevant outline section(s): 2,3,4
- Role in corpus: contrast

## 3. Design-space coding
### 3.1 Game structure
- Information structure: imperfect
- Transition structure: mixed
- Agent structure: single-agent
- Social structure: N/A
- Time structure: turn-based

### 3.2 Environment structure
- Environment type(s): abstract puzzle
- Real game / simulated game / designed task-game hybrid: designed task-game hybrid
- Benchmark unit: episode

### 3.3 Benchmark scope
- Scope: curated suite
- Number of games / tasks: 2 tasks with 3 difficulty levels each and 30 evaluation instances per level (90 instances per task)

### 3.4 Modality
- Observation modality: text or symbolic
- Action modality: semantic
- Perception burden retained: local observability, state tracking, tool use, resource trade-offs, and long-horizon planning
- Perception burden removed: no raw visual perception is required; state is presented through prompts and structured environment feedback

## 4. What this benchmark measures
- Primary capability target: adaptive reasoning in dynamic, partially observable game environments
- Secondary capability target(s): exploration, tool use, risk-reward trade-offs, score optimization, and online abstraction of reusable rules
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? yes
- Does it test social reasoning / deception / cooperation? no
- Does it test visual grounding / spatial-temporal reasoning? no
- Does it test long-horizon autonomy / task completion? partially
- Does it test real-time efficiency? no
- Does it test cross-game transfer / open-ended generalization? no
- Why is a game environment especially suitable here? The maze and match-2 tasks force repeated decisions under changing state while keeping outcomes, efficiency, and failure states easy to verify.

## 5. Interaction paradigm
- Observation channel: text prompts describing current game state, available actions, objectives, and environment feedback
- Action channel: environment actions issued through the benchmark interface on each turn
- Interface type: API / hybrid
- Agent scaffold allowed: memory / reflection / planner
- Is there privileged API access? yes
- How close is the setup to human play? low; the tasks are game-like, but interaction is prompt-driven and the paper's strongest results depend on an explicit online-learning scaffold
- Main ecological-validity trade-off: EvoEmpirBench keeps dynamism and partial observability, but its text-first interface and scaffold-heavy framing make it a diagnostic benchmark rather than an ecological gameplay benchmark

## 6. Evaluation protocol
- Main score: success rate and average score
- Auxiliary score(s): for maze - average steps, exploration, gold, remaining HP, enemy kills, and barriers destroyed; for match-2 - remaining/max steps ratio, score per step, clear per step, and API efficiency
- Evaluation style: completion rate / native score / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: human baselines, proprietary and open-source LLMs, and with-versus-without-Agent-ExpVer comparisons are all reported
- Automatic verifiability: high
- Calibration method: three difficulty levels per task, 30 instances per level, multi-model comparisons, and ablations such as removing TruthWeaver or revealing full vision
- Anti-contamination argument: the paper argues dynamic interactive environments resist the leakage and saturation problems of static reasoning benchmarks, but does not present a stronger benchmark-specific anti-contamination mechanism than that
- Reliability or comparability concerns: the benchmark paper couples new tasks with a new scaffold, so the reported gains mix environment difficulty with Agent-ExpVer effectiveness; the paper also contains some counting ambiguity about total episode numbers between sections

## 7. Main contributions
- Contribution 1: Introduces two dynamic, partially observable game tasks for evaluating adaptive reasoning under uncertainty.
- Contribution 2: Proposes Agent-ExpVer, a three-agent workflow for experience abstraction, validation, and truth maintenance.
- Contribution 3: Reports both model and human baselines, along with ablations that show how much the scaffold contributes.

## 8. Main findings and failure modes
- Core empirical takeaway: stronger models do better, but even top systems still trail humans, and Agent-ExpVer yields notable gains on both maze navigation and match-2; the paper therefore demonstrates dynamic-reasoning difficulty together with scaffold effectiveness, not a clean benchmark-only ranking.
- Notable model failure mode 1: models explore inefficiently in the maze task, taking many steps or failing to convert exploration into successful completion
- Notable model failure mode 2: in match-2, models struggle with compound objectives where immediate eliminations can conflict with long-term score maximization
- Notable model failure mode 3: performance improves substantially under full-vision ablations or scaffold support, showing that partial observability and memory are central bottlenecks
- Does this paper reveal a benchmark-design limitation as well? yes; because the benchmark and the learning workflow are introduced together, it is difficult to separate raw benchmark difficulty from scaffold-driven improvement

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Only as a narrow contrast case showing why dynamic interactive tasks are harder to saturate than static reasoning sets.
- Best use in Section 1 (taxonomy and evolutionary levels): Useful as a narrow dynamic-evaluation branch rather than as a major stage in the main historical narrative.
- Best use in Section 2 (core capabilities evaluated by games): Supports discussion of exploration, partial observability, and multi-objective decision-making in text-based interactive settings.
- Best use in Section 3 (interaction and evaluation paradigm): Good example of a benchmark where prompt interface, memory scaffold, and environment design all jointly determine performance.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Strong support for the claim that benchmark papers should disentangle environment difficulty from workflow engineering.

## 10. Relation to nearby papers
- Closest predecessor(s): SmartPlay, GameArena, Agent-Pro, and other dynamic or game-based reasoning evaluations
- Closest follow-up(s): future dynamic reasoning benchmarks that separate benchmark definition from online-learning scaffolds more cleanly
- Best comparison targets inside our corpus: MazeEval, GameTraversalBenchmark, ReasoningViaVideo, DeepPHY
- What this paper uniquely adds relative to neighbors: It combines dynamic game diagnostics with an explicit online rule-distillation scaffold, then makes the benchmark-method coupling itself part of the empirical story through TruthWeaver and Full-Vision ablations.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- EvoEmpirBench contains two tasks: a locally observable 9 x 9 maze-navigation game and an 8 x 8 match-2 elimination game.
- Each task has Easy, Medium, and Hard settings, and the experiment section reports 30 evaluation instances per level for 90 instances per task.
- The paper introduces Agent-ExpVer with three agents - GeoLink, InsightForce, and TruthWeaver - to collect experience, summarize it, and maintain reusable truths.
- EEB supports both human and agent operation, and the experiment section reports human baselines for both games.
- Reported metrics include success rate and average score for both tasks, plus task-specific efficiency and interaction metrics such as exploration, remaining HP, and API efficiency.
- The paper also includes control ablations such as removing TruthWeaver and revealing Full-Vision or removing props to test how much benchmark constraints drive performance.

### 11.2 Our synthesis / interpretation
- EvoEmpirBench is most useful as a contrast paper on dynamic evaluation design, not as a central benchmark lineage paper.
- Its strongest survey value is methodological: it shows how easily benchmark evaluation, memory support, and workflow engineering can become inseparable in agent papers.

### 11.3 Uncertain or needs re-check
- Section 3 describes a total of 120 diverse task episodes, while the experiment section reports 30 instances per level and 90 instances per task; if exact corpus accounting matters, re-check the released data and supplement.
- If we later need exact gains from removing TruthWeaver, revealing Full-Vision, or disabling props, re-check Tables 4 to 7 and the appendix prompts.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? No immediate reread is required unless we later need exact ablation numbers or want to compare benchmark difficulty against scaffold contribution in detail.
- Which section to read next if needed: 3 / 4 / 5 / ablation tables
- Follow-up question(s): When we discuss dynamic game evaluation, should EvoEmpirBench be cited mainly for its environments, or mainly for the cautionary example that scaffold and benchmark are co-designed?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P2
- Reading depth: deep
- Batch ID: B08
- Outline sections: 2,3,4
- Survey role: contrast
- Paper card path: `paper_cards/B08/EvoEmpirBench.md`
- Check status: unchecked
- Last updated: 2026-04-19
