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
- DSGBench is a multi-game benchmark for LLM-based agents that spans StarCraft II, Civilization, Street Fighter III, Diplomacy, Werewolf, and Stratego. Its main contribution is not just game selection but the capability-centered evaluation framework: strategic planning, real-time decision-making, social reasoning, team collaboration, and adaptive learning, each tied to fine-grained game-specific metrics and decision-trajectory tracking. The framework supports customizable scenarios and a unified Gym-style interface across very different strategy genres. For this survey, DSGBench is one of the strongest platform papers for comparative evaluation across heterogeneous strategic games.

## 2. Position in our survey
- Why-games relevance: A diverse game set can cover multiple dimensions of strategic cognition that would be hard to compare in one real-world benchmark.
- Historical stage: open-ended general-game benchmark
- Narrative level(s): L2 strategic reasoning / L3 social intelligence / L5 cross-game generalization
- Most relevant outline section(s): 1,2,3,5,6
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
- Benchmark intent: diagnostic evaluation / ecological evaluation

### 3.4 Modality
- Primary modality: mostly text / symbolic state
- Perception burden retained: strategic reasoning, social reasoning, temporal control, and action grounding
- Perception burden removed: most games are standardized through text interfaces rather than raw native visuals

## 4. What this benchmark measures
- Primary capability target: strategic decision making across multiple game genres
- Secondary capability target(s): real-time adaptation, social reasoning, team collaboration, and decision consistency
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? yes
- Does it test social reasoning / deception / cooperation? yes
- Does it test visual grounding / spatial-temporal reasoning? partially
- Does it test long-horizon autonomy / task completion? yes
- Does it test real-time efficiency? yes
- Does it test cross-game transfer / open-ended generalization? yes
- Why is a game environment especially suitable here? Games provide controllable but diverse strategic settings that can be scored with both game outcomes and capability-specific submetrics.

## 5. Interaction paradigm
- Observation channel: standardized text observations over game state, plus game-specific prompts and histories
- Action channel: text-grounded or structured game actions through a unified environment interface
- Interface type: API / natural language / hybrid
- Agent scaffold allowed: decision tracking / history
- Is there privileged API access? yes
- How close is the setup to human play? medium-low; DSGBench emphasizes comparability and metric extraction over native interface fidelity
- Main ecological-validity trade-off: the benchmark gains breadth and fine-grained measurement by abstracting most games into text-first interfaces

## 6. Evaluation protocol
- Main score: weighted overall score across five capability dimensions
- Auxiliary score(s): fine-grained metrics such as EER, SUR, APM, EPM, GA, and game-specific social/team metrics
- Evaluation style: hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: multiple frontier LLMs are evaluated in matched scenarios and compared through normalized capability metrics
- Automatic verifiability: high
- Calibration method: game-specific metric normalization and repeated scenario runs
- Anti-contamination argument: live game interaction plus scenario customization create broader coverage than fixed static tasks
- Reliability or comparability concerns: the capability scores depend on many handcrafted metric choices and may reflect interface design as much as raw model ability

## 7. Main contributions
- Contribution 1: Builds a six-game benchmark spanning strategy, fighting, and social games.
- Contribution 2: Introduces a five-dimension capability taxonomy with game-specific fine-grained metrics.
- Contribution 3: Adds decision-trajectory tracking to connect actions with outcomes and contexts.

## 8. Main findings and failure modes
- Core empirical takeaway: different LLMs specialize unevenly across capability dimensions, and no model is strong across all strategic demands.
- Notable model failure mode 1: weak temporal control in real-time settings despite good long-range planning
- Notable model failure mode 2: poor adaptation to dynamic or adversarial shifts
- Notable model failure mode 3: shallow social/team reasoning in Diplomacy and Werewolf-like settings
- Does this paper reveal a benchmark-design limitation as well? yes; it shows that outcome-only metrics miss major differences in how models play and fail

## 9. Why this paper matters for our survey
- Best use in Section 0 (why games): Strong support for the idea that different games reveal different slices of strategic cognition.
- Best use in Section 1 (historical evolution): Represents a mature move from single-game to comparative multi-game evaluation.
- Best use in Section 2 (design space): Excellent for genre-diverse benchmark platforms.
- Best use in Section 3 (capability targets): A direct source for capability-taxonomy discussion.
- Best use in Section 4 (interaction paradigm): Useful for discussing unified text interfaces across heterogeneous games.
- Best use in Section 5 (evaluation protocol): One of the best references for capability-specific fine-grained metrics.
- Best use in Section 6/7 (limitations and future): Supports trajectory-level analysis rather than only final scores.

## 10. Relation to nearby papers
- Closest predecessor(s): SmartPlay, GTBench
- Closest follow-up(s): GameArena
- Best comparison targets inside our corpus: SmartPlay, GTBench, GameArena, StarCraftIIArena
- What this paper uniquely adds relative to neighbors: It combines cross-game breadth with explicit capability-taxonomy scoring and trajectory logging.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- DSGBench covers StarCraft II, Civilization, Street Fighter III, Diplomacy, Werewolf, and Stratego.
- It organizes evaluation around five capability dimensions: strategic planning, real-time decision-making, social reasoning, team collaboration, and adaptive learning.
- The benchmark includes decision-trajectory tracking alongside normalized fine-grained metrics.

### 11.2 Our synthesis / interpretation
- DSGBench is a strong survey anchor for arguing that game benchmarks should separate strategic subcapabilities instead of collapsing everything into win rate.
- It is especially useful when comparing broad platforms against narrower single-game papers.

### 11.3 Uncertain or needs re-check
- Re-check the exact weighting of the overall score if later drafting uses it directly.
- Re-check the appendix metric definitions for each game if we later build a comparison table.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? Yes later, because the metric taxonomy is central survey material.
- Which section to read next if needed: capability metrics / trajectory tracking / game-specific scenarios
- Follow-up question(s): Which metric choices are most stable across games, and which are highly game-specific?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P1
- Reading depth: deep
- Batch ID: B12
- Outline sections: 1,2,3,5,6
- Survey role: representative
- Paper card path: `paper_cards/B12/DSGBench.md`
- Next action: draft-section
- Last updated: 2026-04-05
