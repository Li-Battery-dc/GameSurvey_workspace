# BoardGameArena Board Game Arena: A Framework and Benchmark for Assessing Large Language Models via Strategic Play

## 0. Metadata
- Date: 2025/08
- Venue: arXiv
- Authors: Lucia Cipolina-Kun, Marianna Nezhurina, Jenia Jitsev
- Paper link: https://arxiv.org/pdf/2508.03368v1
- Code link:
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: medium
- Review gate label: usable

## 1. One-paragraph benchmark summary
- Board Game Arena is a framework paper that wraps OpenSpiel board and matrix games into a unified environment for evaluating LLM agents through strategic play. The framework formats game state, legal actions, and sometimes move history into prompts; agents return both an action and a reasoning trace. The paper emphasizes reusable infrastructure, distributed execution, and reasoning-trace analysis rather than a single definitive leaderboard. In this survey, it is most useful as a representative of OpenSpiel-based text interfaces and process-level analysis for board-game play.

## 2. Position in our survey
- Why-games relevance: It shows how classic strategic games can be repackaged into scalable LLM-agent evaluations with logged reasoning traces.
- Historical stage: diagnostic capability probe
- Narrative level(s): L1 rule following / L2 strategic reasoning
- Most relevant outline section(s): 1,2,3,5
- Role in corpus: representative

## 3. Design-space coding
### 3.1 Environment structure
- Information structure: mixed
- Transition structure: mixed
- Agent structure: multi-agent
- Social structure: competitive
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
- Does it test social reasoning / deception / cooperation? partially, in games such as Kuhn Poker
- Does it test visual grounding / spatial-temporal reasoning? no
- Does it test long-horizon autonomy / task completion? partially
- Does it test real-time efficiency? no
- Does it test cross-game transfer / open-ended generalization? partially
- Why is a game environment especially suitable here? Board and matrix games give precise payoffs and legal actions while still exposing different strategic reasoning styles.

## 5. Interaction paradigm
- Observation channel: prompt built from OpenSpiel state, legal moves, and optional history
- Action channel: chosen action plus free-text rationale
- Interface type: natural language / structured action space
- Agent scaffold allowed: none
- Is there privileged API access? yes
- How close is the setup to human play? low to medium; the benchmark keeps strategic structure but replaces ordinary play surfaces with text prompts
- Main ecological-validity trade-off: The framework gains scalability and interpretability by textifying state and logging rationale, but loses human-like interaction fidelity.

## 6. Evaluation protocol
- Main score: cumulative reward or outcome depending on the game
- Auxiliary score(s): decision optimality, reasoning length/coherence, illegal or suboptimal move rates
- Evaluation style: hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: supports random, human, RL, and LLM agent comparisons
- Automatic verifiability: high
- Calibration method: repeated simulations with fixed seeds, paired tests, and bootstrap confidence intervals
- Anti-contamination argument: not central
- Reliability or comparability concerns: empirical coverage in the paper is lighter than the framework scope, and reasoning-trace heuristics are only approximate

## 7. Main contributions
- Contribution 1: Wraps OpenSpiel games in a Gymnasium-like LLM-agent interface.
- Contribution 2: Logs both actions and reasoning traces for later analysis.
- Contribution 3: Adds analysis tools for categorizing strategy explanations and spotting hallucinations or rule violations.

## 8. Main findings and failure modes
- Core empirical takeaway: The framework can expose distinct reasoning styles across games, not just end scores, and reveals that models shift between blocking, positional, and winning-logic patterns depending on the game.
- Notable model failure mode 1: illegal or clearly suboptimal move generation
- Notable model failure mode 2: shallow heuristic rationales disconnected from actual strategy
- Notable model failure mode 3: game-dependent reasoning categories that do not transfer cleanly across settings
- Does this paper reveal a benchmark-design limitation as well? yes; the paper is stronger on framework design than on a large decisive empirical comparison

## 9. Why this paper matters for our survey
- Best use in Section 0 (why games): Demonstrates how games support process-level inspection of reasoning traces.
- Best use in Section 1 (historical evolution): Helps show the move from isolated benchmark scripts to reusable benchmark infrastructure.
- Best use in Section 2 (design space): Useful game-family benchmark with mixed world structures inside one framework.
- Best use in Section 3 (capability targets): Supports strategic reasoning and game-theoretic decision making claims.
- Best use in Section 4 (interaction paradigm): Good illustration of OpenSpiel-state-to-prompt wrappers.
- Best use in Section 5 (evaluation protocol): Relevant for reasoning-trace analysis and optimality-oriented metrics.
- Best use in Section 6/7 (limitations and future): Supports discussion of why rationale logging is useful but imperfect.

## 10. Relation to nearby papers
- Closest predecessor(s): OpenSpiel-based LLM game wrappers and earlier board-game prompting setups
- Closest follow-up(s): BotzoneBench, WhoIsABetterPlayer
- Best comparison targets inside our corpus: SmartPlay, BotzoneBench, WhoIsABetterPlayer, CATArena
- What this paper uniquely adds relative to neighbors: It foregrounds reusable infrastructure and reasoning-trace analysis rather than only ranking models.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- The framework wraps OpenSpiel games, converts state and legal moves into prompts, and asks agents to return both an action and a rationale.
- It records per-step rewards, outcomes, decision optimality, rationale features, and illegal/suboptimal move rates.
- The paper includes tooling for categorizing reasoning traces and flagging hallucinations or rule violations.

### 11.2 Our synthesis / interpretation
- Board Game Arena is most useful as infrastructure evidence for Sections 4 and 5, not as the central empirical anchor for strategic-play results.
- It complements BotzoneBench by trading calibration strength for framework flexibility and richer rationale logging.

### 11.3 Uncertain or needs re-check
- Recheck the experimental section if we later need the exact set of evaluated games rather than the showcased examples.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? No immediate reread; the framework contribution is already clear enough.
- Which section to read next if needed: 2 / 5 / 5.3
- Follow-up question(s): Which reasoning-trace categories are robust enough to reuse in the survey taxonomy?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P1
- Reading depth: deep
- Batch ID: B01
- Outline sections: 1,2,3,5
- Survey role: representative
- Paper card path: `paper_cards/B01/BoardGameArena.md`
- Next action: draft-section
- Last updated: 2026-04-05
