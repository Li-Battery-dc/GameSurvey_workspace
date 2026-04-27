# AIGameStore AI GAMESTORE: Scalable, Open-Ended Evaluation of Machine General Intelligence with Human Games

## 0. Metadata
- Date: 2026/02
- Venue: arXiv
- Authors: Lance Ying, Ryan Truong, Prafull Sharma, Kaiya Ivy Zhao, Nathan Cloos, Kelsey R. Allen, Thomas L. Griffiths, Katherine M. Collins, José Hernández-Orallo, Phillip Isola, Samuel J. Gershman, Joshua B. Tenenbaum
- Paper link: https://arxiv.org/pdf/2602.17594v1
- Code link:
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: medium
- Review gate label: strong

## 1. One-paragraph benchmark summary
- AI GameStore argues that human digital games should become a scalable, open-ended testbed for machine general intelligence. The paper frames this as the "Multiverse of Human Games," then instantiates a first proof-of-concept platform that uses LLMs plus humans-in-the-loop to source and adapt 100 representative games from Apple App Store and Steam charts. It evaluates seven frontier VLMs against human players on short episodes and finds that current models remain far below human performance. For this survey, the paper is one of the clearest anchors for the open-ended, anti-saturation branch.

## 2. Position in our survey
- Why-games relevance: Human games supply a broad, culturally evolved, and hard-to-saturate space for evaluating human-like general intelligence.
- Historical stage: open-ended general-game benchmark
- Benchmark level(s): L4 visual agency / L5 cross-game generalization
- Most relevant outline section(s): 0,1,3,4
- Role in corpus: anchor

## 3. Design-space coding
### 3.1 Structure
- Form: Mixed
- Construction: Generated
- Construction note: real human games adapted into standardized benchmark instances
- Benchmark unit: short play episode

### 3.2 Mechanics profile
- State visibility: mixed
- Transition uncertainty: mixed
- Actor configuration: mixed
- Incentive structure: mixed
- Temporal regime: hybrid

### 3.3 Benchmark scope
- Scope: expandable suite
- Number of games / tasks: 100 in the proof-of-concept release

### 3.4 Modality
- Observation modality: mixed
- Action modality: native control
- Perception burden retained: raw UI understanding, world-model learning, memory, planning, action timing
- Perception burden removed: raw commercial-game execution is replaced by standardized p5.js adaptations and pause-based interaction

## 4. What this benchmark measures
- Primary capability target: broad human-game competence as a proxy for machine general intelligence
- Secondary capability target(s): cross-game generalization, benchmark scalability, action efficiency, human-relative performance
- Does it test rule grounding / legal action generation? partially
- Does it test strategic planning under uncertainty? partially
- Does it test social reasoning / deception / cooperation? partially, depending on the game
- Does it test visual grounding / spatial-temporal reasoning? yes
- Does it test long-horizon autonomy / task completion? partially; the proof-of-concept uses short episodes
- Does it test real-time efficiency? yes
- Does it test cross-game transfer / open-ended generalization? yes
- Why is a game environment especially suitable here? Human games already encode diverse cognitive demands and keep evolving faster than static benchmark curation can.

## 5. Interaction paradigm
- Observation channel: game screenshots, textual game descriptions, action history, and a scratchpad carried across pauses
- Action channel: keyboard actions emitted in five 0.2-second chunks for each paused one-second interval
- Interface type: hybrid
- Agent scaffold allowed: memory
- Is there privileged API access? no
- How close is the setup to human play? medium; the games are adapted from human titles, but the evaluated harness pauses every second and constrains output to keyboard action lists
- Main ecological-validity trade-off: AI GameStore gains breadth and human-relative comparison, but the evaluated suite uses regenerated browser games, standardized controls, and pause-based inference rather than raw commercial-game play.

## 6. Evaluation protocol
- Main score: geometric mean of model scores normalized to median human performance on each game
- Auxiliary score(s): per-game normalized score trajectories, model median normalized score, and runtime for the 120-second play budget
- Evaluation style: human-vs-AI / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: 106 human participants each play 10 games for two minutes, while 7 frontier VLMs are evaluated with a standardized pause-and-act harness
- Automatic verifiability: mixed
- Calibration method: marketplace sampling, human-relative normalization to per-game median scores, and bootstrap confidence intervals
- Anti-contamination argument: partial; the paper motivates continual sourcing and variant generation as anti-saturation mechanisms, but it does not claim contamination can be fully ruled out
- Reliability or comparability concerns: the current platform is a proof of concept with 100 regenerated games, short evaluation windows, and a harness that differs materially from direct human play

## 7. Main contributions
- Contribution 1: Frames the "Multiverse of Human Games" as a benchmark space for machine general intelligence.
- Contribution 2: Introduces a human-in-the-loop platform for sourcing and standardizing representative human digital games.
- Contribution 3: Provides a first 100-game benchmark slice with model-versus-human comparisons.

## 8. Main findings and failure modes
- Core empirical takeaway: current frontier VLMs remain far below humans on the 100-game proof-of-concept suite, with the best models staying below 10 on the human-median-normalized geometric-mean scale
- Notable model failure mode 1: many hard games remain effectively unsolved, with models often falling below 1% to 10% of median human performance
- Notable model failure mode 2: world-model learning, memory, and planning remain major bottlenecks
- Notable model failure mode 3: models take roughly 12x to 18x longer than humans to complete the same 120-second play budget
- Does this paper reveal a benchmark-design limitation as well? yes; the current benchmark slice is compelling but still only a first step toward the much larger platform vision

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): One of the clearest statements for why human games may be a uniquely strong evaluation substrate.
- Best use in Section 1 (taxonomy and evolutionary levels): Captures the move from curated fixed suites toward open-ended benchmark generation. Useful as a maximal-breadth counterpoint to narrow or synthetic suites.
- Best use in Section 2 (core capabilities evaluated by games): Supports claims about memory, planning, and world-model demands in broad game play.
- Best use in Section 3 (interaction and evaluation paradigm): Strong human-relative evaluation case, but also a useful caution that pause-based harness design materially changes the interaction regime.
- Best use in Section 4 (synthesis, bottlenecks, and future design): One of the strongest papers for arguing that benchmark saturation is a design problem, but the current implementation should still be framed as an early platform prototype.

## 10. Relation to nearby papers
- Closest predecessor(s): general game-playing and broad multimodal game benchmarks
- Closest follow-up(s): open-ended platform benchmarks and living game suites
- Best comparison targets inside our corpus: Orak, GVGAILLM, GameVerse, LMGameBench
- What this paper uniquely adds relative to neighbors: It treats the space of human games itself as the benchmark object instead of curating a single fixed suite.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- The paper defines the "Multiverse of Human Games" and proposes AI GameStore as a platform for sourcing representative human games.
- The proof-of-concept release contains 100 games adapted from Apple App Store and Steam top charts.
- Across seven frontier VLMs and 106 human participants, the best models achieve geometric-mean scores below 10 on a scale where each game's human median is normalized to 100.

### 11.2 Our synthesis / interpretation
- AI GameStore is more important as a framing and benchmark-design paper than as a mature finished benchmark.
- The evaluated artifact is best treated as a 100-game proof-of-concept suite for a larger living-benchmark vision, not as a settled end-state platform.

### 11.3 Uncertain or needs re-check
- The paper does not fully settle how faithfully regenerated games preserve the cognitive demands of the source commercial titles, or how much future variants will mitigate contamination in practice.
- Recheck the methods section if we later need the exact human-normalization formula or harness prompt details.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? A targeted reread may be worthwhile later because the synthesis pipeline matters for Section 7.
- Which section to read next if needed: platform-construction methodology and human-comparison setup
- Follow-up question(s): Should AI GameStore anchor the survey's synthesis section on open-ended evaluation?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P0
- Reading depth: deep
- Batch ID: B06
- Outline sections: 0,1,3,4
- Survey role: anchor
- Paper card path: `paper_cards/B06/AIGameStore.md`
- Check status: unchecked
- Next action: draft-section
- Last updated: 2026-04-27
