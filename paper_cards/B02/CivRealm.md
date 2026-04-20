# CivRealm CivRealm: A Learning and Reasoning Odyssey in Civilization for Decision-Making Agents

## 0. Metadata
- Date: 2024/01
- Venue: ICLR 2024
- Authors: Siyuan Qi, Shuo Chen, Yexin Li, Xiangyu Kong, Junqi Wang, Bangcheng Yang, Pring Wong, Yifan Zhong, Xiaoyuan Zhang, Zhaowei Zhang, Nian Liu, Wei Wang, Yaodong Yang, Song-Chun Zhu
- Paper link: https://openreview.net/pdf?id=UBVNwD3hPN
- Code link: https://github.com/bigai-ai/civrealm
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: high
- Review gate label: strong

## 1. One-paragraph benchmark summary
- CivRealm is a Civilization-like benchmark environment built on Freeciv for decision-making agents in a long-horizon, partially observed, multi-agent strategy world. It couples full games that can last for hours or days with a procedurally generated mini-game suite spanning development, battle, and diplomacy, all under shared tensor and language APIs. The paper's strongest value for this survey is not broad cross-game openness, but its explicit stress on delayed strategic consequences, rapidly expanding state and action spaces, and the measurable gap between decomposed mini-games and the full strategic world. CivRealm is therefore best used as evidence about dynamic-space strategic reasoning under privileged but still difficult interfaces.

## 2. Position in our survey
- Why-games relevance: Civilization-like worlds compress economics, warfare, diplomacy, and technology planning into one persistent strategic environment.
- Historical stage: ecological agent benchmark
- Benchmark level(s): L2 strategic reasoning
- Most relevant outline section(s): 1,2,4
- Role in corpus: representative

## 3. Design-space coding
### 3.1 Game structure
- Information structure: imperfect
- Transition structure: stochastic
- Agent structure: multi-agent
- Social structure: mixed
- Time structure: turn-based

### 3.2 World structure
- World type(s): sandbox / open-world / other
- Real game / simulated game / designed task-game hybrid: Freeciv-based strategy world with full games plus generated mini-games
- Benchmark unit: full game / mini-game episode

### 3.3 Benchmark scope
- Scope: open-ended world
- Number of games / tasks: full game plus 10 mini-game types with 10,000 instances each

### 3.4 Modality
- Observation modality: text or symbolic
- Action modality: semantic
- Perception burden retained: partial observability, dynamic multi-object world state, and long-horizon planning over a large evolving map
- Perception burden removed: raw pixels and native control are abstracted into structured map, unit, city, government, technology, and diplomacy observations

## 4. What this benchmark measures
- Primary capability target: long-horizon strategic decision-making in a partially observed, multi-goal, dynamically expanding world
- Secondary capability target(s): dynamic state/action-space management, development and battle subskills, diplomacy-aware play, and transfer from mini-games to full games
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? yes
- Does it test social reasoning / deception / cooperation? partially; diplomacy and negotiation matter in the environment, but they are not the paper's strongest benchmark target
- Does it test visual grounding / spatial-temporal reasoning? no
- Does it test long-horizon autonomy / task completion? yes
- Does it test real-time efficiency? no
- Does it test cross-game transfer / open-ended generalization? partially; it stresses within-platform generalization across maps, players, rules, and mini-games rather than transfer across different games
- Why is a game environment especially suitable here? Civilization-like games naturally combine delayed consequences, multi-goal optimization, hidden information, diplomacy, and expanding action opportunities inside one persistent strategic world.

## 5. Interaction paradigm
- Observation channel: structured observations over map tiles, units, cities, government, technology, and diplomacy; language agents receive world summaries plus local 5x5 views, while Mastaba adds a 15x15 block-level pyramid view
- Action channel: hierarchical discrete actions over unit, city, government, technology, and diplomacy operations; some map-targeted unit actions are restricted to a 9-tile neighborhood to keep action selection tractable
- Interface type: API / structured action space / hybrid
- Agent scaffold allowed: memory / retrieval / planner
- Is there privileged API access? yes
- How close is the setup to human play? low to medium; it preserves strategic structure and turn-based pacing but removes native interface cognition and compresses large-map state into engineered summaries
- Main ecological-validity trade-off: CivRealm preserves long-range strategic and world-state complexity while abstracting away native interface burden and partially factorizing large-space reasoning through structured observations and local action constraints

## 6. Evaluation protocol
- Main score: aggregated full-game score across 16 engine dimensions plus task-specific mini-game victory criteria
- Auxiliary score(s): population, economics, production, cities, researched technologies, units, land-related stats, gold, and other engine-derived dimensions
- Evaluation style: native score / success rate / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: no human baseline; the paper evaluates tensor RL and GPT-3.5-based language agents on full games and automatically generated mini-games, with built-in Freeciv AI available as co-players or opponents in the environment
- Automatic verifiability: high
- Calibration method: automatic mini-game generation, difficulty bands, and consistent API formats across full and mini-game settings
- Anti-contamination argument: procedural variation in maps, players, and rules creates many novel situations within the platform, but contamination resistance is not a central validated claim
- Reliability or comparability concerns: the full game is extremely hard and slow, so many conclusions rely on mini-game results or qualitative full-game behavior; the language interface design also shapes how much large-space reasoning is actually exposed

## 7. Main contributions
- Contribution 1: Introduces a Civilization-like benchmark with both full games and diverse mini-games.
- Contribution 2: Provides dual tensor and language interfaces for RL and LLM agents.
- Contribution 3: Makes long-horizon, multi-goal, and dynamically expanding strategic worlds a benchmark target rather than a background property.

## 8. Main findings and failure modes
- Core empirical takeaway: current agents struggle precisely where CivRealm is most interesting: long-horizon planning and control in a dynamic large-space world. RL can solve some short-horizon mini-games, but remains myopic in full games; Mastaba improves over BaseLang, yet still falls far short of robust full-game competence.
- Notable model failure mode 1: RL favors short-term score gains such as unit production instead of slower city-building strategies that support long-term technology and economic growth
- Notable model failure mode 2: both RL and LLM agents struggle with rapidly expanding state and action spaces and with coordinating many entities over time
- Notable model failure mode 3: LLM agents suffer from limited global perspective and grounding; even Mastaba's broader map context still leaves it weak at balancing gameplay priorities and defending against pirate invasions
- Does this paper reveal a benchmark-design limitation as well? yes; it shows that miniature subgames only partially stand in for the full strategic world, and that interface compression materially shapes what "large-space reasoning" means in practice

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Support the claim that one game can bundle long-horizon, multi-goal, societally flavored decision making into a benchmarkable environment, but do not use it as primary evidence for human-like interaction.
- Best use in Section 1 (taxonomy and evolutionary levels): A representative rich Level 2 strategy-world benchmark that sits between narrow strategic probes and later broader benchmark platforms, without making it a Level 5 cross-game case.
- Best use in Section 2 (core capabilities evaluated by games): Direct evidence for long-horizon strategic planning, delayed consequences, and dynamic state/action-space growth.
- Best use in Section 3 (interaction and evaluation paradigm): Secondary contrast for privileged structured interfaces, local-versus-global observation design, and the full-game versus mini-game evaluation split.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Supports bottleneck claims about myopia, context-limited large-map reasoning, and the mismatch between decomposed subgames and full strategic competence.

## 10. Relation to nearby papers
- Closest predecessor(s): earlier Civilization/Freeciv reasoning work and StarCraft-style large-scale strategy environments
- Closest follow-up(s): later strategy-world and open-world benchmarks that separate rich environment structure from scalable evaluation through subtask generation or stronger agent scaffolds
- Best comparison targets inside our corpus: DSGBench, OpenGuanDan, PillagerBench, StarCraftIIArena
- What this paper uniquely adds relative to neighbors: It offers one of the clearest long-horizon, dynamically expanding single-world strategy benchmarks with both full games and procedurally generated mini-games under shared interfaces.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- Full games can last from several hours to several days, and the environment combines imperfect information, stochastic dynamics, multiple victory paths, changing players, and communication.
- As the game unfolds, the paper states that the state can grow from 10^15 to 10^650 and the action space from 10^4 to 10^166.
- The environment exposes structured observations over map, unit, city, government, technology, and diplomacy state; language agents use world summaries plus local 5x5 views, while Mastaba expands context through a 15x15 block pyramid.
- CivRealm defines 10 types of mini-games and generates 10,000 instances of each, with the same input/output format as the full game.
- RL performs better on mini-games with more immediate rewards but struggles on sparse delayed-reward tasks and on the full game; Mastaba outperforms BaseLang yet still shows grounding and defense weaknesses in full games.

### 11.2 Our synthesis / interpretation
- CivRealm's strongest survey use is as evidence of long-horizon strategic reasoning and dynamic-space control inside one complex world, not as a true cross-game or Level 5 generalization benchmark.
- Diplomacy and communication matter as environment features, but the paper is weaker as a primary social-intelligence source than dedicated social benchmarks.
- The benchmark is also useful because it shows that even privileged structured interfaces do not remove the difficulty of coordinating large evolving worlds over long horizons.

### 11.3 Uncertain or needs re-check
- Re-check the exact full-game aggregated-score weighting if later drafting compares CivRealm's score directly to other benchmark metrics.
- Re-check the exact contribution of rule changes versus random map or player variation if we later make a stronger generalization claim.
- Re-check prompt and retrieval details if Section 3 later needs a more exact account of how much large-space reasoning was delegated to agent scaffolding.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? Audit completed from the full paper; reread only if we later need exact score formulas, action parameterization details, or the precise BaseLang/Mastaba prompt setup.
- Which section to read next if needed: Sections 3.1 to 3.2, 5.2, and Appendix A to C
- Follow-up question(s): When drafting Section 2.2, should CivRealm be used primarily for dynamic-space long-horizon reasoning rather than for diplomacy claims?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P1
- Reading depth: deep
- Batch ID: B02
- Outline sections: 1,2,4
- Survey role: representative
- Paper card path: `paper_cards/B02/CivRealm.md`
- Check status: unchecked
- Next action: draft-section
- Last updated: 2026-04-19
