# KORGym KORGym: A Dynamic Game Platform for LLM Reasoning Evaluation

## 0. Metadata
- Date: 2025/05
- Venue: NeurIPS 2025
- Authors: Jiajun Shi, Jian Yang, Jiaheng Liu, Xingyuan Bu, Jiangjie Chen, Junting Zhou, Kaijing Ma, Zhoufutu Wen, Bingli Wang, Yancheng He, Liang Song, Hualei Zhu, Shilong Li, Xingjian Wang, Wei Zhang, Ruibin Yuan, Yifan Yao, Wenjun Yang, Yunli Wang, Siyuan Fang, Siyu Yuan, Qianyu He, Xiangru Tang, Yingshui Tan, Wangchunshu Zhou, Zhaoxiang Zhang, Zhoujun Li, Wenhao Huang, Ge Zhang
- Paper link: https://arxiv.org/pdf/2505.14552v2
- Code link:
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: high
- Review gate label: usable

## 1. One-paragraph benchmark summary
- KORGym is a broad game platform for evaluating LLM and VLM reasoning across more than fifty tasks and six reasoning dimensions, with both textual and multimodal games and explicit Gymnasium-style reinforcement-learning support. It is motivated by "knowledge-orthogonal" evaluation: using game rules and scenarios that are less entangled with pretraining knowledge to test intrinsic reasoning. The platform includes standardized APIs, configurable difficulty, score normalization across heterogeneous games, and analysis over 19 LLMs and 8 VLMs. For this survey, KORGym is a representative benchmark-platform paper that emphasizes scale, dimension coverage, and RL compatibility more than deep analysis of any one game family.

## 2. Position in our survey
- Why-games relevance: A large game platform can probe many reasoning dimensions under controlled rules while staying less knowledge-dependent than many domain-specific benchmarks.
- Historical stage: benchmark expansion / diagnostic platform
- Narrative level(s): L2 strategic reasoning / L4 visual agency / L5 cross-game generalization
- Most relevant outline section(s): 1,2,3,4
- Role in corpus: representative

## 3. Design-space coding
### 3.1 Environment structure
- Information structure: mixed
- Transition structure: mixed
- Agent structure: mixed
- Social structure: mixed
- Time structure: mixed

### 3.2 World structure
- World type(s): puzzle / board / strategic / multimodal / other
- Real game / simulated game / designed task-game hybrid: genre-diverse suite built from novel games, adapted classics, and multimodal tasks
- Benchmark unit: game run

### 3.3 Benchmark scope
- Scope: genre-diverse suite
- Number of games / tasks: 51+ games across 6 reasoning dimensions, including 9 multimodal games
- Benchmark intent: diagnostic evaluation / train+eval foundation

### 3.4 Modality
- Primary modality: mixed
- Perception burden retained: multi-turn state tracking, rule following, puzzle solving, strategic planning, and multimodal reasoning
- Perception burden removed: standardized APIs smooth over environment-integration details and enable RL-style access

## 4. What this benchmark measures
- Primary capability target: broad reasoning ability across heterogeneous game tasks
- Secondary capability target(s): cross-dimension profiles, modality effects, thinking-versus-non-thinking differences, and RL-induced improvements
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? yes
- Does it test social reasoning / deception / cooperation? partially
- Does it test visual grounding / spatial-temporal reasoning? yes
- Does it test long-horizon autonomy / task completion? partially
- Does it test real-time efficiency? no
- Does it test cross-game transfer / open-ended generalization? yes
- Why is a game environment especially suitable here? A game platform can bundle very different reasoning demands under one API while keeping scoring verifiable and replayable.

## 5. Interaction paradigm
- Observation channel: standardized text or visual game states through KORGym APIs
- Action channel: game actions submitted through generate, verify, and board-print interfaces
- Interface type: API / hybrid
- Agent scaffold allowed: none
- Is there privileged API access? yes
- How close is the setup to human play? low to medium; game rules remain intact, but standardized APIs and normalization make the platform diagnostic rather than native-play oriented
- Main ecological-validity trade-off: KORGym gains breadth and RL support by standardizing interactions, which reduces the friction and irregularity of real gameplay interfaces

## 6. Evaluation protocol
- Main score: Capability Dimension Aggregated Mean across reasoning dimensions
- Auxiliary score(s): raw per-game scores, multimodal-task breakdowns, modality ablations, model-family analyses, and RL analyses
- Evaluation style: native score / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: 19 LLMs and 8 VLMs are compared directly on the platform
- Automatic verifiability: high
- Calibration method: per-game score normalization, dimension-wise aggregation, and log compression for skewed raw scores
- Anti-contamination argument: the platform is explicitly designed around knowledge-orthogonal game tasks that are less likely to be memorized from pretraining
- Reliability or comparability concerns: broad normalization improves fairness across games but also makes the final aggregate score less intuitive than native game metrics

## 7. Main contributions
- Contribution 1: Builds a 50+ game reasoning platform spanning six capability dimensions and multimodal settings.
- Contribution 2: Provides a Gymnasium-like framework that supports both benchmark evaluation and RL use.
- Contribution 3: Studies modality, model-family, thinking-style, and RL effects across one large platform.

## 8. Main findings and failure modes
- Core empirical takeaway: closed-source and thinking models perform best overall, with o3-mini leading the platform and different model families showing stable strength-weakness profiles.
- Notable model failure mode 1: open-source models lag broadly across dimensions
- Notable model failure mode 2: modality shifts change performance patterns in nontrivial ways
- Notable model failure mode 3: explicit reasoning styles can constrain as well as help, rather than uniformly improving performance
- Does this paper reveal a benchmark-design limitation as well? yes; a large normalized platform gives breadth, but the aggregate score can hide game-family-specific behavior

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Good evidence that games can support large-scale, heterogeneous reasoning evaluation.
- Best use in Section 1 (taxonomy and evolutionary levels): Represents the platform turn in which game evaluation becomes benchmark infrastructure rather than a one-off suite. Useful for discussing very broad scope and dimension-based aggregation.
- Best use in Section 2 (core capabilities evaluated by games): Covers mathematical, logical, control, puzzle, spatial, strategic, and multimodal reasoning.
- Best use in Section 3 (interaction and evaluation paradigm): Useful for standardized API-based interaction and RL compatibility. Good source on normalization and dimension-aware aggregation across heterogeneous games.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Helps show the trade-off between platform breadth and interpretability.

## 10. Relation to nearby papers
- Closest predecessor(s): LMGameBench and earlier benchmark suites with Gym-like aspirations
- Closest follow-up(s): larger benchmark platforms that combine evaluation with RL or training loops
- Best comparison targets inside our corpus: [LMGameBench](D:/research_root/GameSurvey/workspace/paper_cards/B08/LMGameBench.md), [Orak](D:/research_root/GameSurvey/workspace/paper_cards/B05/Orak.md), [AI GameStore](D:/research_root/GameSurvey/workspace/paper_cards/B05/AIGameStore.md), [GAMEBoT](D:/research_root/GameSurvey/workspace/paper_cards/B08/GAMEBoT.md)
- What this paper uniquely adds relative to neighbors: It emphasizes one unified, extensible platform with dimension-aware scoring rather than a smaller curated set of games.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- KORGym offers more than fifty games across six reasoning dimensions and includes nine multimodal games.
- The paper evaluates 19 LLMs and 8 VLMs and reports o3-mini as the strongest overall model on the platform.
- Scores are normalized and aggregated with the Capability Dimension Aggregated Mean rather than reported only as raw per-game results.

### 11.2 Our synthesis / interpretation
- KORGym is useful mainly as a platform paper: it matters more for scale and framework design than for any single benchmark narrative.
- It is especially helpful when the survey needs to discuss the difference between broad benchmark infrastructure and tightly scoped comparison suites.

### 11.3 Uncertain or needs re-check
- Re-check Section 4 and the appendix if we later need exact counts by game category or the strongest RL-improvement examples.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? No immediate reread is required unless we later need detailed category composition or the exact CDA Mean formula in prose.
- Which section to read next if needed: 3.2 / 3.3 / 4.2
- Follow-up question(s): Should KORGym or AI GameStore anchor the survey’s discussion of benchmark-platform scale?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P1
- Reading depth: deep
- Batch ID: B08
- Outline sections: 1,2,3,4
- Survey role: representative
- Paper card path: `paper_cards/B08/KORGym.md`
- Next action: draft-section
- Last updated: 2026-04-05
