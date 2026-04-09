# ReasoningViaVideo Reasoning via Video: The First Evaluation of Video Models' Reasoning Abilities through Maze-Solving Tasks

## 0. Metadata
- Date: 2025/11
- Venue: arXiv
- Authors: Cheng Yang, Haiyuan Wan, Yiran Peng, Xin Cheng, Zhaoyang Yu, Jiayi Zhang, Junchi Yu, Xinlei Yu, Xiawu Zheng, Dongzhan Zhou, Chenglin Wu
- Paper link: https://arxiv.org/pdf/2511.15065v2
- Code link:
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: medium
- Review gate label: usable

## 1. One-paragraph benchmark summary
- Reasoning via Video introduces VR-Bench, a maze-centered benchmark for testing whether video generation models can "reason via video" rather than via text. The benchmark contains 7,920 procedurally generated videos across five maze families and multiple visual styles, and it evaluates generated trajectories against optimal paths using exact-match, success, efficiency, and rule-compliance metrics. The paper also fine-tunes a video model and studies test-time scaling through diverse sampling. For this survey, the paper is best used as a multimodal contrast case: it is clearly game-like and evaluation-heavy, but it measures video-trajectory reasoning rather than interactive gameplay agents.

## 2. Position in our survey
- Why-games relevance: Maze tasks provide explicit goals, procedural variation, and objectively checkable trajectories, which makes them useful for controlled visual-reasoning evaluation.
- Historical stage: diagnostic capability probe
- Narrative level(s): L4 visual agency
- Most relevant outline section(s): 2,3,4
- Role in corpus: contrast

## 3. Design-space coding
### 3.1 Environment structure
- Information structure: perfect
- Transition structure: deterministic
- Agent structure: single-agent
- Social structure: N/A
- Time structure: turn-based

### 3.2 World structure
- World type(s): puzzle / maze
- Real game / simulated game / designed task-game hybrid: designed task-game hybrid rendered as video tasks
- Benchmark unit: trajectory

### 3.3 Benchmark scope
- Scope: curated suite
- Number of games / tasks: 7,920 procedurally generated videos across 5 maze types
- Benchmark intent: diagnostic evaluation

### 3.4 Modality
- Primary modality: video
- Perception burden retained: spatial layout reading, temporal continuity, trajectory tracking, and structural consistency
- Perception burden removed: the benchmark does not require interactive control or open-ended environment manipulation

## 4. What this benchmark measures
- Primary capability target: spatial-temporal reasoning through video generation
- Secondary capability target(s): path efficiency, rule compliance, structure preservation, and out-of-domain generalization across styles and maze types
- Does it test rule grounding / legal action generation? partially
- Does it test strategic planning under uncertainty? partially
- Does it test social reasoning / deception / cooperation? no
- Does it test visual grounding / spatial-temporal reasoning? yes
- Does it test long-horizon autonomy / task completion? no
- Does it test real-time efficiency? no
- Does it test cross-game transfer / open-ended generalization? partially
- Why is a game environment especially suitable here? Mazes yield exact optimal paths and procedural variation, so visual-reasoning trajectories can be scored without subjective judgment.

## 5. Interaction paradigm
- Observation channel: maze tasks rendered as videos with style variations and trace-reasoning objectives
- Action channel: generated video trajectories or trajectory-like rollouts rather than discrete game actions
- Interface type: hybrid
- Agent scaffold allowed: other
- Is there privileged API access? no
- How close is the setup to human play? low; the benchmark studies generated video reasoning rather than direct game interaction
- Main ecological-validity trade-off: VR-Bench keeps strong spatial structure and objective evaluation, but it does so by replacing gameplay interaction with video generation

## 6. Evaluation protocol
- Main score: Exact Match and Success Rate
- Auxiliary score(s): Precision Rate, Step Deviation, VLM-score for rule compliance, Maze Fidelity, and Pass@K under diverse sampling
- Evaluation style: completion rate / milestone / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: proprietary and open-source video models are compared against representative VLMs, with supervised fine-tuned variants studied explicitly
- Automatic verifiability: mixed
- Calibration method: trajectory extraction against optimal paths, fixed maze families, difficulty splits, texture shifts, and test-time sampling budgets
- Anti-contamination argument: the benchmark uses procedural generation, varied maze styles, and distribution-shift evaluations
- Reliability or comparability concerns: some rule-compliance scoring depends on a VLM judge, and the maze-only scope narrows generality

## 7. Main contributions
- Contribution 1: Proposes the "reasoning via video" paradigm and a dedicated benchmark, VR-Bench.
- Contribution 2: Builds a procedurally generated maze-video dataset with fine-grained trajectory-level metrics.
- Contribution 3: Shows supervised fine-tuning and diverse test-time sampling can materially improve video-reasoning performance.

## 8. Main findings and failure modes
- Core empirical takeaway: fine-tuned video models outperform strong VLM baselines on difficult maze tasks and benefit from test-time scaling.
- Notable model failure mode 1: generated trajectories sometimes break maze walls or violate path constraints
- Notable model failure mode 2: objects may disappear, reappear, or move inconsistently across frames
- Notable model failure mode 3: structural consistency of the maze can drift across generated frames
- Does this paper reveal a benchmark-design limitation as well? yes; the benchmark is rigorous for spatial reasoning, but it currently centers on maze tasks and not on broader interactive gameplay

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Shows that even stylized game tasks can create objective multimodal reasoning evaluations unavailable in static QA.
- Best use in Section 1 (taxonomy and evolutionary levels): Useful as an offshoot where game-like tasks are repurposed for generative video reasoning rather than action-taking agents. Helps separate action-agent benchmarks from trajectory-generation benchmarks.
- Best use in Section 2 (core capabilities evaluated by games): Strong contrast for spatial-temporal reasoning and rule compliance.
- Best use in Section 3 (interaction and evaluation paradigm): Clarifies that some multimodal benchmarks remove action interfaces entirely and instead evaluate generated rollouts. Useful for discussing exact-path metrics, efficiency metrics, and judge-assisted rule-compliance scoring.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Supports the claim that strong video reasoning does not automatically imply strong interactive agency.

## 10. Relation to nearby papers
- Closest predecessor(s): visual reasoning and maze-style trajectory benchmarks
- Closest follow-up(s): broader video or embodied reasoning benchmarks that move beyond maze-only tasks
- Best comparison targets inside our corpus: [DeepPHY](D:/research_root/GameSurvey/workspace/paper_cards/B06/DeepPHY.md), [TowerMind](D:/research_root/GameSurvey/workspace/paper_cards/B06/TowerMind.md), [Balrog](D:/research_root/GameSurvey/workspace/paper_cards/B03/Balrog.md), [GameplayQA](D:/research_root/GameSurvey/workspace/paper_cards/B03/GameplayQA.md)
- What this paper uniquely adds relative to neighbors: It evaluates reasoning by generated visual rollouts, not by selected actions, and makes test-time scaling a first-class analysis variable.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- VR-Bench contains 7,920 procedurally generated videos spanning Regular Maze, Irregular Maze, 3D Maze, Sokoban, and Trapfield tasks.
- The paper evaluates Exact Match, Success Rate, Precision Rate, Step Deviation, a VLM-based rule-compliance score, and Maze Fidelity.
- The authors report that supervised fine-tuning improves the open-source video model substantially and that diverse sampling at inference gives roughly 10% to 20% gains.

### 11.2 Our synthesis / interpretation
- This paper is valuable mainly as a boundary marker for the survey: it is about game-like reasoning evaluation, but not about game-playing agents in the usual benchmark sense.
- It helps sharpen the interaction-paradigm section by showing that "reasoning in games" can mean trajectory generation rather than action control.

### 11.3 Uncertain or needs re-check
- If we later need exact per-maze scores for video models versus VLMs, re-check Tables 1 to 5.
- Its fit to the main survey narrative should remain explicit as a comparison case rather than a central benchmark lineage.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? Only if we later need a more careful comparison between video-generation reasoning and action-taking multimodal agents.
- Which section to read next if needed: 3.2 / 5 / 8
- Follow-up question(s): Should VR-Bench appear in the main benchmark taxonomy, or only in a subsection on multimodal diagnostic spillover?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P2
- Reading depth: deep
- Batch ID: B06
- Outline sections: 2,3,4
- Survey role: contrast
- Paper card path: `paper_cards/B06/ReasoningViaVideo.md`
- Next action: draft-section
- Last updated: 2026-04-05
