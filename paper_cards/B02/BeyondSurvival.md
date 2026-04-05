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
- Beyond Survival shifts social-deduction evaluation away from pure LLM self-play and toward human-aligned reference judgments. It builds WereBench, a human-verified multimodal Werewolf dataset with over 100 hours of video and rich annotations, then introduces WereAlign, which scores models against strategies used by the winning human faction. The benchmark separates speech evaluation into five dimensions and adds decision-level alignment metrics. For this survey, the paper is most useful as a reference-based social benchmark that evaluates whether model reasoning aligns with successful human play rather than merely whether an LLM can survive in a synthetic game.

## 2. Position in our survey
- Why-games relevance: It uses a socially rich game to ground evaluation against human strategic behavior rather than only model-vs-model outcomes.
- Historical stage: diagnostic capability probe
- Narrative level(s): L3 social intelligence
- Most relevant outline section(s): 3,5,6
- Role in corpus: representative

## 3. Design-space coding
### 3.1 Environment structure
- Information structure: imperfect
- Transition structure: mixed
- Agent structure: multi-agent
- Social structure: mixed
- Time structure: turn-based

### 3.2 World structure
- World type(s): social deduction
- Real game / simulated game / designed task-game hybrid: benchmark built from recorded human gameplay data
- Benchmark unit: timestamped speech or decision instance

### 3.3 Benchmark scope
- Scope: single game
- Number of games / tasks: human Werewolf corpus with 100+ hours of video and derived evaluation items
- Benchmark intent: diagnostic evaluation

### 3.4 Modality
- Primary modality: mixed
- Perception burden retained: multimodal game context, speech content, role information, voting and action logs
- Perception burden removed: direct live actuation by the evaluated model

## 4. What this benchmark measures
- Primary capability target: human-aligned social reasoning in social deduction
- Secondary capability target(s): role inference, deception reasoning, strategic judgment, persuasive speech, counterfactual trade-offs
- Does it test rule grounding / legal action generation? no
- Does it test strategic planning under uncertainty? yes
- Does it test social reasoning / deception / cooperation? yes
- Does it test visual grounding / spatial-temporal reasoning? partially, through multimodal context
- Does it test long-horizon autonomy / task completion? no
- Does it test real-time efficiency? no
- Does it test cross-game transfer / open-ended generalization? no
- Why is a game environment especially suitable here? Social deduction produces naturally entangled reasoning, lying, and coalition behavior that can be aligned against human strategic references.

## 5. Interaction paradigm
- Observation channel: public information available at a focal timestamp, including multimodal human gameplay context
- Action channel: multiple-choice answers for speech tasks and aligned decisions for vote/suspicion tasks
- Interface type: natural language / hybrid
- Agent scaffold allowed: none
- Is there privileged API access? yes
- How close is the setup to human play? medium; the benchmark preserves real human gameplay evidence but turns evaluation into offline question answering and alignment tasks
- Main ecological-validity trade-off: It gains stronger human grounding than synthetic self-play, but models are not actually participating in live conversation.

## 6. Evaluation protocol
- Main score: macro-average speech evaluation accuracy
- Auxiliary score(s): Role Inference, Strategic Judgment, Deception Reasoning, Persuasive Statements, Counterfactual Trade-off, Vote Alignment, Opponent Identification
- Evaluation style: judge-based / milestone / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: winning human faction strategy serves as the reference target
- Automatic verifiability: medium to high
- Calibration method: reference-based multiple-choice construction from annotated human games
- Anti-contamination argument: hidden-role and timestamp-specific public context reduce simple memorization value
- Reliability or comparability concerns: the winning faction is used as a success proxy, which may not always equal globally optimal play

## 7. Main contributions
- Contribution 1: Releases a large human-verified multimodal Werewolf corpus.
- Contribution 2: Introduces WereAlign, a reference-based social-reasoning evaluation paradigm.
- Contribution 3: Breaks social reasoning into five speech dimensions plus decision alignment metrics.

## 8. Main findings and failure modes
- Core empirical takeaway: Most models remain below 50% average speech accuracy, and strategic reasoning is weaker than surface fluency.
- Notable model failure mode 1: strong persuasive phrasing does not imply good counterfactual or deception reasoning
- Notable model failure mode 2: role-dependent performance varies sharply, especially on roles requiring verification and hidden-state reasoning
- Notable model failure mode 3: model rankings show that social strategy alignment is not well predicted by general benchmark strength alone
- Does this paper reveal a benchmark-design limitation as well? yes; it is a strong offline social benchmark, but not a live-agent game benchmark

## 9. Why this paper matters for our survey
- Best use in Section 0 (why games): Shows that games can anchor human-like social reasoning evaluation with richer evidence than generic dialogue tasks.
- Best use in Section 1 (historical evolution): Useful marker for a move from synthetic arenas toward human-grounded evaluation.
- Best use in Section 2 (design space): Social-deduction benchmark built from recorded gameplay rather than live self-play.
- Best use in Section 3 (capability targets): Strong for role inference, deception reasoning, and persuasive strategy.
- Best use in Section 4 (interaction paradigm): Good example of offline contextual evaluation rather than embodied participation.
- Best use in Section 5 (evaluation protocol): Important for winning-faction alignment and dimension-specific speech scoring.
- Best use in Section 6/7 (limitations and future): Supports the claim that fluent dialogue is easier than robust social strategy.

## 10. Relation to nearby papers
- Closest predecessor(s): Werewolf Arena and earlier self-play social-deduction benchmarks
- Closest follow-up(s): WOLF-style finer deception diagnostics
- Best comparison targets inside our corpus: WerewolfArena, Wolf, LLMHanabi
- What this paper uniquely adds relative to neighbors: It anchors social evaluation to human winning strategies instead of only model self-play or peer judgments.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- The paper introduces a multimodal human Werewolf dataset with over 100 hours of video and extensive annotations.
- WereAlign evaluates speech on five dimensions and decisions on metrics such as vote alignment and opponent identification.
- Reported results show that even strong models remain error-prone, especially on deeper strategic reasoning dimensions.

### 11.2 Our synthesis / interpretation
- Beyond Survival is a useful bridge card between live-agent social game benchmarks and offline human-grounded evaluation.
- It is best used when we discuss how to calibrate social benchmarks against successful human behavior rather than only synthetic gameplay.

### 11.3 Uncertain or needs re-check
- Recheck the dataset section if we later need the exact split or rule-variant composition of WereBench.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? No immediate reread; the benchmark structure and main scores are already clear.
- Which section to read next if needed: 4.1 / 4.2 / 5.3
- Follow-up question(s): How defensible is winning-faction alignment as a proxy for optimal social reasoning across roles?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P1
- Reading depth: deep
- Batch ID: B02
- Outline sections: 3,5,6
- Survey role: representative
- Paper card path: `paper_cards/B02/BeyondSurvival.md`
- Next action: draft-section
- Last updated: 2026-04-05
