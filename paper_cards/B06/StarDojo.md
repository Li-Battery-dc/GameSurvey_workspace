# StarDojo StarDojo: Benchmarking Open-Ended Behaviors of Agentic Multimodal LLMs in Production-Living Simulations with Stardew Valley

## 0. Metadata
- Date: 2025/07
- Venue: arXiv
- Authors: Weihao Tan, Changjiu Jiang, Yu Duan, Mingcong Lei, Jiageng Li, Yitian Hong, Xinrun Wang, Bo An
- Paper link: https://arxiv.org/pdf/2507.07445v2.pdf
- Code link: https://github.com/StarDojo2025/stardojo
- Reading depth: deep
- Card status: finalized
- Confidence in this card: high
- Review gate label: strong

## 1. One-paragraph benchmark summary
- StarDojo is a multimodal benchmark built on Stardew Valley that targets production-living behavior rather than only combat or navigation. It provides 1,000 tasks across farming, crafting, exploration, combat, and social interaction, plus a 100-task `StarDojo-Lite` subset and a much longer playthrough objective aimed at earning one million in-game currency. The environment exposes screenshots, structured textual state, high-level callable actions, pausing during inference, and task-specific automatic evaluators based on state comparison. For this survey, StarDojo is a strong ecological benchmark for long-horizon daily-life simulation, but it should be framed as a rich single-world benchmark rather than a cross-game generalization benchmark.

## 2. Position in our survey
- Why-games relevance: Production-living simulators package long-horizon planning, resource management, and social interaction into a grounded interactive world with reusable evaluation hooks.
- Historical stage: ecological agent benchmark
- Benchmark level(s): L3 social intelligence / L4 visual agency / L5 open-ended task generalization
- Most relevant outline section(s): 2,3,4
- Role in corpus: representative

## 3. Design-space coding
### 3.1 Structure
- Form: World
- Construction: Adapted
- Construction note: commercial Stardew Valley wrapped through StarDojoMod/SMAPI, standardized task files, save states, and automatic evaluators
- Benchmark unit: task episode / open-world session

### 3.2 Mechanics profile
- State visibility: mixed
- Transition uncertainty: mixed
- Actor configuration: single-agent
- Incentive structure: mixed
- Temporal regime: hybrid

### 3.3 Benchmark scope
- Scope: open-ended tasks
- Number of games / tasks: 1,000 tasks plus 100-task StarDojo-Lite and an extended playthrough task

### 3.4 Modality
- Observation modality: mixed
- Action modality: semantic
- Perception burden retained: rendered 720p game views, local spatial reasoning, state monitoring, resource scheduling, NPC/task coordination, and task execution over multiple in-game steps or days
- Perception burden removed: StarDojoMod exposes structured state, pause/resume control, and callable action skills, reducing raw keyboard/mouse and full-map-search friction

## 4. What this benchmark measures
- Primary capability target: open-ended multimodal task completion in a daily-life simulation world
- Secondary capability target(s): long-term planning, spatial grounding, task allocation over time, social interaction, and economic management
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? yes
- Does it test social reasoning / deception / cooperation? partially
- Does it test visual grounding / spatial-temporal reasoning? yes
- Does it test long-horizon autonomy / task completion? yes
- Does it test real-time efficiency? partially
- Does it test cross-game transfer / open-ended generalization? no in the cross-game sense; its open-endedness is within one persistent game world
- Why is a game environment especially suitable here? Stardew Valley naturally combines work, exploration, economy, and social life in one persistent world.

## 5. Interaction paradigm
- Observation channel: gameplay screenshots plus structured textual observations about nearby tiles, inventory, character state, and global state
- Action channel: high-level callable skills such as movement, interaction, item selection, and menu operations
- Interface type: native control / API / hybrid
- Agent scaffold allowed: other; the benchmark provides structured text, one-step history, pause-resume support, and high-level skills, while limiting map-level global information and excluding some shortcut navigation support in the main experiments
- Is there privileged API access? yes
- How close is the setup to human play? medium; the world is real and rich, but actions and state are significantly abstracted through the mod and Python wrapper
- Main ecological-validity trade-off: StarDojo gains scalability and evaluability by exposing structured state and pausing the world, which makes it less human-like than pure screen-and-input play

## 6. Evaluation protocol
- Main score: task success rate on StarDojo-Lite and full task suites
- Auxiliary score(s): success by category and difficulty, plus progress on long playthrough
- Evaluation style: completion rate / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: several frontier MLLM agents are tested on the shared task suites, typically with three runs per task; the paper does not provide a direct human baseline
- Automatic verifiability: high
- Calibration method: task-specific evaluators compare current and previous game state, and task initial states are standardized through save files and init commands
- Anti-contamination argument: not a central claim; the paper's contribution is benchmark coverage and instrumentation rather than freshness against pretraining
- Reliability or comparability concerns: performance depends strongly on the privileged observation subset, the provided action abstractions, and the fact that most reported results focus on StarDojo-Lite rather than the full 1,000-task suite

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
- Best use in Section 0 (lead-in and benchmark motivation): Strong evidence that games can model everyday productivity, planning, economy, environmental adaptation, and social behavior in one persistent world rather than isolating a single capability.
- Best use in Section 1 (taxonomy and evolutionary levels): Represents Level-5 single-world open-ended task generalization: a task-wrapped commercial life simulator with 1,000 curated objectives, not a cross-title general-game benchmark.
- Best use in Section 2 (core capabilities evaluated by games): Supports claims about navigation, production chains, resource scheduling, combat, NPC interaction, multimodal grounding, and long-horizon planning. The social evidence should be framed as NPC relationship/trading interaction, not as deep theory-of-mind or multi-agent cooperation.
- Best use in Section 3 (interaction and evaluation paradigm): Useful for discussing privileged wrappers: SMAPI/StarDojoMod expose rendered images, structured textual observations, internal-state initialization, pause-resume inference, action execution, and state-difference evaluators. The image-only, text-only, and real-time ablations make the interface trade-off directly usable.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Supports a bottleneck claim that current MLLM agents fail on spatial grounding, target navigation, medium/hard multi-step tasks, and real-time response pressure even with strong structured support.

## 10. Relation to nearby papers
- Closest predecessor(s): MineDojo, Cradle's Stardew Valley experiments, and other open-world sandbox agent settings
- Closest follow-up(s): later commercial-game benchmark wrappers that combine multimodal observations with automatic evaluators
- Best comparison targets inside our corpus: MCU, MineNPCTask, TeamCraft, GameWorld, FlashAdventure
- What this paper uniquely adds relative to neighbors: It targets everyday production-living behavior, economic routines, and social life inside one commercial world rather than only combat, navigation, or macro-strategy reasoning.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- Stardew Valley includes day/night, energy, weather/seasonal dynamics, production activities, economy, and 45 unique NPCs, giving StarDojo a richer production-living substrate than isolated navigation or combat games.
- StarDojo contains 1,000 tasks across farming, crafting, exploration, combat, and social categories, plus a 100-task StarDojo-Lite subset and an extended playthrough goal of earning one million in-game currency.
- StarDojoMod is built on SMAPI and communicates with the game engine through sockets; it can retrieve rendered images and internal states, execute commands, pause during model inference, run parallel game instances, and support headless operation through Xvfb.
- The main experiments provide 720p screenshots, structured textual observations including a 7x7 local neighborhood and global time/date/budget information, and only current plus previous-step context.
- Seven MLLM agents are evaluated on StarDojo-Lite with three runs per task. GPT-4.1 has the highest overall success rate at 12.7%; other models are below 11%, and medium/hard tasks are near-zero.
- Ablations show that textual information improves grounding, image-only input hurts, removing images hurts tasks that require broader visual context, and disabling pause/resume makes real-time tasks harder because time passes while the model plans.

### 11.2 Our synthesis / interpretation
- StarDojo is one of the strongest corpus papers for arguing that open-world life simulators offer a broader ecological benchmark than combat-centric games alone.
- It is especially useful when discussing how benchmark wrappers trade ecological realism for reliable large-scale evaluation: the world is a real commercial game, but the benchmark relies on privileged observations, action abstractions, state initialization, and automatic checkers.
- It should support visual-agency, long-horizon planning, and production-living generalization claims, not the cross-game-generalization narrative.

### 11.3 Uncertain or needs re-check
- Re-check the exact number of tasks per category and the full playthrough protocol if we later need a detailed table.
- Re-check the precise action-skill inventory and evaluator types if we later build a detailed interaction-design comparison table.
- Keep the limitation visible: running StarDojo requires an official Stardew Valley copy; fishing is excluded; the benchmark focuses on early/mid-game content; and reported model evaluations mainly use StarDojo-Lite.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? Audit completed from the full paper; reread only if we later need a precise comparison of observation subsets, action abstractions, or evaluator design.
- Which section to read next if needed: Sections 3.2 to 3.4 and Appendix C for environment-interface details
- Follow-up question(s): Which benchmark setting is the fairest default comparison point for future work: the Lite subset, the full suite, or the playthrough task?

## 13. Registry sync
- Registry row synced: yes
- Registry status: finalized
- Priority: P1
- Reading depth: deep
- Batch ID: B06
- Outline sections: 2,3,4
- Survey role: representative
- Paper card path: `paper_cards/B06/StarDojo.md`
- Check status: unchecked
- Next action: draft-section
- Last updated: 2026-04-27
