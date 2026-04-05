# StarCraftIIArena StarCraft II Arena: Evaluating LLMs in Strategic Planning, Real-Time Decision Making, and Adaptability

## 0. Metadata
- Date: 2024/09
- Venue: arXiv
- Authors: Wenjie Tang, Yuan Zhou, Erqiang Xu, Keyan Cheng, Minne Li, Zhiyuan Wang
- Paper link: https://openreview.net/pdf?id=o3V7OuPxu4
- Code link:
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: medium
- Review gate label: usable

## 1. One-paragraph benchmark summary
- StarCraft II Arena is an RTS benchmark focused on three capability axes: strategic planning, real-time decision making, and robustness or adaptability. The paper frames SC2 as a high-pressure environment for resource allocation, tech progression, and fast tactical response, then evaluates LLM agents with fine-grained metrics such as resource-allocation efficiency, supply utilization, tech progression, and decision-trace analyses. From the available paper text and abstract, the benchmark appears to extend text-mediated SC2 evaluation toward more capability-specific scoring and robustness analysis. For this survey, it is best used as a follow-up RTS evaluation paper that sharpens metric design, though some implementation details remain less certain in this card than for the arXiv-sourced SC2 papers.

## 2. Position in our survey
- Why-games relevance: RTS games expose the tension between long-term plans and rapidly changing tactical demands.
- Historical stage: ecological agent benchmark
- Narrative level(s): L2 strategic reasoning / L5 cross-game generalization
- Most relevant outline section(s): 2,3,4,5,6
- Role in corpus: representative

## 3. Design-space coding
### 3.1 Environment structure
- Information structure: imperfect
- Transition structure: mixed
- Agent structure: multi-agent
- Social structure: competitive
- Time structure: real-time / hybrid

### 3.2 World structure
- World type(s): RTS
- Real game / simulated game / designed task-game hybrid: StarCraft II benchmark through a text-mediated or structured environment
- Benchmark unit: match / scenario

### 3.3 Benchmark scope
- Scope: single game
- Number of games / tasks: StarCraft II scenarios or matches focused on strategy, real-time decision, and robustness
- Benchmark intent: ecological evaluation / diagnostic evaluation

### 3.4 Modality
- Primary modality: text / symbolic state
- Perception burden retained: strategic state understanding, time pressure, and tactical adaptation
- Perception burden removed: raw visual play appears abstracted away

## 4. What this benchmark measures
- Primary capability target: strategic planning and real-time adaptation in RTS play
- Secondary capability target(s): efficient resource use, tech progression, and robustness across changing situations
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? yes
- Does it test social reasoning / deception / cooperation? no
- Does it test visual grounding / spatial-temporal reasoning? no in the core benchmark as described
- Does it test long-horizon autonomy / task completion? yes
- Does it test real-time efficiency? yes
- Does it test cross-game transfer / open-ended generalization? partially
- Why is a game environment especially suitable here? SC2 tightly couples economy, timing, and adaptation under adversarial pressure.

## 5. Interaction paradigm
- Observation channel: structured or textual game state summaries for SC2
- Action channel: strategic or macro-level game commands
- Interface type: API / hybrid
- Agent scaffold allowed: decision tracing / history
- Is there privileged API access? yes
- How close is the setup to human play? medium-low; the strategic domain is authentic, but the interface is abstracted for LLM control
- Main ecological-validity trade-off: the benchmark seems to gain fine-grained measurement by working over structured RTS interfaces rather than human-native play

## 6. Evaluation protocol
- Main score: composite capability evaluation across strategic planning, real-time decision making, and robustness
- Auxiliary score(s): resource allocation efficiency, supply utilization rate, tech progression rate, economic sustainability, and decision-trace analyses
- Evaluation style: hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: LLM agents are compared through repeated SC2 evaluation with game-specific metrics
- Automatic verifiability: high
- Calibration method: fine-grained RTS metrics and decision-trace inspection
- Anti-contamination argument: dynamic RTS interaction is harder to overfit than static strategic QA
- Reliability or comparability concerns: this card is grounded partly in the abstract and search snippets from the authoritative PDF, so some implementation specifics should be rechecked before using very fine details in draft prose

## 7. Main contributions
- Contribution 1: Frames SC2 evaluation around strategic planning, real-time action, and robustness rather than win rate alone.
- Contribution 2: Introduces fine-grained RTS capability metrics such as resource and tech-efficiency measures.
- Contribution 3: Adds decision-trace-style analysis for understanding agent behavior over time.

## 8. Main findings and failure modes
- Core empirical takeaway: current LLMs still struggle with the combined demands of long-term planning and rapid adaptation in SC2.
- Notable model failure mode 1: inefficient resource allocation and supply management
- Notable model failure mode 2: weak adaptation to dynamic battlefield changes
- Notable model failure mode 3: fragile strategic consistency under real-time pressure
- Does this paper reveal a benchmark-design limitation as well? yes; it argues that broad outcome metrics are too coarse for RTS evaluation

## 9. Why this paper matters for our survey
- Best use in Section 0 (why games): Supports the claim that RTS games remain demanding because they require both planning and speed.
- Best use in Section 1 (historical evolution): A follow-up step after early text-based SC2 evaluations.
- Best use in Section 2 (design space): Useful for single-domain benchmark deepening through better metrics rather than new games.
- Best use in Section 3 (capability targets): Strong for strategic planning versus real-time adaptation distinctions.
- Best use in Section 4 (interaction paradigm): Another reference for abstracted RTS interfaces.
- Best use in Section 5 (evaluation protocol): Particularly useful for fine-grained RTS metrics and decision traces.
- Best use in Section 6/7 (limitations and future): Supports richer metric design in future RTS benchmarks.

## 10. Relation to nearby papers
- Closest predecessor(s): LLMPlayStarCraftII
- Closest follow-up(s): DSGBench
- Best comparison targets inside our corpus: LLMPlayStarCraftII, DSGBench, VLMPlayStarCraftII
- What this paper uniquely adds relative to neighbors: It appears to deepen RTS evaluation through capability-specific metrics rather than only broad win-rate reporting.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- The paper title and abstract state that the benchmark targets strategic planning, real-time decision making, and adaptability in StarCraft II.
- Search-visible paper text identifies metrics including resource-allocation efficiency, supply utilization rate, tech progression rate, and related economic or decision-trace analyses.
- The paper frames SC2 as a benchmark for rapidly changing strategic environments rather than only static plan quality.

### 11.2 Our synthesis / interpretation
- StarCraft II Arena is useful as a metric-design follow-up in the SC2 line, especially when paired with TextStarCraft II and DSGBench.
- Because I could not fully inspect the PDF body line by line in the current environment, this card should be treated as usable rather than strong.

### 11.3 Uncertain or needs re-check
- Re-check the full PDF for exact experimental setup, agent set, and scenario configuration before quoting detailed numbers in survey prose.
- Re-check whether the benchmark is built directly on TextStarCraft II or on a distinct environment implementation.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? Yes if this paper becomes a core RTS citation, because some details need direct PDF verification.
- Which section to read next if needed: evaluation metrics / scenario setup / main quantitative results
- Follow-up question(s): Which robustness dimension is most diagnostic in the reported experiments: economy, tech progression, or tactical reaction?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P1
- Reading depth: deep
- Batch ID: B13
- Outline sections: 2,3,4,5,6
- Survey role: representative
- Paper card path: `paper_cards/B13/StarCraftIIArena.md`
- Next action: draft-section
- Last updated: 2026-04-05
