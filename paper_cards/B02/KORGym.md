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
- KORGym is a Gymnasium-inspired reasoning benchmark/platform that evaluates LLMs and VLMs on 51 games grouped into six reasoning dimensions, including a nine-task multimodal subset. Its main technical contribution is a unified `generate` / `print_board` / `verify` API stack with controllable difficulty, multi-turn interaction, and RL-friendly reward signals, plus a dimension-aware aggregation scheme across heterogeneous games. After full-paper audit, the safest survey use is not as Level 5 cross-game generalization evidence, but as a broad Level 2 reasoning-platform paper: it scales diagnostic game coverage and benchmark engineering, yet it does not evaluate held-out-game transfer, first-contact adaptation, or open-ended benchmark growth.

## 2. Position in our survey
- Why-games relevance: A large suite of rule-driven games can probe multiple reasoning pressures under verifiable interaction loops without collapsing evaluation into one domain or one static question format.
- Historical stage: diagnostic capability probe
- Benchmark level(s): L2 strategic reasoning
- Most relevant outline section(s): 1,2,3
- Role in corpus: representative

## 3. Design-space coding
### 3.1 Game structure
- Information structure: mixed
- Transition structure: mixed
- Agent structure: mixed
- Social structure: mixed
- Time structure: mixed

### 3.2 Environment structure
- Environment type(s): tabletop / abstract puzzle / combat-strategy world
- Real game / simulated game / designed task-game hybrid: designed task-game hybrid mixing puzzles, simplified game adaptations, and multimodal reasoning tasks under one API layer
- Benchmark unit: episode / trajectory

### 3.3 Benchmark scope
- Scope: curated suite
- Number of games / tasks: 51 games across 6 reasoning dimensions, including 9 multimodal games

### 3.4 Modality
- Observation modality: mixed
- Action modality: semantic
- Perception burden retained: rule following, bounded multi-turn state tracking, puzzle solving, spatial reasoning, control interaction, strategic play, and visual reasoning in the multimodal subset
- Perception burden removed: native UI irregularity, raw control difficulty, and most human-facing perception-action noise are abstracted by the standardized game APIs

## 4. What this benchmark measures
- Primary capability target: broad diagnostic evaluation of reasoning performance across heterogeneous but API-mediated game tasks
- Secondary capability target(s): dimension-wise strength and weakness profiles, modality gaps, reasoning-paradigm reliance, and RL-induced changes
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? yes
- Does it test social reasoning / deception / cooperation? no
- Does it test visual grounding / spatial-temporal reasoning? partially; mainly through the separate multimodal subset
- Does it test long-horizon autonomy / task completion? partially; the benchmark uses bounded multi-turn episodes rather than open-ended agent sessions
- Does it test real-time efficiency? no
- Does it test cross-game transfer / open-ended generalization? no; it evaluates a fixed suite rather than held-out or continuously sourced games
- Why is a game environment especially suitable here? Game tasks provide rule-governed, multi-turn, automatically scoreable reasoning settings that can be compared under a shared interaction contract.

## 5. Interaction paradigm
- Observation channel: API-rendered board or state text via `print_board`, with images for the multimodal subset after environment initialization through `generate`
- Action channel: model-produced game moves are checked and executed through `verify`
- Interface type: API / hybrid
- Agent scaffold allowed: none in the main benchmark; RL fine-tuning is analyzed separately rather than exposed as a benchmark-time scaffold
- Is there privileged API access? yes
- How close is the setup to human play? low; KORGym keeps game logic but heavily standardizes observation, action, and scoring
- Main ecological-validity trade-off: KORGym gains breadth, controllability, and RL compatibility by abstracting games into a common API, but that same abstraction removes much of the native perception and control burden that stronger Level 4/5 papers preserve.

## 6. Evaluation protocol
- Main score: Capability Dimension Aggregated Mean over the five text-based reasoning dimensions, with multimodal tasks reported separately for VLMs
- Auxiliary score(s): raw per-game scores, per-dimension results, multimodal-task breakdowns, modality comparisons, behavioral clustering and PCA, reasoning-paradigm ablations, RL analysis, and response-length analysis
- Evaluation style: native score / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: 19 LLMs and 8 VLMs are evaluated zero-shot on seeded game instances; no human baseline is reported
- Automatic verifiability: high
- Calibration method: binary, proportional, or cumulative raw scoring by game; log compression when raw maxima exceed 1; min-max normalization within each game; then dimension-wise averaging
- Anti-contamination argument: the paper motivates the suite through knowledge orthogonality, but it does not provide a direct contamination audit or held-out-data validation
- Reliability or comparability concerns: the aggregated score can hide game-family differences, multimodal results are separated from the main text leaderboard, and the benchmark's standardized interfaces make it a reasoning-diagnostic platform more than a native-play comparison.

## 7. Main contributions
- Contribution 1: Builds a 51-game suite spanning six reasoning dimensions, including nine multimodal tasks.
- Contribution 2: Provides a Gymnasium-inspired framework with standardized APIs, multi-turn interaction, controllable difficulty, and RL-compatible environment design.
- Contribution 3: Runs a broad empirical study over 19 LLMs and 8 VLMs, including modality, reasoning-paradigm, RL, and response-length analyses.

## 8. Main findings and failure modes
- Core empirical takeaway: KORGym reveals stable family-specific reasoning profiles across a broad game suite, with strong closed-source and thinking models leading overall while different families peak on different dimensions.
- Notable model failure mode 1: open-source models lag broadly and show less balanced cross-dimension performance
- Notable model failure mode 2: visual versions are usually much harder than text versions, especially for open-source VLMs
- Notable model failure mode 3: models often over-rely on preferred reasoning paradigms such as code, math, or named algorithms; disabling them can sometimes improve performance
- Does this paper reveal a benchmark-design limitation as well? yes; it shows that benchmark breadth and RL compatibility can be scaled under one framework, but the resulting fixed-suite aggregate still does not amount to cross-game transfer evidence and can obscure per-game behavior.

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Limited use only; it supports the claim that games can scale beyond single-turn reasoning tests, but it is not a primary motivation anchor.
- Best use in Section 1 (taxonomy and evolutionary levels): Use as a Level 2 breadth case where multi-game reasoning coverage grows through platform engineering and dimension aggregation, not as a Level 5 transfer benchmark.
- Best use in Section 2 (core capabilities evaluated by games): Useful for showing how one API-mediated suite bundles mathematical, puzzle, spatial, control, strategic, and multimodal reasoning into one diagnostic benchmark.
- Best use in Section 3 (interaction and evaluation paradigm): Strong evidence for standardized game APIs, controllable difficulty, RL-compatible environment design, and dimension-aware score aggregation across heterogeneous tasks.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Contrast-only use for the trade-off between platform breadth and interpretability; do not use it as evidence of open-ended generalization.

## 10. Relation to nearby papers
- Closest predecessor(s): GameBench, GAMABench, and ReasoningGYM-style reasoning suites
- Closest follow-up(s): DSGBench, LMGameBench, and later benchmark-platform papers that expand API standardization or game coverage
- Best comparison targets inside our corpus: DSGBench, GameBench, LMGameBench, Orak
- What this paper uniquely adds relative to neighbors: It packages 51 heterogeneous reasoning games, multimodal variants, standardized APIs, and RL-ready interaction under one benchmark framework, but it does not add held-out-game transfer or open-ended game sourcing.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- KORGym offers 51 games across six reasoning dimensions and includes nine multimodal games.
- The paper evaluates 19 LLMs and 8 VLMs under zero-shot prompting, with separate reporting for text and multimodal subsets.
- Table 2 positions KORGym as combining multi-turn interaction, RL compatibility, controllable difficulty, and multimodal support in one benchmark.
- Scores are normalized through the Capability Dimension Aggregated Mean rather than reported only as raw per-game results.
- The platform exposes standardized `generate`, `print_board`, and `verify` APIs and is explicitly designed to support reinforcement-learning-style interaction.
- Section 5 reports modality effects, reasoning-paradigm ablations, and RL-linked gains for Doubao-1.5-thinking-pro.

### 11.2 Our synthesis / interpretation
- KORGym is best treated as a broad Level 2 reasoning platform, not as Level 5 cross-game generalization evidence.
- Its survey value comes from scale, API unification, and aggregation design, especially as a bridge between smaller strategic suites and larger benchmark-platform engineering papers.
- Its knowledge-orthogonality framing is a design aspiration and formal motivation, not a demonstrated proof that contamination risk or memorization effects are negligible.

### 11.3 Uncertain or needs re-check
- The paper describes the suite as continuously expandable, but it does not evaluate held-out-game transfer or a true open-ended expansion protocol; avoid collapsing those ideas together in survey prose.
- Re-check Section 5.3 if we later need the strongest RL-improvement examples tied to Doubao-1.5-thinking-pro.
- Re-check Appendix C if we later need exact raw per-game scores or per-dimension game counts beyond the high-level summary.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? Full paper read completed for this audit; no further general reading is required unless we need exact per-game score tables, multimodal details, or the formal knowledge-orthogonality appendix.
- Which section to read next if needed: 3.2 / 3.3 / 5.3 / Appendix B / Appendix C
- Follow-up question(s): If we later compare contamination-mitigation claims across suites, how much of KORGym's knowledge-orthogonality framing can be cited as evidence versus motivation?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P1
- Reading depth: deep
- Batch ID: B02
- Outline sections: 1,2,3
- Survey role: representative
- Paper card path: `paper_cards/B02/KORGym.md`
- Check status: unchecked
- Last updated: 2026-04-21
