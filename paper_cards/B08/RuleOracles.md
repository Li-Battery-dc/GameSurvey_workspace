# RuleOracles LLMs as Rule Oracles: Exploring Real-World Multimodal Reasoning in Tabletop Strategy Games

## 0. Metadata
- Date: 2025/05
- Venue: ICLR 2026
- Authors: Anonymous authors
- Paper link: https://openreview.net/pdf/4d9bf447f073bc4ccf8f6b061730d0ae8c10dd2a.pdf
- Code link:
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: medium
- Review gate label: usable

## 1. One-paragraph benchmark summary
- Rule Oracles introduces LudoBench, a tabletop-strategy benchmark for multimodal rule understanding and state-grounded reasoning. Instead of asking models to play long live matches, it evaluates whether they can read rule materials, parse real game states, and answer grounded questions about legal moves, hidden implications, and short-horizon optimization. The benchmark is organized into three tiers: environment perception, heterogeneous rule integration, and short-horizon strategic reasoning. For this survey, the paper is a useful contrast case because it is deeply game-grounded and multimodal, but it focuses on rule-oracle competence rather than full gameplay agents.

## 2. Position in our survey
- Why-games relevance: Tabletop games package rule systems, hidden information, and strategic trade-offs in a form where state interpretation and rule retrieval can be tested directly.
- Historical stage: diagnostic capability probe
- Narrative level(s): L2 strategic reasoning / L4 visual agency
- Most relevant outline section(s): 2,3,4,5
- Role in corpus: contrast

## 3. Design-space coding
### 3.1 Environment structure
- Information structure: mixed
- Transition structure: mixed
- Agent structure: single-agent
- Social structure: N/A
- Time structure: turn-based

### 3.2 World structure
- World type(s): board / card / other
- Real game / simulated game / designed task-game hybrid: grounded in real tabletop strategy games
- Benchmark unit: question

### 3.3 Benchmark scope
- Scope: curated suite
- Number of games / tasks: 638 QA items across 5 tabletop games in the PDF version consulted
- Benchmark intent: diagnostic evaluation

### 3.4 Modality
- Primary modality: mixed
- Perception burden retained: board-state parsing, component recognition, rulebook retrieval, hidden-information reasoning, and short-horizon planning
- Perception burden removed: no full interactive match loop is required

## 4. What this benchmark measures
- Primary capability target: multimodal rule-grounded reasoning in tabletop games
- Secondary capability target(s): scene perception, cross-modal rule integration, legal-move reasoning, and local strategic optimization
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? partially
- Does it test social reasoning / deception / cooperation? partially
- Does it test visual grounding / spatial-temporal reasoning? yes
- Does it test long-horizon autonomy / task completion? no
- Does it test real-time efficiency? no
- Does it test cross-game transfer / open-ended generalization? partially
- Why is a game environment especially suitable here? Real tabletop games combine visual state, written rules, and strategic constraints, so they naturally expose failures of multimodal rule grounding.

## 5. Interaction paradigm
- Observation channel: visual game states, rulebooks in text or image form, and human textual descriptions of the state
- Action channel: question answers or recommended moves produced from the grounded state
- Interface type: natural language / image / hybrid
- Agent scaffold allowed: none
- Is there privileged API access? no
- How close is the setup to human play? medium; the inputs are real tabletop materials, but the benchmark stops at grounded QA rather than live play
- Main ecological-validity trade-off: Rule Oracles keeps real rulebooks and real game states, but evaluates offline rule reasoning rather than full turn-by-turn gameplay behavior

## 6. Evaluation protocol
- Main score: exact-match accuracy on benchmark questions
- Auxiliary score(s): tier-wise accuracy across T1, T2, and T3; ablations over rulebook modality and state representation; GPT-4o-based postprocessing for answer normalization
- Evaluation style: native score / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: 9 frontier multimodal-capable language models are evaluated directly on the benchmark
- Automatic verifiability: mixed
- Calibration method: tiered task design, structured prompts, and normalization of free-form outputs with GPT-4o
- Anti-contamination argument: the paper emphasizes real game materials and multimodal grounding rather than synthetic text-only tasks
- Reliability or comparability concerns: answer normalization uses GPT-4o postprocessing, and the benchmark studies grounded reasoning rather than full gameplay, so comparison to agent benchmarks must stay qualified

## 7. Main contributions
- Contribution 1: Introduces a multimodal tabletop benchmark centered on rule-grounded reasoning rather than end-to-end gameplay.
- Contribution 2: Organizes tasks into perception, rule integration, and strategic reasoning tiers.
- Contribution 3: Shows that state-of-the-art multimodal models still collapse on the hardest tier even when simpler perception is reasonably strong.

## 8. Main findings and failure modes
- Core empirical takeaway: models perform moderately on perception-heavy tasks, but performance drops sharply on rule integration and especially on short-horizon strategy.
- Notable model failure mode 1: scene parsing errors and incomplete state understanding
- Notable model failure mode 2: weak retrieval and integration of heterogeneous rules from rulebooks
- Notable model failure mode 3: severe degradation on T3 short-horizon strategic reasoning, where the strongest models remain below 13% accuracy
- Does this paper reveal a benchmark-design limitation as well? yes; it shows how far models are from rule-grounded play, but because the benchmark is offline QA, it cannot directly establish full gameplay competence

## 9. Why this paper matters for our survey
- Best use in Section 0 (why games): Shows how games can expose multimodal reasoning failures that static VQA does not capture cleanly.
- Best use in Section 1 (historical evolution): Useful as a later branch where tabletop materials are used for rule-grounding diagnostics.
- Best use in Section 2 (design space): Important contrast case for benchmarks grounded in real rulebooks and physical game states.
- Best use in Section 3 (capability targets): Supports discussion of rule retrieval, legal-move reasoning, and short-horizon tabletop strategy.
- Best use in Section 4 (interaction paradigm): Strong example of multimodal state plus rulebook input without a live agent loop.
- Best use in Section 5 (evaluation protocol): Useful for tiered scoring and for discussing answer normalization versus direct environment verification.
- Best use in Section 6/7 (limitations and future): Helps argue that grounded rule understanding is a bottleneck even before full gameplay is attempted.

## 10. Relation to nearby papers
- Closest predecessor(s): tabletop QA and rule-understanding evaluations
- Closest follow-up(s): multimodal tabletop or rulebook-grounded agent benchmarks with live play
- Best comparison targets inside our corpus: [LMGameBench](D:/research_root/GameSurvey/workspace/paper_cards/B08/LMGameBench.md), [GAMEBoT](D:/research_root/GameSurvey/workspace/paper_cards/B08/GAMEBoT.md), [TowerMind](D:/research_root/GameSurvey/workspace/paper_cards/B06/TowerMind.md), [BoardGameArena](D:/research_root/GameSurvey/workspace/paper_cards/B01/BoardGameArena.md)
- What this paper uniquely adds relative to neighbors: It isolates the rule-oracle stage between "seeing the board" and "actually playing the game".

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- The PDF version consulted describes LudoBench as a 638-question benchmark spanning five tabletop games and three tiers: environment perception, heterogeneous rules integration, and short-horizon optimization.
- The paper reports average accuracy of about 63% on T1, about 36% on T2, and about 8% on T3, with the strongest T3 results still below 13%.
- Text rulebooks help all tested models, while image rulebooks often underperform text and state representations are generally easier in text than in raw visual form.

### 11.2 Our synthesis / interpretation
- Rule Oracles is best used as a boundary paper between multimodal benchmark design and full game-agent evaluation.
- It is especially valuable because it shows that rule-grounded understanding can fail before long-horizon play even begins.

### 11.3 Uncertain or needs re-check
- The OpenReview landing-page abstract and the PDF version appear inconsistent on corpus size and game count; this card follows the PDF because it is the fullest source we could verify.
- The accessed PDF is anonymous, so final author metadata may differ after camera-ready release.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? A targeted reread may be useful later because this paper is unusually relevant to the survey’s rule-grounding discussion.
- Which section to read next if needed: 3 / 4 / 5
- Follow-up question(s): Should Rule Oracles appear in the main benchmark taxonomy, or mainly in a subsection on multimodal rule understanding before gameplay?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P2
- Reading depth: deep
- Batch ID: B08
- Outline sections: 2,3,4,5
- Survey role: contrast
- Paper card path: `paper_cards/B08/RuleOracles.md`
- Next action: draft-section
- Last updated: 2026-04-05
