# InteractiveFictionGames Interactive Fiction Games: A Colossal Adventure

## 0. Metadata
- Date: 2019/09
- Venue: AAAI 2020
- Authors: Matthew Hausknecht, Prithviraj Ammanabrolu, Marc-Alexandre Cote, Xingdi Yuan
- Paper link: https://ojs.aaai.org/index.php/AAAI/article/download/6297/6153
- Code link: https://github.com/microsoft/jericho
- Reading depth: deep
- Card status: finalized
- Confidence in this card: high
- Review gate label: usable

## 1. One-paragraph benchmark summary
- Interactive Fiction Games: A Colossal Adventure introduces Jericho, an environment for studying autonomous language agents in human-authored text-adventure games. The paper argues that parser-based interactive fiction combines combinatorial action spaces, language understanding, commonsense reasoning, and long-horizon planning in a single benchmark family. Jericho supports score detection, move counts, world-change tracking, and template-based action generation for a set of 56 supported human-made games, which makes these historically important text games newly usable as research benchmarks. For this survey, the paper is a key precursor for later long-horizon text-game benchmarks such as TextQuests, but its results should be read alongside the strong instrumentation Jericho provides.

## 2. Position in our survey
- Why-games relevance: Interactive fiction exposes language grounding, exploration, and long-horizon planning inside environments with sparse feedback and machine-verifiable progress.
- Historical stage: diagnostic capability probe
- Benchmark level(s): L2 strategic reasoning; L5 precursor only for fixed IF-suite coverage, not modern open-ended general-game evidence
- Most relevant outline section(s): 0,1,2,3,4
- Role in corpus: anchor

## 3. Design-space coding
### 3.1 Structure
- Form: Arc
- Construction: Wrapped
- Construction note: suite of real human-authored interactive fiction games
- Benchmark unit: full game run

### 3.2 Mechanics profile
- State visibility: partial
- Transition uncertainty: mixed
- Actor configuration: single-agent
- Incentive structure: N/A
- Temporal regime: turn-based

### 3.3 Benchmark scope
- Scope: curated suite
- Number of games / tasks: 56 supported games

### 3.4 Modality
- Observation modality: text or symbolic
- Action modality: semantic
- Perception burden retained: language understanding, combinatorial command generation, and long-horizon state tracking
- Perception burden removed: no visual grounding is required

## 4. What this benchmark measures
- Primary capability target: long-horizon language-grounded game play in text worlds
- Secondary capability target(s): combinatorial action selection, commonsense reasoning, exploration, and sparse-reward progress
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? yes
- Does it test social reasoning / deception / cooperation? no
- Does it test visual grounding / spatial-temporal reasoning? no
- Does it test long-horizon autonomy / task completion? yes
- Does it test real-time efficiency? no
- Does it test cross-game transfer / open-ended generalization? partially; the paper spans a fixed suite of supported IF games and discusses general IF play, but treats truly general unseen-game play as future work
- Why is a game environment especially suitable here? Text adventures combine natural-language interaction with long, branching task structure and precise reward signals.

## 5. Interaction paradigm
- Observation channel: room descriptions, parser feedback, inventory changes, score, and move counts
- Action channel: free-form text commands
- Interface type: natural language
- Agent scaffold allowed: other; Jericho can expose templates, parser vocabulary, world objects, and valid-action signals as handicaps
- Is there privileged API access? yes; Jericho exposes score, move count, and world-change information for supported games
- How close is the setup to human play? medium; play remains parser-based, but the environment instrumentation materially reduces the raw opacity of the original games
- Main ecological-validity trade-off: Jericho preserves classic text-game interaction while adding benchmark instrumentation and action-space shortcuts that make learning and evaluation easier than unaided human-style play

## 6. Evaluation protocol
- Main score: in-game score or game progress
- Auxiliary score(s): move count and world-change detection for supported games
- Evaluation style: native score / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: random, NAIL, TDQN, and DRRN agents are compared on 32 supported games; no controlled human baseline is reported
- Automatic verifiability: high for supported games
- Calibration method: standardized support across 56 games with score, move count, and world-change detection; the experiments normalize scores by maximum possible game score and explicitly report agent handicaps
- Anti-contamination argument: not central
- Reliability or comparability concerns: parser ambiguity and unsupported-game coverage remain limitations, and the strongest learning setups rely on Jericho handicaps such as valid-action detection or template-restricted action spaces

## 7. Main contributions
- Contribution 1: Introduces Jericho as a learning environment for human-authored interactive fiction games.
- Contribution 2: Brings 56 supported text games into a shared benchmarkable interface with score and world-change tracking.
- Contribution 3: Frames parser-based IF as a strong testbed for language-based autonomous agents.

## 8. Main findings and failure modes
- Core empirical takeaway: interactive fiction remains difficult because action spaces are combinatorial and progress requires sustained language-grounded planning; the reported agents achieve low normalized completion across the 32-game evaluation.
- Notable model failure mode 1: poor exploration under large combinatorial command spaces
- Notable model failure mode 2: weak commonsense or affordance understanding in text worlds
- Notable model failure mode 3: dependence on walkthrough-derived action reductions for tractable learning
- Does this paper reveal a benchmark-design limitation as well? yes; it shows that full parser-based action spaces are so large that many benchmark methods still need action-space simplification

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Early evidence that games can preserve closed-loop language interaction, sparse feedback, and long-horizon consequences rather than reducing language ability to static QA.
- Best use in Section 1 (taxonomy and evolutionary levels): Anchor for the `Arc` / `Wrapped` / curated-suite branch of text-game benchmarks, and a useful boundary case showing that many-game coverage inside one genre is not the same as Level 5 open-ended general-game evaluation.
- Best use in Section 2 (core capabilities evaluated by games): Supports claims about language-grounded planning, combinatorial action generation, commonsense affordance reasoning, and textual mapping/state tracking as game-specific capability pressures.
- Best use in Section 3 (interaction and evaluation paradigm): Strong paradigm example for how score, move count, world-change detection, templates, vocabulary, valid-action detection, and other handicaps convert free-form parser games into benchmarkable interfaces while adding privilege.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Helps argue that long-horizon text-game difficulty is often bottlenecked by exploration and action-space management, and that instrumentation can change the evidence from ecological play to scaffolded diagnostic play.

## 10. Relation to nearby papers
- Closest predecessor(s): TextWorld and earlier text-game RL work
- Closest follow-up(s): TextQuests and later long-horizon IF benchmarks
- Best comparison targets inside our corpus: NetHackLearningEnvironment, TextQuests, TextAtari, Mars
- What this paper uniquely adds relative to neighbors: It converts classic human-authored interactive fiction into a reusable benchmark platform rather than a single new environment.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- The paper introduces Jericho as an environment for man-made interactive fiction games and argues that IF games are an excellent testbed for language-based autonomous agents.
- Jericho supports score detection, move counts, and world-change detection for 56 supported games.
- Jericho also exposes templates and parser vocabulary that can be combined into a tractable game-specific action space.
- The paper highlights combinatorial action spaces, language understanding, and commonsense reasoning as central challenges.
- The experiments evaluate random, NAIL, TDQN, and DRRN agents on 32 supported games; normalized completion scores remain low overall.
- The paper explicitly reports handicaps such as input additions, templates/vocabulary, world-object-tree access, and valid-action detection, and encourages future work to report such assumptions.
- The future-work section proposes using supported games as a test set and a larger pool of unsupported games as training data, indicating that truly general IF game playing is not established by the main experiments.

### 11.2 Our synthesis / interpretation
- Jericho is a foundational precursor card for the survey because later text-game work repeatedly builds on its framing of long-horizon language environments.
- It is especially useful for connecting classical text games to modern LLM-agent benchmarks.
- It should be cited as an instrumented text-game platform, not as a clean ecological benchmark in the same sense as later end-to-end agent evaluations.
- It should support fixed-suite text-game lineage and interface-privilege claims, not broad claims that models can generalize across arbitrary games.

### 11.3 Uncertain or needs re-check
- Re-check the exact baseline agents and how much action-space reduction they use if we later compare Jericho directly with TextQuests.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? Audit completed from the full paper; reread only if we later need detailed comparisons among DRRN, TDQN, and NAIL or a precise account of Jericho handicaps.
- Which section to read next if needed: Sections 4 to 6
- Follow-up question(s): How much of later long-horizon text-agent progress comes from better backbones versus better action-space management?

## 13. Registry sync
- Registry row synced: yes
- Registry status: finalized
- Priority: P1
- Reading depth: deep
- Batch ID: B05
- Outline sections: 0,1,2,3,4
- Survey role: anchor
- Paper card path: `paper_cards/B05/InteractiveFictionGames.md`
- Check status: unchecked
- Next action: draft-section
- Last updated: 2026-04-27
