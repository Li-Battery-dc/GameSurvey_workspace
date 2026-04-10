# Batch B13: domain-specialist-competition

## Why This Batch Exists
- Collect domain-specialist and competition-heavy papers that are useful comparison targets but not central survey anchors.
- Support the survey's discussion of specialist competence, training-heavy setups, and domain-specific upper bounds.

## Reading Order

| Order | paper_id | Title | Priority | Recommended depth | Outline anchors | Why this paper is in the batch |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | PokerBench | PokerBench | P2 | deep | 1,2,4 | Imperfect-information specialist benchmark with strong training emphasis. |
| 2 | CompleteChessGames | Complete Chess Games Enable LLM Become A Chess Master | P2 | deep | 1,4 | Chess-specialized training paper and scope-bound comparison target. |
| 3 | PokeChamp | PokéChamp | P2 | deep | 1,2,4 | Expert-level Pokémon agent acting as a specialist upper bound. |
| 4 | LLMPlayStarCraftII | Large Language Models Play StarCraft II | P1 | deep | 1,2,3,4 | Early StarCraft II benchmark showing the text-interface RTS lineage. |
| 5 | StarCraftIIArena | StarCraft II Arena | P1 | deep | 1,2,3,4 | RTS benchmark for strategic planning, real-time adaptation, and robustness. |
| 6 | VLMPlayStarCraftII | VLMs Play StarCraft II | P1 | deep | 1,2,3,4 | Multimodal RTS benchmark extending the StarCraft line into visual decision-making. |
| 7 | MixingExpertKnowledge | Mixing Expert Knowledge | P3 | structured-skim | 1,4 | Boundary-case Go specialist retained for domain-specific upper-bound comparison. |
| 8 | GTOWizardBenchmark | GTO Wizard Benchmark | P1 | deep | 1,2,3,4 | Standardized poker benchmark with a fixed superhuman anchor for specialist calibration. |

## Expected Survey Payoff
- Provide a controlled comparison set for specialist versus general benchmark claims.
- Clarify how much survey attention domain-specialist systems deserve relative to broad benchmarks.

## Questions To Resolve While Reading
- Which papers here are benchmarks versus capability demonstrations with benchmark-like evaluation?
- How should specialist upper bounds be compared against cross-game generalization papers?

## Current Audit Note
- All eight papers in this batch now have reliable `card-reviewed` evidence.
- `StarCraftIIArena` is now usable as reviewed evidence for SC2 metric design, sync-versus-async trade-offs, and decision-trace instrumentation, but its interface details should still be cited narrowly because the paper's implementation description remains thin.

## Exit Criteria
- every paper in this batch has a paper card
- registry rows are synced
- unresolved ambiguity is explicit
- outline gaps exposed by the batch are noted
- batch status in `corpus/batches/batch_index.md` is updated

