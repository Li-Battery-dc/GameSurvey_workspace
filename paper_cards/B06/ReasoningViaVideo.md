# ReasoningViaVideo Reasoning via Video: The First Evaluation of Video Models' Reasoning Abilities through Maze-Solving Tasks

## 0. Metadata
- Date: 2025/11
- Venue: arXiv
- Authors: Cheng Yang, Haiyuan Wan, Yiran Peng, Xin Cheng, Zhaoyang Yu, Jiayi Zhang, Junchi Yu, Xinlei Yu, Xiawu Zheng, Dongzhan Zhou, Chenglin Wu
- Paper link: https://arxiv.org/pdf/2511.15065v2
- Code link:
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: high
- Review gate label: usable

## 1. One-paragraph benchmark summary
- Reasoning via Video introduces VR-Bench, a maze-centered benchmark for testing whether video models can "reason via video" by generating trajectory videos rather than by outputting textual chains of thought or discrete actions. The benchmark contains 7,920 procedurally generated maze videos across five maze families - Regular Maze, Irregular Maze, Trapfield, 3D Maze, and Sokoban - with BFS-derived optimal paths rendered at 24 fps into 192-frame clips. Evaluation combines trajectory-matching metrics such as Exact Match, Success Rate, Precision Rate, and Step Deviation with rule-compliance scoring and Maze Fidelity, and the paper studies both supervised fine-tuning and test-time scaling. For this survey, VR-Bench is a useful contrast case for visual trajectory reasoning, but it should not be treated as an interactive game-agent benchmark.

## 2. Position in our survey
- Why-games relevance: Maze tasks provide explicit goals, procedural variation, and automatically checkable trajectories, making them useful for controlled visual reasoning evaluation.
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
- Time structure: hybrid

### 3.2 World structure
- World type(s): puzzle / maze
- Real game / simulated game / designed task-game hybrid: designed task-game hybrid rendered as trajectory videos
- Benchmark unit: trajectory

### 3.3 Benchmark scope
- Scope: curated suite
- Number of games / tasks: 7,920 procedurally generated videos across 5 maze families
- Benchmark intent: diagnostic evaluation

### 3.4 Modality
- Primary modality: video
- Perception burden retained: spatial layout reading, temporal continuity, trajectory tracking, and structural consistency across frames
- Perception burden removed: the benchmark does not require an agent to take discrete actions or interact with an evolving environment online

## 4. What this benchmark measures
- Primary capability target: spatial-temporal reasoning through generated visual trajectories
- Secondary capability target(s): path efficiency, rule compliance, structural consistency, and generalization across maze styles and difficulty shifts
- Does it test rule grounding / legal action generation? no
- Does it test strategic planning under uncertainty? no
- Does it test social reasoning / deception / cooperation? no
- Does it test visual grounding / spatial-temporal reasoning? yes
- Does it test long-horizon autonomy / task completion? no
- Does it test real-time efficiency? no
- Does it test cross-game transfer / open-ended generalization? no
- Why is a game environment especially suitable here? Procedurally generated mazes supply exact optimal paths and automatically checkable trajectory structure, so visual reasoning quality can be scored without subjective end-task judging.

## 5. Interaction paradigm
- Observation channel: maze images and task prompts that require the model to generate an entire reasoning trajectory as video
- Action channel: generated frame sequences representing a trajectory rather than discrete environment actions
- Interface type: hybrid
- Agent scaffold allowed: other (the paper studies supervised fine-tuning and diverse-sampling test-time scaling)
- Is there privileged API access? no
- How close is the setup to human play? low; the benchmark evaluates trajectory generation rather than closed-loop gameplay
- Main ecological-validity trade-off: VR-Bench preserves rich visual and temporal reasoning demands, but it removes online interaction and substitutes generated rollouts for actual agent control

## 6. Evaluation protocol
- Main score: Exact Match and Success Rate
- Auxiliary score(s): Precision Rate, Step Deviation, VLM-score for rule compliance, Maze Fidelity, and Pass@K under test-time scaling
- Evaluation style: completion rate / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: proprietary and open-source video models are compared against representative VLM baselines; no human gameplay baseline is used
- Automatic verifiability: mixed
- Calibration method: five maze families, procedural generation, difficulty/texture/maze-type generalization splits, fixed 192-frame clips, and varying test-time sample budgets
- Anti-contamination argument: the benchmark relies on procedural generation, multiple visual themes, and held-out shifts in texture, maze type, and difficulty
- Reliability or comparability concerns: rule-compliance scoring depends on a prompt-based VLM judge, and the benchmark's maze-only scope limits how far results can be generalized to interactive game agents

## 7. Main contributions
- Contribution 1: Proposes the reasoning-via-video paradigm, where reasoning is expressed through sequential frame generation instead of textual continuation.
- Contribution 2: Builds VR-Bench, a large procedurally generated maze-video benchmark with trajectory-level metrics and robustness splits.
- Contribution 3: Shows that fine-tuned video models and test-time diverse sampling substantially improve performance on visual trajectory reasoning tasks.

## 8. Main findings and failure modes
- Core empirical takeaway: fine-tuned video models outperform strong VLM baselines on many hard maze tasks, but their gains reflect better trajectory generation rather than interactive agency.
- Notable model failure mode 1: generated trajectories sometimes pass through walls, traps, or other infeasible regions
- Notable model failure mode 2: the moving object can disappear, reappear, or drift inconsistently across frames, breaking temporal coherence
- Notable model failure mode 3: maze layout itself can deform across frames, which is why the paper adds explicit Maze Fidelity and rule-compliance checks
- Does this paper reveal a benchmark-design limitation as well? yes; it rigorously measures spatial reasoning in generated rollouts, but it does not tell us whether the same models can act as interactive agents in comparable environments

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Only as a contrast case showing how game-like tasks can support automatically scored multimodal reasoning diagnostics.
- Best use in Section 1 (taxonomy and evolutionary levels): Useful as an offshoot where game structure is repurposed for generative visual reasoning instead of agent control.
- Best use in Section 2 (core capabilities evaluated by games): Strong contrast for spatial-temporal reasoning, trajectory fidelity, and rule compliance under visual generation.
- Best use in Section 3 (interaction and evaluation paradigm): A clear example of a benchmark that keeps perceptual structure but removes action interfaces, making generated rollouts themselves the evaluation target.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Supports the caution that strong visual reasoning in generated trajectories does not imply strong interactive agency.

## 10. Relation to nearby papers
- Closest predecessor(s): maze-style visual reasoning and trajectory-generation benchmarks
- Closest follow-up(s): broader multimodal or embodied reasoning benchmarks that move from generated trajectories back toward interactive control
- Best comparison targets inside our corpus: `GameplayQA`, `DeepPHY`, `TowerMind`, `Balrog`
- What this paper uniquely adds relative to neighbors: It evaluates reasoning through generated visual rollouts, adds explicit rule-compliance and Maze Fidelity scoring, and shows a test-time scaling effect for video-based reasoning.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- VR-Bench contains 7,920 procedurally generated videos spanning Regular Maze, Irregular Maze, Trapfield, 3D Maze, and Sokoban.
- The benchmark renders BFS-derived optimal paths into 192-frame, 24 fps videos and evaluates generated trajectories using Exact Match, Success Rate, Precision Rate, and Step Deviation.
- The paper also evaluates rule compliance with a VLM judge and adds Maze Fidelity to measure background structural consistency across frames.
- The study reports supervised fine-tuning results and Pass@K gains from diverse test-time sampling.

### 11.2 Our synthesis / interpretation
- VR-Bench is useful in this survey mainly as a boundary case: it is game-structured and diagnostically rigorous, but it is not an agent-play benchmark in the usual sense.
- Its strongest survey value is in the interaction section, where it helps separate visual reasoning benchmarks from actual gameplay benchmarks.

### 11.3 Uncertain or needs re-check
- If we later need exact per-task or per-difficulty scores for specific video models, re-check Table 1 and the appendix generalization tables.
- If we need to compare judge dependence in detail, re-check the VLM-score prompting protocol and the Maze Fidelity computation section.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? No immediate reread is required unless we later want to compare trajectory-level evaluation metrics or test-time scaling in detail.
- Which section to read next if needed: 3.2 / 4 / 8 / 9 / 10
- Follow-up question(s): When we discuss multimodal evaluation, should VR-Bench appear in the main game-benchmark table or in a narrower subsection on video-generation diagnostics?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P2
- Reading depth: deep
- Batch ID: B06
- Outline sections: 2,3,4
- Survey role: contrast
- Paper card path: `paper_cards/B06/ReasoningViaVideo.md`
- Check status: unchecked
- Last updated: 2026-04-09
