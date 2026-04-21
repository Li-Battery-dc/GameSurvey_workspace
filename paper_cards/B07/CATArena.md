# CATArena CATArena: Evaluation of LLM Agents through Iterative Tournament Competitions

## 0. Metadata
- Date: 2025/10
- Venue: arXiv
- Authors: Lingyue Fu, Xin Ding, Yaoming Zhu, Shao Zhang, Lin Qiu, Weiwen Liu, Weinan Zhang, Xuezhi Cao, Xunliang Cai, Jiaxin Ding, Yong Yu
- Paper link: https://arxiv.org/pdf/2510.26852v1
- Code link:
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: high
- Review gate label: usable

## 1. One-paragraph benchmark summary
- CATArena is less a direct gameplay benchmark and more an iterative competitive framework for evaluating code agents that write and refine game strategies. In round 1, agents receive game code and a sample AI, implement an initial strategy, then enter later rounds where they inspect peers’ code and tournament logs before revising their own submissions. The framework covers four board and card games with rule variants and evaluates strategy coding, learning, and generalizability through a cross-round scoring matrix. In this survey, the paper matters mainly as a code-agent tournament protocol rather than as evidence of raw in-game play.

## 2. Position in our survey
- Why-games relevance: It uses open-ended games to keep evaluation unsaturated and to expose whether agents can improve strategies through repeated competition.
- Historical stage: diagnostic capability probe
- Benchmark level(s): L2 strategic reasoning
- Most relevant outline section(s): 1,3,4
- Role in corpus: contrast

## 3. Design-space coding
### 3.1 Structure
- Form: Match
- Construction: Adapted
- Construction note: real games and designed variants used in a code-agent tournament
- Benchmark unit: tournament round

### 3.2 Mechanics profile
- State visibility: mixed
- Transition uncertainty: mixed
- Actor configuration: multi-agent
- Incentive structure: mixed
- Temporal regime: turn-based

### 3.3 Benchmark scope
- Scope: curated suite
- Number of games / tasks: 4 games with variants

### 3.4 Modality
- Observation modality: mixed
- Action modality: semantic
- Perception burden retained: strategy analysis, game-code understanding, opponent adaptation, repeated learning rounds
- Perception burden removed: direct in-environment perception and action generation at play time

## 4. What this benchmark measures
- Primary capability target: strategy coding and peer-learning ability
- Secondary capability target(s): generalization across variants, tournament adaptation, long-run competitiveness
- Does it test rule grounding / legal action generation? yes, but through code generation
- Does it test strategic planning under uncertainty? partially, depending on the specific game arena and variant
- Does it test social reasoning / deception / cooperation? partially, but only indirectly through Bridge and asymmetric card settings
- Does it test visual grounding / spatial-temporal reasoning? no
- Does it test long-horizon autonomy / task completion? no
- Does it test real-time efficiency? no
- Does it test cross-game transfer / open-ended generalization? partially
- Why is a game environment especially suitable here? Open-ended game tournaments keep score meaningful across repeated rounds and make strategic improvement directly observable.

## 5. Interaction paradigm
- Observation channel: game code, sample AI implementations, previous-round peer submissions, rankings, and detailed tournament logs
- Action channel: revised strategy code submissions
- Interface type: hybrid
- Agent scaffold allowed: tool use
- Is there privileged API access? yes
- How close is the setup to human play? low; the benchmark evaluates agents as strategy programmers rather than direct players
- Main ecological-validity trade-off: CATArena measures iterative strategy development in a code-agent workflow, so it says more about code synthesis and adaptation than about human-like gameplay.

## 6. Evaluation protocol
- Main score: strategy-coding, global-learning, and generalizability scores derived from the cross-round scoring matrix
- Auxiliary score(s): counter-adaptation and self-improvement metrics over iterative rounds
- Evaluation style: tournament / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: repeated code-agent tournaments plus an LLM-Player control that outputs moves directly without writing code
- Automatic verifiability: high
- Calibration method: repeated matches, tailored formats for symmetric and asymmetric games, and explicit scoring matrices
- Anti-contamination argument: variants are designed partly to reduce rote memorization
- Reliability or comparability concerns: results depend heavily on the scaffolding given to agents and on the chosen coding workflow

## 7. Main contributions
- Contribution 1: Introduces an iterative peer-learning tournament framework for code agents.
- Contribution 2: Uses four open-ended board and card games with variants to reduce saturation.
- Contribution 3: Defines metrics aimed at separating initial strategy coding from later learning ability.

## 8. Main findings and failure modes
- Core empirical takeaway: CATArena separates initial strategy-coding ability from iterative learning ability, and it shows that code-agent improvement over rounds is often unstable rather than steadily upward.
- Notable model failure mode 1: many agents show limited or erratic gains across rounds instead of consistent iterative improvement
- Notable model failure mode 2: agent-written strategies often remain relatively simple rule-based programs, leaving substantial headroom in strategy coding
- Notable model failure mode 3: direct LLM gameplay behavior and agent-coded strategies diverge substantially, so strategy coding cannot be treated as a proxy for raw gameplay reasoning
- Does this paper reveal a benchmark-design limitation as well? yes; it is evaluating a scaffolded code-agent workflow more than direct in-game interaction

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Shows one way game-based evaluation can resist saturation by using open-ended variants and iterative competition.
- Best use in Section 1 (taxonomy and evolutionary levels): Contrast case for the shift from one-shot gameplay scoring toward agent-improvement and strategy-coding evaluation.
- Best use in Section 2 (core capabilities evaluated by games): Narrow contrast on strategic adaptation, but only through a code-agent workflow rather than direct play.
- Best use in Section 3 (interaction and evaluation paradigm): Strong protocol contrast for iterative tournaments, cross-round scoring matrices, and learning-over-rounds metrics.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Helps argue that agent-learning evaluation remains methodologically unsettled and may drift away from direct-play capability.

## 10. Relation to nearby papers
- Closest predecessor(s): tournament-style board-game evaluations and code-agent benchmarks
- Closest follow-up(s): other peer-learning or self-improving agent evaluations
- Best comparison targets inside our corpus: WhoIsABetterPlayer, GAMEBoT, Clembench, Clembench2024
- What this paper uniquely adds relative to neighbors: It evaluates iterative code revision explicitly, with a scoring matrix that separates strategy coding from later-round learning and adaptation.

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
- Batch ID: B07
- Outline sections: 1,3,4
- Survey role: contrast
- Paper card path: `paper_cards/B07/CATArena.md`
- Next action: draft-section
- Check status: unchecked
- Last updated: 2026-04-10
