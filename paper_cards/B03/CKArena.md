# CKArena Is Your LLM Really Mastering the Concept? A Multi-Agent Benchmark

## 0. Metadata
- Date: 2026/02
- Venue: NeurIPS 2025
- Authors: Shuhang Xu, Weijian Deng, Yixuan Zhou, Fangwei Zhong
- Paper link: https://arxiv.org/pdf/2505.17512v2
- Code link: https://github.com/xushuhang1122/CK-Arena
- Reading depth: deep
- Card status: finalized
- Confidence in this card: medium
- Review gate label: usable

## 1. One-paragraph benchmark summary
- CK-Arena uses the multi-agent Undercover game to test whether language models really understand concepts or only reproduce superficial associations. Six agents receive either a shared concept or a closely related undercover concept, then generate descriptions, infer others’ concepts, and vote out suspected undercover players. The benchmark combines game outcomes, statement-level quality measures, an Elo-style leaderboard, and a snapshot QA benchmark built from gameplay traces. For this survey, it is a useful contrast paper because it recasts social deduction as a probe of conceptual knowledge rather than primarily deception skill.

## 2. Position in our survey
- Why-games relevance: It uses the interaction pressure of a game to force concept use, discrimination, and role-aware description in context.
- Historical stage: diagnostic capability probe
- Benchmark level(s): L3 social intelligence
- Most relevant outline section(s): 2,3,4
- Role in corpus: contrast

## 3. Design-space coding
### 3.1 Structure
- Form: Dialogue
- Construction: Adapted
- Construction note: language game adapted into a conceptual-knowledge benchmark
- Benchmark unit: full game / snapshot item

### 3.2 Mechanics profile
- State visibility: partial
- Transition uncertainty: deterministic
- Actor configuration: multi-agent
- Incentive structure: mixed
- Temporal regime: turn-based

### 3.3 Benchmark scope
- Scope: single game
- Number of games / tasks: 529 concept pairs overall; main evaluation uses 464 game instances across 12 categories, 500 ranking games, and 5,733 snapshot QA items

### 3.4 Modality
- Observation modality: text or symbolic
- Action modality: semantic
- Perception burden retained: semantic similarity, contextual clue interpretation, multi-round description and voting
- Perception burden removed: nonverbal cues and broader embodied play context

## 4. What this benchmark measures
- Primary capability target: conceptual understanding under interactive pressure
- Secondary capability target(s): semantic discrimination, role-aware description, concept-feature mapping, social inference
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? partially
- Does it test social reasoning / deception / cooperation? yes
- Does it test visual grounding / spatial-temporal reasoning? no
- Does it test long-horizon autonomy / task completion? partially
- Does it test real-time efficiency? no
- Does it test cross-game transfer / open-ended generalization? no
- Why is a game environment especially suitable here? The Undercover format forces models to use concepts strategically rather than merely recognize them in isolation.

## 5. Interaction paradigm
- Observation channel: assigned concept, historical statements, and previous-round analysis
- Action channel: short descriptions and voting decisions during gameplay, with snapshot QA used as a separate diagnostic layer
- Interface type: natural language
- Agent scaffold allowed: none
- Is there privileged API access? no
- How close is the setup to human play? medium; the interaction is game-like, but prompts explicitly constrain strategy to isolate conceptual mastery
- Main ecological-validity trade-off: Strategic restrictions help isolate conceptual reasoning, but they narrow the full space of social-game behavior.

## 6. Evaluation protocol
- Main score: leaderboard rating from game outcomes
- Auxiliary score(s): win rate, survival rate, statement-level relevance/reasonableness/novelty, snapshot QA accuracy
- Evaluation style: Elo / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: anchor models plus human-reviewed statement scoring and a human reference on the leaderboard
- Automatic verifiability: medium
- Calibration method: anchor-model ratings over at least 60 rounds plus a +120 Elo offset to correct the civilian role advantage
- Anti-contamination argument: dynamic game interactions and automatically generated QA reduce dependence on fixed static concept questions
- Reliability or comparability concerns: statement quality depends partly on LLM judges and human review, and the benchmark is specific to concept-pair discrimination

## 7. Main contributions
- Contribution 1: Builds a dynamic concept benchmark on top of the Undercover game.
- Contribution 2: Introduces a large concept-pair dataset spanning multiple semantic categories.
- Contribution 3: Derives a 5,733-item snapshot QA benchmark from gameplay traces for finer diagnosis.

## 8. Main findings and failure modes
- Core empirical takeaway: Strong overall language models differ substantially in conceptual mastery, and both the leaderboard and the 5,733-item QA benchmark suggest that adaptive concept use matters more than any single fixed strategy.
- Notable model failure mode 1: models can produce coherent but weakly diagnostic descriptions
- Notable model failure mode 2: concept understanding varies across semantic categories and is not well predicted by generic benchmark strength
- Notable model failure mode 3: overly fixed aggressive or conservative strategies reduce performance sharply
- Does this paper reveal a benchmark-design limitation as well? yes; the benchmark cleanly isolates concept use, but only within one specialized language-game setting

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Shows that interactive games can stress semantic knowledge in use, where concept understanding must survive role pressure, partial clues, and voting consequences.
- Best use in Section 1 (taxonomy and evolutionary levels): Contrast-only Level 3 case: an Undercover-style Dialogue game broadens social benchmarks from deception alone to concept-discrimination under multi-agent interaction.
- Best use in Section 2 (core capabilities evaluated by games): Supports Purpose claims about concept reasoning, semantic boundary control, role-aware description, and inference from partial teammate/opponent clues.
- Best use in Section 3 (interaction and evaluation paradigm): Useful Paradigm evidence for combining dynamic game outcomes with derived diagnostics: Elo-style role-adjusted leaderboard, statement-quality scoring, and snapshot QA from gameplay traces.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Helps argue that general benchmark strength does not guarantee fine-grained conceptual competence, and that fixed aggressive/conservative strategies can fail in interactive semantic games.

## 10. Relation to nearby papers
- Closest predecessor(s): Undercover-game LLM studies and static concept-understanding benchmarks
- Closest follow-up(s): snapshot-style diagnostic benchmarks generated from gameplay traces
- Best comparison targets inside our corpus: BeyondSurvival, WerewolfArena, Wolf, AvalonBench
- What this paper uniquely adds relative to neighbors: It turns a social language game into a benchmark for conceptual knowledge rather than social deception alone.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- CK-Arena uses six-player Undercover games with four civilians and two undercover agents.
- The paper defines 529 concept pairs overall, uses 464 main-evaluation game instances across 12 concrete categories, and builds a 5,733-instance QA benchmark from 500 completed games.
- The leaderboard corrects the civilian role bias with a temporary +120 Elo offset, and fixed-strategy ablations underperform the unconstrained setting.
- The paper reports a strong correlation between snapshot QA performance and game win rates, using the QA layer as a fine-grained diagnostic rather than a replacement for dynamic play.

### 11.2 Our synthesis / interpretation
- CK-Arena is best used as a contrast card inside the social batch because it broadens what social game benchmarks can measure.
- The benchmark is not mainly about persuasion quality; it is about whether concept knowledge survives interactive, role-conditioned use.

### 11.3 Uncertain or needs re-check
- Recheck Appendix A if we later need the exact category distribution or statement-scoring rubric.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? Completed in this audit; the game setup, leaderboard construction, QA benchmark, ablations, and scope limits are now checked against the full paper.
- Which section to read next if needed: 3.3 / 3.4 / 4.5
- Follow-up question(s): Should we place CK-Arena under social intelligence, conceptual reasoning, or both when drafting taxonomy prose?

## 13. Registry sync
- Registry row synced: yes
- Registry status: finalized
- Priority: P2
- Reading depth: deep
- Batch ID: B03
- Outline sections: 2,3,4
- Survey role: contrast
- Paper card path: `paper_cards/B03/CKArena.md`
- Check status: unchecked
- Next action: draft-section
- Last updated: 2026-04-27
