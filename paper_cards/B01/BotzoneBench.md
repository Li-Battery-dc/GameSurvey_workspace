# BotzoneBench BotzoneBench: Scalable LLM Evaluation via Graded AI Anchors

## 0. Metadata
- Date: 2026/01
- Venue: arXiv
- Authors: Lingfeng Li, Yunlong Lu, Yuefei Zhang, Jingyu Yao, Yixin Zhu, KeYuan Cheng, Yongyi Wang, Qirui Zheng, Xionghui Yang, Wenxin Li
- Paper link: https://arxiv.org/pdf/2602.13214v1
- Code link: https://github.com/AMysteriousBeing/BotzoneBench
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: high
- Review gate label: strong

## 1. One-paragraph benchmark summary
- BotzoneBench is a strategic-game benchmark built around a more stable evaluation idea than model-vs-model arenas: compare LLM agents against fixed hierarchies of classic game AIs. It covers eight games spanning deterministic perfect-information settings and stochastic imperfect-information card or tile games on the Botzone platform. The benchmark uses duplicate matches, fixed seeds, and a level-progress skill score to make results interpretable over time. For this survey, the paper is especially valuable in the evaluation-protocol section because it turns game play into a calibrated, longitudinal measurement problem.

## 2. Position in our survey
- Why-games relevance: It shows that games let us build stable, repeatable strategic evaluations instead of volatile peer-only rankings.
- Historical stage: diagnostic capability probe
- Narrative level(s): L1 rule following / L2 strategic reasoning
- Most relevant outline section(s): 0,1,2,3
- Role in corpus: anchor

## 3. Design-space coding
### 3.1 Environment structure
- Information structure: mixed
- Transition structure: mixed
- Agent structure: multi-agent
- Social structure: mixed
- Time structure: turn-based

### 3.2 World structure
- World type(s): board / card / other
- Real game / simulated game / designed task-game hybrid: real competitive games implemented on a benchmark platform
- Benchmark unit: full match

### 3.3 Benchmark scope
- Scope: curated suite
- Number of games / tasks: 8 games
- Benchmark intent: diagnostic evaluation

### 3.4 Modality
- Primary modality: text
- Perception burden retained: strategic state tracking, action history, legal move selection, hidden-information reasoning
- Perception burden removed: raw board or table visuals, low-level UI interaction

## 4. What this benchmark measures
- Primary capability target: strategic reasoning calibrated against graded AI baselines
- Secondary capability target(s): probabilistic reasoning, adaptation across game families, rule-compliant decision making
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? yes
- Does it test social reasoning / deception / cooperation? partially; Texas Hold'em probes bluffing and opponent modeling, while Fight the Landlord adds coalition coordination, but the suite is still centered on strategic competition rather than open-ended social play
- Does it test visual grounding / spatial-temporal reasoning? no
- Does it test long-horizon autonomy / task completion? partially
- Does it test real-time efficiency? no
- Does it test cross-game transfer / open-ended generalization? partially
- Why is a game environment especially suitable here? Games supply fixed rules and automatically checkable outcomes while still supporting graded strategic difficulty.

## 5. Interaction paradigm
- Observation channel: prompt with player identity, current state, action history, and legal moves
- Action channel: text action selected from legal options
- Interface type: natural language / structured action space
- Agent scaffold allowed: none
- Is there privileged API access? yes
- How close is the setup to human play? low to medium; strategic structure is real but the benchmark exposes legal moves, public state, and public history in a strongly normalized textual interface
- Main ecological-validity trade-off: Stability and comparability improve because the benchmark fixes seeds and anchor bots while exposing legal actions explicitly, but that prompt interface is much more privileged than ordinary human play.

## 6. Evaluation protocol
- Main score: anchored skill rating as a `(level, progress)` tuple
- Auxiliary score(s): win rate against each anchor tier
- Evaluation style: hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: graded classic AI anchors
- Automatic verifiability: high
- Calibration method: duplicate matches, fixed random seeds, and pre-calibrated baseline hierarchies
- Anti-contamination argument: not the main claim; the paper focuses more on evaluation stability than dataset contamination
- Reliability or comparability concerns: levels are comparable within a game, not across different games with different baseline ladders, and baseline coverage is weaker in Chess and Texas Hold'em

## 7. Main contributions
- Contribution 1: Replaces volatile LLM-vs-LLM ranking with fixed AI-anchor ladders.
- Contribution 2: Uses duplicate-match design and seeded randomness for fairer cross-model comparison.
- Contribution 3: Introduces an interpretable absolute skill metric and releases a large interaction-log dataset with reasoning traces.

## 8. Main findings and failure modes
- Core empirical takeaway: Under the benchmark's strongly constrained prompting and legal-action exposure, all evaluated models remain rule-compliant, but strategic strength still varies sharply with model size and game family.
- Notable model failure mode 1: small models clear only the weakest anchor tiers
- Notable model failure mode 2: performance varies strongly by game family and hidden-information demands
- Notable model failure mode 3: some models remain behaviorally weak in imperfect-information settings even when their outputs stay well-formed
- Does this paper reveal a benchmark-design limitation as well? yes; cross-game anchor levels are not directly comparable

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Strong evidence that games permit durable, interpretable evaluation standards.
- Best use in Section 1 (taxonomy and evolutionary levels): Marks a shift from ad hoc suite results toward protocol-calibrated benchmarking. Good case of a mixed-information strategic suite.
- Best use in Section 2 (core capabilities evaluated by games): Supports strategic planning, uncertainty handling, and adaptive play.
- Best use in Section 3 (interaction and evaluation paradigm): Typical privileged text-state plus legal-action benchmark interface. One of the clearest anchor-based calibration papers in the corpus.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Helps argue for better cross-benchmark comparability and non-volatile evaluation.

## 10. Relation to nearby papers
- Closest predecessor(s): SmartPlay, GameBench-style strategic suites, traditional game-AI rating ladders
- Closest follow-up(s): CATArena, WhoIsABetterPlayer
- Best comparison targets inside our corpus: SmartPlay, BoardGameArena, OpenGuanDan, CATArena
- What this paper uniquely adds relative to neighbors: Stable AI anchors and seeded duplicate matches make it much stronger on calibration than most LLM arena papers.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- BotzoneBench covers eight games across perfect-information and imperfect-information settings.
- It uses duplicate matches with fixed random seeds and evaluates LLMs against graded classic AI baselines.
- It reports a `(level, progress)` skill score based on clearing anchor tiers with at least 50% win rate, with Tic-Tac-Toe using draw rate for progress because optimal play is solved.
- The paper states that code and data are publicly available at `https://github.com/AMysteriousBeing/BotzoneBench`.

### 11.2 Our synthesis / interpretation
- BotzoneBench is a key protocol paper for this survey because it reframes game benchmarking as stable calibration rather than transient peer comparison.
- Its main weakness is not measurement noise but the highly privileged prompt interface and uneven baseline depth across games.

### 11.3 Uncertain or needs re-check
- Recheck the appendix if we later need the exact anchor roster for each of the eight games.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? Completed in this audit; the prompt design, anchor construction, and `(level, progress)` scoring are now clear enough for survey use.
- Which section to read next if needed: 4.1 / 4.5 / Appendix A
- Follow-up question(s): Which specific anchor ladders are most reusable when we compare calibration across papers?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P0
- Reading depth: deep
- Batch ID: B01
- Outline sections: 0,1,2,3
- Survey role: anchor
- Paper card path: `paper_cards/B01/BotzoneBench.md`
- Check status: unchecked
- Next action: draft-section
- Last updated: 2026-04-09
