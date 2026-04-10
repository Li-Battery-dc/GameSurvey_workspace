# CompleteChessGames Complete Chess Games Enable LLM Become A Chess Master

## 0. Metadata
- Date: 2025/01
- Venue: NAACL
- Authors: Yinqi Zhang, Xintian Han, Haolong Li, Kedi Chen, Shaohui Lin
- Paper link: https://arxiv.org/pdf/2501.17186v2.pdf
- Code link:
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: high
- Review gate label: usable

## 1. One-paragraph benchmark summary
- This paper is primarily a chess-specialist training and evaluation paper rather than a benchmark paper. It trains ChessLLM on a large FEN-to-best-move dataset derived from online games and Stockfish search, then evaluates the model with both static board-state accuracy and full matches against Stockfish. The paper's main survey value is not benchmark creation but the contrast it offers between static move-prediction metrics, legal-move pass rates, and complete-game Elo under a highly abstracted text interface. For this survey, it should be treated as a specialist comparison point on rule grounding, board-state abstraction, and full-game evaluation rather than as a reusable benchmark anchor.

## 2. Position in our survey
- Why-games relevance: Chess remains a clean test of legal action generation and strategic quality under exact rules.
- Historical stage: diagnostic capability probe
- Narrative level(s): L1 rule following / L2 strategic reasoning
- Most relevant outline section(s): 1,2,3,4
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
- Real game / simulated game / designed task-game hybrid: real board game represented through textual FEN states and next-move prediction
- Benchmark unit: move / full game

### 3.3 Benchmark scope
- Scope: single game
- Number of games / tasks: 10,000 evaluation board states plus full-game matches against Stockfish
- Benchmark intent: diagnostic evaluation / specialist evaluation

### 3.4 Modality
- Primary modality: text / symbolic state
- Perception burden retained: board-state interpretation and move legality
- Perception burden removed: no visual board perception or natural GUI interaction

## 4. What this benchmark measures
- Primary capability target: legal and strong chess move generation from textual board state
- Secondary capability target(s): relation between long-round supervision, legal move generation, and match Elo
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? no
- Does it test social reasoning / deception / cooperation? no
- Does it test visual grounding / spatial-temporal reasoning? no
- Does it test long-horizon autonomy / task completion? partially
- Does it test real-time efficiency? no
- Does it test cross-game transfer / open-ended generalization? no
- Why is a game environment especially suitable here? Chess offers exact legality checks and strong external engines for calibrated full-game evaluation.

## 5. Interaction paradigm
- Observation channel: FEN board states encoded as text
- Action channel: next-move generation
- Interface type: natural language / structured action space / hybrid
- Agent scaffold allowed: sampling to recover legal moves during game evaluation
- Is there privileged API access? yes; board states are given in a machine-friendly notation
- How close is the setup to human play? low; the evaluation uses textual board encodings rather than natural board vision
- Main ecological-validity trade-off: the paper measures strategic performance cleanly, but through a strongly abstracted interface

## 6. Evaluation protocol
- Main score: full-game Elo against Stockfish
- Auxiliary score(s): legal-move accuracy, best-move accuracy, pass@1 in actual games, and win rate by Stockfish skill level
- Evaluation style: Elo / accuracy / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: the model is evaluated against Stockfish at different skill levels and on held-out board states
- Automatic verifiability: high
- Calibration method: 10,000 unique board positions and repeated match play against Stockfish
- Anti-contamination argument: no explicit contamination defense beyond arguing that actual games against Stockfish are more robust than a static evaluation set
- Reliability or comparability concerns: results depend heavily on FEN-state abstraction, Stockfish-generated supervision, and legal-move recovery via sampling during game evaluation

## 7. Main contributions
- Contribution 1: Shows that complete-game supervised data can train an LLM to finish full chess games.
- Contribution 2: Connects long-round data quality to large Elo improvements.
- Contribution 3: Uses full-game evaluation against Stockfish rather than only static move prediction.

## 8. Main findings and failure modes
- Core empirical takeaway: with long-round supervision and textual FEN inputs, ChessLLM reaches about 1788 Elo against low-skill Stockfish settings while maintaining high legal-move rates.
- Notable model failure mode 1: weaker play when training data lacks long, complete games
- Notable model failure mode 2: best-move prediction remains much lower than legal-move generation accuracy
- Notable model failure mode 3: performance still depends on sampling to recover legal moves in full games
- Does this paper reveal a benchmark-design limitation as well? yes; it argues that static evaluation sets are insufficient for chess and should be supplemented by actual games

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Limited use; mostly a specialist upper-bound case.
- Best use in Section 1 (taxonomy and evolutionary levels): Useful in the lineage of LLMs entering classical board games. Helps contrast single-game specialists with broader benchmark suites.
- Best use in Section 2 (core capabilities evaluated by games): Supports legal-action and move-quality discussions.
- Best use in Section 3 (interaction and evaluation paradigm): A contrast case for text-encoded board states. Good example of mixing static board evaluation with full-game Elo tests.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Supports caution when broad survey claims rely on specialist-trained models.

## 10. Relation to nearby papers
- Closest predecessor(s): LLMChess and ChessGPT
- Closest follow-up(s): other chess-specialist LLMs
- Best comparison targets inside our corpus: LLMChess, MixingExpertKnowledge, PokerBench
- What this paper uniquely adds relative to neighbors: It is a full-game chess-specialist training case that explicitly compares static board-state evaluation with actual-game Elo under a text-only interface.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- The paper reports roughly 1788 Elo for ChessLLM against Stockfish with sampling up to 10 times to obtain legal moves.
- It uses 10,000 unique board positions in an evaluation set and supplements them with full matches.
- The authors report that long-round data supervision improves Elo by about 350 points over short-round data.
- On in-distribution evaluation data, the paper reports 99.11% legal-move accuracy at 0.5B tokens and 40.11% best-move accuracy at 2.75B tokens.

### 11.2 Our synthesis / interpretation
- This paper is useful mainly as a specialist upper bound and as a warning not to conflate chess-specialized training results with reusable benchmark design.
- It is also a good contrast case for why static board-state metrics and full-game evaluation should be reported together when the interface is heavily abstracted.

### 11.3 Uncertain or needs re-check
- If later drafting needs more detail, re-check the exact training-token scale attached to the strongest Elo point in Figure 1 and the strongest best-move point in Figure 3.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? Already audited from the full paper; revisit only if we later need figure-level numbers in a specialist-comparison subsection.
- Which section to read next if needed: actual games / evaluation-set analysis
- Follow-up question(s): How should the survey describe the dependence of full-game chess results on textual state abstraction and legal-move sampling without overstating the model's strategic depth?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P2
- Reading depth: deep
- Batch ID: B13
- Outline sections: 1,2,3,4
- Survey role: contrast
- Paper card path: `paper_cards/B13/CompleteChessGames.md`
- Next action: draft-section
- Last updated: 2026-04-09
