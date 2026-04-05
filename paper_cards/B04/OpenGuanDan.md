# OpenGuanDan OpenGuanDan: A Large-Scale Imperfect Information Game Benchmark

## 0. Metadata
- Date: 2026/01
- Venue: arXiv
- Authors: Chao Li, Shangdong Yang, Chiheng Zhan, Zhenxing Ge, Yujing Hu, Bingkun Bao, Xingguo Chen, Yang Gao
- Paper link: https://arxiv.org/pdf/2602.00676v1
- Code link: https://github.com/GameAI-NJUPT/OpenGuanDan
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: medium
- Review gate label: usable

## 1. One-paragraph benchmark summary
- OpenGuanDan turns the Chinese four-player card game GuanDan into a benchmark for large-scale imperfect-information decision making. The paper emphasizes the game’s hybrid cooperative-competitive structure, large and variable action spaces, inter-round dependencies, and dynamic team composition. It provides a full simulator, observation and action wrappers, independent per-player APIs, and built-in learning-based and rule-based agents for comparison. In this survey, it is a useful card-game benchmark for partial observability and mixed-objective play rather than for ecological visual interaction.

## 2. Position in our survey
- Why-games relevance: It uses a rich card game to stress hidden information, huge legal-action sets, and teammate coordination inside one benchmark.
- Historical stage: diagnostic capability probe
- Narrative level(s): L2 strategic reasoning / L3 social intelligence
- Most relevant outline section(s): 2,3,5,6
- Role in corpus: representative

## 3. Design-space coding
### 3.1 Environment structure
- Information structure: imperfect
- Transition structure: stochastic
- Agent structure: multi-agent
- Social structure: mixed
- Time structure: turn-based

### 3.2 World structure
- World type(s): card
- Real game / simulated game / designed task-game hybrid: real game benchmark with a custom simulator
- Benchmark unit: full match

### 3.3 Benchmark scope
- Scope: single game
- Number of games / tasks: GuanDan only
- Benchmark intent: diagnostic evaluation

### 3.4 Modality
- Primary modality: symbolic state
- Perception burden retained: hidden hands, action-history tracking, teammate/opponent modeling, variable legal actions
- Perception burden removed: visual card/table interaction

## 4. What this benchmark measures
- Primary capability target: strategic planning under imperfect information with mixed cooperative and competitive incentives
- Secondary capability target(s): belief modeling, large action-space search, long-horizon coordination
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? yes
- Does it test social reasoning / deception / cooperation? yes
- Does it test visual grounding / spatial-temporal reasoning? no
- Does it test long-horizon autonomy / task completion? yes
- Does it test real-time efficiency? no
- Does it test cross-game transfer / open-ended generalization? no
- Why is a game environment especially suitable here? GuanDan compresses hidden information, teammate coordination, and highly compositional legal actions into one controlled ruleset.

## 5. Interaction paradigm
- Observation channel: per-player JSON observations with hand cards, played cards, recent actions, and legal moves
- Action channel: legal card combinations selected through the simulator API
- Interface type: API / structured action space
- Agent scaffold allowed: none
- Is there privileged API access? yes
- How close is the setup to human play? medium; the strategic structure is preserved, but the interface is machine-oriented and symbolic
- Main ecological-validity trade-off: The benchmark preserves the game’s difficult reasoning structure, but removes embodied or social cues outside the formal game state.

## 6. Evaluation protocol
- Main score: competitive match performance
- Auxiliary score(s): pairwise competition results and human-AI match outcomes
- Evaluation style: tournament / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: built-in rule-based and learning-based agents plus human-AI matches
- Automatic verifiability: high
- Calibration method: standardized simulator and shared built-in agents
- Anti-contamination argument: not central
- Reliability or comparability concerns: one game only, with highly specialized rules and strong domain-specific action complexity

## 7. Main contributions
- Contribution 1: Builds a faithful high-efficiency GuanDan simulator and benchmark wrapper.
- Contribution 2: Formalizes the task from both game-theoretic and RL perspectives.
- Contribution 3: Provides built-in agents and human-AI match evaluation for reproducible comparison.

## 8. Main findings and failure modes
- Core empirical takeaway: learning-based GuanDan agents beat rule-based agents but still fall short of superhuman play.
- Notable model failure mode 1: difficulty handling huge variable legal-action spaces
- Notable model failure mode 2: weak belief modeling under hidden information
- Notable model failure mode 3: coordination breaks when teammate structure shifts across rounds
- Does this paper reveal a benchmark-design limitation as well? yes; it is a demanding but highly domain-specific benchmark

## 9. Why this paper matters for our survey
- Best use in Section 0 (why games): Shows how a single rich card game can expose several hard strategic dimensions at once.
- Best use in Section 1 (historical evolution): Helpful later-stage example of specialized imperfect-information benchmarking.
- Best use in Section 2 (design space): Strong anchor for mixed cooperative-competitive card games.
- Best use in Section 3 (capability targets): Direct evidence for partial observability and long-horizon coordination.
- Best use in Section 4 (interaction paradigm): Useful API-based symbolic benchmark comparison.
- Best use in Section 5 (evaluation protocol): Relevant for pairwise tournaments and human-AI comparisons.
- Best use in Section 6/7 (limitations and future): Supports the claim that hidden-information reasoning remains unsolved.

## 10. Relation to nearby papers
- Closest predecessor(s): PokerBench and other imperfect-information card-game benchmarks
- Closest follow-up(s): card-game transfer and tournament benchmarks
- Best comparison targets inside our corpus: BotzoneBench, ComplexCardGames, WhoIsABetterPlayer
- What this paper uniquely adds relative to neighbors: It packages a four-player mixed-objective card game with both human-AI and AI-AI evaluation.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- GuanDan is framed as a four-player, two-team card game with large information sets, variable action spaces, and long-horizon dependencies.
- OpenGuanDan provides a simulator, per-player APIs, wrappers, and built-in rule-based and learning-based agents.
- Reported results show learning-based agents outperform rule-based ones but remain below superhuman performance.

### 11.2 Our synthesis / interpretation
- OpenGuanDan is a strong example of a deep strategic benchmark that stays mostly symbolic rather than ecological.
- It is more useful for Sections 2, 3, and 5 than for the visual-agency branch.

### 11.3 Uncertain or needs re-check
- Recheck Section 5.2 if we later need the full list of built-in agents and their exact training paradigms.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? No immediate reread; the benchmark structure and role are already clear.
- Which section to read next if needed: 3.2 / 5.1 / 5.2
- Follow-up question(s): Which card-game benchmark should anchor the survey's discussion of mixed cooperation and competition?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P1
- Reading depth: deep
- Batch ID: B04
- Outline sections: 2,3,5,6
- Survey role: representative
- Paper card path: `paper_cards/B04/OpenGuanDan.md`
- Next action: draft-section
- Last updated: 2026-04-05
