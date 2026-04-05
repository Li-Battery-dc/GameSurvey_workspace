# Batch B08: benchmark-suite-diagnostics

## Why This Batch Exists
- Compare benchmark suites that emphasize diagnostic instrumentation rather than one game family.
- Support the survey's discussion of measurement design, process metrics, and protocol transparency.

## Reading Order

| Order | paper_id | Title | Priority | Recommended depth | Outline anchors | Why this paper is in the batch |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | LMGameBench | LMGAME-BENCH | P1 | deep | 0,1,2,3,5 | Unified benchmark with explicit perception and memory breakdowns. |
| 2 | GAMEBoT | GAMEBoT | P1 | deep | 2,3,5,6 | Transparent modular evaluation useful for process-level analysis. |
| 3 | KORGym | KORGym | P1 | deep | 1,2,3,5,7 | Dynamic multi-game platform that broadens benchmark coverage. |
| 4 | RuleOracles | LLMs as Rule Oracles | P2 | deep | 2,3,4,5 | Tabletop rulebook benchmark for multimodal rule understanding. |

## Expected Survey Payoff
- Clarify how suites differ in instrumentation granularity and task decomposition.
- Improve the survey's treatment of protocol validity and comparability.

## Questions To Resolve While Reading
- Which metrics here transfer across benchmarks and which are batch-specific inventions?
- How much privileged rule access is acceptable before ecological validity breaks down?

## Exit Criteria
- every paper in this batch has a paper card
- registry rows are synced
- unresolved ambiguity is explicit
- outline gaps exposed by the batch are noted
- batch status in `corpus/batches/batch_index.md` is updated

