# Mars Mars: Situated Inductive Reasoning in an Open-World Environment

## 0. Metadata
- Date: 2024/09
- Venue: NeurIPS 2024 (D&B)
- Authors: Xiaojuan Tang, Jiaqi Li, Yitao Liang, Song-chun Zhu, Muhan Zhang, Zilong Zheng
- Paper link: https://arxiv.org/pdf/2410.08126v2.pdf
- Code link: https://github.com/XiaojuanTang/Mars
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: high
- Review gate label: strong

## 1. One-paragraph benchmark summary
- Mars is an open-world survival benchmark derived from Crafter that is explicitly designed to test situated inductive reasoning rather than recall of commonsense rules. It creates counter-commonsense worlds by changing terrain, survival mechanics, and task dependencies while enforcing design constraints such as achievability and resource balance. Agents must discover the altered rules through interaction and then apply them in later decisions, which makes the benchmark less about memorized world knowledge and more about adaptive hypothesis formation. For this survey, Mars is a strong contrast benchmark because it shows how game environments can test rule induction under interaction, not just task execution under known rules.

## 2. Position in our survey
- Why-games relevance: Games can operationalize rule discovery by forcing agents to infer hidden mechanics through repeated interaction.
- Historical stage: diagnostic capability probe
- Narrative level(s): L2 strategic reasoning / L5 cross-game generalization
- Most relevant outline section(s): 3,4,6,7
- Role in corpus: contrast

## 3. Design-space coding
### 3.1 Environment structure
- Information structure: imperfect
- Transition structure: mixed
- Agent structure: single-agent
- Social structure: N/A
- Time structure: turn-based

### 3.2 World structure
- World type(s): sandbox / open-world / other
- Real game / simulated game / designed task-game hybrid: Crafter-derived open-world with modified mechanics
- Benchmark unit: episode / world instance

### 3.3 Benchmark scope
- Scope: curated suite of modified worlds
- Number of games / tasks: 7 representative worlds selected from combinations of terrain, survival, and task-dependency changes
- Benchmark intent: diagnostic evaluation

### 3.4 Modality
- Primary modality: mixed
- Perception burden retained: local grid observation, inventory, status, and action-outcome interpretation
- Perception burden removed: environment remains lightweight and symbolic compared with richer 3D worlds

## 4. What this benchmark measures
- Primary capability target: situated inductive reasoning about changed world rules
- Secondary capability target(s): exploration, adaptive planning, and rule application under partial observability
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? yes
- Does it test social reasoning / deception / cooperation? no
- Does it test visual grounding / spatial-temporal reasoning? partially
- Does it test long-horizon autonomy / task completion? yes
- Does it test real-time efficiency? no
- Does it test cross-game transfer / open-ended generalization? yes
- Why is a game environment especially suitable here? Interactive worlds let the benchmark hide rules in action consequences rather than revealing them as explicit text constraints.

## 5. Interaction paradigm
- Observation channel: local world view, status values, and inventory descriptions generated from the game state
- Action channel: discrete movement and interaction commands
- Interface type: structured action space / hybrid
- Agent scaffold allowed: reflection / other
- Is there privileged API access? limited to textualized environment descriptors rather than full world mechanics
- How close is the setup to human play? medium-low; the world is game-like and interactive, but still lightweight and benchmark-oriented
- Main ecological-validity trade-off: Mars gains clean control over hidden-rule variation by working in a simplified survival world rather than a richer commercial game

## 6. Evaluation protocol
- Main score: overall score over achievement success rates
- Auxiliary score(s): reward and per-achievement success rate
- Evaluation style: completion rate / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: RL and LLM-based agents are compared across default Crafter and modified Mars worlds
- Automatic verifiability: high
- Calibration method: seven representative worlds chosen across single, double, and triple mechanic modifications
- Anti-contamination argument: the benchmark changes commonsense assumptions, so pretrained knowledge becomes misleading rather than sufficient
- Reliability or comparability concerns: success depends heavily on exploration budget, and the seven reported worlds only sample the larger possible world space

## 7. Main contributions
- Contribution 1: Introduces a counter-commonsense interactive benchmark for situated inductive reasoning.
- Contribution 2: Defines principled world modifications over terrain, survival, and task dependencies.
- Contribution 3: Shows that both RL and LLM agents fail badly once world rules no longer match common priors.

## 8. Main findings and failure modes
- Core empirical takeaway: all evaluated methods degrade sharply on Mars, and even the strongest settings perform poorly on the hardest mixed-rule worlds.
- Notable model failure mode 1: clinging to commonsense priors instead of testing altered mechanics
- Notable model failure mode 2: inducing wrong rules from sparse observations
- Notable model failure mode 3: failing to apply newly discovered rules consistently during planning
- Does this paper reveal a benchmark-design limitation as well? yes; it shows that many existing benchmarks mostly reward stored world knowledge rather than adaptive reasoning

## 9. Why this paper matters for our survey
- Best use in Section 0 (why games): Demonstrates that games can test rule discovery through interaction rather than static QA.
- Best use in Section 1 (historical evolution): Represents a move toward adaptive reasoning benchmarks rather than fixed-rule play only.
- Best use in Section 2 (design space): Useful for defining rule-perturbed task-game hybrids.
- Best use in Section 3 (capability targets): Strong evidence for inductive reasoning and exploration as distinct targets.
- Best use in Section 4 (interaction paradigm): Useful contrast to benchmarks that reveal all task rules upfront.
- Best use in Section 5 (evaluation protocol): A good example of controlled world perturbation as evaluation design.
- Best use in Section 6/7 (limitations and future): Supports the argument that benchmark difficulty should come from novelty, not only from scale.

## 10. Relation to nearby papers
- Closest predecessor(s): Crafter-based achievement benchmarks
- Closest follow-up(s): ARC-AGI-3, StarDojo
- Best comparison targets inside our corpus: ARCAGI3, GameTraversalBenchmark, TextQuests, StarDojo
- What this paper uniquely adds relative to neighbors: It makes the central challenge inferring changed mechanics rather than merely solving a known game.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- Mars modifies Crafter through terrain, survival, and task-dependency changes.
- The main evaluation uses seven worlds spanning single, double, and triple combinations of those changes.
- The benchmark reports reward, success rate, and a log-space overall score, and finds severe degradation from default Crafter to Mars worlds.

### 11.2 Our synthesis / interpretation
- Mars is one of the most useful corpus papers for arguing that game benchmarks can test adaptation to novel rules rather than only execution under fixed rules.
- It is particularly strong for the survey’s limitations section because it exposes how pretrained priors can become liabilities.

### 11.3 Uncertain or needs re-check
- Re-check the exact world definitions in Appendix M if we later need a detailed taxonomy.
- Re-check the best IfR numbers per world if we compare methods quantitatively in prose.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? A targeted reread will likely help later because this paper cleanly anchors adaptive rule-induction claims.
- Which section to read next if needed: world-construction principles / IfR analysis / case studies
- Follow-up question(s): Which modifications are most diagnostic of inductive failure: terrain, survival, or task dependency?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P2
- Reading depth: deep
- Batch ID: B10
- Outline sections: 3,4,6,7
- Survey role: contrast
- Paper card path: `paper_cards/B10/Mars.md`
- Next action: draft-section
- Last updated: 2026-04-05
