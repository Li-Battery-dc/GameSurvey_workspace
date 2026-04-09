# OpenGuanDan OpenGuanDan: A Large-Scale Imperfect Information Game Benchmark

## 0. Metadata
- Date: 2026/01
- Venue: arXiv
- Authors: Chao Li, Shangdong Yang, Chiheng Zhan, Zhenxing Ge, Yujing Hu, Bingkun Bao, Xingguo Chen, Yang Gao
- Paper link: https://arxiv.org/pdf/2602.00676v1
- Code link: https://github.com/GameAI-NJUPT/OpenGuanDan
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: high
- Review gate label: usable

## 1. One-paragraph benchmark summary
- OpenGuanDan turns the Chinese four-player card game GuanDan into a benchmark for large-scale imperfect-information decision making. The paper emphasizes the game’s hybrid cooperative-competitive structure, large and variable action spaces, inter-round dependencies, and dynamic team composition. It provides a full simulator, observation and action wrappers, independent per-player APIs, and built-in learning-based and rule-based agents for comparison. In this survey, it is a useful card-game benchmark for partial observability and mixed-objective play rather than for ecological visual interaction.

## 2. Position in our survey
- Why-games relevance: It uses a rich card game to stress hidden information, huge legal-action sets, and teammate coordination inside one benchmark.
- Historical stage: diagnostic capability probe
- Narrative level(s): L2 strategic reasoning
- Most relevant outline section(s): 1,2,3,4
- Role in corpus: representative

## 3. Design-space coding
### 3.1 Environment structure
- Information structure: imperfect
- Transition structure: mixed
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
- Secondary capability target(s): teammate coordination under partial information, large action-space control, long-horizon round management
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? yes
- Does it test social reasoning / deception / cooperation? partially, through teammate coordination under hidden information rather than language-mediated social reasoning
- Does it test visual grounding / spatial-temporal reasoning? no
- Does it test long-horizon autonomy / task completion? partially
- Does it test real-time efficiency? no
- Does it test cross-game transfer / open-ended generalization? no
- Why is a game environment especially suitable here? GuanDan compresses hidden information, teammate coordination, and highly compositional legal actions into one controlled ruleset.

## 5. Interaction paradigm
- Observation channel: per-player JSON broadcasts with hand cards, unseen cards, played-card histories, recent actions, remaining card counts, levels, wild-card information, and legal moves
- Action channel: independent action-upload APIs for tribute, back-tribute, and card-play decisions over legal combinations
- Interface type: API / structured action space
- Agent scaffold allowed: none
- Is there privileged API access? yes
- How close is the setup to human play? low to medium; the strategic structure is preserved, but the interface exposes rich symbolic state and legal-action information through machine-oriented APIs
- Main ecological-validity trade-off: The benchmark preserves partial observability, mixed incentives, and long multi-round structure, but removes natural perception and exposes formal state/action information unavailable to human players.

## 6. Evaluation protocol
- Main score: pairwise round-reward breakdown and overall win rate
- Auxiliary score(s): human-AI win rates by player skill band and action-time cost
- Evaluation style: tournament / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: built-in rule-based and learning-based GuanDan agents plus human teams grouped by experience level
- Automatic verifiability: high
- Calibration method: standardized simulator, shared built-in agents, and 1000 pairwise games per agent matchup
- Anti-contamination argument: not central
- Reliability or comparability concerns: one specialized game only, and the paper notes that human-AI results may be slightly inflated by volunteers’ unfamiliarity with the simulator.

## 7. Main contributions
- Contribution 1: Builds a faithful high-efficiency GuanDan simulator and benchmark wrapper.
- Contribution 2: Formalizes the task from both game-theoretic and RL perspectives.
- Contribution 3: Provides built-in agents and human-AI match evaluation for reproducible comparison.

## 8. Main findings and failure modes
- Core empirical takeaway: GS2, SDMC, and DanZero clearly outperform rule-based baselines, but even the strongest agents remain below superhuman play and below consistent intermediate-to-advanced human performance.
- Notable model failure mode 1: rule-based agents fail to cover enough critical decision situations to stay competitive in GuanDan’s large, state-dependent action space
- Notable model failure mode 2: current learning-based agents still cannot consistently beat intermediate and advanced human teams
- Notable model failure mode 3: purely self-play-trained agents lag behind GS2, suggesting that learned blueprint strategies alone remain insufficient without stronger online search or refinement
- Does this paper reveal a benchmark-design limitation as well? yes; it is a demanding but highly domain-specific benchmark

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Shows how one specialized card game can combine hidden information, mixed incentives, and long-horizon round structure inside a checkable benchmark.
- Best use in Section 1 (taxonomy and evolutionary levels): Representative specialized imperfect-information card benchmark, especially for mixed cooperative-competitive structure.
- Best use in Section 2 (core capabilities evaluated by games): Direct evidence for strategic planning under uncertainty, large legal-action spaces, and teammate coordination under hidden information.
- Best use in Section 3 (interaction and evaluation paradigm): Useful symbolic/API benchmark contrast with explicit legal-action exposure, built-in agent baselines, and both AI-vs-AI and human-AI evaluation.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Supports the claim that strong self-play agents in hidden-information games still remain below robust human play.

## 10. Relation to nearby papers
- Closest predecessor(s): DanZero, SDMC, and GS2 as prior GuanDan agents rather than benchmark papers
- Closest follow-up(s): multi-game card-benchmark work such as `ComplexCardGames` that reuses GuanDan as one domain within a broader transfer study
- Best comparison targets inside our corpus: `PokerBench`, `ComplexCardGames`, `BotzoneBench`
- What this paper uniquely adds relative to neighbors: It turns GuanDan into a standardized four-player mixed cooperative-competitive benchmark with built-in agents, explicit simulator interfaces, and human-AI calibration.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- GuanDan is framed as a four-player, two-team imperfect-information card game with very large information sets, variable legal-action spaces, mixed cooperative-competitive incentives, and multi-round level progression.
- OpenGuanDan provides a self-developed simulator with observation/action/reward wrappers, independent per-player action-upload APIs, and built-in rule-based and learning-based agents.
- Pairwise evaluation uses 1000 games per agent pair, and human-AI evaluation shows that none of the learning-based agents exceeds a 50% overall win rate against the volunteer human teams.

### 11.2 Our synthesis / interpretation
- OpenGuanDan is a strong example of a deep strategic benchmark that stays mostly symbolic rather than ecological.
- It is more useful for outline Sections 2, 3, and 4 than for any visual-agency discussion.

### 11.3 Uncertain or needs re-check
- Recheck Appendix D if we later need the exact action-time costs, or Section 5.2 if we need the full built-in-agent roster and training details.

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
- Outline sections: 1,2,3,4
- Survey role: representative
- Paper card path: `paper_cards/B04/OpenGuanDan.md`
- Next action: draft-section
- Check status: unchecked
- Last updated: 2026-04-09
