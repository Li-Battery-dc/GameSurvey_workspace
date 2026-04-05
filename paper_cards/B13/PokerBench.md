# PokerBench PokerBench: Training Large Language Models to become Professional Poker Players

## 0. Metadata
- Date: 2025/01
- Venue: AAAI 2025
- Authors: Richard Zhuang, Akshat Gupta, Richard Yang, Aniket Rahane, Zhengyu Li, Gopala Anumanchipalli
- Paper link: https://arxiv.org/pdf/2501.08328v2.pdf
- Code link:
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: high
- Review gate label: strong

## 1. One-paragraph benchmark summary
- PokerBench is a benchmark and training dataset for evaluating LLM poker skill on Texas No-Limit Hold’em decision spots. It uses 1,000 pre-flop and 10,000 post-flop scenarios grounded in game-theory-optimal (GTO) strategies, and it evaluates whether a model chooses the correct action and exact wager amount. The paper also validates benchmark usefulness by showing that models with higher PokerBench scores beat weaker ones over large simulated hand samples. For this survey, PokerBench is a strong specialist benchmark because it operationalizes imperfect-information strategic decision quality without requiring full online play for every training iteration.

## 2. Position in our survey
- Why-games relevance: Poker combines hidden information, opponent modeling, and strategic trade-offs in a fully formalized setting with exact solver references.
- Historical stage: diagnostic capability probe
- Narrative level(s): L2 strategic reasoning / L3 social intelligence
- Most relevant outline section(s): 2,3,6
- Role in corpus: contrast

## 3. Design-space coding
### 3.1 Environment structure
- Information structure: imperfect
- Transition structure: stochastic
- Agent structure: multi-agent
- Social structure: competitive
- Time structure: turn-based

### 3.2 World structure
- World type(s): card
- Real game / simulated game / designed task-game hybrid: benchmark of real poker decision spots derived from solver analysis
- Benchmark unit: decision spot

### 3.3 Benchmark scope
- Scope: single game
- Number of games / tasks: 11,000 spots covering pre-flop and post-flop play
- Benchmark intent: diagnostic evaluation / train+eval foundation

### 3.4 Modality
- Primary modality: text / symbolic state
- Perception burden retained: betting history, hidden-information reasoning, and wager selection
- Perception burden removed: no visual table interface or live timing burden

## 4. What this benchmark measures
- Primary capability target: GTO-aligned poker decision making
- Secondary capability target(s): betting-size precision, balanced strategy selection, and relation between benchmark score and real-play strength
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? yes
- Does it test social reasoning / deception / cooperation? partially through competitive opponent modeling
- Does it test visual grounding / spatial-temporal reasoning? no
- Does it test long-horizon autonomy / task completion? no
- Does it test real-time efficiency? partially
- Does it test cross-game transfer / open-ended generalization? no
- Why is a game environment especially suitable here? Poker has exact strategic references and forces reasoning under hidden information and mixed strategies.

## 5. Interaction paradigm
- Observation channel: textualized poker spot descriptions including hole cards, board, and action history
- Action channel: fold/call/raise-style decisions with explicit sizes
- Interface type: natural language / structured action space / hybrid
- Agent scaffold allowed: none in the benchmark evaluation
- Is there privileged API access? yes; the benchmark presents solver-clean spot state rather than a raw table interface
- How close is the setup to human play? medium-low; it captures strategic essence but abstracts away live table dynamics
- Main ecological-validity trade-off: PokerBench gives up live adaptive play in favor of fast, solver-grounded spot evaluation

## 6. Evaluation protocol
- Main score: action accuracy
- Auxiliary score(s): exact match accuracy and downstream head-to-head results over large hand samples
- Evaluation style: accuracy / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: many frontier and fine-tuned LLMs are compared on the benchmark and then validated in simulated play
- Automatic verifiability: high
- Calibration method: spots are grounded in GTOWizard and WASM-Postflop solver outputs
- Anti-contamination argument: the benchmark is built from many diverse solver spots rather than a small public quiz set
- Reliability or comparability concerns: spot accuracy measures optimal decision quality but not exploitative adaptation in live multi-hand play

## 7. Main contributions
- Contribution 1: Introduces an 11,000-spot poker benchmark with separate pre-flop and post-flop evaluation.
- Contribution 2: Uses exact action and size metrics grounded in GTO solver outputs.
- Contribution 3: Shows that benchmark improvements translate into stronger simulated match performance.

## 8. Main findings and failure modes
- Core empirical takeaway: current frontier LLMs are weak at poker, with GPT-4 only reaching 53.55% action accuracy, but fine-tuning improves performance substantially.
- Notable model failure mode 1: overly tight or unbalanced pre-flop ranges
- Notable model failure mode 2: poor wager-size selection even when the action type is correct
- Notable model failure mode 3: strategy drift away from balanced play in post-flop situations
- Does this paper reveal a benchmark-design limitation as well? yes; it shows that full-game poker evaluation is too expensive to use alone during development, motivating spot benchmarks

## 9. Why this paper matters for our survey
- Best use in Section 0 (why games): Supports the use of games to evaluate hidden-information strategy.
- Best use in Section 1 (historical evolution): A specialist benchmark reflecting a move from full-play engines to faster diagnostic spot evaluation.
- Best use in Section 2 (design space): Useful for decision-spot versus full-trajectory benchmark distinctions.
- Best use in Section 3 (capability targets): Strong evidence on uncertainty, balance, and opponent-aware play.
- Best use in Section 4 (interaction paradigm): A contrast case for text-only strategic state inputs.
- Best use in Section 5 (evaluation protocol): A strong reference for solver-grounded action-level accuracy metrics.
- Best use in Section 6/7 (limitations and future): Supports the idea that specialist domains may need both spot and live-play evaluation.

## 10. Relation to nearby papers
- Closest predecessor(s): solver-based poker AI work
- Closest follow-up(s): exploitative LLM poker systems
- Best comparison targets inside our corpus: BeyondScaling, BotzoneBench, PokeChamp
- What this paper uniquely adds relative to neighbors: It validates a fast benchmark against large-sample live-play outcomes rather than assuming spot accuracy is enough.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- PokerBench contains 1,000 pre-flop spots and 10,000 post-flop spots for 6-max NLH.
- It evaluates both Action Accuracy and Exact Match Accuracy using GTO references.
- The paper reports GPT-4 as the best tested base model at 53.55% action accuracy and shows benchmark gains correlate with simulated match wins over 50k hands.

### 11.2 Our synthesis / interpretation
- PokerBench is a strong benchmark paper for specialist imperfect-information play, especially because it validates benchmark usefulness against actual match results.
- It is best used as a contrast to broader cross-game papers rather than as a survey anchor on its own.

### 11.3 Uncertain or needs re-check
- Re-check the exact post-flop exact-match numbers if later drafting uses them.
- Re-check how much exploitative versus GTO behavior the validation matches truly capture.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? A targeted reread may help later when discussing specialist benchmarks versus live-play evaluation.
- Which section to read next if needed: benchmark construction / metrics / gameplay analysis
- Follow-up question(s): How sensitive is PokerBench to exploitative but non-GTO strong play?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P2
- Reading depth: deep
- Batch ID: B13
- Outline sections: 2,3,6
- Survey role: contrast
- Paper card path: `paper_cards/B13/PokerBench.md`
- Next action: draft-section
- Last updated: 2026-04-05
