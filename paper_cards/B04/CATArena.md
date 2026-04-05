# CATArena CATArena: Evaluation of LLM Agents through Iterative Tournament Competitions

## 0. Metadata
- Date: 2025/10
- Venue: arXiv
- Authors: Lingyue Fu, Xin Ding, Yaoming Zhu, Shao Zhang, Lin Qiu, Weiwen Liu, Weinan Zhang, Xuezhi Cao, Xunliang Cai, Jiaxin Ding, Yong Yu
- Paper link: https://arxiv.org/pdf/2510.26852v1
- Code link:
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: medium
- Review gate label: usable

## 1. One-paragraph benchmark summary
- CATArena is less a direct gameplay benchmark and more an iterative competitive framework for evaluating code agents that write and refine game strategies. Agents receive game code and sample implementations, compete in tournaments, inspect peers’ code and logs, then iterate across rounds. The framework covers four open-ended board and card games with rule variants and computes metrics from a cross-round scoring matrix. In this survey, the paper matters mainly as a tournament-based measure of strategy coding and peer learning rather than of raw interactive game play.

## 2. Position in our survey
- Why-games relevance: It uses open-ended games to keep evaluation unsaturated and to expose whether agents can improve strategies through repeated competition.
- Historical stage: diagnostic capability probe
- Narrative level(s): L2 strategic reasoning
- Most relevant outline section(s): 2,3,5
- Role in corpus: contrast

## 3. Design-space coding
### 3.1 Environment structure
- Information structure: mixed
- Transition structure: mixed
- Agent structure: multi-agent
- Social structure: mixed
- Time structure: turn-based

### 3.2 World structure
- World type(s): board / card
- Real game / simulated game / designed task-game hybrid: real games and designed variants used in a code-agent tournament
- Benchmark unit: tournament round

### 3.3 Benchmark scope
- Scope: game family
- Number of games / tasks: 4 games with variants
- Benchmark intent: diagnostic evaluation

### 3.4 Modality
- Primary modality: code
- Perception burden retained: strategy analysis, game-code understanding, opponent adaptation, repeated learning rounds
- Perception burden removed: direct in-environment perception and action generation at play time

## 4. What this benchmark measures
- Primary capability target: strategy coding and peer-learning ability
- Secondary capability target(s): generalization across variants, tournament adaptation, long-run competitiveness
- Does it test rule grounding / legal action generation? yes, but through code generation
- Does it test strategic planning under uncertainty? yes
- Does it test social reasoning / deception / cooperation? no
- Does it test visual grounding / spatial-temporal reasoning? no
- Does it test long-horizon autonomy / task completion? partially
- Does it test real-time efficiency? no
- Does it test cross-game transfer / open-ended generalization? partially
- Why is a game environment especially suitable here? Open-ended game tournaments keep score meaningful across repeated rounds and make strategic improvement directly observable.

## 5. Interaction paradigm
- Observation channel: game code, sample AI, peer submissions, and tournament logs
- Action channel: revised strategy code submissions
- Interface type: API / other
- Agent scaffold allowed: other
- Is there privileged API access? yes
- How close is the setup to human play? low; the benchmark evaluates agents as strategy programmers rather than direct players
- Main ecological-validity trade-off: CATArena says more about iterative strategy development than about human-like game interaction.

## 6. Evaluation protocol
- Main score: tournament score from the cross-round scoring matrix
- Auxiliary score(s): learning-related metrics over iterative rounds
- Evaluation style: tournament / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: code-agent tournament with repeated rounds
- Automatic verifiability: high
- Calibration method: repeated matches, tailored formats for symmetric and asymmetric games, and explicit scoring matrices
- Anti-contamination argument: variants are designed partly to reduce rote memorization
- Reliability or comparability concerns: results depend heavily on the scaffolding given to agents and on the chosen coding workflow

## 7. Main contributions
- Contribution 1: Introduces an iterative peer-learning tournament framework for code agents.
- Contribution 2: Uses four open-ended board and card games with variants to reduce saturation.
- Contribution 3: Defines metrics aimed at separating initial strategy coding from later learning ability.

## 8. Main findings and failure modes
- Core empirical takeaway: CATArena can differentiate agents by both initial strategy quality and their ability to improve across rounds.
- Notable model failure mode 1: many agents plateau after early rounds instead of learning effectively from logs
- Notable model failure mode 2: strategy transfer weakens when variants alter familiar rules
- Notable model failure mode 3: coding competence and gameplay competence do not always align cleanly
- Does this paper reveal a benchmark-design limitation as well? yes; it is evaluating a scaffolded code-agent workflow more than direct in-game interaction

## 9. Why this paper matters for our survey
- Best use in Section 0 (why games): Shows one way games can stay unsaturated as agent capabilities grow.
- Best use in Section 1 (historical evolution): Represents a move toward evaluation of improvement dynamics rather than one-shot scores.
- Best use in Section 2 (design space): Useful contrast case for code-agent strategy evaluation.
- Best use in Section 3 (capability targets): Supports strategic reasoning and adaptation claims.
- Best use in Section 4 (interaction paradigm): Good counterexample to direct-play benchmarks.
- Best use in Section 5 (evaluation protocol): Relevant for iterative tournaments and learning-over-rounds metrics.
- Best use in Section 6/7 (limitations and future): Helps argue that evaluating agent learning ability is still methodologically unsettled.

## 10. Relation to nearby papers
- Closest predecessor(s): tournament-style board-game evaluations and code-agent benchmarks
- Closest follow-up(s): other peer-learning or self-improving agent evaluations
- Best comparison targets inside our corpus: BotzoneBench, WhoIsABetterPlayer, ComplexCardGames
- What this paper uniquely adds relative to neighbors: It evaluates iterative strategy refinement explicitly instead of only static performance.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- Agents submit strategy code, compete, inspect logs and peer code, then iterate over multiple rounds.
- CATArena covers four board and card games with variants and computes scores from a tournament matrix.
- The framework is intended to measure both baseline strategy coding and subsequent learning ability.

### 11.2 Our synthesis / interpretation
- CATArena is better treated as a meta-evaluation framework for code agents than as a conventional gameplay benchmark.
- It is therefore useful mainly as a protocol contrast inside the strategic branch.

### 11.3 Uncertain or needs re-check
- Recheck Appendix B if we later need the exact formulas for the learning-oriented evaluation metrics.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? No immediate reread; the survey use is mainly conceptual and protocol-oriented.
- Which section to read next if needed: 3.1 / 3.4 / Appendix B
- Follow-up question(s): Should CATArena live in the same survey subsection as direct-play arenas, or in a separate scaffold-evaluation subsection?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P2
- Reading depth: deep
- Batch ID: B04
- Outline sections: 2,3,5
- Survey role: contrast
- Paper card path: `paper_cards/B04/CATArena.md`
- Next action: draft-section
- Last updated: 2026-04-05
