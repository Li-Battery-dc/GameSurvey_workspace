# CompleteChessGames Complete Chess Games Enable LLM Become A Chess Master

## 0. Metadata
- Date: 2025/01
- Venue: NAACL
- Authors: Yinqi Zhang, Xintian Han, Haolong Li, Kedi Chen, Shaohui Lin
- Paper link: https://arxiv.org/pdf/2501.17186v2.pdf
- Code link:
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: medium
- Review gate label: usable

## 1. One-paragraph benchmark summary
- This paper is primarily a specialist training paper rather than a benchmark-creation paper, but it is still relevant because it evaluates an LLM chess model through full games against Stockfish and connects training data quality to gameplay strength. ChessLLM is trained on a large corpus of complete games and predicts moves from textual board encodings such as FEN, then is assessed using legal-move accuracy, best-move accuracy, win rate, and Elo from full matches. The result is a domain-specialist LLM that reaches roughly amateur-competitive play. For this survey, the paper is best treated as an upper-bound specialist comparison point rather than a benchmark anchor.

## 2. Position in our survey
- Why-games relevance: Chess remains a clean test of legal action generation and strategic quality under exact rules.
- Historical stage: diagnostic capability probe / specialist comparison
- Narrative level(s): L2 strategic reasoning
- Most relevant outline section(s): 1,4
- Role in corpus: contrast

## 3. Design-space coding
### 3.1 Environment structure
- Information structure: perfect
- Transition structure: deterministic
- Agent structure: two-player
- Social structure: competitive
- Time structure: turn-based

### 3.2 World structure
- World type(s): board
- Real game / simulated game / designed task-game hybrid: real game represented as text
- Benchmark unit: move / full game

### 3.3 Benchmark scope
- Scope: single game
- Number of games / tasks: 10,000 evaluation board states plus full-game matches against Stockfish
- Benchmark intent: specialist evaluation

### 3.4 Modality
- Primary modality: text / symbolic state
- Perception burden retained: board-state interpretation and move legality
- Perception burden removed: no visual board perception or natural GUI interaction

## 4. What this benchmark measures
- Primary capability target: legal and strong chess move generation from textual board state
- Secondary capability target(s): relation between complete-game training data and match Elo
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? no
- Does it test social reasoning / deception / cooperation? no
- Does it test visual grounding / spatial-temporal reasoning? no
- Does it test long-horizon autonomy / task completion? partially
- Does it test real-time efficiency? no
- Does it test cross-game transfer / open-ended generalization? no
- Why is a game environment especially suitable here? Chess offers exact legality checks and strong external engines for calibrated full-game evaluation.

## 5. Interaction paradigm
- Observation channel: FEN-like board state encoded as text dialogue
- Action channel: next-move generation
- Interface type: natural language / structured action space / hybrid
- Agent scaffold allowed: sampling up to find a legal move
- Is there privileged API access? yes; board states are given in a machine-friendly notation
- How close is the setup to human play? low; the evaluation uses textual board encodings rather than natural board vision
- Main ecological-validity trade-off: the paper measures strategic performance cleanly, but through a strongly abstracted interface

## 6. Evaluation protocol
- Main score: full-game Elo against Stockfish
- Auxiliary score(s): legal move accuracy, best-move accuracy, pass@1, and win rate by Stockfish skill level
- Evaluation style: Elo / accuracy / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: the model is evaluated against Stockfish at different skill levels and on held-out board states
- Automatic verifiability: high
- Calibration method: 10,000 unique board positions and repeated match play against Stockfish
- Anti-contamination argument: full-game evaluation supplements static board-state accuracy
- Reliability or comparability concerns: legal-move sampling and textual board encoding simplify the task relative to natural human play

## 7. Main contributions
- Contribution 1: Shows that complete-game supervised data can train an LLM to finish full chess games.
- Contribution 2: Connects long-round data quality to large Elo improvements.
- Contribution 3: Uses full-game evaluation against Stockfish rather than only static move prediction.

## 8. Main findings and failure modes
- Core empirical takeaway: with high-quality complete-game supervision, a specialist LLM can reach about 1788 Elo and maintain high legal-move accuracy.
- Notable model failure mode 1: weaker play when training data lacks long, complete games
- Notable model failure mode 2: best-move prediction remains much lower than legal-move accuracy
- Notable model failure mode 3: performance still depends on sampling and legality filtering
- Does this paper reveal a benchmark-design limitation as well? yes; it argues that static evaluation sets are insufficient for chess and should be supplemented by actual games

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Limited use; mostly a specialist upper-bound case.
- Best use in Section 1 (taxonomy and evolutionary levels): Useful in the lineage of LLMs entering classical board games. Helps contrast single-game specialists with broader benchmark suites.
- Best use in Section 2 (core capabilities evaluated by games): Supports legal-action and move-quality discussions.
- Best use in Section 3 (interaction and evaluation paradigm): A contrast case for text-encoded board states. Good example of mixing static board evaluation with full-game Elo tests.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Supports caution when broad survey claims rely on specialist-trained models.

## 10. Relation to nearby papers
- Closest predecessor(s): LLMChess
- Closest follow-up(s): other chess-specialist LLMs
- Best comparison targets inside our corpus: LLMChess, PokerBench, MixingExpertKnowledge
- What this paper uniquely adds relative to neighbors: It is a full-game specialist training case built around complete-game supervision rather than a benchmark platform.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- The paper reports roughly 1788 Elo for ChessLLM against Stockfish with sampling up to 10 times to obtain legal moves.
- It uses 10,000 unique board positions in an evaluation set and supplements them with full matches.
- The authors report that long-round data supervision improves Elo by about 350 points over short-round data.

### 11.2 Our synthesis / interpretation
- This paper is useful mainly as a specialist upper bound and a warning not to conflate specialist training results with benchmark breadth.
- It is also a nice example of why full-game evaluation matters even in domains with exact move labels.

### 11.3 Uncertain or needs re-check
- Re-check whether the reported Elo assumes 10-sample legality filtering throughout.
- Re-check the exact legal-move and best-move accuracies at the strongest data scale if later needed.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? Only if we later need a specialist-comparison subsection.
- Which section to read next if needed: evaluation methods / actual games / data-quality analysis
- Follow-up question(s): How much of the final Elo depends on sampling versus the underlying policy quality?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P2
- Reading depth: deep
- Batch ID: B13
- Outline sections: 1,4
- Survey role: contrast
- Paper card path: `paper_cards/B13/CompleteChessGames.md`
- Next action: draft-section
- Last updated: 2026-04-05
