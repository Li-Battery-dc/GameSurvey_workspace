# HumanLevelDiplomacy Human-level play in the game of Diplomacy by combining language models with strategic reasoning

## 0. Metadata
- Date: 2022/11
- Venue: Science 2022
- Authors: Anton Bakhtin, Noam Brown, Emily Dinan, Gabriele Farina, Colin Flaherty, Daniel Fried, Andrew Goff, Jonathan Gray, Hengyuan Hu, Athul Paul Jacob, Mojtaba Komeili, Karthik Konath, Minae Kwon, Adam Lerer, Mike Lewis, Alexander H. Miller, Sasha Mitts, Adithya Renduchintala, Stephen Roller, Dirk Rowe, Weiyan Shi, Joe Spisak, Alexander Wei, David Wu, Hugh Zhang
- Paper link: https://doi.org/10.1126/science.ade9097
- Code link: https://github.com/facebookresearch/diplomacy_cicero
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: medium
- Review gate label: usable

## 1. One-paragraph benchmark summary
- Human-Level Diplomacy is a milestone Science paper rather than a reusable benchmark release: it presents Cicero, a Diplomacy agent that combines controllable dialogue with strategic reasoning and evaluates it in anonymous live games against human players. The paper matters for this survey because Diplomacy makes language strategically consequential: players negotiate privately, model each other's intentions, coordinate joint actions, and manage betrayal under hidden intentions and long horizons. Cicero couples a dialogue model conditioned on intents with KL-regularized planning over predicted human policies, then tests that full system in real online play. For the survey, the paper is best used as an ecological bridge for negotiation-heavy game environments and as a cautionary case on the trade-off between human-like evaluation and benchmark reusability.

## 2. Position in our survey
- Why-games relevance: Diplomacy operationalizes negotiation, trust, coalition formation, and tactical planning inside a formally scored game where language changes the game state indirectly through coordination.
- Historical stage: ecological agent benchmark
- Benchmark level(s): L2 strategic reasoning / L3 social intelligence
- Most relevant outline section(s): 0,1,2,3
- Role in corpus: anchor

## 3. Design-space coding
### 3.1 Game structure
- Information structure: imperfect
- Transition structure: deterministic
- Agent structure: multi-agent
- Social structure: mixed
- Time structure: turn-based

### 3.2 Environment structure
- Environment type(s): tabletop / social interaction arena
- Real game / simulated game / designed task-game hybrid: real board game played online with live human negotiation
- Benchmark unit: full game / league performance

### 3.3 Benchmark scope
- Scope: single game
- Number of games / tasks: 40 anonymous league games, plus an 8-game tournament slice discussed in the paper

### 3.4 Modality
- Observation modality: text or symbolic
- Action modality: semantic
- Perception burden retained: negotiation dialogue, structured board-state reasoning, alliance and intention modeling, and long-horizon strategic coordination
- Perception burden removed: no raw visual perception or native physical interface

## 4. What this benchmark measures
- Primary capability target: negotiation-grounded strategic play with humans
- Secondary capability target(s): belief and intention modeling, coalition management, tactical coordination, and language-conditioned planning
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? yes
- Does it test social reasoning / deception / cooperation? yes
- Does it test visual grounding / spatial-temporal reasoning? no
- Does it test long-horizon autonomy / task completion? yes
- Does it test real-time efficiency? partially; decisions and negotiation occur under short timed turns
- Does it test cross-game transfer / open-ended generalization? no
- Why is a game environment especially suitable here? Diplomacy turns open-ended language into strategically consequential action, so coordination, persuasion, and mistrust become measurable parts of success rather than side tasks.

## 5. Interaction paradigm
- Observation channel: structured board state, recent action history, and private pairwise dialogue histories
- Action channel: natural-language negotiation messages plus simultaneous Diplomacy orders
- Interface type: natural language / structured action space / hybrid
- Agent scaffold allowed: planner / language model / other
- Is there privileged API access? yes; Cicero uses structured board-state access, dialogue-conditioned policy prediction, RL value models, and message filters rather than a raw human-only interface
- How close is the setup to human play? medium; the opponent pool and game objective are highly ecological, but the system itself is a heavily engineered language-plus-planning stack
- Main ecological-validity trade-off: the evaluation is unusually close to real human play, but the system and protocol are difficult to reuse as a standardized benchmark or to compare directly with lighter LLM-agent setups

## 6. Evaluation protocol
- Main score: mean game score and league ranking in anonymous human play
- Auxiliary score(s): tournament placement, dialogue-quality ratings on 126 validation situations, and message-filter evaluations
- Evaluation style: tournament / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: Cicero is entered anonymously into an online human league, where its 40 games involve 82 distinct human opponents; separate expert annotation is used to evaluate dialogue quality
- Automatic verifiability: mixed
- Calibration method: anonymous live league participation, a tournament slice, KL-regularization toward human play, and expert-evaluated dialogue consistency metrics
- Anti-contamination argument: not central
- Reliability or comparability concerns: the paper evaluates one heavily engineered system in live human play, so scores are not directly comparable with later standardized benchmark suites; exact reproduction also depends on supplementary-method details not fully present in the short Science article

## 7. Main contributions
- Contribution 1: Demonstrates human-level play in full-press Diplomacy with a system that combines dialogue and strategic planning.
- Contribution 2: Introduces intent-controlled dialogue grounded in game state and planning outputs rather than free-form imitation alone.
- Contribution 3: Uses KL-regularized, human-compatible planning and evaluates the full system anonymously against humans in live online play.

## 8. Main findings and failure modes
- Core empirical takeaway: in 40 anonymous webDiplomacy league games, Cicero achieved a mean score of 25.8%, more than double the 12.4% average of its human opponents, ranked in the top 10% of participants who played more than one game, and placed first in the paper's 8-game tournament slice.
- Notable model failure mode 1: even with filters, generated messages can still contain grounding errors, contradict plans, or be strategically poor
- Notable model failure mode 2: Cicero reasons about dialogue mainly through current-turn actions rather than modeling longer-term relationship effects across the game
- Notable model failure mode 3: the intent representation limits richer dialogue acts such as asking questions, strategically revealing information, or explaining decisions
- Does this paper reveal a benchmark-design limitation as well? yes; it is a strong ecological demonstration, but its live-human protocol and engineered stack make it much harder to reuse as a standardized benchmark than later corpus papers

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Strong milestone evidence that games can operationalize social strategy and negotiation in ways static language tasks cannot.
- Best use in Section 1 (taxonomy and evolutionary levels): Historical bridge from rule- and strategy-focused game AI toward social, language-mediated, human-in-the-loop evaluation.
- Best use in Section 2 (core capabilities evaluated by games): Direct support for negotiation, intention modeling, trust management, and strategic communication under hidden intentions.
- Best use in Section 3 (interaction and evaluation paradigm): Important example of a hybrid language-plus-planner system evaluated in anonymous human play. Useful for the ecological-validity versus comparability trade-off.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Use as a cautionary milestone showing that impressive ecological performance can coexist with limited benchmark reusability and strong dependence on engineered scaffolds.

## 10. Relation to nearby papers
- Closest predecessor(s): no-press Diplomacy systems, earlier negotiation agents, and human-regularized Diplomacy planning work
- Closest follow-up(s): later social-intelligence and live-interaction benchmarks for LLM agents
- Best comparison targets inside our corpus: CollabOvercooked, LLMCoordination, WerewolfArena, AvalonBench
- What this paper uniquely adds relative to neighbors: It is the clearest corpus example where natural-language negotiation with humans is central to game performance rather than an auxiliary analysis layer

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- Cicero combines a dialogue module with a strategic reasoning module; the dialogue model is grounded in dialogue history, game state, and intents representing planned actions for the speaker and recipient.
- The paper states that WebDiplomacy data includes 125,261 games, of which 40,408 contain dialogue, totaling 12,901,662 messages used for training components of the system.
- In anonymous human play, Cicero played 40 games between 19 August and 13 October 2022, sent 5,277 messages over 72 hours, achieved a mean score of 25.8% against 82 distinct opponents averaging 12.4%, and ranked second out of 19 participants who played at least five games.
- On 126 expert-annotated dialogue situations, the intent-grounded dialogue model improves consistency-with-state, consistency-with-plan, and high-quality message ratings over weaker grounding baselines.

### 11.2 Our synthesis / interpretation
- The safest survey use is as a reviewed ecological milestone and negotiation bridge, not as a reusable benchmark protocol on the same footing as later standardized suites.
- This paper is especially important because its result depends on coupling language with planning and human-compatible regularization; fluent dialogue alone is not the source of performance.

### 11.3 Uncertain or needs re-check
- Reopen the supplementary materials if later drafting needs the exact filter ensemble, full piKL or CoShar-piKL derivations, or the complete tournament-account protocol.
- Avoid writing as though this paper provides a public, directly reusable benchmark with clean cross-paper comparability; its strongest contribution is milestone evidence, not standardization.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? Full paper read completed for this audit. Reopen the supplementary materials only if later drafting needs full algorithmic detail, filter design, or exact league-protocol specifics.
- Which section to read next if needed: Methods / Discussion / supplementary materials
- Follow-up question(s): When drafting, use this paper for negotiation, ecological evaluation, and language-plus-planning arguments rather than for apples-to-apples benchmark score comparison.

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P0
- Reading depth: deep
- Batch ID: B03
- Outline sections: 0,1,2,3
- Survey role: anchor
- Paper card path: `paper_cards/B03/HumanLevelDiplomacy.md`
- Check status: unchecked
- Next action: draft-section
- Last updated: 2026-04-10
