# GameplayQA GameplayQA: A Benchmarking Framework for Decision-Dense POV-Synced Multi-Video Understanding of 3D Virtual Agents

## 0. Metadata
- Date: 2026/03
- Venue: arXiv
- Authors: Yunzhe Wang, Runhui Xu, Kexin Zheng, Tianyi Zhang, Jayavibhav Niranjan Kogundi, Soham Hans, Volkan Ustun
- Paper link: https://arxiv.org/pdf/2603.24329v1
- Code link: https://hats-ict.github.io/gameplayqa/
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: medium
- Review gate label: usable

## 1. One-paragraph benchmark summary
- GameplayQA evaluates whether multimodal models can understand dense, first-person, multi-agent gameplay videos well enough to support agent-like reasoning. The benchmark synchronizes multi-POV footage from nine commercial 3D games, annotates actions, states, objects, and events on multiple tracks, and generates 2.4K diagnostic QA pairs across fifteen task categories. It is not an active-play benchmark; instead, it is a perceptual proxy focused on Self, Other, and World understanding under temporal pressure. In the survey, this paper is most useful as a boundary case between visual game-agent evaluation and high-end video understanding.

## 2. Position in our survey
- Why-games relevance: Games create dense temporally entangled streams of self-actions, other-agent behavior, and world events that are hard to approximate with generic video QA.
- Historical stage: diagnostic capability probe
- Narrative level(s): L4 visual agency
- Most relevant outline section(s): 3,4,5,6
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
- Benchmark intent: diagnostic evaluation

### 3.4 Modality
- Primary modality: video
- Perception burden retained: first-person video, synchronized multi-view timing, self/other/world event tracking
- Perception burden removed: direct action generation and control

## 4. What this benchmark measures
- Primary capability target: agent-centric visual grounding and temporal reasoning
- Secondary capability target(s): multi-agent attribution, first-person state tracking, hallucination resistance
- Does it test rule grounding / legal action generation? no
- Does it test strategic planning under uncertainty? no
- Does it test social reasoning / deception / cooperation? partially
- Does it test visual grounding / spatial-temporal reasoning? yes
- Does it test long-horizon autonomy / task completion? partially
- Does it test real-time efficiency? no
- Does it test cross-game transfer / open-ended generalization? partially
- Why is a game environment especially suitable here? Competitive 3D games produce rapid state changes and overlapping events that stress temporal grounding more than static vision tasks.

## 5. Interaction paradigm
- Observation channel: synchronized first-person gameplay videos plus a question
- Action channel: none; the model answers QA items
- Interface type: natural language
- Agent scaffold allowed: none
- Is there privileged API access? no
- How close is the setup to human play? low to medium; observation realism is high, but there is no action loop
- Main ecological-validity trade-off: GameplayQA keeps the hardest perceptual side of agent play but stops short of actual decision making and control.

## 6. Evaluation protocol
- Main score: QA accuracy
- Auxiliary score(s): category-wise breakdowns and hallucination/error analysis by entity type
- Evaluation style: judge-based
- Human baseline / AI anchor / self-play / model-vs-model setup: model comparison on fixed QA sets
- Automatic verifiability: high
- Calibration method: dense timeline annotation plus manually aligned multi-POV labeling
- Anti-contamination argument: synchronized multi-POV gameplay and combinatorial QA generation reduce the value of shallow benchmark memorization
- Reliability or comparability concerns: because it is passive QA, high scores do not directly imply good game-agent control

## 7. Main contributions
- Contribution 1: Builds a dense multi-POV 3D gameplay video benchmark centered on agent perception.
- Contribution 2: Organizes annotations around a Self / Other / World taxonomy.
- Contribution 3: Provides error analysis for hallucinations and attribution failures in gameplay understanding.

## 8. Main findings and failure modes
- Core empirical takeaway: Current multimodal models still struggle to attribute actions, states, and world events correctly in dense first-person gameplay video.
- Notable model failure mode 1: confusing self-actions with other-agent actions
- Notable model failure mode 2: weak temporal grounding across concurrent events
- Notable model failure mode 3: hallucinating objects or causal relationships in busy scenes
- Does this paper reveal a benchmark-design limitation as well? yes; it is a perceptual proxy, not a full agent benchmark

## 9. Why this paper matters for our survey
- Best use in Section 0 (why games): Shows that gameplay video is a rich source of dynamic perception challenges.
- Best use in Section 1 (historical evolution): Useful marker for the rise of video-understanding proxies in game-agent evaluation.
- Best use in Section 2 (design space): Good example of first-person multi-video observation without action.
- Best use in Section 3 (capability targets): Direct fit for visual grounding, temporal reasoning, and multi-agent attribution.
- Best use in Section 4 (interaction paradigm): Important counterexample to active-play benchmarks.
- Best use in Section 5 (evaluation protocol): Relevant for annotation-heavy QA generation and hallucination analysis.
- Best use in Section 6/7 (limitations and future): Supports the claim that perception is still a bottleneck even before control.

## 10. Relation to nearby papers
- Closest predecessor(s): video QA and egocentric video benchmarks
- Closest follow-up(s): GameVerse and other visual game-agent studies
- Best comparison targets inside our corpus: Balrog, GameVerse, StarBench, FlashAdventure
- What this paper uniquely adds relative to neighbors: It isolates dense first-person multi-agent perception from the action loop more cleanly than the other visual papers.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- GameplayQA uses synchronized multi-POV footage from nine commercial 3D games and constructs 2.4K QA pairs.
- The benchmark organizes labels with a six-primitive taxonomy over Self, Other, and World entities.
- The paper reports category-level error analysis showing persistent failures in temporal attribution and hallucination.

### 11.2 Our synthesis / interpretation
- GameplayQA should not be treated as evidence that a model can play games well; it is evidence that game-like perception remains hard.
- It is therefore most helpful as a supporting card for the visual-grounding section rather than as a central ecological benchmark.

### 11.3 Uncertain or needs re-check
- Recheck Appendix C if we later need the exact list of commercial games or category counts by title.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? No immediate reread; the benchmark scope and role are already clear.
- Which section to read next if needed: 3.1 / 3.2 / 4.2
- Follow-up question(s): Where should the survey draw the boundary between agent-centric video understanding and actual game-agent evaluation?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P1
- Reading depth: deep
- Batch ID: B03
- Outline sections: 3,4,5,6
- Survey role: representative
- Paper card path: `paper_cards/B03/GameplayQA.md`
- Next action: draft-section
- Last updated: 2026-04-05
