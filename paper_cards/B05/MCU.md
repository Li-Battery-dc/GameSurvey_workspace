# MCU MCU: An Evaluation Framework for Open-Ended Game Agents

## 0. Metadata
- Date: 2025/05
- Venue: ICML 2025
- Authors: Xinyue Zheng, Haowei Lin, Kaichen He, Zihao Wang, Zilong Zheng, Yitao Liang
- Paper link: https://arxiv.org/pdf/2310.08367v4
- Code link: https://github.com/CraftJarvis/MCU
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: high
- Review gate label: strong

## 1. One-paragraph benchmark summary
- MCU turns Minecraft into a large-scale benchmark for open-ended game agents by combining thousands of executable atomic tasks, compositional task generation, and an automatic video-based evaluator. The framework collects 3,452 atomic tasks across 11 major categories and 41 subcategories, varies difficulty through task configuration generation, and uses a VLM-based AutoEval procedure aligned to human judgments. For this survey, MCU is a key representative of open-ended, task-compositional benchmarking in a raw embodied environment.

## 2. Position in our survey
- Why-games relevance: Minecraft supports enormous state diversity, human-like control, and creative open-ended tasks that are hard to reduce to fixed benchmark labels.
- Historical stage: open-ended benchmark expansion
- Narrative level(s): L2 strategic reasoning / L4 embodied multimodal interaction
- Most relevant outline section(s): 0,2,3,4
- Role in corpus: representative

## 3. Design-space coding
### 3.1 Environment structure
- Information structure: imperfect
- Transition structure: mixed
- Agent structure: single-agent
- Social structure: none
- Time structure: real-time

### 3.2 World structure
- World type(s): open world / crafting / embodied
- Real game / simulated game / designed task-game hybrid: real Minecraft benchmark with generated task configurations
- Benchmark unit: task episode

### 3.3 Benchmark scope
- Scope: open-ended task universe
- Number of games / tasks: 3,452 atomic tasks plus compositional variants
- Benchmark intent: diagnostic evaluation

### 3.4 Modality
- Primary modality: visual control
- Perception burden retained: raw RGB observations, mouse-keyboard control, long-horizon exploration, creativity, error recovery
- Perception burden removed: some setup overhead through automated task instantiation

## 4. What this benchmark measures
- Primary capability target: open-ended task completion and generalization in Minecraft
- Secondary capability target(s): creativity, error recognition and correction, material use, efficiency
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? yes
- Does it test social reasoning / deception / cooperation? no
- Does it test visual grounding / spatial-temporal reasoning? yes
- Does it test long-horizon autonomy / task completion? yes
- Does it test real-time efficiency? partially
- Does it test cross-game transfer / open-ended generalization? yes
- Why is a game environment especially suitable here? Minecraft combines rich perception, open-ended objectives, and safe programmable task generation in one widely used environment.

## 5. Interaction paradigm
- Observation channel: 640x360 RGB frames through MineStudio
- Action channel: mouse and keyboard actions in unmodified Minecraft
- Interface type: GUI
- Agent scaffold allowed: none
- Is there privileged API access? no
- How close is the setup to human play? high; MCU preserves human-like observation and control more than most benchmark suites in this corpus
- Main ecological-validity trade-off: MCU is highly ecological, but automated task setup and VLM judging introduce benchmark-specific assumptions.

## 6. Evaluation protocol
- Main score: AutoEval task assessment with task-success and multi-dimensional ratings
- Auxiliary score(s): task progress, material selection and usage, action control, error recognition and correction, creative attempts, and efficiency
- Evaluation style: hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: human labels are used to validate AutoEval rather than as the primary baseline
- Automatic verifiability: mixed
- Calibration method: AutoEval achieves reported 91.5% alignment with human judgments and is compared for cost and efficiency
- Anti-contamination argument: not central
- Reliability or comparability concerns: AutoEval is scalable, but benchmark conclusions depend partly on a VLM judge and on task-configuration quality

## 7. Main contributions
- Contribution 1: Collects 3,452 atomic tasks across 11 major categories and 41 subcategories.
- Contribution 2: Introduces a task-composition and task-configuration pipeline for scalable difficulty variation.
- Contribution 3: Builds AutoEval, a VLM-based automatic evaluator for open-ended Minecraft trajectories.

## 8. Main findings and failure modes
- Core empirical takeaway: even strong agents struggle as task diversity and difficulty increase, especially on higher-order dimensions beyond simple completion
- Notable model failure mode 1: agents improve on basic task completion and material usage but remain weak on creativity
- Notable model failure mode 2: error recognition and correction remain a major weakness
- Notable model failure mode 3: higher difficulty and novel task configurations degrade performance noticeably
- Does this paper reveal a benchmark-design limitation as well? yes; the move to scalable automatic evaluation is necessary, but it shifts trust onto the evaluator itself

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Strong evidence that open-world games can support diverse, scalable agent evaluation.
- Best use in Section 1 (taxonomy and evolutionary levels): Important step from small Minecraft task sets toward benchmark-scale coverage. Useful open-ended task-composition comparison point.
- Best use in Section 2 (core capabilities evaluated by games): Direct evidence for planning, creativity, and error correction as distinct axes.
- Best use in Section 3 (interaction and evaluation paradigm): One of the best raw-control ecological benchmarks in the corpus. Essential reference for automated evaluation in open-ended settings.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Supports discussion of VLM judges, task quality, and scalable evaluation design.

## 10. Relation to nearby papers
- Closest predecessor(s): MineDojo and earlier Minecraft task benchmarks
- Closest follow-up(s): open-ended Minecraft and embodied agent evaluation platforms
- Best comparison targets inside our corpus: AI GameStore, BALROG, Orak, PillagerBench
- What this paper uniquely adds relative to neighbors: It makes large-scale task composition and automated open-ended evaluation central rather than incidental.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- MCU includes 3,452 atomic tasks, 11 major categories, and 41 subcategories, with compositional task generation for further scaling.
- The benchmark uses unmodified Minecraft with RGB observations and mouse-keyboard actions.
- AutoEval is reported to reach 91.5% alignment with human ratings and to provide multi-dimensional assessment beyond binary task success.

### 11.2 Our synthesis / interpretation
- MCU is especially valuable for the survey because it separates open-ended task diversity from open-ended evaluation, then tackles both explicitly.
- It is also one of the best cards for arguing that "success rate" alone is inadequate for open-ended game agents.

### 11.3 Uncertain or needs re-check
- Recheck Section 3.1 and Appendix F if we later need exact baseline identities or the hardest evaluation-mode settings.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? A later targeted reread is worthwhile because the AutoEval design will likely matter in drafting.
- Which section to read next if needed: 2.3 / 2.5 / 3.1
- Follow-up question(s): Should MCU anchor our discussion of automatic evaluation in open-ended worlds?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P1
- Reading depth: deep
- Batch ID: B05
- Outline sections: 0,2,3,4
- Survey role: representative
- Paper card path: `paper_cards/B05/MCU.md`
- Next action: draft-section
- Last updated: 2026-04-05
