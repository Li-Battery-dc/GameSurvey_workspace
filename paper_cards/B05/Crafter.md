# Crafter Benchmarking the Spectrum of Agent Capabilities

## 0. Metadata
- Date: 2021/09
- Venue: ICLR 2022
- Authors: Danijar Hafner
- Paper link: https://arxiv.org/pdf/2109.06780.pdf
- Code link: https://github.com/danijar/crafter
- Reading depth: structured-skim
- Card status: card-reviewed
- Confidence in this card: medium
- Review gate label: usable

## 1. One-paragraph benchmark summary
- Crafter is an open-world survival environment designed to evaluate a broad spectrum of agent abilities within a single game rather than across many separate benchmarks. Agents receive only raw 64x64 image observations and are scored through semantically meaningful achievements, which range from basic resource collection to tool creation and survival milestones. The paper's main benchmark argument is that a single, carefully designed world can reveal generalization, deep exploration, and long-horizon reasoning more efficiently than running many narrow tasks. For this survey, Crafter is an important historical precursor for later LLM and VLM game-benchmark work that uses one rich game world to test multiple capabilities.

## 2. Position in our survey
- Why-games relevance: A survival game can package exploration, planning, resource dependencies, and long horizons into one automatically scored environment.
- Historical stage: ecological agent benchmark
- Narrative level(s): L4 visual agency / L5 cross-game generalization
- Most relevant outline section(s): 0,1,2,3,7
- Role in corpus: anchor

## 3. Design-space coding
### 3.1 Environment structure
- Information structure: imperfect
- Transition structure: stochastic
- Agent structure: single-agent
- Social structure: N/A
- Time structure: hybrid

### 3.2 World structure
- World type(s): sandbox / open-world
- Real game / simulated game / designed task-game hybrid: designed task-game hybrid built as a research environment
- Benchmark unit: episode

### 3.3 Benchmark scope
- Scope: single game
- Number of games / tasks: 1 environment with 22 achievements
- Benchmark intent: diagnostic evaluation / train+eval foundation

### 3.4 Modality
- Primary modality: image
- Perception burden retained: local visual observation, exploration, resource management, and long-horizon planning
- Perception burden removed: no language understanding or high-fidelity 3D control burden

## 4. What this benchmark measures
- Primary capability target: broad agent competence inside one rich environment
- Secondary capability target(s): deep exploration, long-term reasoning, achievement breadth, and generalization across survival subskills
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? yes
- Does it test social reasoning / deception / cooperation? no
- Does it test visual grounding / spatial-temporal reasoning? yes
- Does it test long-horizon autonomy / task completion? yes
- Does it test real-time efficiency? partially
- Does it test cross-game transfer / open-ended generalization? partially
- Why is a game environment especially suitable here? A survival world naturally builds dependency chains among resources, tools, and hazards, which lets a single environment test many abilities at once.

## 5. Interaction paradigm
- Observation channel: local top-down RGB view plus standard environment feedback
- Action channel: discrete control actions for movement, interaction, combat, and crafting
- Interface type: GUI interaction / structured action space / hybrid
- Agent scaffold allowed: none
- Is there privileged API access? no in the core benchmark
- How close is the setup to human play? medium; the world is game-like and visually grounded, though simplified relative to commercial open-world games
- Main ecological-validity trade-off: Crafter is much more realistic than symbolic toy tasks, but its simplified visuals and action space make it more diagnostic than fully ecological

## 6. Evaluation protocol
- Main score: achievement-based benchmark score
- Auxiliary score(s): per-achievement success rates and reward-based learning results
- Evaluation style: milestone / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: RL baselines compare reward-driven and unsupervised agents
- Automatic verifiability: high
- Calibration method: semantically meaningful achievement set and geometric-mean aggregation over achievement success rates
- Anti-contamination argument: custom research environment rather than a heavily documented public game
- Reliability or comparability concerns: a single environment cannot by itself justify broad general-game claims, even if it spans many subskills

## 7. Main contributions
- Contribution 1: Introduces an open-world survival benchmark that evaluates multiple abilities in one environment.
- Contribution 2: Uses 22 semantically meaningful achievements instead of only sparse reward or score.
- Contribution 3: Argues that broad achievement coverage is a practical way to benchmark general agent capabilities.

## 8. Main findings and failure modes
- Core empirical takeaway: unlocking the full achievement spectrum remains difficult, which makes Crafter a durable benchmark for broad agent competence.
- Notable model failure mode 1: weak deep exploration beyond easy early achievements
- Notable model failure mode 2: difficulty sustaining long dependency chains needed for advanced tools and resources
- Notable model failure mode 3: narrow optimization on frequent achievements rather than broad capability growth
- Does this paper reveal a benchmark-design limitation as well? yes; it shows both the value and the limits of using one environment as a proxy for many capabilities

## 9. Why this paper matters for our survey
- Best use in Section 0 (why games): Strong early argument that one game can measure a wide capability spectrum under automatic scoring.
- Best use in Section 1 (historical evolution): Important precursor to later open-world and general-capability game benchmarks.
- Best use in Section 2 (design space): Useful for the distinction between single-world breadth and multi-game breadth.
- Best use in Section 3 (capability targets): Supports long-horizon planning, exploration, and visual grounding claims.
- Best use in Section 4 (interaction paradigm): Useful contrast against later heavily scaffolded LLM-agent interfaces.
- Best use in Section 5 (evaluation protocol): Good reference for achievement-based milestone scoring and geometric-mean aggregation.
- Best use in Section 6/7 (limitations and future): Helps motivate why later work moved from one broad environment to multi-game suites and open-world platforms.

## 10. Relation to nearby papers
- Closest predecessor(s): earlier RL environments such as MiniGrid and Obstacle Tower
- Closest follow-up(s): MineDojo, MCU, TeamCraft, Orak
- Best comparison targets inside our corpus: Orak, MCU, TeamCraft, StarDojo
- What this paper uniquely adds relative to neighbors: It is a clean early case for broad capability evaluation inside one open-world environment rather than a cross-game suite.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- Crafter is an open-world survival game with visual input designed to evaluate a range of general abilities within one environment.
- The benchmark uses 22 achievements and aggregates achievement success rates with a geometric mean.
- The paper argues that consistently unlocking the full set requires strong generalization, deep exploration, and long-term reasoning.

### 11.2 Our synthesis / interpretation
- Crafter is a key historical bridge from RL benchmark design to later LLM and VLM game benchmarks that claim to measure broad agent competence.
- It is best treated as a precursor and conceptual anchor, not as an LLM benchmark in the narrow sense.

### 11.3 Uncertain or needs re-check
- Re-check the exact action-space description and baseline score table if we later compare Crafter quantitatively with later open-world benchmarks.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? A targeted reread is likely useful later because Crafter will support the historical-evolution section.
- Which section to read next if needed: environment / evaluation / discussion
- Follow-up question(s): How much later LLM benchmark work inherits the achievement-style evaluation logic from Crafter?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P1
- Reading depth: structured-skim
- Batch ID: B05
- Outline sections: 0,1,2,3,7
- Survey role: anchor
- Paper card path: `paper_cards/B05/Crafter.md`
- Next action: draft-section
- Last updated: 2026-04-08
