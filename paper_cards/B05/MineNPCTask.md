# MineNPCTask MineNPC-Task: Task Suite for Memory-Aware Minecraft Agents

## 0. Metadata
- Date: 2026/01
- Venue: arXiv
- Authors: Tamil Sudaravan Mohan Doss, Michael Xu, Sudha Rao, Andrew D. Wilson, Balasaravanan Thoravi Kumaravel
- Paper link: https://arxiv.org/pdf/2601.05215.pdf
- Code link:
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: medium
- Review gate label: usable

## 1. One-paragraph benchmark summary
- MineNPC-Task is a Minecraft benchmark and evaluation harness for memory-aware, mixed-initiative LLM agents. Instead of relying on synthetic prompts, it builds tasks from player-authored requests collected through co-play with expert users, then normalizes them into templates with explicit preconditions, dependencies, and machine-checkable validators. The benchmark focuses on how agents clarify ambiguous requests, remember prior context, and recover from failures while acting through public Mineflayer APIs under a bounded-knowledge policy that forbids hidden-state shortcuts. For this survey, it is a strong recent benchmark for long-horizon task execution with memory, repair, and cooperative interaction in an open-world game, but it should be described as API-grounded rather than visually embodied.

## 2. Position in our survey
- Why-games relevance: Minecraft supports long task arcs, tool dependencies, navigation, and mixed-initiative cooperation in a world where outcomes can still be checked from in-world evidence.
- Historical stage: ecological agent benchmark
- Narrative level(s): L2 strategic reasoning / L3 social intelligence
- Most relevant outline section(s): 2,3,4
- Role in corpus: representative

## 3. Design-space coding
### 3.1 Environment structure
- Information structure: mixed
- Transition structure: mixed
- Agent structure: single-agent
- Social structure: cooperative
- Time structure: hybrid

### 3.2 World structure
- World type(s): sandbox / open-world
- Real game / simulated game / designed task-game hybrid: Minecraft-based benchmark with naturalistic player-authored tasks
- Benchmark unit: full task arc / trajectory

### 3.3 Benchmark scope
- Scope: single game
- Number of games / tasks: 44 high-level tasks and 216 subtasks in the initial evaluation snapshot

### 3.4 Modality
- Primary modality: symbolic state
- Perception burden retained: chat-grounded task understanding, inventory and equipment tracking, nearby-entity grounding, navigation, and memory over extended interaction
- Perception burden removed: raw visual perception and low-level motor control are both abstracted through Mineflayer APIs and bounded execution policies

## 4. What this benchmark measures
- Primary capability target: memory-aware mixed-initiative task completion in an open-world game
- Secondary capability target(s): clarification, repair, precondition reasoning, inventory management, and navigation reliability
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? yes
- Does it test social reasoning / deception / cooperation? yes for cooperation and clarification, not deception
- Does it test visual grounding / spatial-temporal reasoning? no; the evaluated setup does not rely on raw visual input
- Does it test long-horizon autonomy / task completion? yes
- Does it test real-time efficiency? partially
- Does it test cross-game transfer / open-ended generalization? no
- Why is a game environment especially suitable here? Minecraft combines grounded tasks, resource dependencies, and long-horizon interaction in a world where validators can judge success from actual game evidence.

## 5. Interaction paradigm
- Observation channel: player chat, inventory and equipment state, nearby entities and blocks within loaded chunks, and lightweight memory traces
- Action channel: natural-language clarification plus high-level actions executed through public Mineflayer APIs
- Interface type: natural language / API / hybrid
- Agent scaffold allowed: memory / planner / other
- Is there privileged API access? yes
- How close is the setup to human play? medium-low; the task structure comes from real co-play, but execution happens under a bounded-knowledge harness with high-level APIs instead of direct GUI control
- Main ecological-validity trade-off: the benchmark preserves realistic user requests and open-world dependencies, but Mineflayer access, bounded clarifications, and validator-backed judging simplify the control problem

## 6. Evaluation protocol
- Main score: validator-based subtask completion
- Auxiliary score(s): failure breakdowns, repair traces, and participant experience measures
- Evaluation style: completion rate / process-level / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: initial benchmark instantiation evaluates GPT-4o across player-authored tasks from 8 experienced players
- Automatic verifiability: high
- Calibration method: explicit preconditions, dependency structure, single-turn clarification, and machine-checkable validators under a bounded-knowledge policy
- Anti-contamination argument: tasks come from user-authored co-play rather than synthetic benchmark prompts, and evaluation is grounded in in-world evidence
- Reliability or comparability concerns: the current empirical snapshot is narrow and depends on one bounded harness design plus one primary model snapshot

## 7. Main contributions
- Contribution 1: Introduces a player-authored Minecraft benchmark for memory-aware mixed-initiative NPC agents.
- Contribution 2: Provides a bounded, reproducible evaluation harness with validators and explicit event logging.
- Contribution 3: Surfaces concrete failure categories such as code execution, inventory handling, referencing, and navigation.

## 8. Main findings and failure modes
- Core empirical takeaway: under the bounded Mineflayer setup, GPT-4o still fails 71 of 216 subtasks, showing that realistic Minecraft assistance remains brittle once memory, repair, and world dependencies are required.
- Notable model failure mode 1: code or execution faults during action realization
- Notable model failure mode 2: inventory and tool misuse across multi-step tasks
- Notable model failure mode 3: navigation, referencing, and context misunderstandings during mixed-initiative interaction
- Does this paper reveal a benchmark-design limitation as well? yes; it shows that fair open-world evaluation depends heavily on bounded policies and validator design

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Strong evidence that games can ground realistic, multi-step user requests in a verifiable environment.
- Best use in Section 1 (taxonomy and evolutionary levels): Useful as a recent Minecraft benchmark that adds memory and mixed initiative to the lineage. Good open-world cooperative benchmark with validator-based evaluation, but not a visual-agency anchor.
- Best use in Section 2 (core capabilities evaluated by games): Direct support for long-horizon memory, repair, and task completion.
- Best use in Section 3 (interaction and evaluation paradigm): Important for natural-language clarification plus tool or API execution. Strong example of machine-checkable validators and bounded benchmark policies.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Supports the claim that memory and repair remain fragile even in heavily instrumented open-world setups.

## 10. Relation to nearby papers
- Closest predecessor(s): MineDojo, TeamCraft, MCU, Minecraft NPC and agent work
- Closest follow-up(s): broader mixed-initiative sandbox benchmarks
- Best comparison targets inside our corpus: EMemBench, StarDojo, MCU, InteractiveFictionGames
- What this paper uniquely adds relative to neighbors: It centers user-authored tasks, memory-aware interaction, and repair traces rather than only benchmark task success.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- The benchmark builds on player-authored Minecraft requests collected through formative and summative co-play with expert players.
- The harness uses explicit preconditions, machine-checkable validators, single-turn clarification, and public Mineflayer APIs under a bounded-knowledge policy.
- In the initial snapshot, GPT-4o is evaluated on 44 tasks comprising 216 subtasks across 8 experienced players, with 71 subtask failures concentrated in code execution, inventory or tool handling, referencing, and navigation.

### 11.2 Our synthesis / interpretation
- MineNPC-Task is one of the more realistic recent cards for Section 6 because it focuses on how open-world agents fail in actual mixed-initiative use.
- It is especially useful as a bridge from sandbox-game benchmarks to benchmark-design questions about fairness and bounded evaluation.
- It should support the scaffolded-API and mixed-initiative discussion, not the visual-agency narrative.

### 11.3 Uncertain or needs re-check
- Re-check the exact mapping from 44 high-level tasks to task families and the formal success metric if we later compare it quantitatively with TeamCraft or MCU.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? Audit completed from the full paper; reread only if we later need exact template schemas, validator JSONs, or breakdown counts by task family.
- Which section to read next if needed: Sections 3 to 6 and Appendix E
- Follow-up question(s): How much of the failure profile is due to memory limits versus Mineflayer-level execution constraints?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P1
- Reading depth: deep
- Batch ID: B05
- Outline sections: 2,3,4
- Survey role: representative
- Paper card path: `paper_cards/B05/MineNPCTask.md`
- Check status: unchecked
- Next action: draft-section
- Last updated: 2026-04-10
