# EvoEmpirBench EvoEmpirBench: Dynamic Spatial Reasoning with Agent-ExpVer

## 0. Metadata
- Date: 2025/09
- Venue: arXiv
- Authors: Pukun Zhao, Longxiang Wang, Miaowei Wang, Chen Chen, Fanqing Zhou, Haojian Huang
- Paper link: https://arxiv.org/pdf/2509.12718v1
- Code link:
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: high
- Review gate label: usable

## 1. One-paragraph benchmark summary
- EvoEmpirBench is a dynamic reasoning benchmark built around two interactive tasks: a partially observable maze-navigation game and a match-2 elimination game. It is paired with Agent-ExpVer, a three-agent online-learning workflow that interacts with the environment, distills reusable rules, and updates structured memory without parameter tuning. The benchmark emphasizes adaptive behavior, exploration, and multi-step planning in dynamic settings rather than static reasoning accuracy. For this survey, EvoEmpirBench is a useful contrast case for narrow dynamic reasoning tasks and for the way benchmark results are entangled with an explicit agentic scaffold.

## 2. Position in our survey
- Why-games relevance: Dynamic games make it possible to test exploration, risk management, and adaptation under partial observability with automatically measurable outcomes.
- Historical stage: diagnostic capability probe
- Narrative level(s): L2 strategic reasoning
- Most relevant outline section(s): 3,4,6
- Role in corpus: contrast

## 3. Design-space coding
### 3.1 Environment structure
- Information structure: imperfect
- Transition structure: mixed
- Agent structure: single-agent
- Social structure: N/A
- Time structure: turn-based

### 3.2 World structure
- World type(s): puzzle / maze
- Real game / simulated game / designed task-game hybrid: designed task-game hybrid
- Benchmark unit: episode

### 3.3 Benchmark scope
- Scope: curated suite
- Number of games / tasks: 2 tasks with 3 difficulty levels each and 30 instances per level
- Benchmark intent: diagnostic evaluation

### 3.4 Modality
- Primary modality: text
- Perception burden retained: partial observability, state tracking, tool and resource management, and multi-step planning
- Perception burden removed: no raw visual perception is required; state is delivered through text prompts and APIs

## 4. What this benchmark measures
- Primary capability target: adaptive reasoning in dynamic partially observable game environments
- Secondary capability target(s): exploration, risk-reward trade-offs, score optimization, and online abstraction of reusable rules
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? yes
- Does it test social reasoning / deception / cooperation? no
- Does it test visual grounding / spatial-temporal reasoning? no
- Does it test long-horizon autonomy / task completion? yes
- Does it test real-time efficiency? no
- Does it test cross-game transfer / open-ended generalization? no
- Why is a game environment especially suitable here? The maze and match-2 tasks force repeated action choices under dynamic constraints while keeping progress, score, and failure states measurable.

## 5. Interaction paradigm
- Observation channel: text prompts describing current game state, objectives, available actions, and environment feedback
- Action channel: environment actions selected through the benchmark interface
- Interface type: API / hybrid
- Agent scaffold allowed: memory / reflection / other
- Is there privileged API access? yes
- How close is the setup to human play? low to medium; the tasks are game-like, but interaction is prompt-and-API mediated rather than GUI play
- Main ecological-validity trade-off: EvoEmpirBench increases dynamism and partial observability, but its text-first interface and scaffolded workflow make it more diagnostic than ecological

## 6. Evaluation protocol
- Main score: success rate and average score
- Auxiliary score(s): maze metrics such as steps, exploration, gold, remaining HP, kills, and barriers; match-2 metrics such as remaining-step ratio, score per step, clear per step, and API efficiency
- Evaluation style: completion rate / native score / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: human baselines, proprietary and open-source LLM baselines, and ablations with versus without Agent-ExpVer
- Automatic verifiability: high
- Calibration method: fixed difficulty levels, 30 instances per level, broad model roster, and explicit with-versus-without-workflow comparisons
- Anti-contamination argument: the benchmark argues for dynamic interactive environments as a counterweight to static benchmark leakage and saturation
- Reliability or comparability concerns: part of the reported gains come from the Agent-ExpVer workflow, so the benchmark paper mixes environment difficulty with scaffold effectiveness

## 7. Main contributions
- Contribution 1: Introduces two dynamic reasoning games aimed at exploration, planning, and adaptation under uncertainty.
- Contribution 2: Proposes Agent-ExpVer, a three-agent workflow for online abstraction and memory-guided adaptation.
- Contribution 3: Benchmarks both proprietary and open-source models against humans and shows the effect of the workflow on game performance.

## 8. Main findings and failure modes
- Core empirical takeaway: stronger models perform better, but even top systems remain below humans, and Agent-ExpVer yields consistent gains on both maze and match-2 tasks.
- Notable model failure mode 1: weaker models take many more steps and still fail to complete tasks reliably
- Notable model failure mode 2: models struggle with compound objectives in match-2, where immediate elimination efficiency can conflict with long-term score maximization
- Notable model failure mode 3: smaller models lag substantially even when the workflow is added
- Does this paper reveal a benchmark-design limitation as well? yes; because the paper couples a new benchmark with a new workflow, it is harder to separate raw benchmark difficulty from scaffold-driven performance improvements

## 9. Why this paper matters for our survey
- Best use in Section 0 (why games): Good example of why dynamic games remain harder than static reasoning datasets.
- Best use in Section 1 (historical evolution): Useful as a later narrow branch focused on adaptive online reasoning rather than broad benchmark suites.
- Best use in Section 2 (design space): Helps define the boundary between dynamic single-agent diagnostics and broader game-benchmark platforms.
- Best use in Section 3 (capability targets): Supports discussion of exploration, resource trade-offs, and adaptation under partial observability.
- Best use in Section 4 (interaction paradigm): Useful when discussing prompt-and-API game interfaces and scaffolded memory.
- Best use in Section 5 (evaluation protocol): Highlights how game benchmarks can expose multiple complementary metrics instead of one scalar score.
- Best use in Section 6/7 (limitations and future): Supports the argument that benchmark papers should disentangle environment difficulty from workflow engineering.

## 10. Relation to nearby papers
- Closest predecessor(s): dynamic text-game and online-learning agent benchmarks
- Closest follow-up(s): later dynamic or scaffold-heavy game diagnostics
- Best comparison targets inside our corpus: [DeepPHY](D:/research_root/GameSurvey/workspace/paper_cards/B06/DeepPHY.md), [TowerMind](D:/research_root/GameSurvey/workspace/paper_cards/B06/TowerMind.md), [LMGameBench](D:/research_root/GameSurvey/workspace/paper_cards/B08/LMGameBench.md), [PuzzlePlex](D:/research_root/GameSurvey/workspace/paper_cards/B05/PuzzlePlex.md)
- What this paper uniquely adds relative to neighbors: It combines dynamic game diagnostics with an explicit online rule-distillation workflow and shows both the benchmark and the scaffold together.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- EvoEmpirBench contains two tasks, maze navigation and match-2 elimination, each with three difficulty levels and 30 instances per level.
- The paper evaluates proprietary and open-source LLMs and reports human baselines as well as versions augmented by Agent-ExpVer.
- The evaluation includes task-specific metrics beyond success and score, such as exploration and health in maze navigation and API efficiency in match-2.

### 11.2 Our synthesis / interpretation
- EvoEmpirBench is more useful as a narrow dynamic-reasoning comparison paper than as a central benchmark lineage paper.
- It is especially useful for the survey’s limitations discussion because it blurs the line between benchmark design and scaffold design.

### 11.3 Uncertain or needs re-check
- Re-check Section 5 if we later need exact per-model deltas from Agent-ExpVer on both tasks.
- Its survey placement should remain explicit as partial-scope because the benchmark covers only two designed games.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? No immediate reread is required unless we later need exact ablation numbers for benchmark-versus-workflow comparisons.
- Which section to read next if needed: 3.3 / 5 / Appendix B
- Follow-up question(s): Should EvoEmpirBench be cited mainly for dynamic-evaluation design, or also for the risks of benchmark and scaffold co-design?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P2
- Reading depth: deep
- Batch ID: B06
- Outline sections: 3,4,6
- Survey role: contrast
- Paper card path: `paper_cards/B06/EvoEmpirBench.md`
- Next action: draft-section
- Last updated: 2026-04-05
