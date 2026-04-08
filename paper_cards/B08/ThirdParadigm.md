# ThirdParadigm A Third Paradigm for LLM Evaluation: Dialogue Game-Based Evaluation using clembench

## 0. Metadata
- Date: 2025/07
- Venue: arXiv
- Authors: David Schlangen, Sherzod Hakimov, Chalamalasetti Kranti, Jonathan Jordan, Philipp Sadler
- Paper link: https://arxiv.org/pdf/2507.08491.pdf
- Code link: https://github.com/clembench/clembench
- Reading depth: structured-skim
- Card status: card-reviewed
- Confidence in this card: medium
- Review gate label: usable

## 1. One-paragraph benchmark summary
- A Third Paradigm for LLM Evaluation is a meta-evaluation paper that argues for dialogue game-based evaluation as a complement to both reference-based benchmarks and preference-based arenas. It uses clembench as the concrete implementation of this third paradigm and emphasizes repeatable, multi-turn, reference-free interactions with explicit goals. The paper's main contribution is conceptual and infrastructural rather than a new game suite: it explains why dialogue games combine some of the control of static benchmarks with some of the ecological validity of interactive user evaluation. For this survey, it is valuable because it gives a clear theoretical frame for why certain game benchmarks matter even when they are narrow in world content.

## 2. Position in our survey
- Why-games relevance: Game-like interaction provides goal-directed, repeatable, multi-turn evaluation that sits between fixed-instance testing and open-ended human preference.
- Historical stage: diagnostic capability probe
- Narrative level(s): L1 rule following / L3 social intelligence
- Most relevant outline section(s): 0,1,5,7
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
- Number of games / tasks: extensible framework rather than a fixed task count
- Benchmark intent: diagnostic evaluation

### 3.4 Modality
- Primary modality: text
- Perception burden retained: multi-turn language interaction, goal tracking, and rule-conditioned dialogue
- Perception burden removed: no visual or embodied interface burden

## 4. What this benchmark measures
- Primary capability target: goal-directed multi-turn interaction under repeatable evaluation
- Secondary capability target(s): dialogue-game control, reference-free benchmarking, and benchmark extensibility
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? partially
- Does it test social reasoning / deception / cooperation? partially
- Does it test visual grounding / spatial-temporal reasoning? no
- Does it test long-horizon autonomy / task completion? partially
- Does it test real-time efficiency? no
- Does it test cross-game transfer / open-ended generalization? no
- Why is a game environment especially suitable here? Dialogue games can be repeated, scored, and extended while still forcing interactive behavior rather than single-turn answer generation.

## 5. Interaction paradigm
- Observation channel: benchmark prompts, dialogue histories, and game logic provided through clembench
- Action channel: natural-language responses under game rules
- Interface type: natural language
- Agent scaffold allowed: none
- Is there privileged API access? yes through the framework's game master and evaluation logic
- How close is the setup to human play? medium; it preserves interaction but inside tightly specified benchmark tasks
- Main ecological-validity trade-off: the framework increases ecological validity relative to static benchmarks while remaining more controlled than open user-arena evaluation

## 6. Evaluation protocol
- Main score: framework-defined game success rather than one universal scalar score
- Auxiliary score(s): repeatability, extensibility, and targeted capability probes through benchmark games
- Evaluation style: completion rate / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: not the central contribution; the focus is the evaluation paradigm and reusable framework
- Automatic verifiability: mixed-high
- Calibration method: benchmark-controlled multi-turn interactions with reusable game instances
- Anti-contamination argument: dialogue games can be extended and tailored, which helps avoid overreliance on fixed public test instances
- Reliability or comparability concerns: results still depend on the specific dialogue games implemented, so framework quality does not remove task-design risk

## 7. Main contributions
- Contribution 1: Articulates dialogue game-based evaluation as a third paradigm between reference-based and preference-based evaluation.
- Contribution 2: Presents clembench as a mature reusable implementation of that paradigm.
- Contribution 3: Explains how users can benchmark their own models and extend the benchmark with new targeted tests.

## 8. Main findings and failure modes
- Core empirical takeaway: dialogue game-based evaluation offers a practical middle ground between control and ecological validity.
- Notable model failure mode 1: not the primary focus; the paper emphasizes evaluation design more than one new model failure table
- Notable model failure mode 2: current adoption barriers stem partly from lack of mature reusable implementations
- Notable model failure mode 3: benchmark conclusions remain sensitive to the specific dialogue games chosen
- Does this paper reveal a benchmark-design limitation as well? yes; it explicitly frames the limitations of both static reference benchmarks and open preference arenas

## 9. Why this paper matters for our survey
- Best use in Section 0 (why games): Gives a direct conceptual argument for why game-based evaluation fills a gap left by static and arena-style evaluation.
- Best use in Section 1 (historical evolution): Useful for framing the dialogue-game branch as a distinct historical development.
- Best use in Section 2 (design space): Helpful for representing framework-level benchmark contributions.
- Best use in Section 3 (capability targets): Secondary; more about evaluation framing than one capability axis.
- Best use in Section 4 (interaction paradigm): Strong support for controlled natural-language interaction settings.
- Best use in Section 5 (evaluation protocol): One of the best sources on reference-free, repeatable, multi-turn evaluation.
- Best use in Section 6/7 (limitations and future): Supports the argument that future game benchmarks should balance ecological validity with repeatability and extensibility.

## 10. Relation to nearby papers
- Closest predecessor(s): clembench and clembench-2024
- Closest follow-up(s): future dialogue-game benchmark frameworks and reusable interactive evaluation stacks
- Best comparison targets inside our corpus: Clembench, Clembench2024, TextArena, LMGameBench
- What this paper uniquely adds relative to neighbors: It makes the evaluation philosophy itself the main scientific contribution rather than only the benchmark instances.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- The paper argues that LLM evaluation currently has two main paradigms, reference-based and preference-based evaluation, and proposes dialogue game-based evaluation as a third complementary paradigm.
- It presents clembench as a mature reusable implementation optimized for broader use.
- The paper emphasizes multi-turn, reference-free, repeatable interactions and explains how the framework can benchmark one's own models or be extended with new tests.

### 11.2 Our synthesis / interpretation
- This is a survey-methodology card more than a benchmark card, but it is highly useful because it provides a principled vocabulary for discussing why game-based evaluation exists.
- It helps connect narrower dialogue-game benchmarks to the broader evaluation landscape.

### 11.3 Uncertain or needs re-check
- Re-check whether the latest paper version includes any new empirical results beyond the framework description before citing it as evidence about model performance.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? A targeted reread is worthwhile if we later need exact wording for the evaluation-paradigm section.
- Which section to read next if needed: introduction / framework / extension guidance
- Follow-up question(s): Should this paper be cited in Section 0 as evaluation philosophy or mainly in Section 5 as protocol framing?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P2
- Reading depth: structured-skim
- Batch ID: B08
- Outline sections: 0,1,5,7
- Survey role: contrast
- Paper card path: `paper_cards/B08/ThirdParadigm.md`
- Next action: draft-section
- Last updated: 2026-04-08
