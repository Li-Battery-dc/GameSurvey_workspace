# Batch B07: evaluation-paradigms-and-instrumentation

## Why This Batch Exists
- Collect papers whose main contribution is how the benchmark measures agents: arenas, diagnostics, live evaluation, or methodology framing.
- Support Section 3 and Section 4's benchmark-design critique.

## Suggested Drafting Order

| Order | paper_id | Title | Survey role | Outline anchors | Why this paper is in the batch |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | GAMEBoT | GAMEBoT: Transparent Assessment of LLM Reasoning in Games | contrast | 1,3,4 | Transparent subproblem decomposition clarifies process metrics beyond raw win rate. |
| 2 | Clembench | clembench: Using Game Play to Evaluate Chat-Optimized Language Models as Conversational Agents | representative | 1,3 | Dialogue-game evaluation framework that broadens benchmark instrumentation beyond win rate and static task instances. |
| 3 | Clembench2024 | clembench-2024: A Challenging, Dynamic, Complementary, Multilingual Benchmark and Underlying Flexible Framework for LLMs as Multi-Action Agents | contrast | 1,3,4 | Framework expansion that adds multilingual and multi-action dialogue games to the clembench line. |
| 4 | ThirdParadigm | A Third Paradigm for LLM Evaluation: Dialogue Game-Based Evaluation using clembench | contrast | 0,1,3,4 | Meta-evaluation framing paper that helps position dialogue games against static and arena-style evaluation. |
| 5 | CATArena | CATArena: Evaluation of LLM Agents through Iterative Tournament | contrast | 1,3,4 | Contrast case for code-agent tournament evaluation, iterative peer learning, and variant-based non-saturation; not direct-play evidence. |
| 6 | WhoIsABetterPlayer | Who is a Better Player: LLM against LLM | contrast | 1,3,4 | Pool-dependent LLM-vs-LLM board-game arena useful for Elo/PLG methodology contrast and ranking-instability cautions. |
| 7 | GameArena | GameArena: Evaluating LLM Reasoning Through Live Computer Games | representative | 0,1,3,4 | Live human-game benchmark with retrospective reasoning analysis and far higher useful-session yield than chat arenas. |
| 8 | ARCAGI3 | ARC-AGI-3: A New Challenge for Frontier Agentic Intelligence | contrast | 2,3,4 | Boundary L2/L5 contrast on first-contact adaptation, private OOD generalization, and harness-versus-general-agent evaluation policy; not a visual-agency benchmark. |
| 9 | GameWorld | GameWorld: Towards Standardized and Verifiable Evaluation of Multimodal Game Agents | anchor | 0,1,2,3,4 | Standardized browser-game benchmark with state-verifiable evaluation, dual control interfaces, capability-layer diagnostics, and reproducibility analyses; broad suite coverage, but not a held-out transfer benchmark. |

## Expected Survey Payoff
- Make the evaluation-design comparison explicit instead of burying it inside environment sections.
- Keep process metrics, live play, tournaments, and benchmark meta-framing in one working set.

## Questions To Resolve While Drafting
- Which scoring families are comparable, and which answer fundamentally different questions?
- Where do live arenas, process metrics, and diagnostic decompositions give stronger evidence than raw outcome scores?

## Batch Use Note
- Use this batch to draft Section 3.2 and the benchmark-design bottlenecks in Section 4.2.
