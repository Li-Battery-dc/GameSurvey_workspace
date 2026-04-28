# MCU MCU: An Evaluation Framework for Open-Ended Game Agents

## 0. Metadata
- Date: 2025/05
- Venue: ICML 2025
- Authors: Xinyue Zheng, Haowei Lin, Kaichen He, Zihao Wang, Zilong Zheng, Yitao Liang
- Paper link: https://arxiv.org/pdf/2310.08367v4
- Code link: https://github.com/CraftJarvis/MCU
- Reading depth: deep
- Card status: finalized
- Confidence in this card: high
- Review gate label: strong

## 1. One-paragraph benchmark summary
- MCU turns Minecraft into a large-scale benchmark for open-ended game agents by combining thousands of executable atomic tasks, compositional task generation, and an automatic video-based evaluator. The framework collects 3,452 atomic tasks across 11 major categories and 41 subcategories, varies difficulty through task configuration generation, and uses a VLM-based AutoEval procedure aligned to human judgments. For this survey, MCU is a key representative of open-ended, task-compositional benchmarking in a raw embodied environment.

## 2. Position in our survey
- Why-games relevance: Minecraft supports enormous state diversity, human-like control, and creative open-ended tasks that are hard to reduce to fixed benchmark labels.
- Historical stage: ecological agent benchmark
- Benchmark level(s): L4 visual agency / L5 open-ended task generalization
- Most relevant outline section(s): 0,1,2,3,4
- Role in corpus: representative

## 3. Design-space coding
### 3.1 Structure
- Form: World
- Construction: Generated
- Construction note: real Minecraft benchmark with generated task configurations
- Benchmark unit: task episode

### 3.2 Mechanics profile
- State visibility: partial
- Transition uncertainty: mixed
- Actor configuration: single-agent
- Incentive structure: N/A
- Temporal regime: real-time

### 3.3 Benchmark scope
- Scope: open-ended tasks
- Number of games / tasks: 3,452 atomic tasks plus compositional variants

### 3.4 Modality
- Observation modality: visual image
- Action modality: native control
- Perception burden retained: raw RGB observations, mouse-keyboard control, long-horizon exploration, creativity, error recovery
- Perception burden removed: some setup overhead through automated task instantiation

## 4. What this benchmark measures
- Primary capability target: open-ended task completion and intra-world generalization in Minecraft
- Secondary capability target(s): creativity, error recognition and correction, material use, efficiency
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? yes
- Does it test social reasoning / deception / cooperation? no
- Does it test visual grounding / spatial-temporal reasoning? yes
- Does it test long-horizon autonomy / task completion? yes
- Does it test real-time efficiency? partially
- Does it test cross-game transfer / open-ended generalization? partially; it stresses broad task generalization inside one world rather than transfer across different games
- Why is a game environment especially suitable here? Minecraft combines rich perception, open-ended objectives, and safe programmable task generation in one widely used environment.

## 5. Interaction paradigm
- Observation channel: 640x360 RGB frames through MineStudio
- Action channel: mouse and keyboard actions in unmodified Minecraft
- Interface type: GUI
- Agent scaffold allowed: other (the benchmark is agent-agnostic, but the native interface itself is raw RGB plus mouse-keyboard control)
- Is there privileged API access? no for evaluated agents; diagnostic state such as inventory and GUI status is available only for tracking, recording, and evaluation
- How close is the setup to human play? high; MCU preserves human-like observation and control more than most benchmark suites in this corpus
- Main ecological-validity trade-off: MCU is highly ecological, but automated task setup and VLM judging introduce benchmark-specific assumptions.

## 6. Evaluation protocol
- Main score: AutoEval task progress plus multi-dimensional task-quality ratings
- Auxiliary score(s): task progress, material selection and usage, action control, error recognition and correction, creative attempts, and efficiency
- Evaluation style: hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: human labels are used to validate AutoEval rather than as the primary gameplay baseline
- Automatic verifiability: mixed
- Calibration method: AutoEval is validated on 500 trajectories from 60 tasks with expert human annotations and reaches reported 91.5% average agreement on evaluation dimensions
- Anti-contamination argument: not central
- Reliability or comparability concerns: AutoEval is scalable, but benchmark conclusions depend partly on a VLM judge and on task-configuration quality

## 7. Main contributions
- Contribution 1: Collects 3,452 atomic tasks across 11 major categories and 41 subcategories.
- Contribution 2: Introduces a task-composition and task-configuration pipeline for scalable difficulty variation.
- Contribution 3: Builds AutoEval, a VLM-based automatic evaluator for open-ended Minecraft trajectories.

## 8. Main findings and failure modes
- Core empirical takeaway: even strong agents struggle as task diversity, composition, and difficulty increase, especially on creativity, efficiency, and error recovery beyond simple completion
- Notable model failure mode 1: agents improve on basic task completion and material usage but remain weak on creativity
- Notable model failure mode 2: error recognition and correction remain a major weakness
- Notable model failure mode 3: higher difficulty and novel task configurations degrade performance noticeably
- Does this paper reveal a benchmark-design limitation as well? yes; the move to scalable automatic evaluation is necessary, but it shifts trust onto the evaluator itself

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Strong evidence that games can support diverse, scalable agent evaluation because Minecraft combines a large open-world state space, human-like control, and programmable task instantiation.
- Best use in Section 1 (taxonomy and evolutionary levels): Important Level 5 example for single-world open-ended task generalization. It should be explicitly separated from cross-title transfer suites such as Orak/GameVerse and generated human-game platforms such as AI GameStore.
- Best use in Section 2 (core capabilities evaluated by games): Direct evidence that open-ended task competence decomposes into planning, tool/material use, action control, creativity, error recognition/correction, and efficiency rather than binary completion alone.
- Best use in Section 3 (interaction and evaluation paradigm): One of the best raw-control ecological benchmarks in the corpus: agents receive 640x360 RGB observations and use mouse-keyboard actions in unmodified Minecraft, while evaluation uses VLM judging over trajectory videos.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Supports discussion of VLM judges, task quality, scalable task generation, and why open-ended benchmarks need process-level evaluation beyond success rate.

## 10. Relation to nearby papers
- Closest predecessor(s): MineDojo and earlier Minecraft task benchmarks
- Closest follow-up(s): open-ended Minecraft and embodied agent evaluation platforms
- Best comparison targets inside our corpus: StarDojo, MineNPCTask, TeamCraft, GameWorld, TextQuests
- What this paper uniquely adds relative to neighbors: It makes large-scale task composition and automated open-ended evaluation central rather than incidental.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- MCU includes 3,452 atomic tasks, 11 major categories, and 41 subcategories, with compositional task generation for further scaling.
- The benchmark uses unmodified Minecraft with RGB observations and mouse-keyboard actions.
- Task configuration generation uses an LLM to instantiate environment prerequisites, random factors, and task descriptions, then verifies/refines configurations through simulator feedback.
- AutoEval evaluates trajectory videos with VLM-generated criteria and scores dimensions such as task progress, action control, error recognition and correction, creative attempts, task completion efficiency, and material selection/usage.
- AutoEval is reported to reach 91.5% alignment with human ratings and to provide multi-dimensional assessment beyond binary task success.
- The paper introduces MCU-Turbo as a canonical protocol with 80 atomic tasks and 20 compositional tasks under Simple and Hard regimes.

### 11.2 Our synthesis / interpretation
- MCU is especially valuable for the survey because it separates open-ended task diversity from open-ended evaluation, then tackles both explicitly.
- It is also one of the best cards for arguing that "success rate" alone is inadequate for open-ended game agents.
- For Level 5, use MCU as single-world open-ended task evidence rather than cross-game generalization evidence.

### 11.3 Uncertain or needs re-check
- MCU's strongest methodological claim still depends on a VLM judge and LLM-generated task configurations, so those components should stay visible in any survey use.
- Recheck Section 3.1 and Appendix F if we later need exact baseline identities or the hardest evaluation-mode settings.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? A later targeted reread is worthwhile because the AutoEval design will likely matter in drafting.
- Which section to read next if needed: 2.3 / 2.5 / 3.1
- Follow-up question(s): Should MCU anchor our discussion of automatic evaluation in open-ended taskss?

## 13. Registry sync
- Registry row synced: yes
- Registry status: finalized
- Priority: P1
- Reading depth: deep
- Batch ID: B06
- Outline sections: 0,1,2,3,4
- Survey role: representative
- Paper card path: `paper_cards/B06/MCU.md`
- Check status: unchecked
- Next action: draft-section
- Last updated: 2026-04-27
