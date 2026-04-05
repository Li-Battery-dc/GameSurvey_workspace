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
- Historical stage: benchmark expansion / platform vision
- Narrative level(s): L2 strategic reasoning / L4 embodied multimodal interaction
- Most relevant outline section(s): 0,1,2,5,7
- Role in corpus: anchor

## 3. Design-space coding
### 3.1 Environment structure
- Information structure: mixed
- Transition structure: mixed
- Agent structure: mixed
- Social structure: mixed
- Time structure: mixed

### 3.2 World structure
- World type(s): mixed human digital games
- Real game / simulated game / designed task-game hybrid: real human games adapted into standardized benchmark instances
- Benchmark unit: short play episode

### 3.3 Benchmark scope
- Scope: open-ended platform
- Number of games / tasks: 100 in the proof-of-concept release
- Benchmark intent: open-ended general evaluation

### 3.4 Modality
- Primary modality: visual control
- Perception burden retained: raw UI understanding, world-model learning, memory, planning, action timing
- Perception burden removed: some platform-specific friction through standardization and containerization

## 4. What this benchmark measures
- Primary capability target: broad human-game competence as a proxy for machine general intelligence
- Secondary capability target(s): cross-game generalization, sample efficiency, action efficiency, human-relative performance
- Does it test rule grounding / legal action generation? partially
- Does it test strategic planning under uncertainty? partially
- Does it test social reasoning / deception / cooperation? partially, depending on the game
- Does it test visual grounding / spatial-temporal reasoning? yes
- Does it test long-horizon autonomy / task completion? partially; the proof-of-concept uses short episodes
- Does it test real-time efficiency? yes
- Does it test cross-game transfer / open-ended generalization? yes
- Why is a game environment especially suitable here? Human games already encode diverse cognitive demands and keep evolving faster than static benchmark curation can.

## 5. Interaction paradigm
- Observation channel: game screens and standardized game instances
- Action channel: game controls executed in the benchmarked environments
- Interface type: GUI / other
- Agent scaffold allowed: none
- Is there privileged API access? no
- How close is the setup to human play? high in spirit, though the platform standardizes and containerizes games for benchmark use
- Main ecological-validity trade-off: AI GameStore gains breadth and realism, but the current proof-of-concept still uses short episodes rather than full-game mastery.

## 6. Evaluation protocol
- Main score: human-relative game performance
- Auxiliary score(s): average percentage of human score and speed comparisons
- Evaluation style: human-vs-AI / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: 106 human players versus 7 frontier VLMs
- Automatic verifiability: mixed
- Calibration method: representative game sourcing from major digital storefront charts and direct human comparison
- Anti-contamination argument: yes; the paper explicitly motivates open-ended human games as a way to resist benchmark saturation
- Reliability or comparability concerns: the current platform is still a proof of concept with only 100 games and short evaluation windows

## 7. Main contributions
- Contribution 1: Frames the "Multiverse of Human Games" as a benchmark space for machine general intelligence.
- Contribution 2: Introduces a human-in-the-loop platform for sourcing and standardizing representative human digital games.
- Contribution 3: Provides a first 100-game benchmark slice with model-versus-human comparisons.

## 8. Main findings and failure modes
- Core empirical takeaway: current frontier VLMs remain far below humans across the GameStore proof-of-concept slice
- Notable model failure mode 1: models score below 10% of human average on the majority of games
- Notable model failure mode 2: world-model learning, memory, and planning remain major bottlenecks
- Notable model failure mode 3: models are much slower than humans in play
- Does this paper reveal a benchmark-design limitation as well? yes; the current benchmark slice is compelling but still only a first step toward the much larger platform vision

## 9. Why this paper matters for our survey
- Best use in Section 0 (why games): One of the clearest statements for why human games may be a uniquely strong evaluation substrate.
- Best use in Section 1 (historical evolution): Captures the move from curated fixed suites toward open-ended benchmark generation.
- Best use in Section 2 (design space): Useful as a maximal-breadth counterpoint to narrow or synthetic suites.
- Best use in Section 3 (capability targets): Supports claims about memory, planning, and world-model demands in broad game play.
- Best use in Section 4 (interaction paradigm): Strong evidence for human-like GUI interaction as an evaluation target.
- Best use in Section 5 (evaluation protocol): Useful human-relative evaluation anchor.
- Best use in Section 6/7 (limitations and future): One of the strongest papers for arguing that benchmark saturation is a design problem, not just a model problem.

## 10. Relation to nearby papers
- Closest predecessor(s): general game-playing and broad multimodal game benchmarks
- Closest follow-up(s): open-ended platform benchmarks and living game suites
- Best comparison targets inside our corpus: Orak, MCU, GVGAI-LLM, BALROG
- What this paper uniquely adds relative to neighbors: It treats the space of human games itself as the benchmark object instead of curating a single fixed suite.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- The paper defines the "Multiverse of Human Games" and proposes AI GameStore as a platform for sourcing representative human games.
- The proof-of-concept release contains 100 games adapted from Apple App Store and Steam top charts.
- Across seven frontier VLMs and human comparisons, the best models achieve less than 10% of the human average on most games and remain well below humans overall.

### 11.2 Our synthesis / interpretation
- AI GameStore is more important as a framing and benchmark-design paper than as a mature finished benchmark.
- It is nevertheless already strong enough to anchor the survey's anti-saturation and open-endedness discussion.

### 11.3 Uncertain or needs re-check
- Recheck the methods section if we later need the exact game-sourcing pipeline or the precise human-normalization formula.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? A targeted reread may be worthwhile later because the synthesis pipeline matters for Section 7.
- Which section to read next if needed: platform-construction methodology and human-comparison setup
- Follow-up question(s): Should AI GameStore anchor the survey's future-work section on open-ended evaluation?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P0
- Reading depth: deep
- Batch ID: B05
- Outline sections: 0,1,2,5,7
- Survey role: anchor
- Paper card path: `paper_cards/B05/AIGameStore.md`
- Next action: draft-section
- Last updated: 2026-04-05
