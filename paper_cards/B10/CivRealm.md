# CivRealm CivRealm: A Learning and Reasoning Odyssey in Civilization for Decision-Making Agents

## 0. Metadata
- Date: 2024/01
- Venue: ICLR 2025
- Authors: Siyuan Qi, Shuo Chen, Yexin Li, Xiangyu Kong, Junqi Wang, Bangcheng Yang, Pring Wong, Yifan Zhong, Xiaoyuan Zhang, Zhaowei Zhang, Nian Liu, Wei Wang, Yaodong Yang, Song-Chun Zhu
- Paper link: https://arxiv.org/pdf/2401.10568v2.pdf
- Code link: https://github.com/bigai-ai/civrealm
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: high
- Review gate label: strong

## 1. One-paragraph benchmark summary
- CivRealm is a Civilization-like decision-making environment built on Freeciv that targets learning and reasoning in long-horizon, multi-agent strategy play. It supports both full games that can last for hours or days and a large family of automatically generated mini-games spanning development, battle, and diplomacy. The environment offers both tensor and language APIs, explicitly foregrounding imperfect information, stochasticity, multi-goal planning, diplomacy, communication, and changing action spaces. For this survey, CivRealm is a strong benchmark platform for long-horizon strategic worlds that sit between specialist board games and broader open-ended world benchmarks.

## 2. Position in our survey
- Why-games relevance: Civilization-like worlds compress economics, warfare, diplomacy, and technology planning into one persistent strategic environment.
- Historical stage: open-ended general-game benchmark
- Narrative level(s): L2 strategic reasoning / L3 social intelligence
- Most relevant outline section(s): 1,2,4
- Role in corpus: representative

## 3. Design-space coding
### 3.1 Environment structure
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
- Benchmark intent: open-ended evaluation / train+eval foundation

### 3.4 Modality
- Primary modality: symbolic state / text
- Perception burden retained: partial observability, relational world state, and long-horizon planning
- Perception burden removed: raw pixels are abstracted into structured map, unit, city, government, technology, and diplomacy observations

## 4. What this benchmark measures
- Primary capability target: long-horizon strategic decision-making in a partially observed multi-goal world
- Secondary capability target(s): diplomacy, tactical battle control, development planning, and transfer from mini-games to full games
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? yes
- Does it test social reasoning / deception / cooperation? yes
- Does it test visual grounding / spatial-temporal reasoning? no
- Does it test long-horizon autonomy / task completion? yes
- Does it test real-time efficiency? no
- Does it test cross-game transfer / open-ended generalization? yes for within-platform generalization to novel maps, rules, and mini-games, but not for cross-title transfer
- Why is a game environment especially suitable here? Civilization-like games naturally combine multiple strategic objectives, hidden information, and long-range consequences in a single formal world.

## 5. Interaction paradigm
- Observation channel: structured information about map tiles, units, cities, government, technology, and diplomacy
- Action channel: rich discrete actions over unit, city, government, technology, and diplomacy operations
- Interface type: API / hybrid
- Agent scaffold allowed: other; the platform provides tensor and language APIs, and the language baselines in the paper use AutoGPT-like decomposition rather than pure direct play
- Is there privileged API access? yes
- How close is the setup to human play? medium-low; it captures strategic structure well but abstracts away the original GUI
- Main ecological-validity trade-off: CivRealm preserves deep strategic structure while sacrificing native-interface cognition and almost all human-like interaction friction

## 6. Evaluation protocol
- Main score: aggregated game score plus task-specific mini-game victory criteria
- Auxiliary score(s): population, cities, technologies, units, explored land, and other engine-derived dimensions
- Evaluation style: native score / win rate / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: RL and LLM-based agents are tested on both full games and automatically generated mini-games, including built-in AI opponents
- Automatic verifiability: high
- Calibration method: automatic mini-game generation, difficulty bands, and consistent API formats across full and mini-game settings
- Anti-contamination argument: procedural variation in maps, players, and rules creates many novel situations
- Reliability or comparability concerns: the full game is extremely hard and slow, so conclusions often rely heavily on mini-game performance rather than full-game mastery

## 7. Main contributions
- Contribution 1: Introduces a Civilization-like benchmark with both full games and diverse mini-games.
- Contribution 2: Provides dual tensor and language interfaces for RL and LLM agents.
- Contribution 3: Emphasizes open-ended strategic features such as imperfect information, diplomacy, and dynamic action spaces.

## 8. Main findings and failure modes
- Core empirical takeaway: both RL and LLM agents remain far from strong full-game play, even when some mini-game competence is achievable.
- Notable model failure mode 1: myopic strategies that optimize short-term gains over long-term civilization growth
- Notable model failure mode 2: weak handling of dynamic, expanding state and action spaces
- Notable model failure mode 3: poor diplomatic and multi-goal reasoning in the full game
- Does this paper reveal a benchmark-design limitation as well? yes; it shows that miniature subgames are valuable but can only partially stand in for the full strategic world

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Strong evidence that strategy games can bundle many real-world decision dimensions into one environment.
- Best use in Section 1 (taxonomy and evolutionary levels): A key waypoint in the move from narrow games toward broader decision worlds. Helps define open-ended, multi-goal strategy worlds without claiming human-like interface fidelity.
- Best use in Section 2 (core capabilities evaluated by games): Useful for planning, diplomacy, uncertainty, and transfer discussions.
- Best use in Section 3 (interaction and evaluation paradigm): A clear example of language/API access to a deep strategy environment. Good reference for combining full-game and mini-game evaluation.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Supports the need for benchmarks that test strategic breadth without collapsing into overly narrow tasks.

## 10. Relation to nearby papers
- Closest predecessor(s): StarCraft-style strategy environments and earlier Civilization or Diplomacy-inspired decision-making work
- Closest follow-up(s): later benchmark platforms that combine broad strategic worlds with more explicit agent-facing interfaces
- Best comparison targets inside our corpus: DSGBench, OpenGuanDan, HumanLevelDiplomacy, StarDojo
- What this paper uniquely adds relative to neighbors: It offers one of the clearest long-horizon strategic worlds with both diplomacy and automatically generated curriculum-like mini-games under one platform.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- CivRealm supports full Freeciv games plus 10 types of mini-games with 10,000 instances each.
- The environment exposes observations over map, unit, city, government, technology, and diplomacy state.
- It provides both tensor and language APIs and reports that full-game progress remains difficult for both RL and LLM methods.

### 11.2 Our synthesis / interpretation
- CivRealm is a strong representative of open-ended strategic-world benchmarks rather than a narrow single-game probe.
- It is especially valuable for contrasting full-world evaluation against decomposed diagnostic mini-games.
- It is better used as a strategic-world generalization platform than as evidence of ecological or human-like play.

### 11.3 Uncertain or needs re-check
- Re-check the exact mini-game taxonomy and reward definitions if we later need a formal comparison table.
- Re-check the strongest reported language-agent baseline numbers for full game versus mini-games.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? Audit completed from the full paper; reread only if we later need exact full-game score dimensions or the detailed BaseLang/Mastaba setup.
- Which section to read next if needed: Sections 3.1 to 3.2 and Appendix A.1 to A.2
- Follow-up question(s): Which mini-games transfer best to full-game competence, and how much of the difficulty comes from diplomacy versus dynamic action growth?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P1
- Reading depth: deep
- Batch ID: B10
- Outline sections: 1,2,4
- Survey role: representative
- Paper card path: `paper_cards/B10/CivRealm.md`
- Check status: unchecked
- Next action: draft-section
- Last updated: 2026-04-09
