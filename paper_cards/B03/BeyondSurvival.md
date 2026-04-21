# BeyondSurvival Beyond Survival: Evaluating LLMs in Social Deduction Games with Human-Aligned Strategies

## 0. Metadata
- Date: 2025/10
- Venue: arXiv
- Authors: Zirui Song, Yuan Huang, Junchang Liu, Haozhe Luo, Chenxi Wang, Lang Gao, Zixiang Xu, Mingfei Han
- Paper link: https://arxiv.org/pdf/2510.11389v1
- Code link:
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: medium
- Review gate label: usable

## 1. One-paragraph benchmark summary
- Beyond Survival shifts social-deduction evaluation away from live LLM self-play and toward human-grounded reference evaluation. The paper builds WereBench from 100+ hours of televised Panda Kill footage, reconstructs public game logs and MVP-centered highlight moments, and then introduces WereAlign, which asks models to choose speech or decisions aligned with successful human play. Speech evaluation covers five dimensions, while decision evaluation measures vote alignment and opponent-role inference. For this survey, the paper is most useful as an offline, human-aligned contrast case rather than as a live-agent benchmark.

## 2. Position in our survey
- Why-games relevance: It uses a socially rich game to ground evaluation against human strategic behavior rather than only model-vs-model outcomes.
- Historical stage: diagnostic capability probe
- Benchmark level(s): L3 social intelligence
- Most relevant outline section(s): 2,3,4
- Role in corpus: representative

## 3. Design-space coding
### 3.1 Structure
- Form: Dialogue
- Construction: Adapted
- Construction note: benchmark built from recorded human gameplay data
- Benchmark unit: timestamped speech or decision instance

### 3.2 Mechanics profile
- State visibility: partial
- Transition uncertainty: mixed
- Actor configuration: multi-agent
- Incentive structure: mixed
- Temporal regime: turn-based

### 3.3 Benchmark scope
- Scope: single game
- Number of games / tasks: 80+ human games, 100+ hours of video, 15 rule variants, 48 players, and derived WereAlign items

### 3.4 Modality
- Observation modality: mixed
- Action modality: semantic
- Perception burden retained: multimodal game context, speech content, role information, voting and action logs
- Perception burden removed: direct live actuation by the evaluated model

## 4. What this benchmark measures
- Primary capability target: human-aligned social reasoning in social deduction
- Secondary capability target(s): role inference, deception reasoning, strategic judgment, persuasive speech, counterfactual trade-offs
- Does it test rule grounding / legal action generation? no
- Does it test strategic planning under uncertainty? yes
- Does it test social reasoning / deception / cooperation? yes
- Does it test visual grounding / spatial-temporal reasoning? no; the source corpus is multimodal, but WereAlign evaluates models on reconstructed public context rather than raw video perception
- Does it test long-horizon autonomy / task completion? no
- Does it test real-time efficiency? no
- Does it test cross-game transfer / open-ended generalization? no
- Why is a game environment especially suitable here? Social deduction produces naturally entangled reasoning, lying, and coalition behavior that can be aligned against human strategic references.

## 5. Interaction paradigm
- Observation channel: reconstructed public context at a focal timestamp, including rules, public logs, and speech history from human games
- Action channel: multiple-choice answers for five speech dimensions plus structured vote and opponent-role predictions
- Interface type: natural language / hybrid
- Agent scaffold allowed: none
- Is there privileged API access? no
- How close is the setup to human play? low to medium; the source data come from real human play, but evaluated models answer offline items rather than participate in live dialogue
- Main ecological-validity trade-off: It gains stronger human grounding than synthetic self-play, but models are not actually participating in live conversation.

## 6. Evaluation protocol
- Main score: macro-average speech evaluation accuracy
- Auxiliary score(s): Role Inference, Strategic Judgment, Deception Reasoning, Persuasive Statements, Counterfactual Trade-off, Vote Alignment, Opponent Identification
- Evaluation style: multiple-choice / alignment / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: the reference target is the winning faction MVP trajectory reconstructed from annotated human games
- Automatic verifiability: high
- Calibration method: human-verified reconstruction, MVP-grounded positive options, and human-checked adversarial negative options
- Anti-contamination argument: not the main claim; the paper leans on time-indexed human-game contexts rather than a broad saturation argument
- Reliability or comparability concerns: the benchmark is built from one televised Werewolf source, uses MVP-from-winning-faction behavior as reference, and does not test live interaction

## 7. Main contributions
- Contribution 1: Releases a large human-verified multimodal Werewolf corpus.
- Contribution 2: Introduces WereAlign, a reference-based social-reasoning evaluation paradigm.
- Contribution 3: Breaks social reasoning into five speech dimensions plus decision alignment metrics.

## 8. Main findings and failure modes
- Core empirical takeaway: Most models remain below 50% average speech accuracy, and strategic reasoning dimensions such as deception reasoning and counterfactual trade-off are markedly harder than persuasive phrasing.
- Notable model failure mode 1: strong persuasive phrasing does not imply good counterfactual or deception reasoning
- Notable model failure mode 2: role-dependent performance varies sharply, especially on roles requiring verification and hidden-state reasoning
- Notable model failure mode 3: model rankings show that social strategy alignment is not well predicted by general benchmark strength alone
- Does this paper reveal a benchmark-design limitation as well? yes; it is a strong offline social benchmark, but not a live-agent game benchmark

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Shows that games can anchor human-like social reasoning evaluation with richer evidence than generic dialogue tasks.
- Best use in Section 1 (taxonomy and evolutionary levels): Secondary contrast only; it shows a move from synthetic arenas toward human-grounded evaluation, but it is not a level-defining taxonomy anchor.
- Best use in Section 2 (core capabilities evaluated by games): Strong for role inference, deception reasoning, and persuasive strategy.
- Best use in Section 3 (interaction and evaluation paradigm): Good example of offline contextual evaluation rather than embodied participation. Important for winning-faction alignment and dimension-specific speech scoring.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Supports the claim that fluent dialogue is easier than robust social strategy.

## 10. Relation to nearby papers
- Closest predecessor(s): WerewolfArena and earlier self-play social-deduction benchmarks
- Closest follow-up(s): WOLF is the nearest later contrast on statement-level instrumentation rather than a direct continuation of the human-grounded setup
- Best comparison targets inside our corpus: WerewolfArena, LLMHanabi, Wolf, AvalonBench
- What this paper uniquely adds relative to neighbors: It anchors social evaluation to human winning strategies instead of only model self-play or peer judgments.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- WereBench contains 100+ hours of Panda Kill footage, 80+ games, 15 rule variants, and 48 human players, with strong agreement on speaker attribution and log reconstruction.
- WereAlign evaluates speech on five dimensions and decisions with Vote Alignment and Opponent Identification.
- The best reported speech macro-average is 0.720 for Gemini-2.5-Pro, while most models remain below 0.50.

### 11.2 Our synthesis / interpretation
- Beyond Survival is a useful bridge card between live-agent social game benchmarks and offline human-grounded evaluation.
- It is best used when we discuss how to calibrate social benchmarks against successful human behavior rather than only synthetic gameplay.

### 11.3 Uncertain or needs re-check
- Recheck the dataset section if we later need the exact split or rule-variant composition of WereBench.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? Completed in this audit; the dataset-construction, reference-answer generation, main results, intervention analysis, and limitations sections are now checked against the full paper.
- Which section to read next if needed: 4.1 / 4.2 / 5.3
- Follow-up question(s): How defensible is winning-faction alignment as a proxy for optimal social reasoning across roles?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P1
- Reading depth: deep
- Batch ID: B03
- Outline sections: 2,3,4
- Survey role: representative
- Paper card path: `paper_cards/B03/BeyondSurvival.md`
- Check status: unchecked
- Next action: draft-section
- Last updated: 2026-04-10
