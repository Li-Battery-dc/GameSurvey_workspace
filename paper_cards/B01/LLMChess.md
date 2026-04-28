# LLMChess LLM CHESS: Benchmarking Reasoning and Instruction-Following in LLMs through Chess

## 0. Metadata
- Date: 2025/12
- Venue: arXiv
- Authors: Sai Kolasani, Maxim Saplin, Nicholas Crispino, Kyle Montgomery, Jared Quincy Davis, Matei Zaharia, Chi Wang, Chenguang Wang
- Paper link: https://arxiv.org/pdf/2512.01992v1
- Code link: https://github.com/maxim-saplin/llm_chess
- Reading depth: deep
- Card status: finalized
- Confidence in this card: high
- Review gate label: usable

## 1. One-paragraph benchmark summary
- LLM Chess uses full chess games to benchmark both reasoning quality and instruction following in a tightly controlled agentic setting. Instead of letting models directly emit moves from raw board text, it gives them three actions: fetch the board, fetch legal moves, or make a move, then scores the resulting gameplay with chess-native and benchmark-native metrics. The benchmark first tests many models against random play and then evaluates stronger models against a chess engine with varying difficulty. It matters for this survey because it is a clean single-game probe of legal action generation, tool use, and strategic reasoning under a combinatorially rich ruleset.

## 2. Position in our survey
- Why-games relevance: Chess supplies a high-contamination-resistance, automatically verifiable environment where legal-move errors and strategic weakness are easy to separate.
- Historical stage: diagnostic capability probe
- Benchmark level(s): L1 rule understanding / L2 strategic reasoning
- Most relevant outline section(s): 1,2,3
- Role in corpus: representative

## 3. Design-space coding
### 3.1 Structure
- Form: Match
- Construction: Adapted
- Construction note: real game with engine-mediated benchmark wrapper
- Benchmark unit: full game

### 3.2 Mechanics profile
- State visibility: full
- Transition uncertainty: deterministic
- Actor configuration: multi-agent
- Incentive structure: competitive
- Temporal regime: turn-based

### 3.3 Benchmark scope
- Scope: single game
- Number of games / tasks: chess only

### 3.4 Modality
- Observation modality: text or symbolic
- Action modality: semantic
- Perception burden retained: board-state interpretation, legal move selection, long-horizon tactical consequences
- Perception burden removed: raw visual board perception and natural move history handling

## 4. What this benchmark measures
- Primary capability target: rule grounding and instruction-following in a strategic board game
- Secondary capability target(s): tactical planning, long-horizon reasoning, tool use discipline
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? no
- Does it test social reasoning / deception / cooperation? no
- Does it test visual grounding / spatial-temporal reasoning? partially, in symbolic board space
- Does it test long-horizon autonomy / task completion? yes
- Does it test real-time efficiency? no
- Does it test cross-game transfer / open-ended generalization? no
- Why is a game environment especially suitable here? Chess has precise legality rules, strong engine supervision, and enough combinatorial depth to keep the benchmark informative as models improve.

## 5. Interaction paradigm
- Observation channel: optional tool calls for current board and legal moves
- Action channel: UCI move strings via `make_move`
- Interface type: API / hybrid
- Agent scaffold allowed: tool use
- Is there privileged API access? yes
- How close is the setup to human play? low to medium; it preserves chess logic but gives explicit tools and withholds move history
- Main ecological-validity trade-off: The agentic tool setup surfaces instruction-following failures clearly, but it is more scaffolded than ordinary human chess play because legal moves are exposed and move history is omitted.

## 6. Evaluation protocol
- Main score: Win/Loss percentage
- Auxiliary score(s): Elo, per-ply chess-engine metrics, instruction-following error rates
- Evaluation style: win rate / Elo / process metrics / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: random-agent gating plus fixed Dragon 1 engine opponents; no human baseline
- Automatic verifiability: high
- Calibration method: engine skill ladders, maximum-likelihood Elo estimation with 95% confidence intervals, and Stockfish-based per-ply move-quality metrics
- Anti-contamination argument: chess's combinatorial richness and engine-based play reduce simple benchmark saturation
- Reliability or comparability concerns: the privileged tools, omitted move history, prompt-format sensitivity, and timeout behavior all materially affect results

## 7. Main contributions
- Contribution 1: Turns chess into an agentic benchmark with tool calls rather than plain next-move prediction.
- Contribution 2: Measures instruction-following errors separately from chess strength.
- Contribution 3: Uses engine-grounded per-ply metrics and Elo to keep the benchmark informative as models improve.

## 8. Main findings and failure modes
- Core empirical takeaway: Many models cannot reliably beat even a random opponent, and the strongest tested models still peak only around average online-player Elo when grounded against a calibrated chess engine.
- Notable model failure mode 1: many losses are caused by wrong actions and other instruction-following failures rather than purely bad chess
- Notable model failure mode 2: performance is highly sensitive to legal-move access, board representation, and whether the setup stays fully agentic
- Notable model failure mode 3: timeout and model-serving failures can materially degrade high-reasoning models under realistic time limits
- Does this paper reveal a benchmark-design limitation as well? yes; the chosen tool access simplifies some real chess burdens while intentionally foregrounding others

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Illustrates how a familiar deterministic game can reveal agentic failures that static chess positions or next-move prediction hide: full-game play exposes tool-use, formatting, legality, timeouts, and recovery failures.
- Best use in Section 1 (taxonomy and evolutionary levels): Strong single-game Level 1/2 diagnostic probe. It keeps the game form simple and fully observable, which makes the boundary between legal participation and deeper chess strength easy to explain.
- Best use in Section 2 (core capabilities evaluated by games): Good evidence for rule grounding, instruction-following, tool-use discipline, tactical reasoning, and symbolic spatial planning under a large combinatorial state space.
- Best use in Section 3 (interaction and evaluation paradigm): Strong interface-privilege case: the benchmark exposes `get_current_board`, `get_legal_moves`, and `make_move`, omits move history, and shows through ablations that legal-move access, board representation, and simplifying the agentic tool loop materially change performance.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Supports the claim that instruction following and interface robustness remain bottlenecks even in formal domains, and that calibrated engine ladders can keep a single-game benchmark informative as models improve.

## 10. Relation to nearby papers
- Closest predecessor(s): chess-as-reasoning studies and earlier chess finetuning papers
- Closest follow-up(s): BoardGameArena, BotzoneBench
- Best comparison targets inside our corpus: BoardGameArena, BotzoneBench, SmartPlay, GTBench
- What this paper uniquely adds relative to neighbors: It explicitly separates chess strength from benchmarked tool-use and instruction-following reliability.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- LLM Chess gives models three actions: get the current board, get legal moves, or make a move in UCI notation.
- The benchmark caps games at 100 moves, allows up to 10 conversation turns per ply, and omits move history while preserving board-state access.
- It reports Win/Loss, Elo with 95% confidence intervals for stronger models, and per-game/per-ply indicators including instruction-following errors.
- The paper finds that most models cannot consistently beat a random opponent, and reasoning models perform much better than non-reasoning ones.
- The engine phase uses Komodo Dragon 1 skill levels as calibrated opponents; the strongest reported model peaks around Elo 758 in this setup.
- Ablations show the agentic interface itself is a measured burden: providing only `make_move` while putting board and legal moves directly in the prompt improves win/loss for both tested models, while removing legal-move access has model-dependent effects.

### 11.2 Our synthesis / interpretation
- This card is most useful as a narrow diagnostic benchmark rather than a broad strategic-play benchmark.
- The privileged tool setup is a feature for measurement clarity, but it also limits ecological claims and makes robustness to interface changes a central interpretive caveat.

### 11.3 Uncertain or needs re-check
- Recheck Appendix B or C if we later need exact engine settings, ablations, or centipawn-threshold definitions.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? Completed in this audit; the design choices, ablations, Elo procedure, and timeout behavior are now clear enough for survey use.
- Which section to read next if needed: 2.1 / 2.2 / Appendix A
- Follow-up question(s): Which tool-access ablation should anchor our discussion of privileged interfaces?

## 13. Registry sync
- Registry row synced: yes
- Registry status: finalized
- Priority: P1
- Reading depth: deep
- Batch ID: B01
- Outline sections: 1,2,3
- Survey role: representative
- Paper card path: `paper_cards/B01/LLMChess.md`
- Check status: unchecked
- Next action: draft-section
- Last updated: 2026-04-27
