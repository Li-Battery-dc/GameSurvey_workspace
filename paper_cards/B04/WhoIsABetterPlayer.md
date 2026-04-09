# WhoIsABetterPlayer Who is a Better Player: LLM against LLM

## 0. Metadata
- Date: 2025/08
- Venue: arXiv
- Authors: Yingjie Zhou, Jiezhang Cao, Farong Wen, Li Xu, Yanwei Jiang, Jun Jia, Ronghui Li, Xiaohong Liu, Yu Zhou, Xiongkuo Min, Jie Guo, Zicheng Zhang, Guangtao Zhai
- Paper link: https://arxiv.org/pdf/2508.04720v1
- Code link:
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: high
- Review gate label: usable

## 1. One-paragraph benchmark summary
- This paper builds Qi Town, an LLM-vs-LLM board-game platform that runs round-robin tournaments across five games and scores models with technical and affective metrics. It combines four fixed-rule games, namely Tic-Tac-Toe, Gomoku, Reversi, and Chess, with a Free-Style mode where agents negotiate rules before play, then analyzes outcomes using Elo, Performance Loop Graphs (PLGs), and Positive Sentiment Score (PSS). For this survey, it is mainly a contrast case for pool-dependent arena evaluation rather than a stable benchmark anchor.

## 2. Position in our survey
- Why-games relevance: Board games create a dynamic alternative to static QA benchmarks and expose strategic instability through direct model-vs-model interaction.
- Historical stage: diagnostic capability probe
- Narrative level(s): L2 strategic reasoning
- Most relevant outline section(s): 1,3,4
- Role in corpus: contrast

## 3. Design-space coding
### 3.1 Environment structure
- Information structure: perfect
- Transition structure: deterministic
- Agent structure: multi-agent
- Social structure: competitive
- Time structure: turn-based

### 3.2 World structure
- World type(s): board
- Real game / simulated game / designed task-game hybrid: real board games plus one designed free-style negotiation variant
- Benchmark unit: tournament match

### 3.3 Benchmark scope
- Scope: curated suite
- Number of games / tasks: 5 games
- Benchmark intent: diagnostic evaluation

### 3.4 Modality
- Primary modality: text
- Perception burden retained: board-state reasoning, move planning, opponent adaptation, rule negotiation in Free-Style
- Perception burden removed: visual board perception and physical interaction

## 4. What this benchmark measures
- Primary capability target: adversarial strategic play under direct LLM-vs-LLM competition
- Secondary capability target(s): tournament ranking stability, emotional response patterns, rule negotiation
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? no
- Does it test social reasoning / deception / cooperation? partially, through Free-Style negotiation and sentiment tracking
- Does it test visual grounding / spatial-temporal reasoning? no
- Does it test long-horizon autonomy / task completion? no
- Does it test real-time efficiency? no
- Does it test cross-game transfer / open-ended generalization? no
- Why is a game environment especially suitable here? Repeated adversarial play makes cyclic win-loss structure visible in a way static benchmarks cannot.

## 5. Interaction paradigm
- Observation channel: textual board states in standardized notation, game rules, and turn context
- Action channel: move choice plus a short analysis and emotion output
- Interface type: natural language
- Agent scaffold allowed: none
- Is there privileged API access? yes
- How close is the setup to human play? low to medium; the strategic core is preserved, but state exposure and emotional logging are benchmark-specific
- Main ecological-validity trade-off: Qi Town captures adversarial pressure, but the evaluation remains highly relative to the selected model pool and prompt framing.

## 6. Evaluation protocol
- Main score: Elo rating
- Auxiliary score(s): Performance Loop Graphs and Positive Sentiment Score
- Evaluation style: tournament / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: round-robin LLM-vs-LLM competition with no human baseline or fixed non-LLM anchor
- Automatic verifiability: high
- Calibration method: shared round-robin scheduling over 20 LLMs, unified textual interface, and three repeated tournament cycles
- Anti-contamination argument: not central
- Reliability or comparability concerns: results are pool-dependent, and PLG or sentiment metrics are harder to compare across benchmarks than anchored win-rate protocols

## 7. Main contributions
- Contribution 1: Introduces Qi Town, a tournament platform for 20 LLM players across multiple board games.
- Contribution 2: Adds Performance Loop Graphs to visualize cyclic win-loss relations among models.
- Contribution 3: Tracks Positive Sentiment Score as a psychological-style companion metric during gameplay.

## 8. Main findings and failure modes
- Core empirical takeaway: game-by-game leaders differ, and the large loops revealed by PLGs show that relative arena performance is less stable than a single Elo ranking suggests.
- Notable model failure mode 1: capabilities remain uneven across games, with some models still showing weak play even in simpler fixed-rule settings
- Notable model failure mode 2: PLGs reveal large cyclical win-loss structures, indicating unstable relative ordering outside a few draw-heavy settings such as chess
- Notable model failure mode 3: emotional positivity is largely independent of technical performance and varies strongly by game type
- Does this paper reveal a benchmark-design limitation as well? yes; the benchmark is informative as an arena study, but relative rankings remain volatile and pool-sensitive

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Demonstrates how games can generate dynamic benchmark content rather than fixed question sets.
- Best use in Section 1 (taxonomy and evolutionary levels): Example of modern LLM-vs-LLM arena framing. Useful small-suite board-game comparison point.
- Best use in Section 2 (core capabilities evaluated by games): Supports strategic planning and opponent adaptation discussion, but only narrowly.
- Best use in Section 3 (interaction and evaluation paradigm): Representative text-board interface. Good contrast against anchor-based protocols like BotzoneBench.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Strong evidence that relative arenas alone may overstate ranking stability.

## 10. Relation to nearby papers
- Closest predecessor(s): arena-style board-game and chess evaluations
- Closest follow-up(s): CATArena and other tournament-centric protocols
- Best comparison targets inside our corpus: `BotzoneBench`, `CATArena`, `BoardGameArena`
- What this paper uniquely adds relative to neighbors: It explicitly visualizes cyclical ranking structure with PLGs and adds a self-reported affect metric on top of LLM-vs-LLM competition results.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- Qi Town supports five games, including fixed-rule board games and a Free-Style mode where LLMs negotiate rules before play.
- The paper evaluates 20 LLM players using round-robin tournaments and reports Elo, Performance Loop Graphs, and Positive Sentiment Score.
- The authors argue that cyclic win-loss relations in PLGs expose instability that aggregate ranking metrics can hide.

### 11.2 Our synthesis / interpretation
- This paper is more useful as a methodological caution about relative arenas than as a benchmark foundation for later drafting.
- PSS is interesting but secondary; Elo and PLG are the parts most relevant to the survey.

### 11.3 Uncertain or needs re-check
- Recheck Section 4.3 or Appendix B if we later need the exact PLG construction procedure or sentiment-scoring formula.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? No immediate reread; the survey value is mostly protocol-level.
- Which section to read next if needed: 3.5 / 3.6 / 4.2
- Follow-up question(s): How should we position PLG relative to Elo when discussing ranking reliability?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P2
- Reading depth: deep
- Batch ID: B04
- Outline sections: 1,3,4
- Survey role: contrast
- Paper card path: `paper_cards/B04/WhoIsABetterPlayer.md`
- Next action: draft-section
- Check status: unchecked
- Last updated: 2026-04-09
