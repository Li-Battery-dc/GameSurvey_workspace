# Clembench2024 clembench-2024: A Challenging, Dynamic, Complementary, Multilingual Benchmark and Underlying Flexible Framework for LLMs as Multi-Action Agents

## 0. Metadata
- Date: 2024/05
- Venue: arXiv
- Authors: Anne Beyer, Kranti Chalamalasetti, Sherzod Hakimov, Brielen Madureira, Philipp Sadler, David Schlangen
- Paper link: https://arxiv.org/pdf/2405.20859.pdf
- Code link: https://github.com/clembench/clembench
- Reading depth: structured-skim
- Card status: card-reviewed
- Confidence in this card: medium
- Review gate label: usable

## 1. One-paragraph benchmark summary
- clembench-2024 is an expansion of the original clembench framework that stresses dynamic benchmark maintenance, multilingual evaluation, and broader multi-action interaction. The paper argues that dialogue-game evaluation can remain current without collapsing into contamination-prone static test sets, and it shows that human performance still remains substantially above top model performance. It also uses the framework to examine questions such as how prompting language affects agent behavior. For this survey, the paper is useful because it turns clembench from a proof-of-concept framework into an evolving benchmark program.

## 2. Position in our survey
- Why-games relevance: Dialogue games make it possible to keep evaluation dynamic, multi-turn, and automatically scoreable while still targeting interactive agency.
- Historical stage: diagnostic capability probe
- Narrative level(s): L1 rule following / L3 social intelligence
- Most relevant outline section(s): 1,3,4,5,7
- Role in corpus: contrast

## 3. Design-space coding
### 3.1 Environment structure
- Information structure: mixed
- Transition structure: mixed
- Agent structure: multi-agent
- Social structure: mixed
- Time structure: turn-based

### 3.2 World structure
- World type(s): other
- Real game / simulated game / designed task-game hybrid: dialogue-game benchmark framework
- Benchmark unit: interaction episode

### 3.3 Benchmark scope
- Scope: curated suite
- Number of games / tasks: expanded clembench suite with dynamic, multilingual, and multi-action extensions
- Benchmark intent: diagnostic evaluation

### 3.4 Modality
- Primary modality: text
- Perception burden retained: conversational grounding, multi-turn planning, and language-sensitive task execution
- Perception burden removed: no visual burden and no open-ended real-world interaction noise

## 4. What this benchmark measures
- Primary capability target: robust conversational agency under dynamic interactive evaluation
- Secondary capability target(s): multilingual sensitivity, benchmark non-saturation, and framework extensibility
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? partially
- Does it test social reasoning / deception / cooperation? partially
- Does it test visual grounding / spatial-temporal reasoning? no
- Does it test long-horizon autonomy / task completion? partially
- Does it test real-time efficiency? no
- Does it test cross-game transfer / open-ended generalization? partially
- Why is a game environment especially suitable here? Game-like interaction supports repeatable, multi-turn, automatically scoreable evaluation while staying flexible enough to add new test forms.

## 5. Interaction paradigm
- Observation channel: benchmark prompts, dialogue history, and game-specific textual context
- Action channel: language actions inside framework-defined dialogue games
- Interface type: natural language
- Agent scaffold allowed: none
- Is there privileged API access? yes through benchmark-controlled game logic and scoring
- How close is the setup to human play? medium; the interaction is linguistic and multi-turn, but still highly controlled
- Main ecological-validity trade-off: clembench-2024 improves realism relative to static QA but remains less open-ended than natural user interaction

## 6. Evaluation protocol
- Main score: game or task success within the dialogue framework
- Auxiliary score(s): multilingual comparisons, human-versus-model gaps, and non-saturation analyses
- Evaluation style: completion rate / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: model comparisons plus human reference performance
- Automatic verifiability: mixed-high
- Calibration method: dynamic benchmark updates, multilingual prompt variants, and complementary task design
- Anti-contamination argument: the paper explicitly argues that dynamic interactive games help avoid contamination and keep pace with model releases
- Reliability or comparability concerns: the exact conclusions depend on which games and prompt languages are instantiated in the framework

## 7. Main contributions
- Contribution 1: Extends clembench into a more dynamic, complementary, multilingual benchmark and framework.
- Contribution 2: Shows that human performance remains much higher than top model performance.
- Contribution 3: Demonstrates that the framework can study practical questions such as prompting-language effects and model choice for interactive systems.

## 8. Main findings and failure modes
- Core empirical takeaway: dialogue-game evaluation remains unsaturated, and human performance still substantially exceeds the best models.
- Notable model failure mode 1: performance remains brittle under multilingual prompting
- Notable model failure mode 2: newer models improve, but not enough to saturate the interactive tasks
- Notable model failure mode 3: capability estimates depend on prompt language and benchmark instantiation choices
- Does this paper reveal a benchmark-design limitation as well? yes; it emphasizes that interactive benchmarks need continuous maintenance to stay diagnostic

## 9. Why this paper matters for our survey
- Best use in Section 0 (why games): Good evidence that game-like interaction supports dynamic and contamination-aware evaluation.
- Best use in Section 1 (historical evolution): Important follow-up showing how a dialogue-game framework matures after the initial proof of concept.
- Best use in Section 2 (design space): Helps represent dialogue-game frameworks that evolve over time.
- Best use in Section 3 (capability targets): Supports conversational agency and language-sensitive interactive reasoning.
- Best use in Section 4 (interaction paradigm): Useful for natural-language multi-action evaluation under benchmark control.
- Best use in Section 5 (evaluation protocol): Strong reference for dynamic maintenance, human gaps, and multilingual prompt effects.
- Best use in Section 6/7 (limitations and future): Supports the claim that future benchmarks must remain updateable and contamination-aware.

## 10. Relation to nearby papers
- Closest predecessor(s): clembench
- Closest follow-up(s): A Third Paradigm for LLM Evaluation
- Best comparison targets inside our corpus: Clembench, ThirdParadigm, TextArena, GAMEBoT
- What this paper uniquely adds relative to neighbors: It makes benchmark maintenance, multilingual extension, and non-saturation arguments central parts of the contribution.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- The paper presents clembench-2024 as a dynamic, complementary, multilingual benchmark and framework for LLMs as multi-action agents.
- It argues that the framework can keep up with new model developments while helping avoid data contamination.
- The authors report that human performance is substantially higher than even the best models and use the framework to study prompting-language effects.

### 11.2 Our synthesis / interpretation
- This paper matters less for introducing a new benchmark family than for showing how an interactive benchmark can remain scientifically useful over time.
- It is one of the better sources for arguing that benchmark maintenance is itself part of benchmark design.

### 11.3 Uncertain or needs re-check
- Re-check the exact suite composition and multilingual setup if we later need a more precise comparison with TextArena or GAMEBoT.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? Yes, if we later want the exact multilingual or dynamic-update protocol.
- Which section to read next if needed: framework changes / multilingual analysis / discussion
- Follow-up question(s): Which parts of clembench-2024 most directly improve contamination resistance rather than only expanding task breadth?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P2
- Reading depth: structured-skim
- Batch ID: B08
- Outline sections: 1,3,4,5,7
- Survey role: contrast
- Paper card path: `paper_cards/B08/Clembench2024.md`
- Next action: draft-section
- Last updated: 2026-04-08
