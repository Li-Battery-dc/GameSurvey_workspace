# InteractiveFictionGames Interactive Fiction Games: A Colossal Adventure

## 0. Metadata
- Date: 2019/09
- Venue: AAAI 2020
- Authors: Matthew Hausknecht, Prithviraj Ammanabrolu, Marc-Alexandre Cote, Xingdi Yuan
- Paper link: https://ojs.aaai.org/index.php/AAAI/article/download/6297/6153
- Code link: https://github.com/microsoft/jericho
- Reading depth: structured-skim
- Card status: card-reviewed
- Confidence in this card: medium
- Review gate label: usable

## 1. One-paragraph benchmark summary
- Interactive Fiction Games: A Colossal Adventure introduces Jericho, an environment for studying autonomous language agents in human-authored text-adventure games. The paper argues that parser-based interactive fiction combines combinatorial action spaces, language understanding, commonsense reasoning, and long-horizon planning in a single benchmark family. Jericho supports score detection, move counts, and world-change tracking for a set of 56 human-made games, which makes these historically important text games newly usable as research benchmarks. For this survey, the paper is a key precursor for later long-horizon text-game benchmarks such as TextQuests.

## 2. Position in our survey
- Why-games relevance: Interactive fiction exposes language grounding, exploration, and long-horizon planning inside environments with sparse feedback and machine-verifiable progress.
- Historical stage: ecological agent benchmark
- Narrative level(s): L2 strategic reasoning / L5 cross-game generalization
- Most relevant outline section(s): 0,1,2,3,4
- Role in corpus: anchor

## 3. Design-space coding
### 3.1 Environment structure
- Information structure: imperfect
- Transition structure: mixed
- Agent structure: single-agent
- Social structure: N/A
- Time structure: turn-based

### 3.2 World structure
- World type(s): adventure
- Real game / simulated game / designed task-game hybrid: suite of real human-authored interactive fiction games
- Benchmark unit: full game run

### 3.3 Benchmark scope
- Scope: curated suite
- Number of games / tasks: 56 supported games
- Benchmark intent: train+eval foundation

### 3.4 Modality
- Primary modality: text
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
- Does it test cross-game transfer / open-ended generalization? yes
- Why is a game environment especially suitable here? Text adventures combine natural-language interaction with long, branching task structure and precise reward signals.

## 5. Interaction paradigm
- Observation channel: room descriptions, parser feedback, inventory changes, score, and move counts
- Action channel: free-form text commands
- Interface type: natural language
- Agent scaffold allowed: none in the core benchmark framing
- Is there privileged API access? yes; Jericho exposes score, move count, and world-change information for supported games
- How close is the setup to human play? medium-high; play remains parser-based, but the environment instrumentation makes learning and evaluation easier than raw emulator use
- Main ecological-validity trade-off: Jericho preserves classic text-game interaction while adding benchmark instrumentation that slightly reduces opacity

## 6. Evaluation protocol
- Main score: in-game score or game progress
- Auxiliary score(s): move count and world-change detection for supported games
- Evaluation style: native score / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: the paper studies text agents across a broad set of supported games
- Automatic verifiability: high for supported games
- Calibration method: standardized environment support across 56 games with score and world-change detection
- Anti-contamination argument: not central
- Reliability or comparability concerns: parser ambiguity and unsupported-game coverage remain limitations, and some methods rely on walkthrough-derived action reductions

## 7. Main contributions
- Contribution 1: Introduces Jericho as a learning environment for human-authored interactive fiction games.
- Contribution 2: Brings 56 supported text games into a shared benchmarkable interface with score and world-change tracking.
- Contribution 3: Frames parser-based IF as a strong testbed for language-based autonomous agents.

## 8. Main findings and failure modes
- Core empirical takeaway: interactive fiction remains difficult because action spaces are combinatorial and progress requires sustained language-grounded planning.
- Notable model failure mode 1: poor exploration under large combinatorial command spaces
- Notable model failure mode 2: weak commonsense or affordance understanding in text worlds
- Notable model failure mode 3: dependence on walkthrough-derived action reductions for tractable learning
- Does this paper reveal a benchmark-design limitation as well? yes; it shows that full parser-based action spaces are so large that many benchmark methods still need action-space simplification

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Strong early example of how games package language grounding and long-horizon planning.
- Best use in Section 1 (taxonomy and evolutionary levels): Core historical root for later text-game agent benchmarks. Useful for the text-adventure region of the survey taxonomy.
- Best use in Section 2 (core capabilities evaluated by games): Supports long-horizon planning, exploration, and rule grounding.
- Best use in Section 3 (interaction and evaluation paradigm): Anchor case for free-form natural-language action. Important precursor for score-based and progress-based text-game evaluation.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Helps explain why long-horizon text benchmarks remain hard even with strong language models.

## 10. Relation to nearby papers
- Closest predecessor(s): TextWorld and earlier text-game RL work
- Closest follow-up(s): TextQuests and later long-horizon IF benchmarks
- Best comparison targets inside our corpus: TextQuests, TextAtari, Mars, NetHackLearningEnvironment
- What this paper uniquely adds relative to neighbors: It converts classic human-authored interactive fiction into a reusable benchmark platform rather than a single new environment.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- The paper introduces Jericho as an environment for man-made interactive fiction games and argues that IF games are an excellent testbed for language-based autonomous agents.
- Jericho supports score detection, move counts, and world-change detection for 56 supported games.
- The paper highlights combinatorial action spaces, language understanding, and commonsense reasoning as central challenges.

### 11.2 Our synthesis / interpretation
- Jericho is a foundational precursor card for the survey because later text-game work repeatedly builds on its framing of long-horizon language environments.
- It is especially useful for connecting classical text games to modern LLM-agent benchmarks.

### 11.3 Uncertain or needs re-check
- Re-check the exact baseline agents and how much action-space reduction they use if we later compare Jericho directly with TextQuests.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? Yes, if we later need a cleaner historical bridge from TextWorld to modern IF-agent benchmarks.
- Which section to read next if needed: environment support / experiments / discussion
- Follow-up question(s): How much of later long-horizon text-agent progress comes from better backbones versus better action-space management?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P1
- Reading depth: structured-skim
- Batch ID: B10
- Outline sections: 0,1,2,3,4
- Survey role: anchor
- Paper card path: `paper_cards/B10/InteractiveFictionGames.md`
- Next action: draft-section
- Last updated: 2026-04-08
