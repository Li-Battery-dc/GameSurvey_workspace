# KORGym KORGym: A Dynamic Game Platform for LLM Reasoning Evaluation

## 0. Metadata
- Date: 2025/05
- Venue: NeurIPS 2025
- Authors: Jiajun Shi, Jian Yang, Jiaheng Liu, Xingyuan Bu, Jiangjie Chen, Junting Zhou, Kaijing Ma, Zhoufutu Wen, Bingli Wang, Yancheng He, Liang Song, Hualei Zhu, Shilong Li, Xingjian Wang, Wei Zhang, Ruibin Yuan, Yifan Yao, Wenjun Yang, Yunli Wang, Siyuan Fang, Siyu Yuan, Qianyu He, Xiangru Tang, Yingshui Tan, Wangchunshu Zhou, Zhaoxiang Zhang, Zhoujun Li, Wenhao Huang, Ge Zhang
- Paper link: https://arxiv.org/pdf/2505.14552v2
- Code link: https://github.com/multimodal-art-projection/KORGym
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: high
- Review gate label: usable

## 1. One-paragraph benchmark summary
- KORGym is a large game platform for evaluating LLM and VLM reasoning across 51 games and six reasoning dimensions, with both textual and multimodal tasks and explicit Gymnasium-style reinforcement-learning support. It is motivated by knowledge-orthogonal evaluation: the authors deliberately prefer game settings they see as less entangled with pretraining knowledge so the benchmark better reflects intrinsic reasoning ability. The platform provides standardized `generate`, `print_board`, and `verify` APIs, configurable difficulty, and dimension-aware score aggregation across heterogeneous games. For this survey, KORGym is most useful as a representative benchmark-platform paper that emphasizes scale, API standardization, and aggregation design more than deep empirical analysis of any single game family.

## 2. Position in our survey
- Why-games relevance: A large game platform can probe many reasoning dimensions under controlled rules while staying less knowledge-dependent than many domain-specific benchmarks.
- Historical stage: diagnostic capability probe
- Narrative level(s): L2 strategic reasoning / L5 cross-game generalization
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
- World type(s): board / puzzle / other
- Real game / simulated game / designed task-game hybrid: genre-diverse suite built from novel games, adapted classics, and multimodal tasks
- Benchmark unit: game run

### 3.3 Benchmark scope
- Scope: genre-diverse suite
- Number of games / tasks: 51 games across 6 reasoning dimensions, including 9 multimodal games
- Benchmark intent: diagnostic evaluation

### 3.4 Modality
- Primary modality: mixed
- Perception burden retained: multi-turn state tracking, rule following, puzzle solving, strategic planning, and multimodal reasoning
- Perception burden removed: standardized APIs smooth over environment integration and native UI irregularity, especially for text-rendered tasks

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
- Action channel: game actions submitted through the `verify` API after state rendering through `generate` and `print_board`
- Interface type: API / hybrid
- Agent scaffold allowed: none
- Is there privileged API access? yes
- How close is the setup to human play? low to medium; game rules remain intact, but standardized APIs and normalization make the platform diagnostic rather than native-play oriented
- Main ecological-validity trade-off: KORGym gains breadth and RL support by standardizing interactions, which reduces the friction and irregularity of real gameplay interfaces

## 6. Evaluation protocol
- Main score: Capability Dimension Aggregated Mean across the non-multimodal reasoning dimensions, with separate multimodal task results reported for VLMs
- Auxiliary score(s): raw per-game scores, multimodal-task breakdowns, modality ablations, model-family analyses, reasoning-paradigm ablations, and RL analyses
- Evaluation style: native score / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: 19 LLMs and 8 VLMs are evaluated zero-shot on seeded game instances; the paper does not include a human baseline
- Automatic verifiability: high
- Calibration method: per-game score normalization, dimension-wise aggregation, and log compression for skewed raw scores
- Anti-contamination argument: the platform is explicitly designed around knowledge-orthogonal game tasks that are argued to be less entangled with pretraining data, but this is a design rationale rather than an empirical contamination audit
- Reliability or comparability concerns: broad normalization improves fairness across games but makes the final aggregate score less intuitive than native metrics, and multimodal performance is not merged into one single cross-model headline table

## 7. Main contributions
- Contribution 1: Builds a 51-game reasoning platform spanning six capability dimensions and multimodal settings.
- Contribution 2: Provides a Gymnasium-like framework that supports both benchmark evaluation and RL use.
- Contribution 3: Studies modality, model-family, thinking-style, and RL effects across one large platform.

## 8. Main findings and failure modes
- Core empirical takeaway: closed-source and thinking models perform best overall on the text-based leaderboard, with o3-mini leading the five non-multimodal reasoning dimensions and different model families showing stable strength-weakness profiles.
- Notable model failure mode 1: open-source models lag broadly across dimensions
- Notable model failure mode 2: modality shifts change performance patterns in nontrivial ways
- Notable model failure mode 3: explicit reasoning styles can constrain as well as help, rather than uniformly improving performance
- Does this paper reveal a benchmark-design limitation as well? yes; a large normalized platform gives breadth, but the aggregate score can hide game-family-specific behavior

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Good evidence that games can support large-scale, heterogeneous reasoning evaluation.
- Best use in Section 1 (taxonomy and evolutionary levels): Represents the platform turn in which game evaluation becomes benchmark infrastructure rather than a one-off suite. Useful for discussing very broad scope and dimension-based aggregation.
- Best use in Section 2 (core capabilities evaluated by games): Covers mathematical, logical, control, puzzle, spatial, strategic, and multimodal reasoning.
- Best use in Section 3 (interaction and evaluation paradigm): Useful for standardized API-based interaction, RL compatibility, and dimension-aware aggregation across heterogeneous games.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Helps show the trade-off between platform breadth, normalization, and interpretability.

## 10. Relation to nearby papers
- Closest predecessor(s): LMGameBench and earlier benchmark suites with Gym-like aspirations
- Closest follow-up(s): larger benchmark platforms that combine evaluation with RL or training loops
- Best comparison targets inside our corpus: AIGameStore, LMGameBench, TextArena, Orak
- What this paper uniquely adds relative to neighbors: It emphasizes one unified, extensible platform with dimension-aware scoring rather than a smaller curated set of games.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- KORGym offers 51 games across six reasoning dimensions and includes nine multimodal games.
- The paper evaluates 19 LLMs and 8 VLMs.
- o3-mini leads the text-based five-dimension leaderboard among the reported LLMs, while multimodal-task results are reported separately for VLMs.
- Scores are normalized and aggregated with the Capability Dimension Aggregated Mean rather than reported only as raw per-game results.
- The platform exposes standardized `generate`, `print_board`, and `verify` APIs and is explicitly designed to support reinforcement-learning-style interaction.

### 11.2 Our synthesis / interpretation
- KORGym is useful mainly as a platform paper: it matters more for scale and framework design than for any single benchmark narrative.
- It is especially helpful when the survey needs to discuss the difference between broad benchmark infrastructure and tightly scoped comparison suites.
- Its knowledge-orthogonality framing is best treated as a benchmark-design aspiration, not as a demonstrated proof that contamination risk is low.

### 11.3 Uncertain or needs re-check
- Re-check Section 5.3 if we later need the strongest RL-improvement examples tied to Doubao-1.5-thinking-pro.
- Re-check Appendix C if we later need exact raw per-game scores rather than normalized aggregates.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? Full paper read completed for this audit; no further general reading is required unless we need exact raw-score tables or the full multimodal breakdown.
- Which section to read next if needed: 3.3 / 4.2 / 5.3
- Follow-up question(s): Should KORGym or AI GameStore anchor the survey’s discussion of benchmark-platform scale?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P1
- Reading depth: deep
- Batch ID: B06
- Outline sections: 1,2,3,4
- Survey role: representative
- Paper card path: `paper_cards/B06/KORGym.md`
- Check status: unchecked
- Last updated: 2026-04-10
