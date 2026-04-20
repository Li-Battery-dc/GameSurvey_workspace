# RuleOracles LLMs as Rules Oracles: Exploring Real-World Multimodal Reasoning in Tabletop Strategy Game Environments

## 0. Metadata
- Date: 2026/01
- Venue: ICLR 2026
- Authors: Joseph J. Peper, Sai Krishna Gandra, Yunxiang Zhang, Vaibhav Chennareddy, Shloki Jha, Ali Payani, Lu Wang
- Paper link: https://openreview.net/pdf?id=TOgQ00DEek
- Code link:
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: high
- Review gate label: usable

## 1. One-paragraph benchmark summary
- RuleOracles introduces LudoBench, a multimodal tabletop-game benchmark that tests whether vision-capable language models can parse a board state, consult the corresponding rulebook, and answer grounded questions about that situation. The benchmark covers five mainstream tabletop strategy games and 638 QA items organized into three cumulative tiers: environment perception, heterogeneous rules integration, and short-horizon optimization. Unlike agent benchmarks that study long matches, LudoBench focuses on the "first-time player" comprehension problem: can a model look at a cluttered board state, retrieve the right rule clauses, and apply them correctly without a legality checker or interactive simulator support in the loop. For this survey, it is best used as a contrast paper showing that rule-grounded multimodal understanding is a meaningful precursor to gameplay, but not yet equivalent to closed-loop play.

## 2. Position in our survey
- Why-games relevance: Real tabletop games force the benchmark to couple visual scene understanding, long heterogeneous rulebooks, and game-specific rule application in a way generic VQA tasks usually do not.
- Historical stage: diagnostic capability probe
- Benchmark level(s): L1 rule understanding
- Most relevant outline section(s): 1,2,3
- Role in corpus: contrast

## 3. Design-space coding
### 3.1 Game structure
- Information structure: perfect
- Transition structure: deterministic
- Agent structure: single-agent
- Social structure: N/A
- Time structure: turn-based

### 3.2 Environment structure
- Environment type(s): tabletop
- Real game / simulated game / designed task-game hybrid: real tabletop games staged in Tabletop Simulator for a diagnostic benchmark
- Benchmark unit: question

### 3.3 Benchmark scope
- Scope: curated suite
- Number of games / tasks: 5 games, 638 questions

### 3.4 Modality
- Observation modality: mixed
- Action modality: semantic
- Perception burden retained: board-image parsing, spatial relations, iconography interpretation, rulebook retrieval, and grounded cross-modal reasoning
- Perception burden removed: no live gameplay loop, action execution, or long-horizon opponent adaptation

## 4. What this benchmark measures
- Primary capability target: multimodal rulebook-grounded game comprehension
- Secondary capability target(s): visual state perception, rule retrieval and disambiguation, rule application, score or legality reasoning, valid-action identification in QA form, and short-horizon tactical optimization
- Does it test rule grounding / legal action generation? partially; it directly tests rule grounding and valid-action identification in question form, but not free-form in-environment action generation
- Does it test strategic planning under uncertainty? partially; Tier 3 asks for short-horizon optimization, but the benchmark uses deterministic, fully observable scenarios
- Does it test social reasoning / deception / cooperation? no
- Does it test visual grounding / spatial-temporal reasoning? yes
- Does it test long-horizon autonomy / task completion? no
- Does it test real-time efficiency? no
- Does it test cross-game transfer / open-ended generalization? no
- Why is a game environment especially suitable here? Tabletop games provide dense visual states and precise rule constraints, so failures in perception, rule retrieval, and application become directly inspectable.

## 5. Interaction paradigm
- Observation channel: one or more game-state images plus the rulebook in `None`, `Text`, or `Image` form, followed by a natural-language question
- Action channel: semistructured natural-language answer rather than in-environment actions
- Interface type: natural language / image / hybrid
- Agent scaffold allowed: none
- Is there privileged API access? no
- How close is the setup to human play? low-to-medium; the benchmark uses human-legible board views and full rules, but stops before interactive play and collapses behavior into offline QA
- Main ecological-validity trade-off: LudoBench retains real board-state and rulebook complexity, but it operationalizes game understanding as offline QA rather than closed-loop gameplay

## 6. Evaluation protocol
- Main score: exact-match QA accuracy
- Auxiliary score(s): tier-wise accuracy, game-wise and modality-wise breakdowns, hobbyist-human accuracy, plurality-oracle solvability, and targeted rule-retrieval error analysis
- Evaluation style: hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: nine multimodal frontier LMs are evaluated on the same benchmark, and hobbyist annotator accuracy is reported as a human reference during dataset validation rather than as a separate leaderboard-style evaluation pass
- Automatic verifiability: high; answers are designed to have one resolved label, then exact-match is computed after a verified normalization step
- Calibration method: three cumulative reasoning tiers, three rulebook modalities, five games, annotator disagreement resolution, and plurality-vote headroom analysis
- Anti-contamination argument: not central; the paper motivates unfamiliar real-world game materials and rulebook access, but does not present a dedicated contamination audit
- Reliability or comparability concerns: this is an offline comprehension benchmark rather than a live-play benchmark; answer normalization relies on a GPT-4o post-processing step; and some long image rulebooks exceeded Claude 4.5 Sonnet's context window on selected splits

## 7. Main contributions
- Contribution 1: Introduces a 638-question multimodal tabletop benchmark spanning five games and three cumulative reasoning tiers.
- Contribution 2: Reframes game benchmarking around first-time rulebook-grounded comprehension rather than only long-horizon play.
- Contribution 3: Provides modality, solvability, and error analyses that separate perception failures from rule-retrieval and rule-application failures.

## 8. Main findings and failure modes
- Core empirical takeaway: even strong frontier multimodal models struggle on grounded tabletop reasoning, with average performance dropping from about 63% on Tier 1 perception to 36% on Tier 2 rule integration and 8% on Tier 3 optimization, while hobbyist annotators remain far stronger; the paper's key rule-understanding result is that richer rulebooks improve retrieval more than faithful situated application.
- Notable model failure mode 1: brittle scene parsing in cluttered states, including counting, orientation, and spatial-relation errors
- Notable model failure mode 2: retrieving relevant rules but misapplying them because the current game state is misunderstood or the rule is overgeneralized from surface patterns
- Notable model failure mode 3: failing to update intermediate states during multi-step optimization, producing invalid or greedy plans
- Does this paper reveal a benchmark-design limitation as well? yes; it shows that rulebook access alone is not enough, but it also remains a pre-play diagnostic benchmark rather than evidence of human-like game competence

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Limited contrast case showing that games can expose multimodal reasoning failures before an agent ever enters a live control loop.
- Best use in Section 1 (taxonomy and evolutionary levels): Useful as a Level-1 edge case showing that rule-following can stay visually grounded and rulebook-heavy without yet becoming a visual-agency benchmark.
- Best use in Section 2 (core capabilities evaluated by games): Direct support for rule grounding, rule retrieval versus rule application, and the way visual grounding errors contaminate rule-understanding evaluation.
- Best use in Section 3 (interaction and evaluation paradigm): Strong example of an image-plus-rulebook interface, modality ablations, and exact-answer scoring for grounded game comprehension without environment interaction.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Helps argue that multimodal rule understanding is itself a bottleneck, but should not be overused as evidence about full gameplay or ecological agent performance.

## 10. Relation to nearby papers
- Closest predecessor(s): textified or structured rule-following benchmarks such as SmartPlay, LLMChess, and BoardGameArena, plus simpler board-image reasoning setups with far less rulebook complexity
- Closest follow-up(s): multimodal game benchmarks that turn grounded understanding into action or control, such as StarBench and VideoGameBench
- Best comparison targets inside our corpus: SmartPlay, BoardGameArena, LVLMGamePlayers, StarBench
- What this paper uniquely adds relative to neighbors: It isolates the stage between "seeing the board and reading the rules" and "actually playing the game", and it directly shows that rule retrieval can improve without solving situated rule application

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- LudoBench contains 638 questions across five tabletop games: Kingdomino, Carcassonne, Catan, Res Arcana, and Pax Renaissance 2e, with 200 Tier 1 items, 200 Tier 2 items, and 238 Tier 3 items.
- The benchmark uses deterministic, fully observable scenarios staged in Tabletop Simulator, excluding hidden information and chance events so that each question has a single resolved answer; Tier 3 questions either assume no opponent interaction or explicitly specify opponent behavior.
- Tier 1 tests environment perception without rulebook use, Tier 2 tests situated rules integration such as score or valid-action questions, and Tier 3 tests short-horizon optimization under tractable constraints.
- Across all systems, average accuracy is about 63% on Tier 1, 36% on Tier 2, and 8% on Tier 3; the paper also reports hobbyist validation accuracy of 96.7%, 89.1%, and 82.2% across the three tiers.
- In a 30-question Pax Renaissance Tier-2 error analysis with GPT-4o, rule retrieval rises from 20% with no rulebook to 73% with text and 90% with image rulebooks, while correct rule application rises only from 17% to 64% and then drops to 56%.
- The paper reports that textual rulebooks help all models, while image rulebooks have mixed effects and can hurt some systems relative to text.

### 11.2 Our synthesis / interpretation
- This paper is best treated as a visually grounded Level-1 contrast case, not as a true Level-4 visual-agency benchmark: it preserves real game materials, but still evaluates comprehension rather than action.
- It is especially useful for the survey because it makes a clean point that giving a model the rulebook is not the same as getting correct situated rule understanding; retrieval and application break in different ways.

### 11.3 Uncertain or needs re-check
- Reopen Appendix C if later drafting needs the exact prompt template or the full evaluated-model configuration table.
- Reopen Appendices D, F, and J if later drafting needs the paper's detailed Tier-3 walkthroughs, hallucination taxonomy, or annotator-conflict breakdown.
- Avoid phrasing that treats LudoBench as a live-play or ecological benchmark, or that turns its valid-action QA into evidence of robust action generation.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? Full paper read completed for this audit. Reopen appendices only if later drafting needs prompt details, failure-taxonomy detail, or annotation-process specifics.
- Which section to read next if needed: Appendix C / Appendix D / Appendix F / Appendix J
- Follow-up question(s): Use this paper mainly for rule-grounding, rule-understanding failure decomposition, and multimodal-interface arguments, not as direct evidence of strong gameplay.

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P2
- Reading depth: deep
- Batch ID: B01
- Outline sections: 1,2,3
- Survey role: contrast
- Paper card path: `paper_cards/B01/RuleOracles.md`
- Check status: unchecked
- Last updated: 2026-04-18
