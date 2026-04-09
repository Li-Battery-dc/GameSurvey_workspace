# RuleOracles LLMs as Rules Oracles: Exploring Real-World Multimodal Reasoning in Tabletop Strategy Game Environments

## 0. Metadata
- Date: 2026/01
- Venue: ICLR 2026
- Authors: Joseph J Peper, Sai Krishna Gandra, Yunxiang Zhang, Vaibhav Chennareddy, Shloki Jha, Ali Payani, Lu Wang
- Paper link: https://openreview.net/forum?id=TOgQ00DEek
- Code link:
- Reading depth: deep
- Card status: card-draft
- Confidence in this card: low
- Review gate label: blocked

## 1. One-paragraph benchmark summary
- Rules Oracles introduces LudoBench, a tabletop-strategy benchmark for multimodal rule understanding and state-grounded reasoning. Rather than asking models to play long live matches, it evaluates whether a vision-enabled LM can combine a pictured tabletop scene with corresponding rules and answer grounded questions about the situation. The official OpenReview forum page describes three cumulative capabilities: environment perception, heterogeneous rules integration, and short-horizon optimization. For this survey, the paper is still a useful contrast case because it is deeply game-grounded and multimodal, but this audit could not verify the full paper text: the official PDF endpoint returned `403`, and accessible official sources disagree on release scope.

## 2. Position in our survey
- Why-games relevance: Tabletop games package rule systems, hidden information, and strategic trade-offs in a form where state interpretation and rule retrieval can be tested directly.
- Historical stage: diagnostic capability probe
- Narrative level(s): L2 strategic reasoning / L4 visual agency
- Most relevant outline section(s): 1,2,3
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
- Number of games / tasks: 638 benchmark questions in the accessible Hugging Face dataset page; official sources disagree on the exact game count
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
- Observation channel: visual tabletop states paired with corresponding rulesets
- Action channel: grounded question answers about the pictured scenario, including recommended local actions in some items
- Interface type: natural language / image / hybrid
- Agent scaffold allowed: none
- Is there privileged API access? no
- How close is the setup to human play? medium; the inputs are real tabletop materials, but the benchmark stops at grounded QA rather than live play
- Main ecological-validity trade-off: Rule Oracles keeps real rulebooks and real game states, but evaluates offline rule reasoning rather than full turn-by-turn gameplay behavior

## 6. Evaluation protocol
- Main score: exact-match accuracy on benchmark questions
- Auxiliary score(s): tier-wise accuracy across the three cumulative capabilities and knowledge-ablation analysis reported on the official forum page
- Evaluation style: native score / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: frontier vision-enabled language models are evaluated directly on the benchmark, but the currently accessible official sources do not expose the full evaluated-model table
- Automatic verifiability: mixed
- Calibration method: tiered task design and grounded question answering over paired scene-plus-rules inputs
- Anti-contamination argument: no explicit contamination audit was verifiable from the accessible official sources; the paper instead emphasizes unfamiliar real-world tabletop materials and multimodal grounding
- Reliability or comparability concerns: the benchmark studies grounded reasoning rather than full gameplay, and this audit could not verify the full methods section because the official PDF endpoint was inaccessible in the current environment

## 7. Main contributions
- Contribution 1: Introduces a multimodal tabletop benchmark centered on rule-grounded reasoning rather than end-to-end gameplay.
- Contribution 2: Organizes tasks into perception, rule integration, and strategic reasoning tiers.
- Contribution 3: Shows that frontier models remain weak on the hardest situated multi-step reasoning tier even when simpler perception is materially stronger.

## 8. Main findings and failure modes
- Core empirical takeaway: accessible official sources show that models perform materially better on simple perception tasks than on rule integration and especially on short-horizon multi-step reasoning.
- Notable model failure mode 1: scene parsing errors and incomplete state understanding
- Notable model failure mode 2: weak retrieval and integration of heterogeneous rules from rulebooks
- Notable model failure mode 3: severe degradation on the hardest situated multi-step reasoning tasks, where the official forum summary says the strongest models fall below 10% accuracy
- Does this paper reveal a benchmark-design limitation as well? yes; it shows how far models are from rule-grounded play, but because the benchmark is offline QA and the full methods text could not be verified here, its exact evaluation protocol still needs a later full-text recheck

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Shows how games can expose multimodal reasoning failures that static VQA does not capture cleanly.
- Best use in Section 1 (taxonomy and evolutionary levels): Useful as a later branch where tabletop materials are used for rule-grounding diagnostics. Important contrast case for benchmarks grounded in real rulebooks and physical game states.
- Best use in Section 2 (core capabilities evaluated by games): Supports discussion of rule retrieval, legal-move reasoning, and short-horizon tabletop strategy.
- Best use in Section 3 (interaction and evaluation paradigm): Strong example of multimodal state plus rulebook input without a live agent loop. Useful for tiered scoring and for discussing answer normalization versus direct environment verification.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Helps argue that grounded rule understanding is a bottleneck even before full gameplay is attempted, but do not rely on it for fine-grained methodological claims until the full text is re-verified.

## 10. Relation to nearby papers
- Closest predecessor(s): tabletop QA and rule-understanding evaluations
- Closest follow-up(s): multimodal tabletop or rulebook-grounded agent benchmarks with live play
- Best comparison targets inside our corpus: LMGameBench, GAMEBoT, TowerMind, BoardGameArena
- What this paper uniquely adds relative to neighbors: It isolates the rule-oracle stage between "seeing the board" and "actually playing the game".

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- The official OpenReview forum page describes LudoBench as a benchmark over three cumulative capabilities: environment perception, heterogeneous rules integration, and short-horizon optimization.
- The same forum page reports that even the strongest models reach only about 68% accuracy on simple environment perception tasks and fall below 10% on situated multi-step comprehension puzzles.
- The public Hugging Face dataset page for `launch/LudoBench` exposes 638 test rows and shows six distinct `Game` values in the current dataset viewer.

### 11.2 Our synthesis / interpretation
- Rule Oracles is best used as a boundary paper between multimodal benchmark design and full game-agent evaluation.
- It is especially valuable because it shows that rule-grounded understanding can fail before long-horizon play even begins.
- This card should currently be treated as a scoped contrast reference, not as a stable anchor, because the full official PDF could not be retrieved during the audit.

### 11.3 Uncertain or needs re-check
- The official OpenReview forum page and the public Hugging Face dataset page disagree on release scope: the forum abstract says three games, while the dataset viewer shows six `Game` values.
- The official OpenReview PDF endpoint returned `403 Forbidden` in the current environment, so this audit could not verify the full methods, evaluated model list, or answer-normalization details from the full text.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? yes; a full-text read is still required before this paper can safely return to `card-reviewed`
- Which section to read next if needed: full PDF methods / experiments / appendix once the official PDF becomes accessible
- Follow-up question(s): Should Rule Oracles appear in the main benchmark taxonomy, or mainly in a subsection on multimodal rule understanding before gameplay?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-draft
- Priority: P2
- Reading depth: deep
- Batch ID: B08
- Outline sections: 1,2,3
- Survey role: contrast
- Paper card path: `paper_cards/B08/RuleOracles.md`
- Check status: unchecked
- Last updated: 2026-04-09
