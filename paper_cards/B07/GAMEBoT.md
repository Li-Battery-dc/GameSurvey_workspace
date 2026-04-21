# GAMEBoT GAMEBoT: Transparent Assessment of LLM Reasoning in Games

## 0. Metadata
- Date: 2024/12
- Venue: ACL 2025
- Authors: Wenye Lin, Jonathan Roberts, Yunhan Yang, Samuel Albanie, Zongqing Lu, Kai Han
- Paper link: https://arxiv.org/pdf/2412.13602v2
- Code link:
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: high
- Review gate label: strong

## 1. One-paragraph benchmark summary
- GAMEBoT is a competitive game benchmark that evaluates both final outcomes and intermediate reasoning steps rather than treating win rate as the whole story. It covers eight games across board, action, card, and game-theoretic categories, decomposes each decision into two to three rule-verifiable subproblems, and scores both the intermediate reasoning outputs and the eventual game result. The benchmark combines curated game-specific CoT prompts, 20-match head-to-head competitions, and rule-based solvers for subproblem validation to expose hidden reasoning failures that outcome-only evaluation would miss. For this survey, GAMEBoT is most useful as a protocol paper showing how game benchmarks can become more interpretable while also becoming more prompt-shaped.

## 2. Position in our survey
- Why-games relevance: Games provide repeated, rule-bounded decision points where intermediate reasoning can be checked against ground truth rather than inferred from a single final answer.
- Historical stage: diagnostic capability probe
- Benchmark level(s): L2 strategic reasoning
- Most relevant outline section(s): 1,3,4
- Role in corpus: contrast

## 3. Design-space coding
### 3.1 Structure
- Form: Match
- Construction: Wrapped
- Construction note: curated suite of existing games under unified text interfaces
- Benchmark unit: match

### 3.2 Mechanics profile
- State visibility: mixed
- Transition uncertainty: mixed
- Actor configuration: multi-agent
- Incentive structure: mixed
- Temporal regime: hybrid

### 3.3 Benchmark scope
- Scope: curated suite
- Number of games / tasks: 8 games

### 3.4 Modality
- Observation modality: text or symbolic
- Action modality: semantic
- Perception burden retained: rule understanding, game-state tracking, subgoal reasoning, and opponent-aware decision making
- Perception burden removed: gameplay is represented in text rather than through native visual interfaces

## 4. What this benchmark measures
- Primary capability target: process-level reasoning quality during gameplay
- Secondary capability target(s): spatial reasoning, mathematical reasoning, long-term path planning, risk management, and competitive collaboration depending on the game
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? yes
- Does it test social reasoning / deception / cooperation? partially
- Does it test visual grounding / spatial-temporal reasoning? no
- Does it test long-horizon autonomy / task completion? partially
- Does it test real-time efficiency? no
- Does it test cross-game transfer / open-ended generalization? no
- Why is a game environment especially suitable here? Games naturally decompose into repeated decisions, so intermediate reasoning can be aligned with local subproblems instead of judged only by final success.

## 5. Interaction paradigm
- Observation channel: text representations of the current game state plus curated chain-of-thought prompts with game rules and strategy hints
- Action channel: explicit reasoning steps followed by a chosen move
- Interface type: natural language
- Agent scaffold allowed: other
- Is there privileged API access? yes
- How close is the setup to human play? medium-low; the games are real, but play is mediated through text states and prompt decomposition
- Main ecological-validity trade-off: GAMEBoT improves interpretability by decomposing reasoning, but the prompt and subproblem design intervene strongly in the natural play process

## 6. Evaluation protocol
- Main score: paired outcome score and intermediate-step score for each game
- Auxiliary score(s): per-subproblem accuracy or F1, plus prompt-baseline comparisons for selected games
- Evaluation style: tournament / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: 17 LLMs compete head-to-head in 20-match pairings against each other, with a random player as baseline and rule-based verification of intermediate reasoning
- Automatic verifiability: high
- Calibration method: 20 matches per model pairing with side balancing, curated but model-agnostic CoT prompts, and exact rule-based checking for each game's subproblems
- Anti-contamination argument: dynamic competition broadens the exposed state distribution relative to fixed single-agent game datasets
- Reliability or comparability concerns: conclusions depend on the quality of the manually designed subproblem decompositions and on prompts that already inject game-specific strategic knowledge

## 7. Main contributions
- Contribution 1: Introduces a benchmark that evaluates both final gameplay outcomes and intermediate reasoning steps.
- Contribution 2: Covers eight games spanning different game types and strategic demands.
- Contribution 3: Uses rule-based subproblem verification to make benchmark scores more interpretable.

## 8. Main findings and failure modes
- Core empirical takeaway: intermediate-step scores strongly predict final outcomes overall, but some games expose mismatches where outcome-only evaluation would misread model ability.
- Notable model failure mode 1: models can achieve acceptable final outcomes while still showing weak intermediate reasoning quality
- Notable model failure mode 2: performance is highly inconsistent across games, even for strong models
- Notable model failure mode 3: all tested LLMs nearly fail some multi-hop subproblems, such as Othello wedge detection, Checkers sacrifice reasoning, and Connect4 opponent-threat detection
- Does this paper reveal a benchmark-design limitation as well? yes; it shows that subproblem design itself becomes part of the benchmark and can shape what is being measured

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Demonstrates why repeated interactive decisions make game environments suitable for process-level reasoning evaluation.
- Best use in Section 1 (taxonomy and evolutionary levels): Useful as a newer response to the criticism that game benchmarks often measure only outcomes. Helps distinguish broad game suites from process-oriented diagnostic suites.
- Best use in Section 2 (core capabilities evaluated by games): Supports discussion of decomposable reasoning skills inside games.
- Best use in Section 3 (interaction and evaluation paradigm): Good contrast case for heavily prompt-shaped interfaces. One of the best references for outcome versus process evaluation.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Supports the claim that future benchmarks may need process supervision, but that process definitions are themselves a benchmark-design choice.

## 10. Relation to nearby papers
- Closest predecessor(s): GTBench and other outcome-focused strategic suites
- Closest follow-up(s): benchmark designs that include process metrics or richer instrumentation
- Best comparison targets inside our corpus: Clembench, Clembench2024, ThirdParadigm, CATArena
- What this paper uniquely adds relative to neighbors: It makes intermediate reasoning verification the center of the benchmark rather than an auxiliary analysis.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- GAMEBoT evaluates 17 LLMs across eight games that include Othello, Checkers, TicTacToe, Connect4, Pong, Surround, Texas Hold'em, and Negotiation v2.
- Each move is decomposed into 2-3 subproblems with rule-based verification, and the benchmark reports both outcome scores and intermediate-step scores.
- The benchmark runs 20 head-to-head matches for each model pairing, with each model playing 10 matches as first player and 10 as second player.
- The strongest reported average intermediate-step score is only 0.52, and Appendix C shows near-total failure on some complex subproblems.

### 11.2 Our synthesis / interpretation
- GAMEBoT is one of the clearest papers in the corpus for arguing that outcome-only game benchmarking can be misleading.
- It is especially useful for Section 3 because it formalizes a concrete alternative rather than only criticizing win rate.
- It should be used as a process-evaluation contrast case, not as evidence of human-like or minimally scaffolded game play.

### 11.3 Uncertain or needs re-check
- Re-check Section 3.1.3 and Appendix G if we later need the exact game-specific exceptions where outcome and intermediate scores diverge most.
- Re-check Appendix B if we later need the full wording of each subproblem design or the Negotiation v2 modification details.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? Full paper read completed for this audit; no further general reading is needed unless we need game-specific examples or exact subproblem wording.
- Which section to read next if needed: Appendix B / Section 3.1.3 / Appendix G
- Follow-up question(s): Which GAMEBoT games provide the cleanest examples for showing why process metrics can overturn outcome-only rankings?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P1
- Reading depth: deep
- Batch ID: B07
- Outline sections: 1,3,4
- Survey role: contrast
- Paper card path: `paper_cards/B07/GAMEBoT.md`
- Check status: unchecked
- Last updated: 2026-04-10
