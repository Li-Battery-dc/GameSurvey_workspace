# StarDojo StarDojo: Benchmarking Open-Ended Behaviors of Agentic Multimodal LLMs in Production-Living Simulations with Stardew Valley

## 0. Metadata
- Date: 2025/07
- Venue: arXiv
- Authors: Weihao Tan, Changjiu Jiang, Yu Duan, Mingcong Lei, Jiageng Li, Yitian Hong, Xinrun Wang, Bo An
- Paper link: https://arxiv.org/pdf/2507.07445v2.pdf
- Code link: https://github.com/StarDojo2025/stardojo
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: high
- Review gate label: strong

## 1. One-paragraph benchmark summary
- StarDojo is an open-ended multimodal benchmark built on Stardew Valley that targets production-living behavior rather than only combat or navigation. It provides 1,000 tasks across farming, crafting, exploration, combat, and social interaction, plus a 100-task `StarDojo-Lite` subset and a much longer playthrough objective aimed at earning one million in-game currency. The environment exposes both screenshots and structured textual state, supports pausing during inference, and includes task-specific automatic evaluators based on state comparison. For this survey, StarDojo is a major anchor for open-world daily-life simulation as a game benchmark for agentic MLLMs.

## 2. Position in our survey
- Why-games relevance: Production-living simulators package long-horizon planning, resource management, and social interaction into a grounded interactive world with reusable evaluation hooks.
- Historical stage: open-ended general-game benchmark
- Narrative level(s): L2 strategic reasoning / L4 visual agency / L5 cross-game generalization
- Most relevant outline section(s): 3,4,5,6,7
- Role in corpus: representative

## 3. Design-space coding
### 3.1 Environment structure
- Information structure: mixed
- Transition structure: mixed
- Agent structure: single-agent
- Social structure: mixed
- Time structure: hybrid

### 3.2 World structure
- World type(s): sandbox / open-world / other
- Real game / simulated game / designed task-game hybrid: commercial game with benchmark task wrappers
- Benchmark unit: task episode / open-world session

### 3.3 Benchmark scope
- Scope: open-ended world
- Number of games / tasks: 1,000 tasks plus 100-task StarDojo-Lite and an extended playthrough task
- Benchmark intent: ecological evaluation

### 3.4 Modality
- Primary modality: mixed
- Perception burden retained: first-person screenshots, local spatial reasoning, state monitoring, and task coordination over time
- Perception burden removed: direct mod access exposes internal state and callable skills, reducing raw interface friction

## 4. What this benchmark measures
- Primary capability target: open-ended multimodal task completion in a daily-life simulation world
- Secondary capability target(s): long-term planning, spatial grounding, task allocation over time, social interaction, and economic management
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? yes
- Does it test social reasoning / deception / cooperation? partially
- Does it test visual grounding / spatial-temporal reasoning? yes
- Does it test long-horizon autonomy / task completion? yes
- Does it test real-time efficiency? partially
- Does it test cross-game transfer / open-ended generalization? partially
- Why is a game environment especially suitable here? Stardew Valley naturally combines work, exploration, economy, and social life in one persistent world.

## 5. Interaction paradigm
- Observation channel: gameplay screenshots plus structured textual observations about nearby tiles, inventory, character state, and global state
- Action channel: high-level callable skills such as movement, interaction, item selection, and menu operations
- Interface type: GUI interaction / API / hybrid
- Agent scaffold allowed: memory / other
- Is there privileged API access? yes
- How close is the setup to human play? medium; the world is real and rich, but actions and state are significantly abstracted through the mod and Python wrapper
- Main ecological-validity trade-off: StarDojo gains scalability and evaluability by exposing structured state and pausing the world, which makes it less human-like than pure screen-and-input play

## 6. Evaluation protocol
- Main score: task success rate on StarDojo-Lite and full task suites
- Auxiliary score(s): success by category and difficulty, plus progress on long playthrough
- Evaluation style: completion rate / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: several frontier MLLM agents are tested on the shared task suites, typically with three runs per task
- Automatic verifiability: high
- Calibration method: task-specific evaluators compare current and previous game state, and task initial states are standardized through save files and init commands
- Anti-contamination argument: live interaction with a modded commercial game plus many procedurally configured tasks reduces answer memorization
- Reliability or comparability concerns: performance depends strongly on the privileged observation subset and the provided action abstractions, especially for navigation-heavy tasks

## 7. Main contributions
- Contribution 1: Introduces a large open-ended benchmark on Stardew Valley with 1,000 tasks and a practical lite subset.
- Contribution 2: Builds a cross-platform environment with multimodal observations, task initialization, and automatic evaluation.
- Contribution 3: Shows that current MLLM agents fail badly on medium and hard tasks, especially navigation-heavy and social tasks.

## 8. Main findings and failure modes
- Core empirical takeaway: the best evaluated model reaches only 12.7% overall success on StarDojo-Lite, with performance collapsing on medium and hard tasks.
- Notable model failure mode 1: inability to localize and approach target objects reliably in visual scenes
- Notable model failure mode 2: excessive caution and inefficient movement leading to step-limit failures
- Notable model failure mode 3: hallucinated or inconsistent use of textual state relative to the image
- Does this paper reveal a benchmark-design limitation as well? yes; it shows that richer observation APIs materially change difficulty, so benchmark reporting must expose what state is privileged

## 9. Why this paper matters for our survey
- Best use in Section 0 (why games): Strong evidence that games can model everyday productivity, planning, and social behavior in one world.
- Best use in Section 1 (historical evolution): Represents the move toward open-world life-simulation benchmarks for agentic MLLMs.
- Best use in Section 2 (design space): A key case for open-world, task-wrapped commercial games.
- Best use in Section 3 (capability targets): Supports claims about navigation, planning, social interaction, and multimodal grounding.
- Best use in Section 4 (interaction paradigm): Useful for discussing privileged APIs versus more human-like interfaces.
- Best use in Section 5 (evaluation protocol): Strong example of scalable automatic evaluation through state-difference task checkers.
- Best use in Section 6/7 (limitations and future): Supports the need for better spatial grounding and more explicit communication tools in collaborative/open-ended settings.

## 10. Relation to nearby papers
- Closest predecessor(s): Cradle-style game agents, CivRealm
- Closest follow-up(s): TeamCraft, GameArena
- Best comparison targets inside our corpus: TeamCraft, CivRealm, Mars, TextQuests, LMGAME-BENCH
- What this paper uniquely adds relative to neighbors: It targets everyday production-living behavior and social routines rather than only combat, navigation, or board-state reasoning.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- StarDojo contains 1,000 tasks across farming, crafting, exploration, combat, and social categories, plus a 100-task lite subset.
- The environment exposes screenshots, textual state, callable actions, and automatic evaluators based on state comparison.
- The best reported overall success on StarDojo-Lite is 12.7%, with near-zero success on many medium and hard tasks.

### 11.2 Our synthesis / interpretation
- StarDojo is one of the strongest corpus papers for arguing that open-world life simulators offer a broader ecological benchmark than combat-centric games alone.
- It is especially useful when discussing how benchmark wrappers can trade off ecological realism against reliable large-scale evaluation.

### 11.3 Uncertain or needs re-check
- Re-check the exact number of tasks per category and the full playthrough protocol if we later need a detailed table.
- Re-check whether map-level global information is fully excluded in the main experimental setting or only in some tasks.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? Yes later, because this paper can anchor the open-world limitations section.
- Which section to read next if needed: observation space / action space / qualitative failure analysis
- Follow-up question(s): Which benchmark setting is the fairest "default" comparison point for future work: the lite subset, the full suite, or the playthrough task?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P1
- Reading depth: deep
- Batch ID: B10
- Outline sections: 3,4,5,6,7
- Survey role: representative
- Paper card path: `paper_cards/B10/StarDojo.md`
- Next action: draft-section
- Last updated: 2026-04-05
