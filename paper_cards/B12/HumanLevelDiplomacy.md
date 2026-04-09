# HumanLevelDiplomacy Human-level play in the game of Diplomacy by combining language models with strategic reasoning

## 0. Metadata
- Date: 2022/11
- Venue: Science 2022
- Authors: Anton Bakhtin, Noam Brown, Emily Dinan, Gabriele Farina, Colin Flaherty, Daniel Fried, Andrew Goff, Jonathan Gray, Hengyuan Hu, Athul Paul Jacob, Mojtaba Komeili, Karthik Konath, Minae Kwon, Adam Lerer, Mike Lewis, Alexander H. Miller, Sasha Mitts, Adithya Renduchintala, Stephen Roller, Dirk Rowe, Weiyan Shi, Joe Spisak, Alexander Wei, David Wu, Hugh Zhang
- Paper link: https://doi.org/10.1126/science.ade9097
- Code link: https://github.com/facebookresearch/diplomacy_cicero
- Reading depth: structured-skim
- Card status: card-reviewed
- Confidence in this card: medium
- Review gate label: usable

## 1. One-paragraph benchmark summary
- This paper presents Cicero, an AI system that achieved human-level performance in the negotiation strategy game Diplomacy by combining language modeling with strategic planning and reinforcement-learning components. Strictly speaking, it is not a benchmark paper in the same sense as the other items in this batch; its core contribution is a high-impact capability demonstration in a socially rich game environment. However, it matters greatly for this survey because Diplomacy is one of the strongest known settings where natural-language negotiation, hidden intentions, alliance formation, and tactical planning are all required together. For historical framing, this paper is a major bridge between formal game evaluation and later benchmark work on negotiation and multi-agent social intelligence.

## 2. Position in our survey
- Why-games relevance: Diplomacy combines negotiation, hidden intentions, coalition management, and long-horizon strategic planning inside a fully game-structured environment.
- Historical stage: ecological agent benchmark
- Narrative level(s): L2 strategic reasoning / L3 social intelligence
- Most relevant outline section(s): 0,1,2,3,4
- Role in corpus: anchor

## 3. Design-space coding
### 3.1 Environment structure
- Information structure: imperfect
- Transition structure: mixed
- Agent structure: multi-agent
- Social structure: mixed
- Time structure: turn-based

### 3.2 World structure
- World type(s): board / social strategy
- Real game / simulated game / designed task-game hybrid: real game with live human play
- Benchmark unit: full game / league performance

### 3.3 Benchmark scope
- Scope: single game
- Number of games / tasks: 40 games in an anonymous online Diplomacy league
- Benchmark intent: ecological evaluation

### 3.4 Modality
- Primary modality: text / symbolic state
- Perception burden retained: negotiation dialogue, board-state planning, belief and intent inference, and long-horizon coordination
- Perception burden removed: no raw visual perception burden

## 4. What this benchmark measures
- Primary capability target: social strategic competence under natural-language negotiation
- Secondary capability target(s): belief modeling, tactical planning, coalition management, and language-conditioned decision making
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? yes
- Does it test social reasoning / deception / cooperation? yes
- Does it test visual grounding / spatial-temporal reasoning? partially
- Does it test long-horizon autonomy / task completion? yes
- Does it test real-time efficiency? no
- Does it test cross-game transfer / open-ended generalization? no
- Why is a game environment especially suitable here? Diplomacy uniquely combines explicit rules with open-ended negotiation, so it makes strategic language use operational rather than decorative.

## 5. Interaction paradigm
- Observation channel: game state, dialogue history, and strategic context
- Action channel: natural-language negotiation plus game orders
- Interface type: natural language / structured action space / hybrid
- Agent scaffold allowed: planner / other
- Is there privileged API access? yes through the full Cicero system stack
- How close is the setup to human play? high in terms of game structure and human opponents, but the agent itself uses a heavily engineered planning stack
- Main ecological-validity trade-off: the evaluation is highly ecological, but the system is not a pure backbone-model benchmark and is difficult to compare directly to lighter-weight LLM evaluations

## 6. Evaluation protocol
- Main score: online league performance in human games
- Auxiliary score(s): average-score advantage over humans and league ranking
- Evaluation style: tournament / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: Cicero is evaluated in an anonymous online league against human players
- Automatic verifiability: mixed
- Calibration method: live league participation across 40 games
- Anti-contamination argument: not central
- Reliability or comparability concerns: this is not a standardized public benchmark protocol, and reproducibility depends on live human play plus a complex engineered system

## 7. Main contributions
- Contribution 1: Demonstrates human-level play in Diplomacy with a language-plus-planning system.
- Contribution 2: Integrates language modeling with strategic reasoning and belief inference inside a negotiation game.
- Contribution 3: Provides a high-impact milestone for socially situated game-agent competence.

## 8. Main findings and failure modes
- Core empirical takeaway: Cicero achieved more than double the average score of human players and ranked in the top 10 percent of league participants who played more than one game.
- Notable model failure mode 1: raw language modeling alone is not sufficient; the paper relies on a specialized strategic stack rather than a plain LLM agent
- Notable model failure mode 2: comparison to later lightweight benchmark agents is difficult because evaluation depends on one heavily engineered system
- Notable model failure mode 3: the work is less reusable as a benchmark protocol than as a historical milestone
- Does this paper reveal a benchmark-design limitation as well? yes; it highlights the gap between impressive game performance and easily reusable benchmark methodology

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Strongest high-level example that games can operationalize language-based social strategy in a way static NLP tasks cannot.
- Best use in Section 1 (taxonomy and evolutionary levels): Essential historical bridge from capability demonstrations to later negotiation and cooperation benchmarks. Useful for mixed cooperative-competitive games with both language and tactical planning.
- Best use in Section 2 (core capabilities evaluated by games): Direct support for negotiation, belief modeling, and long-horizon social strategy.
- Best use in Section 3 (interaction and evaluation paradigm): Important example of a hybrid language-plus-planner game agent. Good contrast case for live human-league evaluation rather than fixed benchmark suites.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Supports the claim that high ecological validity often comes with low comparability and heavy system engineering.

## 10. Relation to nearby papers
- Closest predecessor(s): prior Diplomacy AI and negotiation systems
- Closest follow-up(s): negotiation and cooperation benchmarks for LLM agents
- Best comparison targets inside our corpus: CollabOvercooked, LLMCoordination, StrategicHanabi, GTBench
- What this paper uniquely adds relative to neighbors: It is the clearest high-profile milestone where natural-language strategic interaction with humans was central to performance.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- The abstract states that Cicero is the first AI agent to achieve human-level performance in Diplomacy by combining a language model with planning and reinforcement-learning algorithms.
- Across 40 games in an anonymous online Diplomacy league, Cicero achieved more than double the average score of human players and ranked in the top 10 percent of participants who played more than one game.
- The abstract emphasizes that the system infers players' beliefs and intentions from conversations and generates dialogue in pursuit of its plans.

### 11.2 Our synthesis / interpretation
- This is a historically essential survey card even though it is not a benchmark paper in the strict repository sense.
- Its value is mostly as a milestone proving that negotiation-heavy game environments are a serious testbed for language agents.

### 11.3 Uncertain or needs re-check
- Re-check the full Science paper or supplementary materials if we later need exact league setup, ablations, or failure analysis beyond the abstract-level milestone claim.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? Yes, if we decide to use Cicero as a central historical bridge rather than only a milestone citation.
- Which section to read next if needed: method / evaluation / supplementary materials
- Follow-up question(s): How should this paper be framed so that it informs the survey without being mistaken for a standardized benchmark release?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P0
- Reading depth: structured-skim
- Batch ID: B12
- Outline sections: 0,1,2,3,4
- Survey role: anchor
- Paper card path: `paper_cards/B12/HumanLevelDiplomacy.md`
- Next action: draft-section
- Last updated: 2026-04-08
