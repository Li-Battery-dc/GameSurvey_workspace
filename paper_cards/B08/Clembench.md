# Clembench clembench: Using Game Play to Evaluate Chat-Optimized Language Models as Conversational Agents

## 0. Metadata
- Date: 2023/05
- Venue: EMNLP 2023
- Authors: Kranti Chalamalasetti, Jana Gotze, Sherzod Hakimov, Brielen Madureira, Philipp Sadler, David Schlangen
- Paper link: https://aclanthology.org/2023.emnlp-main.689.pdf
- Code link: https://github.com/clembench/clembench
- Reading depth: structured-skim
- Card status: card-reviewed
- Confidence in this card: medium
- Review gate label: usable

## 1. One-paragraph benchmark summary
- clembench is a dialogue-game evaluation framework for chat-optimized language models. Instead of testing models on static prompts or on open-ended user preference alone, it places them in carefully constructed interactive settings that probe instruction following, goal orientation, and situated language understanding through constrained gameplay. The original paper presents five interaction settings and shows that even comparatively simple games remain far from saturated. For this survey, clembench is an important methodological branch because it argues that game-like conversational interaction can itself be a reusable evaluation paradigm.

## 2. Position in our survey
- Why-games relevance: Dialogue games create repeatable multi-turn interaction with explicit goals, which lets the benchmark test conversational agency rather than only response quality.
- Historical stage: diagnostic capability probe
- Narrative level(s): L1 rule following / L3 social intelligence
- Most relevant outline section(s): 1,2,3
- Role in corpus: representative

## 3. Design-space coding
### 3.1 Environment structure
- Information structure: mixed
- Transition structure: mixed
- Agent structure: mixed
- Social structure: mixed
- Time structure: turn-based

### 3.2 World structure
- World type(s): other
- Real game / simulated game / designed task-game hybrid: designed dialogue-game benchmark
- Benchmark unit: interaction episode

### 3.3 Benchmark scope
- Scope: curated suite
- Number of games / tasks: 5 interaction settings in v1.0, instantiated as 7 benchmark datasets and 250 instances
- Benchmark intent: diagnostic evaluation

### 3.4 Modality
- Primary modality: text
- Perception burden retained: conversational grounding, instruction following, multi-turn planning, and goal-directed dialogue
- Perception burden removed: no visual grounding or embodied action burden

## 4. What this benchmark measures
- Primary capability target: conversational agency under goal-directed interactive play
- Secondary capability target(s): instruction following, strategic goal orientation, and situated language understanding
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? partially
- Does it test social reasoning / deception / cooperation? partially
- Does it test visual grounding / spatial-temporal reasoning? no
- Does it test long-horizon autonomy / task completion? partially
- Does it test real-time efficiency? no
- Does it test cross-game transfer / open-ended generalization? no
- Why is a game environment especially suitable here? Dialogue games make it possible to probe multi-turn behavior with explicit goals and automatic scoring, rather than only judging isolated responses.

## 5. Interaction paradigm
- Observation channel: text prompts, dialogue history, and game-specific instructions
- Action channel: natural-language responses inside benchmark-controlled game loops
- Interface type: natural language
- Agent scaffold allowed: none
- Is there privileged API access? yes in the sense that the framework controls the game master and success conditions
- How close is the setup to human play? medium; the interaction is conversational, but the settings are highly constructed for diagnosis
- Main ecological-validity trade-off: clembench gains control and repeatability by using constrained dialogue games rather than open-ended real-world interaction

## 6. Evaluation protocol
- Main score: percentage of episodes played to completion plus game-specific quality scores, summarized overall as `clemscore`
- Auxiliary score(s): per-game quality metrics such as speed, F1, or Cohen's kappa depending on the setting
- Evaluation style: completion rate / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: chat-optimized models are evaluated in self-play across the same interaction settings; the paper assumes human performance would be near ceiling but does not report a human baseline
- Automatic verifiability: mixed-high
- Calibration method: programmatic Game Master control, repeated benchmark instances, and fixed prompts shared across models
- Anti-contamination argument: constructed interaction settings reduce direct overlap with standard benchmark instances
- Reliability or comparability concerns: results depend on the chosen game set, some experiments use relatively small instance counts, and closed-model APIs can drift over time

## 7. Main contributions
- Contribution 1: Introduces a reusable dialogue-game framework for evaluating chat-optimized language models.
- Contribution 2: Demonstrates five interaction settings that probe conversational agency under constrained goals.
- Contribution 3: Shows that these metrics remain unsaturated and track model development over time.

## 8. Main findings and failure modes
- Core empirical takeaway: newer chat models perform better, but even the simple example games remain far from saturated.
- Notable model failure mode 1: failing to follow game-play instructions consistently over multiple turns
- Notable model failure mode 2: weak objective fulfillment even when local responses appear fluent
- Notable model failure mode 3: brittle multi-turn behavior under constrained conversational goals
- Does this paper reveal a benchmark-design limitation as well? yes; it shows that static evaluation misses behavior that only appears under multi-turn interaction

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Strong argument that games can evaluate dialogue agency in a way static benchmarks cannot.
- Best use in Section 1 (taxonomy and evolutionary levels): Important branch in the move toward interaction-first evaluation. Useful for dialogue games as a benchmark family distinct from board or video games.
- Best use in Section 2 (core capabilities evaluated by games): Supports instruction following and conversational agency discussion.
- Best use in Section 3 (interaction and evaluation paradigm): Strong anchor for pure natural-language game interaction. Helps frame automatic scoring for multi-turn, reference-free interaction.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Supports dialogue-game evaluation as a reusable benchmark pattern, not just one-off tasks.

## 10. Relation to nearby papers
- Closest predecessor(s): situated language understanding and dialogue-game evaluation proposals
- Closest follow-up(s): clembench-2024 and A Third Paradigm for LLM Evaluation
- Best comparison targets inside our corpus: TextArena, Clembench2024, ThirdParadigm, GAMEBoT
- What this paper uniquely adds relative to neighbors: It establishes dialogue-game evaluation as a concrete benchmark framework rather than only a conceptual proposal.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- The paper investigates five interaction settings for evaluating chat-optimized language models through gameplay.
- Benchmark v1.0 contains 250 instances distributed across taboo, wordle, wordle+clue, wordle+clue+critic, drawing, reference, and private/shared datasets.
- It argues that LLMs can be meaningfully evaluated by exposing them to constrained game-like settings designed to challenge specific capabilities.
- The authors report that the metrics remain far from saturated and that newer models generally perform better, with GPT-4 achieving the strongest overall reported `clemscore`.

### 11.2 Our synthesis / interpretation
- clembench is less about game diversity than about evaluation philosophy, which makes it especially relevant for the survey's paradigm section.
- It is one of the clearest alternatives to both static benchmark evaluation and open preference-arena evaluation.

### 11.3 Uncertain or needs re-check
- Re-check the exact names and scoring details of the five interaction settings if we later compare dialogue-game frameworks in more detail.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? Full paper read completed for this audit; revisit only if we later need exact prompt templates or per-game scoring formulas.
- Which section to read next if needed: Section 4 / Section 5 / Appendix B
- Follow-up question(s): Which of the five settings best captures benchmarkable conversational agency rather than narrow instruction following?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P1
- Reading depth: structured-skim
- Batch ID: B08
- Outline sections: 1,2,3
- Survey role: representative
- Paper card path: `paper_cards/B08/Clembench.md`
- Check status: unchecked
- Last updated: 2026-04-09
