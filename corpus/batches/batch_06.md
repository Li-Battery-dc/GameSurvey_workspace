# Batch B06: level-5-generalization-and-open-endedness

## Why This Batch Exists
- Keep the Level 5 evidence together: cross-game generalization, expandable game spaces, and open-ended task generalization.
- Separate true cross-title transfer from single-world open-ended task diversity while keeping both under the Level 5 narrative.
- Support Level 5 in Section 1 and Section 2.5 on transfer, scale, open-endedness, and benchmark growth.

## Suggested Drafting Order

| Order | paper_id | Title | Survey role | Outline anchors | Why this paper is in the batch |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | AIGameStore | AI GAMESTORE: Scalable, Open-Ended Evaluation of Machine General Intelligence with Human Games | anchor | 0,1,3,4 | Open-ended platform vision for evaluating human-like general intelligence across human games. |
| 2 | Orak | Orak: A Foundational Benchmark for Training and Evaluating LLM Agents on 12-Genre Video Games | anchor | 1,2,3,4 | Broad curated train-and-eval benchmark bridging benchmark suites and cross-game generalization. |
| 3 | GVGAILLM | GVGAI-LLM: Evaluating Large Language Model Agents with Infinite Games | representative | 1,2,3,4 | General video game benchmark with procedural breadth and reproducible ASCII state interfaces. |
| 4 | GameVerse | GameVerse: Can VLMs Learn from Video-based Reflection? | representative | 1,2,3,4 | Cross-game VLM benchmark with reflect-and-retry loops and milestone evaluation. |
| 5 | TextQuests | TextQuests: How Good are LLMs at Text-Based Video Games? | representative | 2,3,4 | Multi-game text-adventure suite that brings long-horizon parser games into the Level 5 evidence block, with scaffold caveats. |
| 6 | TextAtari | TextAtari: 100K Frames Game Playing with Language Agents | contrast | 2,3,4 | Textified 23-game Atari suite useful as a privileged-interface Level 5 contrast on long-horizon cross-game control. |
| 7 | MCU | MCU: An Evaluation Framework for Open-Ended Game Agents | representative | 0,1,2,3,4 | Open-ended Minecraft benchmark with task composition and human-aligned AutoEval; strong for single-world open-ended task generalization. |
| 8 | StarDojo | StarDojo: Benchmarking Open-Ended Behaviors of Agentic Multimodal LLMs in Production-Living Simulations with Stardew Valley | representative | 2,3,4 | Production-living simulation benchmark for open-ended task diversity inside a rich commercial world; not cross-title transfer. |
| 9 | PuzzleJAX | PuzzleJAX: A Benchmark for Reasoning and Learning | contrast | 1,2,4 | PuzzleScript-to-JAX family gives an expandable symbolic-game contrast on DSL-backed breadth and overfitting resistance. |
| 10 | LMGameBench | LMGAME-BENCH: How Good are LLMs at Playing Games? | representative | 0,1,2,3 | Unified game benchmark with explicit perception and memory breakdowns for agent evaluation. |
| 11 | TextArena | TextArena | representative | 1,2,3,4 | Competitive text-game suite with online-play ratings that broadens benchmark-platform discussion. |

## Expected Survey Payoff
- Distinguish curated multi-game suites, expandable game families, and single-world open-ended task spaces.
- Give the survey one clean evidence block for Level 5: transfer, saturation resistance, benchmark growth, and open-ended task evaluation.

## Questions To Resolve While Drafting
- Which papers truly test transfer, and which mostly enlarge the benchmark surface?
- How should the survey distinguish benchmark breadth from open-endedness?
- Which single-world open-ended task benchmarks should be described as Level 5 evidence without being overclaimed as cross-game transfer?
- Use GameWorld as a boundary comparison: a 34-game suite with open-ended tasks can broaden coverage without yet constituting held-out cross-game transfer.

## Batch Use Note
- Use this batch to draft Level 5 and Section 2.5 on transfer, scale, and open-ended benchmark growth.
