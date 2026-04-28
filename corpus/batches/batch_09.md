# Batch B09: specialist-calibration-and-domain-upper-bounds

## Why This Batch Exists
- Keep specialist poker, chess, Pokemon, StarCraft, and Go papers together as calibration and upper-bound contrasts.
- Support Sections 2, 3, and 4 without letting domain-specific training systems dominate the cross-game narrative.

## Suggested Drafting Order

| Order | paper_id | Title | Survey role | Outline anchors | Why this paper is in the batch |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | PokerBench | PokerBench: Training Large Language Models to become Professional Poker Players | contrast | 1,2,3,4 | Solver-grounded poker spot benchmark plus training set; useful contrast for specialist calibration and for the gap between cheap diagnostic evaluation and live match play. |
| 2 | GTOWizardBenchmark | GTO Wizard Benchmark | representative | 1,2,3,4 | Standardized poker benchmark with a fixed superhuman anchor and AIVAT variance reduction, useful for specialist calibration comparisons. |
| 3 | CompleteChessGames | Complete Chess Games Enable LLM Become A Chess Master | contrast | 1,2,3,4 | Chess-specialized training and evaluation paper using FEN-to-move supervision and Stockfish games; useful contrast on rule grounding, abstract interfaces, and static-versus-actual-game evaluation. |
| 4 | MixingExpertKnowledge | Mixing Expert Knowledge: Bring Human Thoughts Back To the Game of Go | peripheral | 1,2,3,4 | Go-specialist training-and-evaluation paper useful as a boundary case for structured expert-data injection and benchmark-level upper bounds. |
| 5 | PokeChamp | PokéChamp: an Expert-level Minimax Language Agent | contrast | 1,2,3,4 | Pokemon specialist system paper with rich offline and live evaluation; useful contrast on LLM-plus-search design under partial observability and strict time budgets. |
| 6 | PokeAgentChallenge | The PokeAgent Challenge: Competitive and Long-Context Learning at Scale | contrast | 1,2,3,4 | Dual-track Pokemon challenge for FH-BT/Glicko leaderboard design, harness effects, Level 2 battling, and Level 4 speedrunning; use as living benchmark evidence, not one combined score. |
| 7 | ComplexCardGames | Can Large Language Models Master Complex Card Games? | contrast | 1,2,3,4 | Training-heavy card-game suite for rule-similar transfer, interference, and general-capability retention; useful contrast rather than ecological benchmark. |
| 8 | LLMPlayStarCraftII | Large Language Models Play StarCraft II: Benchmarks and A Chain of Summarization Approach | representative | 1,2,3,4 | Early StarCraft II benchmark establishing the text-interface macro-RTS lineage for LLM agents and CoS-style history compression. |
| 9 | StarCraftIIArena | StarCraft II Arena: Evaluating LLMs in Strategic Planning, Real-Time Decision Making, and Adaptability | representative | 1,2,3,4 | Specialist RTS benchmark useful for fine-grained metric design, sync-vs-async comparison, and decision tracing; cite interface details narrowly because the implementation description remains thin. |
| 10 | VLMPlayStarCraftII | VLMs Play StarCraft II: A Benchmark and Multimodal Decision Method | representative | 1,2,3,4 | Multimodal StarCraft II benchmark extending the RTS line into visual tactical decision-making and componentized VLM control. |

## Expected Survey Payoff
- Provide a clean contrast between general benchmark design and expert-domain calibration stacks.
- Keep fixed anchors, solver-grounded evaluation, and heavily engineered specialist systems visible but scoped.

## Questions To Resolve While Drafting
- Which specialist results are benchmark contributions versus system papers with evaluation attached?
- How should the survey use these upper bounds without letting them overtake the main benchmark narrative?

## Batch Use Note
- Use this batch as controlled contrast material for calibration, specialist interfaces, and domain-specific upper bounds.
