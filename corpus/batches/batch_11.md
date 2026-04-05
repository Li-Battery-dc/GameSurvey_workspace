# Batch B11: symbolic-spatial-diagnostics

## Why This Batch Exists
- Keep a later batch for narrow symbolic, spatial, and planning diagnostics.
- Support comparison against broader game benchmarks without letting these specialized tasks dominate the core queue.

## Reading Order

| Order | paper_id | Title | Priority | Recommended depth | Outline anchors | Why this paper is in the batch |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | PuzzleJAX | PuzzleJAX | P2 | deep | 2,3,6,7 | Procedural puzzle suite for reasoning-transfer comparison. |
| 2 | SudokuBench | Sudoku-Bench | P2 | deep | 2,3,6 | Creative logical reasoning benchmark with limited gameplay interaction. |
| 3 | CrossWordBench | CrossWordBench | P2 | deep | 2,3,4,6 | Symbolic reasoning benchmark based on controllable crossword tasks. |
| 4 | VGRPBench | VGRP-Bench | P2 | deep | 3,4,6 | Visual grid puzzle benchmark for rule comprehension and spatial reasoning. |
| 5 | MazeEval | MazeEval | P2 | deep | 3,4,6 | Compact maze-planning benchmark for navigation under sequential decisions. |
| 6 | GameTraversalBenchmark | GameTraversalBenchmark | P2 | deep | 3,4,6 | 2D game-map traversal benchmark for multi-step planning. |
| 7 | ARCAGI3Exploration | ARC-AGI-3 Interactive Reasoning | P3 | structured-skim | 2,3,7 | Boundary-case interactive reasoning task retained as an adjacent comparison item. |

## Expected Survey Payoff
- Preserve a comparison set for specialized diagnostics without inflating their survey centrality.
- Make it easier to separate narrow reasoning probes from fuller game-agent benchmarks.

## Questions To Resolve While Reading
- Which of these tasks should count as games for this survey and which should stay as adjacent diagnostics?
- When do symbolic planning gains fail to transfer into richer interactive settings?

## Exit Criteria
- every paper in this batch has a paper card
- registry rows are synced
- unresolved ambiguity is explicit
- outline gaps exposed by the batch are noted
- batch status in `corpus/batches/batch_index.md` is updated

