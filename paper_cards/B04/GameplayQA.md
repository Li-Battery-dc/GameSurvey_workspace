# GameplayQA GameplayQA: A Benchmarking Framework for Decision-Dense POV-Synced Multi-Video Understanding of 3D Virtual Agents

## 0. Metadata
- Date: 2026/03
- Venue: arXiv
- Authors: Yunzhe Wang, Runhui Xu, Kexin Zheng, Tianyi Zhang, Jayavibhav Niranjan Kogundi, Soham Hans, Volkan Ustun
- Paper link: https://arxiv.org/pdf/2603.24329v1
- Code link: https://hats-ict.github.io/gameplayqa/
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: high
- Review gate label: usable

## 1. One-paragraph benchmark summary
- GameplayQA evaluates whether multimodal models can understand dense, first-person, multi-agent gameplay videos well enough to support agent-centric perception and temporal reasoning. It builds 2,365 multiple-choice QA pairs from synchronized multi-POV footage spanning nine commercial 3D games, organized into fifteen task categories over Self, Other, and World entities. It is not an active-play benchmark: the model only answers diagnostic questions about gameplay videos. In the survey, this paper is best used as a perceptual boundary case for visual game-agent evaluation rather than as evidence of end-to-end game-playing competence.

## 2. Position in our survey
- Why-games relevance: Games create dense temporally entangled streams of self-actions, other-agent behavior, and world events that are hard to approximate with generic video QA.
- Historical stage: diagnostic capability probe
- Narrative level(s): L4 visual agency
- Most relevant outline section(s): 2,3,4
- Role in corpus: representative

## 3. Design-space coding
### 3.1 Environment structure
- Information structure: mixed
- Transition structure: mixed
- Agent structure: multi-agent
- Social structure: mixed
- Time structure: real-time

### 3.2 World structure
- World type(s): other
- Real game / simulated game / designed task-game hybrid: real commercial games turned into a video benchmark
- Benchmark unit: question

### 3.3 Benchmark scope
- Scope: curated suite
- Number of games / tasks: 9 games, 2.4K QA pairs, 15 task categories

### 3.4 Modality
- Primary modality: video
- Perception burden retained: first-person video, synchronized multi-view timing, self/other/world event tracking
- Perception burden removed: direct action generation and control

## 4. What this benchmark measures
- Primary capability target: agent-centric visual grounding and temporal reasoning
- Secondary capability target(s): multi-agent attribution, first-person state tracking, hallucination resistance
- Does it test rule grounding / legal action generation? no
- Does it test strategic planning under uncertainty? no
- Does it test social reasoning / deception / cooperation? no; it probes other-agent attribution at the perceptual level rather than social strategy
- Does it test visual grounding / spatial-temporal reasoning? yes
- Does it test long-horizon autonomy / task completion? no
- Does it test real-time efficiency? no
- Does it test cross-game transfer / open-ended generalization? no
- Why is a game environment especially suitable here? Competitive 3D games produce rapid state changes and overlapping events that stress temporal grounding more than static vision tasks.

## 5. Interaction paradigm
- Observation channel: synchronized first-person gameplay videos plus a question
- Action channel: none; the model selects an answer for a diagnostic QA item
- Interface type: natural language
- Agent scaffold allowed: none
- Is there privileged API access? no
- How close is the setup to human play? low to medium; observation realism is high, but there is no action loop
- Main ecological-validity trade-off: GameplayQA keeps the hardest perceptual side of agent play but stops short of actual decision making and control.

## 6. Evaluation protocol
- Main score: QA accuracy
- Auxiliary score(s): category-wise breakdowns, distractor-type analysis, entity-type analysis, and ablations over missing or shuffled video information
- Evaluation style: multiple-choice accuracy / diagnostic
- Human baseline / AI anchor / self-play / model-vs-model setup: fixed QA benchmark with frontier MLLM comparison and a human reference score
- Automatic verifiability: high
- Calibration method: dense human-in-the-loop timeline annotation, manually aligned multi-POV labeling, and blind filtering to remove question-only language priors
- Anti-contamination argument: the benchmark combines synchronized gameplay footage with blind filtering and visual ablations, so questions cannot be solved reliably from language priors alone
- Reliability or comparability concerns: annotation errors can propagate through template-based QA generation, and free-form model outputs are post-processed into option letters

## 7. Main contributions
- Contribution 1: Builds a dense multi-POV 3D gameplay video benchmark centered on agent perception.
- Contribution 2: Organizes annotations around a Self / Other / World taxonomy.
- Contribution 3: Provides error analysis for hallucinations and attribution failures in gameplay understanding.

## 8. Main findings and failure modes
- Core empirical takeaway: Current multimodal models still show a meaningful gap to humans on dense gameplay video understanding, especially on temporal and cross-video reasoning.
- Notable model failure mode 1: confusing self-actions with other-agent actions
- Notable model failure mode 2: weak temporal grounding across concurrent events
- Notable model failure mode 3: hallucinating objects or causal relationships in busy scenes
- Does this paper reveal a benchmark-design limitation as well? yes; it is a perceptual proxy, not a full agent benchmark

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Shows that gameplay video is a rich source of dynamic perception challenges.
- Best use in Section 1 (taxonomy and evolutionary levels): Useful as a boundary case showing how far visual-game evaluation can move toward perception-heavy video understanding without closing the action loop.
- Best use in Section 2 (core capabilities evaluated by games): Direct fit for visual grounding, temporal reasoning, and multi-agent attribution.
- Best use in Section 3 (interaction and evaluation paradigm): Important counterexample to active-play benchmarks. Relevant for diagnostic annotation pipelines, blind filtering, and distractor-based hallucination analysis.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Supports the claim that perception is still a bottleneck even before control.

## 10. Relation to nearby papers
- Closest predecessor(s): MarioQA, EgoSchema, MVU-Eval, and other egocentric or video-QA benchmarks
- Closest follow-up(s): nearby visual game-agent papers that reintroduce control, such as GameVerse, StarBench, and FlashAdventure
- Best comparison targets inside our corpus: FlashAdventure, StarBench, Balrog, VideoGameBench
- What this paper uniquely adds relative to neighbors: It isolates dense first-person multi-POV perception, agent-role attribution, and hallucination diagnosis more cleanly than the active-play papers in this batch.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- GameplayQA builds 2,365 multiple-choice QA pairs from synchronized gameplay videos spanning nine commercial 3D games and 100 video instances.
- The benchmark uses a six-primitive Self-Other-World label system and organizes questions into fifteen categories over three cognitive levels.
- The paper reports a substantial human-model gap: the best model reaches 71.3% overall accuracy versus 80.5% for humans.
- The evaluation includes blind filtering and visual ablations showing the benchmark cannot be solved reliably from language priors alone.

### 11.2 Our synthesis / interpretation
- GameplayQA should not be treated as evidence that a model can play games well; it is evidence that dense gameplay perception and attribution remain hard even before action is introduced.
- It is most useful as a supporting card for visual grounding and benchmark-design discussion, not as a core ecological play benchmark.

### 11.3 Uncertain or needs re-check
- Recheck the appendix if we later need per-game category counts or want to cite the small 213-question cross-domain transfer experiment separately from the main gameplay benchmark.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? No immediate reread; the benchmark scope and role are already clear.
- Which section to read next if needed: 3 / 4 / limitations
- Follow-up question(s): Where should the survey draw the boundary between agent-centric video understanding and actual game-agent evaluation?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P1
- Reading depth: deep
- Batch ID: B04
- Outline sections: 2,3,4
- Survey role: representative
- Paper card path: `paper_cards/B04/GameplayQA.md`
- Next action: draft-section
- Last updated: 2026-04-10
