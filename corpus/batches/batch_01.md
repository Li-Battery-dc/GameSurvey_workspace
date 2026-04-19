# Batch B01: rule-grounded-foundations

## Why This Batch Exists
- Consolidate the papers that best establish games as controlled, rule-grounded evaluation environments.
- Support Level 1 and early Level 2 drafting with one evidence block for legal moves, state tracking, calibration, and interface privilege.

## Suggested Drafting Order

| Order | paper_id | Title | Survey role | Outline anchors | Why this paper is in the batch |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | SmartPlay | SmartPlay | anchor | 0,1,2,3 | Foundational multi-game agent benchmark for rule-grounded evaluation, capability decomposition, and textified interface trade-offs. |
| 2 | GTBench | GTBench: Uncovering the Strategic Reasoning Limitations of LLMs via Game-Theoretic Evaluations | anchor | 0,1,2,3 | Game-theoretic task design and LLM-vs-LLM evaluation make it a core formal reasoning anchor. |
| 3 | BotzoneBench | BotzoneBench: Scalable LLM Evaluation via Graded AI Anchors | anchor | 0,1,2,3 | Anchor for scalable protocol design with fixed AI skill tiers across games. |
| 4 | LLMChess | LLM CHESS: Benchmarking Reasoning and Instruction-Following in LLMs through Chess | representative | 1,2,3 | Representative single-game probe for legal action, privileged tool access, and instruction-following under chess rules. |
| 5 | BoardGameArena | Game Reasoning Arena: A Framework and Benchmark for Assessing Reasoning Capabilities of Large Language Models via Game Play | representative | 1,3 | OpenSpiel-based small strategic-game framework for privileged text play, prompt-interface analysis, and reasoning-trace inspection. |
| 6 | GridBasedGameCompetitions | Evaluating Large Language Models with Grid-Based Game Competitions: An Extensible LLM Benchmark and Leaderboard | contrast | 1,2,3 | Simple grid-game leaderboard benchmark that fits as a controlled strategic precursor. |
| 7 | RuleOracles | LLMs as Rules Oracles: Exploring Real-World Multimodal Reasoning in Tabletop Strategy Game Environments | contrast | 1,2,3 | Contrast paper for multimodal rule-grounding in real tabletop games; strongest for rulebook integration and interface-design discussion rather than live gameplay claims. |

## Expected Survey Payoff
- Lock down the opening contrast between static QA and closed-loop game interaction.
- Keep rule grounding, legal action generation, and controlled evaluation protocols in the same citation cluster.

## Questions To Resolve While Drafting
- Which papers should carry the Level 1 narrative versus appear only as contrasts on abstraction or calibration?
- How should the survey separate rule fidelity from deeper strategic competence?

## Batch Use Note
- Use this batch to draft the lead-in, Level 1 taxonomy, and the rule-grounding/interface trade-off sections.
