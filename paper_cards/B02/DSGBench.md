# DSGBench DSGBench: A Diverse Strategic Game Benchmark for Evaluating LLM-based Agents in Complex Decision-Making Environments

## 0. Metadata
- Date: 2025/03
- Venue: arXiv
- Authors: Wenjie Tang, Yuan Zhou, Erqiang Xu, Keyan Cheng, Minne Li, Liquan Xiao
- Paper link: https://arxiv.org/pdf/2503.06047v1.pdf
- Code link: https://github.com/DeciBrain-Group/DSGBench
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: high
- Review gate label: strong

## 1. One-paragraph benchmark summary
- DSGBench is a six-game benchmark for LLM-based agents spanning StarCraft II, Civilization, Street Fighter III, Diplomacy, Werewolf, and Stratego. Its core contribution is a theory-inspired evaluation framework that maps these games onto five decision-making dimensions, game-specific fine-grained metrics, customizable scenarios, and a decision-tracking pipeline inside a unified Gym-style framework with standardized text-based interaction loops. The paper is strong as a broad diagnostic platform for comparing heterogeneous strategic games and for showing why win rate alone is too coarse, but it is not an open-ended, transfer-oriented, or human-interface-faithful benchmark. For this survey, DSGBench is best used as a comparative suite for strategic reasoning and evaluation design rather than as evidence of Level 5 generalization.

## 2. Position in our survey
- Why-games relevance: A diverse game set can cover multiple dimensions of strategic cognition that would be hard to compare in one real-world benchmark.
- Historical stage: diagnostic capability probe
- Benchmark level(s): L2 strategic reasoning / L3 social intelligence
- Most relevant outline section(s): 1,2,3,4
- Role in corpus: representative

## 3. Design-space coding
### 3.1 Game structure
- Information structure: mixed
- Transition structure: mixed
- Agent structure: mixed
- Social structure: mixed
- Time structure: mixed

### 3.2 Environment structure
- Environment type(s): tabletop / social interaction arena / combat-strategy world
- Real game / simulated game / designed task-game hybrid: multi-game benchmark over established strategic games
- Benchmark unit: match / scenario

### 3.3 Benchmark scope
- Scope: curated suite
- Number of games / tasks: 6 games with customizable scenarios

### 3.4 Modality
- Observation modality: text or symbolic
- Action modality: semantic
- Perception burden retained: strategic reasoning, social reasoning, temporal control, multi-step planning, and action grounding under standardized state descriptions
- Perception burden removed: raw visuals, native interfaces, and most human-facing control burdens are abstracted into text-based interfaces

## 4. What this benchmark measures
- Primary capability target: theory-inspired multi-dimensional evaluation of strategic decision making across heterogeneous games
- Secondary capability target(s): long-term planning, real-time decision-making, social reasoning, team collaboration, and adaptive learning
- Does it test rule grounding / legal action generation? partially; mainly through text-action grounding accuracy rather than rule-following as the main benchmark goal
- Does it test strategic planning under uncertainty? yes
- Does it test social reasoning / deception / cooperation? yes
- Does it test visual grounding / spatial-temporal reasoning? no
- Does it test long-horizon autonomy / task completion? partially; it probes long-horizon strategic consistency, not open-ended task completion
- Does it test real-time efficiency? yes
- Does it test cross-game transfer / open-ended generalization? no; it spans multiple games but does not evaluate held-out transfer or open-ended generalization
- Why is a game environment especially suitable here? Games provide multi-agent, uncertainty-heavy, and customizable decision settings where strategic subskills can be instrumented more directly than in static tasks.

## 5. Interaction paradigm
- Observation channel: standardized text observations over game state, objectives, roles, and histories, delivered through observation-to-prompt loops
- Action channel: text outputs grounded into game-specific legal actions through response-to-action loops
- Interface type: natural language / structured action space / hybrid
- Agent scaffold allowed: other (game-specific prompt templates and reasoning prompts; no model fine-tuning reported in evaluation)
- Is there privileged API access? yes; all six environments are wrapped into standardized text interfaces rather than native player views
- How close is the setup to human play? low; DSGBench emphasizes comparability and metric extraction over native interface fidelity
- Main ecological-validity trade-off: the benchmark gains breadth, controllability, and fine-grained measurement by abstracting all games into standardized text-first interfaces

## 6. Evaluation protocol
- Main score: weighted overall score aggregated from five capability dimensions
- Auxiliary score(s): capability-specific metric families such as RPM/EER/SUR/TCR, APM/EPM, BIR/IRP, ASR/AD/KSR/VSS, and WR/GA
- Evaluation style: hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: no human baseline; six LLMs are evaluated across standardized scenarios against built-in game AI or GPT-4o-mini opponents, with 10 matches per scenario
- Automatic verifiability: high
- Calibration method: scenario-specific controllable variables, repeated runs, and metric normalization with predefined min/max values before weighted aggregation
- Anti-contamination argument: not central
- Reliability or comparability concerns: the capability scores depend on theory- and expert-defined metric mappings, weights, and adjustment factors whose choices are not fully justified for cross-paper comparison, and the textified interface may reflect prompt/interface design as much as underlying raw game skill

## 7. Main contributions
- Contribution 1: Builds a six-game benchmark spanning strategy, fighting, and social games.
- Contribution 2: Introduces a human-cognition-inspired five-dimension evaluation framework with game-specific fine-grained metrics and weighted capability scoring.
- Contribution 3: Adds customizable scenarios and a unified decision-tracking framework, with the paper's qualitative trajectory analysis demonstrated most concretely in StarCraft II.

## 8. Main findings and failure modes
- Core empirical takeaway: different LLMs specialize unevenly across the five reported capability dimensions, and no model is uniformly strong across strategic planning, real-time control, social reasoning, collaboration, and adaptive learning.
- Notable model failure mode 1: weak temporal control in real-time settings despite good long-range planning
- Notable model failure mode 2: difficulty adapting to unexpected opponent strategies or rapidly changing game states
- Notable model failure mode 3: inconsistent social and team reasoning in Diplomacy and Werewolf, especially for weaker open-source models
- Does this paper reveal a benchmark-design limitation as well? yes; it shows that outcome-only metrics miss major differences in how models play, but its own multi-dimensional scores still depend on handcrafted mappings and heavily textified interfaces

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Use it to argue that win rate alone is too coarse and that different strategic games expose different slices of decision-making capability.
- Best use in Section 1 (taxonomy and evolutionary levels): Represents a mature move from single-game probes to comparative multi-game diagnostic suites. Use it as broad curated-suite coverage, not as a full Level 5 transfer benchmark.
- Best use in Section 2 (core capabilities evaluated by games): A direct source for theory-inspired strategic capability decomposition, but do not treat its five dimensions as a cleanly validated cognitive factorization.
- Best use in Section 3 (interaction and evaluation paradigm): Useful for discussing unified text interfaces across heterogeneous games, handcrafted metric families, weighted aggregation, and trajectory-based analysis.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Supports claims about capability specialization, temporal/social weaknesses, and the trade-off between richer diagnostics and comparability.

## 10. Relation to nearby papers
- Closest predecessor(s): GameBench, GTBench, SmartPlay
- Closest follow-up(s): BeyondScaling, BoardGameArena, GameArena
- Best comparison targets inside our corpus: BeyondScaling, GameBench, GAMABench, TMGBench
- What this paper uniquely adds relative to neighbors: It combines six-game breadth with a theory-inspired capability decomposition, game-specific metric families, weighted aggregation, and decision-tracking in one unified framework.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- DSGBench covers StarCraft II, Civilization, Street Fighter III, Diplomacy, Werewolf, and Stratego.
- Section 4.1 motivates five capability dimensions from Dual Systems Cognitive Theory, Distributed Cognition Theory, and Dynamic Decision Theory: strategic planning, real-time decision-making, social reasoning, team collaboration, and adaptive learning.
- Table 2 maps these capability dimensions to different games, scenario types, and game-specific metric families rather than using a single universal metric.
- All environments are encapsulated as standardized text-based interfaces, and each scenario is run for 10 matches against built-in AI or GPT-4o-mini opponents.
- Table 6 reports strong specialization across dimensions rather than a single uniformly dominant model.

### 11.2 Our synthesis / interpretation
- DSGBench is a strong survey source for arguing that strategic-game evaluation benefits from theory-inspired subcapability breakdowns and metric families instead of collapsing everything into win rate.
- The paper supports multi-dimensional strategic evaluation, but not a strict or validated decomposition of reasoning into independent cognitive factors.
- Its breadth across multiple games does not by itself make it a Level 5 generalization benchmark; its safest use is as a broad diagnostic suite and interface-design contrast.

### 11.3 Uncertain or needs re-check
- Re-check the exact values or justification of the capability weights and adjustment factors if later drafting uses the overall score directly.
- Re-check per-game metric formulas in Appendix B before building any cross-paper comparison table.
- Keep in mind that the paper's trajectory-analysis results section is demonstrated most concretely in StarCraft II, so avoid implying equally detailed multi-game trajectory evidence unless reopened.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? No immediate follow-up needed; the full paper has been read for this audit. Reopen Appendix A or B only if we need exact metric formulas, weighting details, or scenario tables.
- Which section to read next if needed: Appendix A/B framework details and metric formulas
- Follow-up question(s): Which metric choices are robust enough for cross-paper comparison, and which remain too game-specific to compare cleanly?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P1
- Reading depth: deep
- Batch ID: B02
- Outline sections: 1,2,3,4
- Survey role: representative
- Paper card path: `paper_cards/B02/DSGBench.md`
- Check status: unchecked
- Next action: draft-section
- Last updated: 2026-04-19
