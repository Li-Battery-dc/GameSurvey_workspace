# GameTraversalBenchmark GameTraversalBenchmark: Evaluating Planning Abilities Of Large Language Models Through Traversing 2D Game Maps

## 0. Metadata
- Date: 2024/10
- Venue: NeurIPS 2024 (Datasets and Benchmarks)
- Authors: Muhammad Umair Nasir, Steven James, Julian Togelius
- Paper link: https://arxiv.org/pdf/2410.07765v1.pdf
- Code link: https://github.com/umair-nasir14/Game-Traversal-Benchmark
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: high
- Review gate label: usable

## 1. One-paragraph benchmark summary
- GameTraversalBenchmark (GTB) evaluates LLM planning on diverse 2D grid-based maps represented as character strings and generated through the Word2World pipeline. For each objective on a map, a model must generate an action sequence in one go, and the benchmark scores not only whether the agent reaches the target, but also how close it gets, how long the path is relative to the A* reference, and how many generation errors it makes. GTB also includes an optional one-shot retry condition and simple random baselines, showing that many models still fail to convert rough distance awareness into correct action planning. For this survey, GTB is best used as a symbolic multi-objective planning probe and as a contrast case for scoring "almost-right" plans in static game-like worlds.

## 2. Position in our survey
- Why-games relevance: Traversal tasks turn planning into a measurable sequential control problem with exact optimal-path references.
- Historical stage: diagnostic capability probe
- Narrative level(s): L2 strategic reasoning
- Most relevant outline section(s): 2,3,4
- Role in corpus: contrast

## 3. Design-space coding
### 3.1 Environment structure
- Information structure: perfect
- Transition structure: deterministic
- Agent structure: single-agent
- Social structure: N/A
- Time structure: turn-based

### 3.2 World structure
- World type(s): puzzle / maze / other
- Real game / simulated game / designed task-game hybrid: LLM-generated 2D game-like maps from a game-design pipeline
- Benchmark unit: map episode with multiple objectives

### 3.3 Benchmark scope
- Scope: curated suite
- Number of games / tasks: 150 maps with varied sizes, path lengths, and objective counts
- Benchmark intent: diagnostic evaluation

### 3.4 Modality
- Primary modality: symbolic state / text
- Perception burden retained: parsing map strings, route planning, and multi-objective sequencing
- Perception burden removed: no visual or real-time input

## 4. What this benchmark measures
- Primary capability target: path planning over symbolic maps
- Secondary capability target(s): path efficiency, output-format control, and multi-objective traversal under exact map information
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? no
- Does it test social reasoning / deception / cooperation? no
- Does it test visual grounding / spatial-temporal reasoning? no visual grounding
- Does it test long-horizon autonomy / task completion? partially
- Does it test real-time efficiency? no
- Does it test cross-game transfer / open-ended generalization? partially
- Why is a game environment especially suitable here? Game maps provide exact optimal-path baselines and multiple evaluation metrics beyond simple success or failure.

## 5. Interaction paradigm
- Observation channel: full map strings, current position, current objective coordinates, tile legend, and carried-over reward/state information from prior objectives
- Action channel: zero-shot action sequences over four movement directions, with an optional one-shot retry using previous actions and distance feedback
- Interface type: natural language / structured action space / hybrid
- Agent scaffold allowed: none in zero-shot; the optional one-shot setting adds limited feedback from the previous attempt
- Is there privileged API access? yes
- How close is the setup to human play? low; this is a symbolic planning abstraction
- Main ecological-validity trade-off: GTB isolates planning well but strips away perception, interaction feedback, and richer world dynamics

## 6. Evaluation protocol
- Main score: GTB-Score combining reward, path length, and generation errors
- Auxiliary score(s): mean generation errors, mean path length, mean actions taken, Top-0, Top-1, and Top-5 accuracy
- Evaluation style: hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: multiple LLMs and preliminary large reasoning models are compared against A* optimal references plus Random-FP and Random-RP baselines
- Automatic verifiability: high
- Calibration method: A* shortest paths define optimal references for each objective
- Anti-contamination argument: the 2D symbolic map representation is unusual for LLM training corpora and generated from a game-design pipeline
- Reliability or comparability concerns: the benchmark is static and symbolic, uses a fixed prompt for all models, and reports o1/o1-mini only as single-run preliminary results that are not directly comparable to the multi-seed main table

## 7. Main contributions
- Contribution 1: Builds a map-traversal benchmark over 150 diverse 2D game maps.
- Contribution 2: Introduces a composite metric that includes path quality and generation control.
- Contribution 3: Shows that even strong LLMs remain far from optimal planning in this simple-looking domain, with many models trailing a simple fixed-length random baseline.

## 8. Main findings and failure modes
- Core empirical takeaway: only the strongest frontier models clearly beat the stronger random baseline, and even reasoning models remain well below optimal traversal performance.
- Notable model failure mode 1: generating poor action sequences despite roughly correct path length intuition
- Notable model failure mode 2: syntax or generation-control errors
- Notable model failure mode 3: weak internal map construction on deceptive layouts
- Does this paper reveal a benchmark-design limitation as well? yes; it shows that natural-language planning competence and rough distance estimation do not automatically transfer to symbolic traversal tasks

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Minor contrast only; it shows that game-like traversal tasks give precise planning metrics, but it is not a central motivation anchor for broader game-agent benchmarking.
- Best use in Section 1 (taxonomy and evolutionary levels): Minor boundary-case contrast for symbolic traversal benchmarks derived from game-generation pipelines rather than human-play interfaces.
- Best use in Section 2 (core capabilities evaluated by games): Supports path planning and route-following discussions.
- Best use in Section 3 (interaction and evaluation paradigm): A contrast case for one-shot action-sequence generation. Useful for discussing composite metrics beyond pure success rate.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Shows the limits of simple symbolic planning transfer.

## 10. Relation to nearby papers
- Closest predecessor(s): PlanBench-like symbolic planning tasks
- Closest follow-up(s): MazeEval
- Best comparison targets inside our corpus: ReasoningViaVideo, EvoEmpirBench, MazeEval, DeepPHY
- What this paper uniquely adds relative to neighbors: It combines optimal-path references with generation-quality penalties in a multi-objective traversal setting.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- GTB uses 150 generated maps from the Word2World pipeline with diverse sizes, path lengths, and objective counts.
- It evaluates models with GTB-Score, MGE, MPL, MAT, and Top-0/1/5 accuracy, using A* to define optimal path references per objective.
- The benchmark includes Random-FP and Random-RP baselines, and the paper notes that all but the strongest LLMs perform worse than the fixed-length random baseline.
- The paper reports GPT-4-Turbo at 44.97 GTBS in the main table and o1 at 67.84 GTBS in a preliminary single-run comparison, both still far below optimal A* behavior.

### 11.2 Our synthesis / interpretation
- GTB is a clean symbolic-planning benchmark, but it is best treated as a lower-level probe rather than as evidence of broad game competence.
- It is especially useful when comparing different ways benchmarks score "almost right" plans.
- The paper also suggests that some models may infer approximate path length without constructing a usable internal map for action planning.

### 11.3 Uncertain or needs re-check
- Re-check the exact reward formulas if we later compare GTB-Score directly with other composite metrics.
- Re-check the one-shot versus zero-shot prompt setup if needed for a methods comparison.
- If we later compare GTB to navigation-style agent benchmarks, re-check how much the reward carry-over across objectives matters for its sequential character.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? No immediate reread is needed; the current audit already depends on the benchmark definition, scoring rules, and baseline comparisons.
- Which section to read next if needed: metrics / random-baseline discussion / preliminary reasoning-model results
- Follow-up question(s): How much of the remaining gap comes from planning versus brittle output formatting and action-sequence control?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P2
- Reading depth: deep
- Batch ID: B08
- Outline sections: 2,3,4
- Survey role: contrast
- Paper card path: `paper_cards/B08/GameTraversalBenchmark.md`
- Next action: draft-section
- Check status: unchecked
- Last updated: 2026-04-10
