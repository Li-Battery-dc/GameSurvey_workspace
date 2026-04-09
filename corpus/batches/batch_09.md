# Batch B09: visual-agent-lineage

## Why This Batch Exists
- Backfill the visual-agent lineage behind the current ecological core.
- Compare raw pixels, low-level control, and early LVLM game evaluation with the newer visual batches.

## Reading Order

| Order | paper_id | Title | Priority | Recommended depth | Outline anchors | Why this paper is in the batch |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | VideoGameBench | VideoGameBench | P1 | deep | 2,3,4 | Raw-visual real-time benchmark and direct comparison target for BALROG. |
| 2 | VMage | V-MAGE | P1 | deep | 2,3,4 | Visual-centric agent benchmark with Elo-style evaluation. |
| 3 | LVLMGamePlayers | Are Large Vision-Language Models Good Game Players? | P2 | deep | 1,2,3,4 | Early visual-game baseline for historical comparison. |
| 4 | INGVP | ING-VP | P2 | deep | 2,3,4 | Benchmark focused on easy vision-game failure cases and spatial planning limits. |
| 5 | AtariGPT | Atari-GPT | P2 | deep | 2,3,4 | Low-level multimodal control benchmark for reaction speed and perception. |

## Expected Survey Payoff
- Give the survey a historical visual branch instead of relying only on the newest multimodal papers.
- Sharpen the discussion of observation channels and privileged interfaces.

## Questions To Resolve While Reading
- Which of these benchmarks genuinely evaluate agent play versus visual understanding proxies?
- How should low-level control papers be compared to GUI and first-person benchmarks?

## Exit Criteria
- every paper in this batch has a paper card
- registry rows are synced
- unresolved ambiguity is explicit
- outline gaps exposed by the batch are noted
- batch status in `corpus/batches/batch_index.md` is updated

