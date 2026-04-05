# Wolf WOLF: Werewolf-based Observations for LLM Deception and Falsehoods

## 0. Metadata
- Date: 2025/12
- Venue: NeurIPS 2025 Workshop
- Authors: Mrinal Agarwal, Saad Rana, Theo Sundoro, Hermela Berhe, Spencer Kim, Vasu Sharma, Sean O'Brien, Kevin Zhu
- Paper link: https://arxiv.org/pdf/2512.09187v1
- Code link:
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: high
- Review gate label: strong

## 1. One-paragraph benchmark summary
- WOLF extends the social-deduction benchmark line by separating deception production from deception detection inside a programmable Werewolf environment. It keeps a fixed eight-player role setup, but treats every debate statement as a scored analysis unit with speaker self-labels, peer deception judgments, and longitudinal suspicion tracking. The paper adds a more explicit methodology for measuring types of deception such as omission, distortion, misdirection, and fabrication. In this survey, WOLF is valuable because it turns social-game play into a more diagnostic deception benchmark instead of only an end-to-end tournament.

## 2. Position in our survey
- Why-games relevance: It shows that games can provide repeated, adversarial, role-grounded deception events rather than isolated lie-detection examples.
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
- Real game / simulated game / designed task-game hybrid: real game adapted into a measurement-oriented benchmark
- Benchmark unit: statement plus full game

### 3.3 Benchmark scope
- Scope: single game
- Number of games / tasks: 100 simulated Werewolf games in the reported evaluation
- Benchmark intent: diagnostic evaluation

### 3.4 Modality
- Primary modality: text
- Perception burden retained: dialogue, repeated accusations, role incentives, temporal evidence accumulation
- Perception burden removed: human nonverbal cues and real embodied social presence

## 4. What this benchmark measures
- Primary capability target: deception generation and deception detection
- Secondary capability target(s): role-conditioned honesty, suspicion calibration, longitudinal social inference
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? yes
- Does it test social reasoning / deception / cooperation? yes
- Does it test visual grounding / spatial-temporal reasoning? no
- Does it test long-horizon autonomy / task completion? yes
- Does it test real-time efficiency? no
- Does it test cross-game transfer / open-ended generalization? no
- Why is a game environment especially suitable here? Werewolf forces lies, uncertainty, and trust calibration to arise naturally from role incentives over repeated rounds.

## 5. Interaction paradigm
- Observation channel: role-grounded prompts, debate history, and evolving suspicion context
- Action channel: bids, public statements, votes, and night actions plus private self/peer analyses
- Interface type: natural language / hybrid
- Agent scaffold allowed: other
- Is there privileged API access? yes
- How close is the setup to human play? medium; the benchmark keeps interactive debate and hidden roles, but uses structured self- and peer-labeling unavailable in normal play
- Main ecological-validity trade-off: WOLF gains strong measurement clarity by instrumenting every statement, but those extra labels partly change the natural setting.

## 6. Evaluation protocol
- Main score: deception-detection quality over statement-level judgments
- Auxiliary score(s): faction win rates, per-role suspicion, observer precision/recall, ROC AUC, AUPRC, temporal suspicion slopes
- Evaluation style: hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: model-vs-model game simulation with internal self/peer labels
- Automatic verifiability: medium
- Calibration method: 100 full games, role-balanced roster, and probabilistic suspicion tracking with exponential smoothing
- Anti-contamination argument: not central
- Reliability or comparability concerns: self-labeled deception serves as ground truth, so the benchmark measures model-internal role behavior rather than independently verified human deception

## 7. Main contributions
- Contribution 1: Separates deception production from deception detection inside one social benchmark.
- Contribution 2: Adds statement-level measurement and a structured deception taxonomy.
- Contribution 3: Tracks temporal suspicion dynamics and calibration rather than only final outcomes.

## 8. Main findings and failure modes
- Core empirical takeaway: LLM agents can sustain deception in play, but peers detect it only weakly and with low recall, leaving werewolves advantaged.
- Notable model failure mode 1: observer recall is low even when precision is decent
- Notable model failure mode 2: honest roles such as Seer and Doctor are often over-flagged because withholding looks deceptive
- Notable model failure mode 3: subtle omissions and misdirection persist longer than overt fabrications
- Does this paper reveal a benchmark-design limitation as well? yes; the benchmark depends on self-reported deception labels as a reference signal

## 9. Why this paper matters for our survey
- Best use in Section 0 (why games): Shows how repeated social interaction creates richer deceptive behavior than static truthfulness datasets.
- Best use in Section 1 (historical evolution): Represents a move from social-game tournaments toward instrumented deception diagnostics.
- Best use in Section 2 (design space): Helpful social-deduction design point with statement-level units.
- Best use in Section 3 (capability targets): Excellent fit for deception generation, detection, and belief tracking.
- Best use in Section 4 (interaction paradigm): Illustrates highly instrumented role-grounded prompting and private scratchpads.
- Best use in Section 5 (evaluation protocol): Useful for calibration metrics, suspicion trajectories, and per-role statistics.
- Best use in Section 6/7 (limitations and future): Supports the claim that deception detection remains weak and poorly calibrated.

## 10. Relation to nearby papers
- Closest predecessor(s): Werewolf Arena and deception-detection studies
- Closest follow-up(s): BeyondSurvival
- Best comparison targets inside our corpus: WerewolfArena, BeyondSurvival, LLMHanabi
- What this paper uniquely adds relative to neighbors: It measures lying and lie detection separately at the statement level instead of treating social success as a single score.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- WOLF uses fixed eight-player Werewolf games and treats each statement as a separate unit of deception analysis.
- It records speaker self-assessments, peer suspicion, and deception types, then aggregates per-role and temporal metrics over 100 games.
- The reported results show werewolves winning most games and observer accuracy remaining weak despite persistent suspicion.

### 11.2 Our synthesis / interpretation
- WOLF is one of the clearest papers in this corpus for arguing that social-game benchmarks can measure more than final win rates.
- It is best read as a measurement framework for deception dynamics, not as a broad benchmark of general social play.

### 11.3 Uncertain or needs re-check
- Recheck Section 4.5 if we later need the exact metric formulas used in the calibration analysis.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? No immediate reread; the key methodology and results are already clear.
- Which section to read next if needed: 4.1 / 4.5 / 5.7
- Follow-up question(s): How portable is WOLF's self-labeled deception protocol to non-Werewolf social benchmarks?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P1
- Reading depth: deep
- Batch ID: B02
- Outline sections: 3,5,6
- Survey role: representative
- Paper card path: `paper_cards/B02/Wolf.md`
- Next action: draft-section
- Last updated: 2026-04-05
