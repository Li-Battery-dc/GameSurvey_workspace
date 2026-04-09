# LLMHanabi LLM-Hanabi: Evaluating Multi-Agent Gameplays with Theory-of-Mind and Rationale Inference in Imperfect Information Collaboration Game

## 0. Metadata
- Date: 2025/10
- Venue: EMNLP 2025 workshop
- Authors: Fangzhou Liang, Tianshi Zheng, Chunkit Chan, Yauwai Yim, Yangqiu Song
- Paper link: https://arxiv.org/pdf/2510.04980v1
- Code link:
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: medium
- Review gate label: usable

## 1. One-paragraph benchmark summary
- LLM-Hanabi uses the cooperative imperfect-information card game Hanabi to evaluate whether language models can infer the rationale behind teammates’ hints and actions. The benchmark couples ordinary game performance with explicit Theory-of-Mind scoring, separating first-order rationale inference from second-order reasoning about others’ interpretations. All evaluation is run in a five-player Hanabi setting with repeated games and standard Hanabi resources. This makes the paper a useful cooperative counterpart to the Werewolf line in the survey’s social-intelligence section.

## 2. Position in our survey
- Why-games relevance: Cooperative games let the benchmark test hidden-state reasoning and partner modeling without collapsing everything into competition or deception.
- Historical stage: diagnostic capability probe
- Narrative level(s): L3 social intelligence
- Most relevant outline section(s): 1,2,3,4
- Role in corpus: representative

## 3. Design-space coding
### 3.1 Environment structure
- Information structure: imperfect
- Transition structure: deterministic
- Agent structure: multi-agent
- Social structure: cooperative
- Time structure: turn-based

### 3.2 World structure
- World type(s): card
- Real game / simulated game / designed task-game hybrid: real game adapted into an LLM benchmark
- Benchmark unit: full game

### 3.3 Benchmark scope
- Scope: single game
- Number of games / tasks: five-player Hanabi games with 30-50 runs per model
- Benchmark intent: diagnostic evaluation

### 3.4 Modality
- Primary modality: text
- Perception burden retained: hidden information, partner hints, rationale interpretation, multi-agent coordination
- Perception burden removed: visual card handling and embodied table interaction

## 4. What this benchmark measures
- Primary capability target: theory-of-mind and rationale inference in collaboration
- Secondary capability target(s): cooperative planning, hidden-state reasoning, hint interpretation
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? yes
- Does it test social reasoning / deception / cooperation? yes
- Does it test visual grounding / spatial-temporal reasoning? no
- Does it test long-horizon autonomy / task completion? yes
- Does it test real-time efficiency? no
- Does it test cross-game transfer / open-ended generalization? no
- Why is a game environment especially suitable here? Hanabi forces agents to infer what partners mean under strict information constraints, which makes ToM measurable in actual play.

## 5. Interaction paradigm
- Observation channel: standard Hanabi game state plus teammate hints and actions
- Action channel: cooperative play actions and generated ToM statements
- Interface type: natural language / structured action space
- Agent scaffold allowed: other
- Is there privileged API access? yes
- How close is the setup to human play? medium; it preserves Hanabi’s hidden-information structure but uses prompt-based inference and explicit ToM outputs
- Main ecological-validity trade-off: The benchmark cleanly measures rationale inference, but the explicit ToM reporting is more instrumented than natural gameplay.

## 6. Evaluation protocol
- Main score: Game Score
- Auxiliary score(s): ToM Score, first-order ToM, second-order ToM, correlation between ToM and game success
- Evaluation style: hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: repeated same-model cooperative play
- Automatic verifiability: high
- Calibration method: fixed five-player setup, 30-50 games per model, standard Hanabi resources
- Anti-contamination argument: not central
- Reliability or comparability concerns: performance is benchmarked in one cooperative game only, and explicit CoT prompting may shape outcomes

## 7. Main contributions
- Contribution 1: Builds a Hanabi benchmark centered on rationale inference rather than only score.
- Contribution 2: Separates first-order and second-order theory-of-mind.
- Contribution 3: Shows a strong empirical link between ToM quality and cooperative success.

## 8. Main findings and failure modes
- Core empirical takeaway: Better ToM scores correlate strongly with better Hanabi performance, and first-order ToM matters more than second-order ToM.
- Notable model failure mode 1: weak partner-rationale inference leads directly to lower team scores
- Notable model failure mode 2: second-order ToM remains much harder than first-order interpretation
- Notable model failure mode 3: standard LLMs trail large reasoning models on both gameplay and ToM
- Does this paper reveal a benchmark-design limitation as well? yes; the benchmark is narrow but clean, so it is better for mechanism probing than for broad generalization claims

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Shows how cooperative games can probe interactive inference beyond solitary reasoning.
- Best use in Section 1 (taxonomy and evolutionary levels): Useful expansion from adversarial social games toward collaboration-centered social benchmarks. Clean cooperative imperfect-information benchmark anchor.
- Best use in Section 2 (core capabilities evaluated by games): Direct evidence for cooperation and rationale inference.
- Best use in Section 3 (interaction and evaluation paradigm): Helpful case of prompt-instrumented cooperative play. Strong for dual scoring with gameplay and ToM metrics.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Supports the claim that partner modeling remains a major bottleneck.

## 10. Relation to nearby papers
- Closest predecessor(s): Hanabi-based AI collaboration studies and ToM benchmarks
- Closest follow-up(s): broader cooperative game benchmarks
- Best comparison targets inside our corpus: WerewolfArena, Wolf, CKArena
- What this paper uniquely adds relative to neighbors: It gives the batch a cooperative imperfect-information benchmark with explicit ToM scoring rather than deception-only focus.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- The benchmark uses five-player Hanabi games and evaluates both Game Score and ToM Score.
- ToM Score averages first-order and second-order rationale-inference scores over hint interactions.
- The paper reports a strong positive correlation between ToM proficiency and cooperative game performance.

### 11.2 Our synthesis / interpretation
- LLM-Hanabi is a useful balancing card for the social batch because it shows that social intelligence is not only about lying and detecting lies.
- Its real value is conceptual clarity: it ties specific ToM subskills to cooperative outcomes.

### 11.3 Uncertain or needs re-check
- Recheck Appendix A if we later need the exact model roster or prompt wording used in the cooperative runs.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? No immediate reread; the metric design and takeaways are already clear enough.
- Which section to read next if needed: 3.3 / 4.2 / 4.3
- Follow-up question(s): How transferable is first-order ToM from Hanabi to richer real-time cooperative settings?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P1
- Reading depth: deep
- Batch ID: B02
- Outline sections: 1,2,3,4
- Survey role: representative
- Paper card path: `paper_cards/B02/LLMHanabi.md`
- Next action: draft-section
- Last updated: 2026-04-05
