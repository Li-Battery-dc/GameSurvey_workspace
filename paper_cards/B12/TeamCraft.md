# TeamCraft TeamCraft: A Benchmark for Multi-Modal Multi-Agent Systems in Minecraft

## 0. Metadata
- Date: 2024/12
- Venue: arXiv
- Authors: Qian Long, Zhi Li, Ran Gong, Ying Nian Wu, Demetri Terzopoulos, Xiaofeng Gao
- Paper link: https://arxiv.org/pdf/2412.05255v1.pdf
- Code link: https://github.com/teamcraft-bench/teamcraft
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: high
- Review gate label: strong

## 1. One-paragraph benchmark summary
- TeamCraft is a multimodal multi-agent benchmark in Minecraft aimed at collaborative task planning and execution. It provides 55,000 procedurally generated task variants, multimodal prompts with orthographic views, expert demonstrations for imitation learning, and explicit generalization splits over goals, scenes, and numbers of agents. The benchmark studies building, clearing, farming, and smelting tasks under centralized and decentralized control, and it shows that current VLA-style systems still struggle badly with coordination and generalization. For this survey, TeamCraft is a major reference for visually grounded multi-agent collaboration in open-world environments.

## 2. Position in our survey
- Why-games relevance: Minecraft-like worlds support open-ended cooperation, tool use, spatial planning, and multimodal task specification at scale.
- Historical stage: open-ended general-game benchmark
- Narrative level(s): L4 visual agency / L5 cross-game generalization
- Most relevant outline section(s): 2,3,4
- Role in corpus: representative

## 3. Design-space coding
### 3.1 Environment structure
- Information structure: mixed
- Transition structure: mixed
- Agent structure: multi-agent
- Social structure: cooperative
- Time structure: turn-based / hybrid

### 3.2 World structure
- World type(s): sandbox / open-world
- Real game / simulated game / designed task-game hybrid: Minecraft-based task benchmark
- Benchmark unit: collaborative task episode

### 3.3 Benchmark scope
- Scope: procedural-infinite / open-ended world
- Number of games / tasks: 55,000 task variants across multiple task families
- Benchmark intent: ecological evaluation / train+eval foundation

### 3.4 Modality
- Primary modality: mixed
- Perception burden retained: first-person RGB observation, inventory, spatial reasoning, and multimodal prompt grounding
- Perception burden removed: MineFlayer executes higher-level skills instead of low-level motor control

## 4. What this benchmark measures
- Primary capability target: multimodal collaborative planning and execution
- Secondary capability target(s): coordination under partial information, task allocation, and generalization to new goals, scenes, and agent counts
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? yes
- Does it test social reasoning / deception / cooperation? cooperation
- Does it test visual grounding / spatial-temporal reasoning? yes
- Does it test long-horizon autonomy / task completion? yes
- Does it test real-time efficiency? partially
- Does it test cross-game transfer / open-ended generalization? yes
- Why is a game environment especially suitable here? Minecraft supports rich cooperative tasks with grounded objects and spatial dependencies while remaining highly configurable.

## 5. Interaction paradigm
- Observation channel: first-person RGB views, inventories, and multimodal prompts with language plus orthographic images
- Action channel: high-level skills such as obtaining blocks, farming, placing items, and smelting-related actions
- Interface type: GUI interaction / API / hybrid
- Agent scaffold allowed: planner / demonstrations
- Is there privileged API access? yes in the planning and execution stack
- How close is the setup to human play? medium; the world is rich and multimodal, but the control layer uses high-level skills through MineFlayer
- Main ecological-validity trade-off: TeamCraft preserves a complex world and realistic collaboration structure, but high-level skills and expert demonstrations reduce low-level control burden

## 6. Evaluation protocol
- Main score: task success rate
- Auxiliary score(s): subgoal success rate and redundancy rate
- Evaluation style: completion rate / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: centralized and decentralized baselines are trained and tested on held-out generalization splits
- Automatic verifiability: high
- Calibration method: procedurally generated tasks, solvability checks, and explicit OOD splits
- Anti-contamination argument: procedural variation over goals, scenes, agent counts, and inventories reduces fixed-instance memorization
- Reliability or comparability concerns: performance depends strongly on whether centralized control and privileged demonstrations are available

## 7. Main contributions
- Contribution 1: Builds a large Minecraft benchmark for multimodal multi-agent collaboration.
- Contribution 2: Provides multimodal prompts, expert demonstrations, and explicit OOD splits.
- Contribution 3: Shows that current models generalize poorly to novel goals and unseen numbers of agents, especially in decentralized settings.

## 8. Main findings and failure modes
- Core empirical takeaway: current multimodal collaborative agents remain far from robust, especially on unseen goals, novel numbers of agents, and decentralized control.
- Notable model failure mode 1: poor task allocation leading to redundant work
- Notable model failure mode 2: weak 3D spatial grounding from visual prompts
- Notable model failure mode 3: ignoring some agents or failing to use them effectively in larger teams
- Does this paper reveal a benchmark-design limitation as well? yes; it shows that centralized success can mask how weak decentralized coordination really is

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Demonstrates why open-world games are strong testbeds for embodied collaboration.
- Best use in Section 1 (taxonomy and evolutionary levels): A key multi-agent multimodal benchmark in the Minecraft lineage. Important for cooperative open-world benchmarks with procedural task variation.
- Best use in Section 2 (core capabilities evaluated by games): Supports claims about coordination, visual grounding, and workload allocation.
- Best use in Section 3 (interaction and evaluation paradigm): Strong example of multimodal prompts specifying collaborative tasks. Good reference for subgoal success and redundancy metrics.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Supports the need for explicit communication and better decentralized agent modeling.

## 10. Relation to nearby papers
- Closest predecessor(s): MineDojo, MineRL, Marlo
- Closest follow-up(s): StarDojo, GameArena
- Best comparison targets inside our corpus: StarDojo, GameArena, DSGBench
- What this paper uniquely adds relative to neighbors: It focuses on multimodal cooperative task allocation and OOD generalization rather than single-agent open-world play.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- TeamCraft contains 55,000 unique task variants with one expert demonstration each.
- It uses multimodal prompts, first-person RGB observations, and high-level action skills over Minecraft.
- The benchmark reports task success, subgoal success, and redundancy, and finds much worse performance in decentralized settings.

### 11.2 Our synthesis / interpretation
- TeamCraft is one of the strongest corpus papers for cooperative multimodal environments.
- Its explicit goal/scene/agent-count splits are especially valuable for survey claims about generalization.

### 11.3 Uncertain or needs re-check
- Re-check the exact counts per task family if later drafting needs them.
- Re-check whether GPT-4o one-shot results were run under the same action constraints as trained baselines.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? Yes later, because the generalization protocol is likely draft-worthy.
- Which section to read next if needed: task design / metrics / generalization results
- Follow-up question(s): Which task families most strongly separate centralized from decentralized agents?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P1
- Reading depth: deep
- Batch ID: B12
- Outline sections: 2,3,4
- Survey role: representative
- Paper card path: `paper_cards/B12/TeamCraft.md`
- Next action: draft-section
- Last updated: 2026-04-05
