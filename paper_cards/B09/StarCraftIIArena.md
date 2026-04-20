# StarCraftIIArena StarCraft II Arena: Evaluating LLMs in Strategic Planning, Real-Time Decision Making, and Adaptability

## 0. Metadata
- Date: 2024/09
- Venue: OpenReview / ICLR 2025 submission rejected
- Authors: Wenjie Tang, Yuan Zhou, Erqiang Xu, Keyan Cheng, Minne Li, Zhiyuan Wang
- Paper link: https://openreview.net/pdf?id=o3V7OuPxu4
- Code link:
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: medium
- Review gate label: usable

## 1. One-paragraph benchmark summary
- StarCraft II Arena is a specialist RTS benchmark paper that evaluates LLM agents along three decomposed axes: strategic planning, real-time decision-making, and adaptability. Rather than relying only on final match success, it introduces fine-grained capability metrics such as resource gathering, supply use, action efficiency, and win or error trends, and pairs them with a decision-tracking system that records intermediate strategic choices. The paper applies this benchmark to seven proprietary and open models and emphasizes that different models excel on different sub-capabilities even within the same StarCraft II domain. For this survey, the paper is most useful as a metric-design follow-up inside the SC2 line, not as a strong interface or ecological-play anchor.

## 2. Position in our survey
- Why-games relevance: RTS games compress long-term planning, time-bounded response, and adaptation to opponent behavior into a single adversarial environment.
- Historical stage: diagnostic capability probe
- Benchmark level(s): L2 strategic reasoning
- Most relevant outline section(s): 1,2,3,4
- Role in corpus: representative

## 3. Design-space coding
### 3.1 Game structure
- Information structure: imperfect
- Transition structure: mixed
- Agent structure: multi-agent
- Social structure: competitive
- Time structure: hybrid

### 3.2 World structure
- World type(s): RTS
- Real game / simulated game / designed task-game hybrid: StarCraft II benchmark scenarios with tracked high-level strategic decisions
- Benchmark unit: match / scenario

### 3.3 Benchmark scope
- Scope: single game
- Number of games / tasks: scenarios organized around Macro, Rush, and Random opponent strategies under Async and Sync modes; the main result table reports 10 games per model

### 3.4 Modality
- Observation modality: mixed
- Action modality: semantic
- Perception burden retained: partial observability, resource and army-state reasoning, strategic adaptation, and real-time response pressure
- Perception burden removed: the exact observation serialization and low-level control pathway are underdescribed in the paper, so the full human-play burden is not recoverable from the text alone

## 4. What this benchmark measures
- Primary capability target: strategic planning versus real-time execution trade-offs in RTS play
- Secondary capability target(s): resource management, supply and tech progression, action efficiency, and adaptation across games
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? yes
- Does it test social reasoning / deception / cooperation? no
- Does it test visual grounding / spatial-temporal reasoning? partially; spatial-temporal reasoning is central, but the paper does not clearly expose a raw visual interface
- Does it test long-horizon autonomy / task completion? yes
- Does it test real-time efficiency? yes
- Does it test cross-game transfer / open-ended generalization? no
- Why is a game environment especially suitable here? StarCraft II forces the benchmark to evaluate long-horizon planning, adversarial adaptation, and time pressure together rather than as separate static tasks.

## 5. Interaction paradigm
- Observation channel: the paper formalizes the setting as a StarCraft II POMDP with state, observation, and valid-action spaces, and its decision-trace examples reference current game state and mission objectives
- Action channel: tracked high-level decisions such as training units, building structures, research, scouting, and expansion choices; the paper also describes a high-level and low-level two-stage reasoning process
- Interface type: API / structured action space / hybrid
- Agent scaffold allowed: planner / other
- Is there privileged API access? partially; the paper clearly exposes structured state and valid-action abstractions, but does not fully specify the concrete observation serialization or low-level executor
- How close is the setup to human play? medium-low; the benchmark preserves RTS time pressure and adversarial dynamics, but its strongest contribution is capability instrumentation rather than a human-like interface
- Main ecological-validity trade-off: StarCraft II Arena keeps real RTS dynamics and timing pressure, but abstracts interaction into capability-oriented tracked decisions whose exact implementation is thinner than in stronger environment papers

## 6. Evaluation protocol
- Main score: overall weighted capability score plus win rate
- Auxiliary score(s): strategic-planning metrics `RPM`, `EER`, `SUR`, `TRR`; real-time metrics `APM`, `EPM`; adaptability metrics `WinRateTrend` and `ErrorRateTrend`; and qualitative decision-trace analysis
- Evaluation style: hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: seven LLMs are evaluated across the benchmark scenarios; the main result table reports `x/10` win-rate outcomes and per-capability scores, but the paper does not provide a human baseline
- Automatic verifiability: mixed-high; quantitative metrics are logged from gameplay, while decision-trace interpretation adds a qualitative layer
- Calibration method: scenario weighting and normalization, Macro/Rush/Random opponent-strategy scenes, and Sync/Async timing modes
- Anti-contamination argument: not central
- Reliability or comparability concerns: the paper underdescribes the concrete interface and opponent implementation, and it contains terminology inconsistencies across tables and captions such as `RPM` versus `RMA`, `EER` versus `RUE`, and `WinRateTrend` versus `WRGR`

## 7. Main contributions
- Contribution 1: Reframes SC2 evaluation around three decomposed capabilities instead of outcome-only win rates.
- Contribution 2: Introduces fine-grained RTS metrics for planning, action efficiency, and adaptation.
- Contribution 3: Adds decision-trace analysis to inspect intermediate strategic choices over time.

## 8. Main findings and failure modes
- Core empirical takeaway: the paper reports that model strengths are uneven across SC2 sub-capabilities: GPT-4o leads in strategic planning, Llama 3.1 8B leads in real-time decision-making, and Llama 3.1 70B leads in adaptability, showing that win rate alone hides important within-domain differences.
- Notable model failure mode 1: strong long-term planners can still respond too slowly in synchronous, time-critical settings
- Notable model failure mode 2: models struggle to adapt consistently under incomplete information and rapidly evolving opponent strategies
- Notable model failure mode 3: capability-specific metrics reveal that overall match outcomes can hide weak resource management, inefficient action use, or slow improvement over repeated games
- Does this paper reveal a benchmark-design limitation as well? yes; it shows why outcome-only RTS evaluation is too coarse, but its own benchmark description leaves some interface and setup details underspecified

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Limited support for the claim that games reveal timing-sensitive failures invisible in static tests.
- Best use in Section 1 (taxonomy and evolutionary levels): Useful as a later specialist RTS benchmark that deepens one game domain through metric design rather than through broader game coverage.
- Best use in Section 2 (core capabilities evaluated by games): Direct support for separating long-term planning, rapid response, and adaptation inside a single RTS benchmark.
- Best use in Section 3 (interaction and evaluation paradigm): Best used for fine-grained metric design, sync-versus-async comparison, and decision-trace instrumentation; do not rely on it as the main source for interface specifics.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Supports the survey's argument that real-time execution and strategic planning can diverge sharply and need separate evaluation.

## 10. Relation to nearby papers
- Closest predecessor(s): LLMPlayStarCraftII
- Closest follow-up(s): VLMPlayStarCraftII and later multimodal or RTS-specific evaluation papers
- Best comparison targets inside our corpus: LLMPlayStarCraftII, VLMPlayStarCraftII, PokerBench, GTOWizardBenchmark
- What this paper uniquely adds relative to neighbors: It is the clearest SC2 paper in the corpus that turns capability decomposition and intermediate decision tracing into the main benchmark contribution

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- The paper defines StarCraft II Arena around three evaluation dimensions: strategic planning, real-time decision-making, and adaptability.
- Table 2 pairs those dimensions with quantitative metrics: `RPM`, `EER`, `SUR`, and `TRR` for planning; `APM` and `EPM` for real-time decision-making; and `WinRateTrend` plus `ErrorRateTrend` for adaptability, alongside Macro/Rush/Random scenes and Sync/Async modes.
- Table 4 reports results for seven models: GPT-4o, GPT-4o mini, GPT-3.5 Turbo, Gemini 1.5 Flash, DeepSeek-V2.5, Llama-3.1-8B-Instruct, and Llama-3.1-70B-Instruct.
- The main results state that GPT-4o has the highest strategic-planning score (`62.01`), Llama-3.1-8B-Instruct has the highest real-time score (`47.05`), and Llama-3.1-70B-Instruct has the highest adaptability score (`52.77`).
- Table 3 provides decision-trace examples with ordered high-level actions such as `TRAIN`, `BUILD`, `RESEARCH`, `SCOUTING`, and `EXPAND`, plus natural-language strategy and suggestion fields.
- Appendix Table 6 describes the benchmark's game manual as a standard `1v1` setting on Jagannatha LE with the usual StarCraft II resource and base structure.

### 11.2 Our synthesis / interpretation
- This paper is safest as a reviewed metric-design comparison inside the SC2 lineage, not as a definitive source on how to build the interaction loop of an RTS benchmark.
- It is especially useful for the survey because it exposes a strategy-versus-speed split similar in spirit to other time-pressure papers, but within a single familiar RTS domain.

### 11.3 Uncertain or needs re-check
- The paper does not clearly specify the exact observation serialization, the concrete low-level executor, or the full opponent implementation, so interface claims should stay narrow.
- Some terminology is inconsistent across the paper's tables and captions, so later drafting should prefer the formulas and names in the main text plus Appendix A.1 over noisier captions.
- If later drafting needs exact scenario weighting or overall-score construction details, re-check Equation 2 and the scenario-weight definitions.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? Full paper read completed for this audit. Reopen only if later drafting needs exact score aggregation, scenario weighting, or deeper implementation detail than the current paper clearly provides.
- Which section to read next if needed: Section 4.2 / Section 4.3 / Appendix A.1 / Appendix A.2
- Follow-up question(s): If we compare RTS benchmarks in the survey, how much of the observed difference comes from time pressure versus interface abstraction?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P1
- Reading depth: deep
- Batch ID: B09
- Outline sections: 1,2,3,4
- Survey role: representative
- Paper card path: `paper_cards/B09/StarCraftIIArena.md`
- Check status: unchecked
- Next action: draft-section
- Last updated: 2026-04-10
