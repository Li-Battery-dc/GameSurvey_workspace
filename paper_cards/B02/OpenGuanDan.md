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
- OpenGuanDan turns the Chinese four-player card game GuanDan into a benchmark for large-scale imperfect-information decision making. The paper emphasizes hybrid cooperative-competitive play, large and variable legal-action spaces, inter-round dependencies, and dynamic team composition, and it packages these inside a custom simulator with observation, action, and reward wrappers plus independent per-player APIs. Crucially, the reported experiments evaluate built-in GuanDan AI agents and human-AI matchups, not LLM or VLM agents. In this survey, it is therefore a boundary-case contrast for hidden-information game complexity and symbolic API design rather than a direct benchmark paper for LFMs.

## 2. Position in our survey
- Why-games relevance: It uses a hard hidden-information card game to package large legal-action sets, teammate coordination, and inter-round dependencies into a checkable decision-making testbed, but that testbed is not instantiated as an LLM/VLM benchmark in the paper itself.
- Historical stage: diagnostic capability probe
- Benchmark level(s): L2 strategic reasoning
- Most relevant outline section(s): 2,3,4
- Role in corpus: contrast

## 3. Design-space coding
### 3.1 Game structure
- Information structure: imperfect
- Transition structure: mixed
- Agent structure: multi-agent
- Social structure: mixed
- Time structure: turn-based

### 3.2 Environment structure
- Environment type(s): tabletop
- Real game / simulated game / designed task-game hybrid: real game benchmark with a custom simulator
- Benchmark unit: full match

### 3.3 Benchmark scope
- Scope: single game
- Number of games / tasks: GuanDan only

### 3.4 Modality
- Observation modality: text or symbolic
- Action modality: semantic
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
- Reliability or comparability concerns: one specialized game only; the paper's LLM compatibility is claimed at the API level rather than empirically tested; and the human-AI results may be slightly inflated by volunteers’ unfamiliarity with the simulator.

## 7. Main contributions
- Contribution 1: Builds a faithful high-efficiency GuanDan simulator and benchmark wrapper.
- Contribution 2: Formalizes the task from both game-theoretic and RL perspectives.
- Contribution 3: Provides built-in agents and human-AI match evaluation for reproducible comparison.

## 8. Main findings and failure modes
- Core empirical takeaway: Among the built-in GuanDan agents, GS2, SDMC, and DanZero clearly outperform rule-based baselines, but none of the evaluated agents reaches superhuman play or consistently matches intermediate-to-advanced human teams.
- Notable model failure mode 1: rule-based agents fail to cover enough critical decision situations to stay competitive in GuanDan’s large, state-dependent action space
- Notable model failure mode 2: current learning-based agents still cannot consistently beat intermediate and advanced human teams
- Notable model failure mode 3: purely self-play-trained agents lag behind GS2, suggesting that learned blueprint strategies alone remain insufficient without stronger online search or refinement
- Does this paper reveal a benchmark-design limitation as well? yes; it is a demanding but highly domain-specific benchmark

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Not a direct fit. At most, use it as a boundary reminder that game complexity alone does not make a paper a benchmark for LFMs.
- Best use in Section 1 (taxonomy and evolutionary levels): Minor boundary contrast only. It shows a modern single-game symbolic benchmark outside the direct LLM/VLM evaluation line, not a level-defining anchor.
- Best use in Section 2 (core capabilities evaluated by games): Narrow contrast for hidden-information strategic difficulty, large legal-action spaces, and mixed cooperative-competitive play; do not cite it as direct LLM/VLM evidence.
- Best use in Section 3 (interaction and evaluation paradigm): Strongest use. The paper cleanly documents privileged symbolic observations, legal-action exposure, built-in AI baselines, and human-AI versus AI-versus-AI evaluation, while illustrating that API compatibility with LLMs is not the same as benchmarking them.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Use only as a cautionary scope case: a hard game benchmark can still sit outside our target literature when it evaluates specialized non-LFM agents rather than foundation-model agents.

## 10. Relation to nearby papers
- Closest predecessor(s): DanZero, SDMC, and GS2 as prior GuanDan agents rather than benchmark papers
- Closest follow-up(s): No direct LFM-focused follow-up appears in our current corpus; the nearest neighboring card-game papers are `ComplexCardGames`, `PokerBench`, and `GTOWizardBenchmark`, which actually evaluate foundation-model-facing or LLM-centered setups.
- Best comparison targets inside our corpus: PokerBench, GTOWizardBenchmark, ComplexCardGames, DSGBench
- What this paper uniquely adds relative to neighbors: It contributes a hard GuanDan simulator, explicit per-player APIs, and non-LFM built-in baselines, making it more useful as a scope boundary and interface contrast than as direct evidence about LFMs.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- GuanDan is framed as a four-player, two-team imperfect-information card game with very large information sets, variable legal-action spaces, mixed cooperative-competitive incentives, and multi-round level progression.
- OpenGuanDan provides a self-developed simulator with observation, action, and reward wrappers plus independent action-upload APIs; both the main text and Appendix C say the API supports game-theory, RL, and LLM agent integration.
- The empirical evaluation in Section 6 covers pairwise comparisons among built-in GuanDan AI agents and human-AI evaluation of the learning-based agents; no LLM- or VLM-specific benchmark results are reported.
- Pairwise evaluation uses 1000 games per agent pair, and human-AI evaluation with 16 volunteers in 8 teams shows that none of the evaluated learning-based agents exceeds a 50% overall win rate.

### 11.2 Our synthesis / interpretation
- For this survey, OpenGuanDan is best treated as a boundary contrast: it demonstrates hidden-information benchmark design and symbolic API privilege, but it is not a direct benchmark paper for LLM/VLM agents.
- Its main value is in Sections 3 and 4, where it helps distinguish between "LLM-compatible interface" claims and actual LFM evaluation.

### 11.3 Uncertain or needs re-check
- Recheck Appendix D only if we later need exact per-agent inference-speed numbers; the benchmark's non-LFM scope is already clear from the abstract, Section 6, and Appendix C.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? Already completed in this audit; no further reread is needed unless we want exact timing numbers from Appendix D.
- Which section to read next if needed: Appendix C / Appendix D
- Follow-up question(s): If the survey scope tightens to direct LLM/VLM benchmarks only, should OpenGuanDan remain as a contrast card or be parked as peripheral background?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P2
- Reading depth: deep
- Batch ID: B02
- Outline sections: 2,3,4
- Survey role: contrast
- Paper card path: `paper_cards/B02/OpenGuanDan.md`
- Next action: contrast-only
- Check status: unchecked
- Last updated: 2026-04-19
