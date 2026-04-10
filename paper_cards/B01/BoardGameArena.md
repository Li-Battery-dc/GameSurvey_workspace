# BoardGameArena Game Reasoning Arena: A Framework and Benchmark for Assessing Reasoning Capabilities of Large Language Models via Game Play

## 0. Metadata
- Date: 2025/08
- Venue: arXiv
- Authors: Lucia Cipolina-Kun, Marianna Nezhurina, Jenia Jitsev
- Paper link: https://arxiv.org/pdf/2508.03368v3
- Code link: https://github.com/SLAMPAI/game_reasoning_arena
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: medium
- Review gate label: usable

## 1. One-paragraph benchmark summary
- Game Reasoning Arena is a framework paper that wraps OpenSpiel board and matrix games into a unified environment for evaluating LLM agents through strategic play. The framework formats game state, legal actions, and sometimes move history into prompts; agents return both an action and a reasoning trace under a structured output schema. The current paper version emphasizes reusable infrastructure, distributed execution, prompt architecture, and richer reasoning-profile analysis across games rather than a single definitive leaderboard. In this survey, it is most useful as a representative of OpenSpiel-based text interfaces and process-level analysis for board-game play.

## 2. Position in our survey
- Why-games relevance: It shows how classic strategic games can be repackaged into scalable LLM-agent evaluations with logged reasoning traces.
- Historical stage: diagnostic capability probe
- Narrative level(s): L1 rule following / L2 strategic reasoning
- Most relevant outline section(s): 1,2,3
- Role in corpus: representative

## 3. Design-space coding
### 3.1 Environment structure
- Information structure: mixed
- Transition structure: mixed
- Agent structure: multi-agent
- Social structure: mixed
- Time structure: turn-based / hybrid

### 3.2 World structure
- World type(s): board / card / other
- Real game / simulated game / designed task-game hybrid: real game family wrapped through OpenSpiel
- Benchmark unit: turn or full match

### 3.3 Benchmark scope
- Scope: game family
- Number of games / tasks: multiple OpenSpiel games; examples include Connect Four, Kuhn Poker, and Tic-Tac-Toe
- Benchmark intent: diagnostic evaluation

### 3.4 Modality
- Primary modality: text
- Perception burden retained: strategic state reading, legal-action choice, optional short move history, reasoning-trace generation
- Perception burden removed: raw boards and direct GUI play

## 4. What this benchmark measures
- Primary capability target: strategic decision making plus interpretable reasoning traces
- Secondary capability target(s): equilibrium-aware play, error avoidance, opponent-aware reasoning patterns
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? yes
- Does it test social reasoning / deception / cooperation? partially, through bluffing in Kuhn Poker and cooperation trade-offs in iterated Prisoner's Dilemma
- Does it test visual grounding / spatial-temporal reasoning? no
- Does it test long-horizon autonomy / task completion? partially
- Does it test real-time efficiency? no
- Does it test cross-game transfer / open-ended generalization? partially
- Why is a game environment especially suitable here? Board and matrix games give precise payoffs and legal actions while still exposing different strategic reasoning styles.

## 5. Interaction paradigm
- Observation channel: prompt built from OpenSpiel state, legal moves, and optional history
- Action channel: chosen action plus free-text rationale
- Interface type: natural language / structured action space
- Agent scaffold allowed: other (reasoning directive plus structured JSON-style output schema)
- Is there privileged API access? yes
- How close is the setup to human play? low to medium; the benchmark keeps strategic structure but replaces ordinary play surfaces with text prompts
- Main ecological-validity trade-off: The framework gains scalability and interpretability by textifying state, exposing legal actions, and imposing structured outputs, but loses human-like interaction fidelity.

## 6. Evaluation protocol
- Main score: cumulative reward or outcome depending on the game
- Auxiliary score(s): decision optimality, reasoning length/coherence, illegal or suboptimal move rates, and reasoning-profile distributions
- Evaluation style: hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: the framework supports random, heuristic, RL, human, and LLM agent comparisons; the paper itself emphasizes multi-agent comparative runs and reasoning-profile analysis
- Automatic verifiability: high
- Calibration method: repeated simulations with fixed seeds, paired tests, and bootstrap confidence intervals
- Anti-contamination argument: not central
- Reliability or comparability concerns: empirical coverage in the paper is lighter than the framework scope, and reasoning-trace heuristics are only approximate

## 7. Main contributions
- Contribution 1: Wraps OpenSpiel games in a Gymnasium-like LLM-agent interface.
- Contribution 2: Logs both actions and reasoning traces for later analysis.
- Contribution 3: Adds analysis tools for categorizing strategy explanations, tracking reasoning-profile changes across games, and spotting hallucinations or rule violations.

## 8. Main findings and failure modes
- Core empirical takeaway: The current paper version shows that reasoning profiles vary both by game and by agent, so the framework is informative not just about end scores but about how strategic style shifts across settings.
- Notable model failure mode 1: illegal or clearly suboptimal move generation remains a tracked error mode
- Notable model failure mode 2: some agents collapse into narrow reasoning styles tied to a specific game structure
- Notable model failure mode 3: strategic explanations can look coherent while still depending on shallow keyword-detectable heuristics
- Does this paper reveal a benchmark-design limitation as well? yes; the paper is stronger on framework design than on a large decisive empirical comparison

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Demonstrates how games support process-level inspection of reasoning traces.
- Best use in Section 1 (taxonomy and evolutionary levels): Helps show the move from isolated benchmark scripts to reusable benchmark infrastructure. Useful game-family benchmark with mixed world structures inside one framework.
- Best use in Section 2 (core capabilities evaluated by games): Supports strategic reasoning and game-theoretic decision making claims.
- Best use in Section 3 (interaction and evaluation paradigm): Good illustration of OpenSpiel-state-to-prompt wrappers, structured reasoning directives, and JSON-style output constraints. Relevant for reasoning-trace analysis and optimality-oriented metrics.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Supports discussion of why rationale logging is useful but imperfect.

## 10. Relation to nearby papers
- Closest predecessor(s): OpenSpiel-based LLM game wrappers and earlier board-game prompting setups
- Closest follow-up(s): BotzoneBench, WhoIsABetterPlayer
- Best comparison targets inside our corpus: BotzoneBench, SmartPlay, GTBench, LLMChess
- What this paper uniquely adds relative to neighbors: It foregrounds reusable infrastructure and reasoning-trace analysis rather than only ranking models.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- The framework wraps OpenSpiel games, converts state and legal moves into prompts, and asks agents to return both an action and a rationale.
- Prompts are augmented with a reasoning directive and a structured schema specifying `reasoning` and `action` fields.
- It records per-step rewards, outcomes, decision optimality, rationale features, and illegal or suboptimal move rates, and reports statistical comparisons with paired tests and bootstrap confidence intervals.
- The current paper version includes tooling for categorizing reasoning traces, tracking cross-game reasoning profiles, and flagging hallucinations or rule violations.

### 11.2 Our synthesis / interpretation
- Board Game Arena is most useful as infrastructure evidence for Section 3, not as the central empirical anchor for strategic-play results.
- It complements BotzoneBench by trading calibration strength for framework flexibility and richer rationale logging.

### 11.3 Uncertain or needs re-check
- Recheck the experimental section if we later need the exact model roster or the full reasoning-taxonomy definitions used in the latest arXiv version.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? Completed in this audit; the framework design, prompt architecture, evaluation statistics, and latest reasoning-profile analyses are now clear enough for survey use.
- Which section to read next if needed: 2 / 5 / 5.3
- Follow-up question(s): Which reasoning-trace categories are robust enough to reuse in the survey taxonomy?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P1
- Reading depth: deep
- Batch ID: B01
- Outline sections: 1,2,3
- Survey role: representative
- Paper card path: `paper_cards/B01/BoardGameArena.md`
- Check status: unchecked
- Next action: draft-section
- Last updated: 2026-04-10
