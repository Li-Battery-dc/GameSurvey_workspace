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
- DSGBench is a six-game benchmark for LLM-based agents spanning StarCraft II, Civilization, Street Fighter III, Diplomacy, Werewolf, and Stratego. Its core contribution is the capability-centered evaluation framework: five decision-making dimensions, game-specific fine-grained metrics, customizable scenarios, and decision-trajectory tracking, all wrapped in a unified Gym-style framework with standardized text-based interaction loops. The paper is strong as a broad diagnostic platform for comparing heterogeneous strategic games, but it is not an open-ended or human-interface-faithful benchmark. For this survey, DSGBench is best used as a comparative suite for strategic reasoning and evaluation design rather than as evidence of cross-game transfer in the stronger Level 5 sense.

## 2. Position in our survey
- Why-games relevance: A diverse game set can cover multiple dimensions of strategic cognition that would be hard to compare in one real-world benchmark.
- Historical stage: diagnostic capability probe
- Narrative level(s): L2 strategic reasoning / L3 social intelligence
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
- World type(s): RTS / board / social deduction / fighting / other
- Real game / simulated game / designed task-game hybrid: multi-game benchmark over established strategic games
- Benchmark unit: match / scenario

### 3.3 Benchmark scope
- Scope: genre-diverse suite
- Number of games / tasks: 6 games with customizable scenarios
- Benchmark intent: diagnostic evaluation

### 3.4 Modality
- Primary modality: text / symbolic state
- Perception burden retained: strategic reasoning, social reasoning, temporal control, multi-step planning, and action grounding under standardized state descriptions
- Perception burden removed: raw visuals, native GUIs, and most human-facing control burdens are abstracted into text-based interfaces

## 4. What this benchmark measures
- Primary capability target: strategic decision making across multiple game genres
- Secondary capability target(s): real-time adaptation, social reasoning, team collaboration, and decision consistency
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? yes
- Does it test social reasoning / deception / cooperation? yes
- Does it test visual grounding / spatial-temporal reasoning? no
- Does it test long-horizon autonomy / task completion? yes
- Does it test real-time efficiency? yes
- Does it test cross-game transfer / open-ended generalization? partially
- Why is a game environment especially suitable here? Games provide controllable but diverse strategic settings that can be scored with both game outcomes and capability-specific submetrics.

## 5. Interaction paradigm
- Observation channel: standardized text observations over game state, objectives, and histories, delivered through observation-to-prompt loops
- Action channel: text-based or text-grounded actions mapped into the underlying environments through response-to-action loops
- Interface type: natural language / structured action space / hybrid
- Agent scaffold allowed: other (game-specific prompt templates and reasoning frameworks; no model fine-tuning in evaluation)
- Is there privileged API access? yes; all six environments are wrapped into standardized text interfaces rather than native player views
- How close is the setup to human play? medium-low; DSGBench emphasizes comparability and metric extraction over native interface fidelity
- Main ecological-validity trade-off: the benchmark gains breadth, controllability, and fine-grained measurement by abstracting all games into standardized text-first interfaces

## 6. Evaluation protocol
- Main score: weighted overall score across five capability dimensions
- Auxiliary score(s): capability-specific metric families such as RPM/EER/SUR/TCR, APM/EPM, BIR/IRP, ASR/AD/KSR/VSS, and WR/GA
- Evaluation style: hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: six LLMs are evaluated across standardized scenarios against built-in game AI or GPT-4o-mini opponents, with 10 matches per scenario
- Automatic verifiability: high
- Calibration method: scenario-specific controllable variables, repeated runs, and metric normalization with predefined min/max values before weighted aggregation
- Anti-contamination argument: not central
- Reliability or comparability concerns: the capability scores depend on handcrafted metric mappings and weights, and the textified interface may reflect prompt/interface design as much as underlying raw game skill

## 7. Main contributions
- Contribution 1: Builds a six-game benchmark spanning strategy, fighting, and social games.
- Contribution 2: Introduces a five-dimension capability framework with game-specific fine-grained metrics and weighted capability scoring.
- Contribution 3: Adds decision-trajectory tracking plus customizable scenarios in a unified Gym-style framework.

## 8. Main findings and failure modes
- Core empirical takeaway: different LLMs specialize unevenly across capability dimensions, and no model is uniformly strong across long-term planning, real-time control, social reasoning, collaboration, and adaptive learning.
- Notable model failure mode 1: weak temporal control in real-time settings despite good long-range planning
- Notable model failure mode 2: poor adaptation to dynamic or adversarial shifts
- Notable model failure mode 3: inconsistent social and team reasoning in Diplomacy and Werewolf, especially for weaker open-source models
- Does this paper reveal a benchmark-design limitation as well? yes; it shows that outcome-only metrics miss major differences in how models play and that broad cross-game coverage can still rely on heavily textified interfaces

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Strong support for the idea that different games reveal different slices of strategic cognition.
- Best use in Section 1 (taxonomy and evolutionary levels): Represents a mature move from single-game probes to comparative multi-game diagnostic suites. Use it as genre-diverse breadth, not as a full Level 5 transfer benchmark.
- Best use in Section 2 (core capabilities evaluated by games): A direct source for capability-taxonomy discussion.
- Best use in Section 3 (interaction and evaluation paradigm): Useful for discussing unified text interfaces across heterogeneous games, weighted capability scores, and trajectory-based analysis.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Supports trajectory-level analysis rather than only final scores.

## 10. Relation to nearby papers
- Closest predecessor(s): SmartPlay, GTBench
- Closest follow-up(s): BoardGameArena, GameArena
- Best comparison targets inside our corpus: BeyondScaling, GameBench, GAMABench, TMGBench
- What this paper uniquely adds relative to neighbors: It combines six-game breadth with explicit capability-taxonomy scoring, weighted aggregation, and decision-trajectory logging in one framework.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- DSGBench covers StarCraft II, Civilization, Street Fighter III, Diplomacy, Werewolf, and Stratego.
- It organizes evaluation around five capability dimensions: strategic planning, real-time decision-making, social reasoning, team collaboration, and adaptive learning, with a weighted overall score.
- All environments are encapsulated as standardized text-based interfaces, and each scenario is run for 10 matches against built-in AI or GPT-4o-mini opponents.

### 11.2 Our synthesis / interpretation
- DSGBench is a strong survey source for arguing that game benchmarks should separate strategic subcapabilities instead of collapsing everything into win rate.
- Its breadth across multiple games does not by itself make it a strong Level 5 generalization benchmark; its safest use is as a broad diagnostic suite and interface-design contrast.

### 11.3 Uncertain or needs re-check
- Re-check the exact weighting of the overall score if later drafting uses it directly.
- Re-check the appendix metric definitions for each game if we later build a comparison table.

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
- Last updated: 2026-04-10
