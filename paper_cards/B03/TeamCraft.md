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
- TeamCraft is a multimodal multi-agent Minecraft benchmark for collaborative task planning and execution. It provides 55,000 unique task variants across building, clearing, farming, and smelting, each paired with one procedurally generated expert demonstration, plus explicit Goal, Scene, and Agents generalization splits. Agents receive first-person RGB observations, inventory state, and multimodal task prompts with orthographic views, but act through a MineFlayer-backed high-level skill layer rather than low-level end-to-end control. For this survey, TeamCraft is a major reference for visually grounded multi-agent collaboration in an open-world-style environment, not for cross-game transfer in the stronger Level 5 sense.

## 2. Position in our survey
- Why-games relevance: Minecraft-like worlds support open-ended cooperation, tool use, spatial planning, and multimodal task specification at scale.
- Historical stage: ecological agent benchmark
- Benchmark level(s): L3 social intelligence / L4 visual agency
- Most relevant outline section(s): 2,3,4
- Role in corpus: representative

## 3. Design-space coding
### 3.1 Game structure
- Information structure: mixed
- Transition structure: mixed
- Agent structure: multi-agent
- Social structure: cooperative
- Time structure: hybrid

### 3.2 World structure
- World type(s): sandbox / open-world
- Real game / simulated game / designed task-game hybrid: Minecraft-based task benchmark
- Benchmark unit: collaborative task episode

### 3.3 Benchmark scope
- Scope: single game
- Number of games / tasks: 55,000 task variants across four task families

### 3.4 Modality
- Observation modality: mixed
- Action modality: semantic
- Perception burden retained: first-person RGB observation, inventory, spatial reasoning, and multimodal prompt grounding
- Perception burden removed: MineFlayer executes higher-level skills instead of low-level motor control

## 4. What this benchmark measures
- Primary capability target: multimodal collaborative planning and execution
- Secondary capability target(s): coordination under partial information, task allocation, and generalization to new goals, scenes, and agent counts
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? yes
- Does it test social reasoning / deception / cooperation? yes; cooperation, workload allocation, and partial-information coordination
- Does it test visual grounding / spatial-temporal reasoning? yes
- Does it test long-horizon autonomy / task completion? yes
- Does it test real-time efficiency? partially
- Does it test cross-game transfer / open-ended generalization? partially; it tests within-Minecraft generalization over goals, scenes, and agent counts rather than cross-game transfer
- Why is a game environment especially suitable here? Minecraft supports rich cooperative tasks with grounded objects and spatial dependencies while remaining highly configurable.

## 5. Interaction paradigm
- Observation channel: first-person RGB views, inventories, and multimodal prompts with language plus three orthographic views; centralized control also receives all agents' observations and action history
- Action channel: eight high-level skills such as obtaining blocks, farming, placing items, breaking blocks, and smelting-related actions
- Interface type: API / structured action space / hybrid
- Agent scaffold allowed: planner / demonstrations / centralized controller
- Is there privileged API access? yes; MineFlayer executes high-level skills through low-level Minecraft APIs, and demonstrations are planner-generated with privileged environment information
- How close is the setup to human play? medium-low; the world is rich and visually grounded, but control is abstracted into high-level skills and centralized variants see all agents
- Main ecological-validity trade-off: TeamCraft preserves multimodal world grounding and collaboration pressure, but MineFlayer skills, planner-generated demonstrations, and centralized control reduce low-level control and communication burdens

## 6. Evaluation protocol
- Main score: task success rate
- Auxiliary score(s): subgoal success rate and redundancy rate
- Evaluation style: completion rate / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: TeamCraft-VLA 7B/13B models are trained in centralized and decentralized settings; the paper also includes a text grid-world ablation and a one-shot GPT-4o proprietary VLA comparison
- Automatic verifiability: high
- Calibration method: procedurally generated tasks with solvability checks, a test set plus Goal/Scene/Agents generalization splits, and 950 held-out test cases
- Anti-contamination argument: not central
- Reliability or comparability concerns: performance depends strongly on MineFlayer's oracle-like skill execution, planner-generated demonstrations, and whether centralized control or explicit team-level information is available

## 7. Main contributions
- Contribution 1: Builds a large Minecraft benchmark for multimodal multi-agent collaboration.
- Contribution 2: Provides multimodal prompts, planner-generated expert demonstrations, and explicit Goal/Scene/Agents generalization splits.
- Contribution 3: Shows that current models generalize poorly to novel goals and unseen numbers of agents, especially under decentralized control.

## 8. Main findings and failure modes
- Core empirical takeaway: current multimodal collaborative agents remain far from robust, especially on unseen goals, novel numbers of agents, and decentralized control; grid-world text descriptions are substantially easier than the full multimodal setting.
- Notable model failure mode 1: poor task allocation leading to redundant work
- Notable model failure mode 2: weak 3D spatial grounding and object-state recognition from visual prompts
- Notable model failure mode 3: ignoring the fourth agent or failing to use larger teams effectively under the Agents split
- Does this paper reveal a benchmark-design limitation as well? yes; centralized success can mask weak decentralized coordination, and the benchmark still relies on MineFlayer rather than end-to-end low-level control

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Demonstrates why open-world games are strong testbeds for embodied collaboration.
- Best use in Section 1 (taxonomy and evolutionary levels): A key multi-agent multimodal benchmark in the Minecraft lineage. Use it as a cooperative visual-agent benchmark, not as a cross-game generalization anchor.
- Best use in Section 2 (core capabilities evaluated by games): Supports claims about coordination, visual grounding, and workload allocation.
- Best use in Section 3 (interaction and evaluation paradigm): Strong example of multimodal prompts specifying collaborative tasks, MineFlayer-backed high-level action interfaces, and centralized-versus-decentralized evaluation.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Supports the need for explicit communication and better decentralized agent modeling.

## 10. Relation to nearby papers
- Closest predecessor(s): MineDojo, MineRL, Marlo
- Closest follow-up(s): MCU, StarDojo
- Best comparison targets inside our corpus: CollabOvercooked, AvalonBench, WerewolfArena, Wolf
- What this paper uniquely adds relative to neighbors: It centers multimodal multi-agent collaboration in Minecraft, with explicit Goal/Scene/Agents generalization splits and a centralized-versus-decentralized comparison rather than single-agent open-world play.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- TeamCraft contains 55,000 unique task variants with one expert demonstration each.
- It uses multimodal prompts with three orthographic views, first-person RGB observations, inventory state, and eight MineFlayer-backed high-level actions over Minecraft.
- The benchmark evaluates task success, subgoal success, and redundancy on held-out Goal, Scene, and Agents splits, and reports much worse performance in decentralized settings.

### 11.2 Our synthesis / interpretation
- TeamCraft is one of the strongest corpus papers for cooperative multimodal environments.
- Its explicit Goal/Scene/Agents splits are especially valuable for survey claims about within-environment generalization.
- Its safest survey use is as a visual collaborative Minecraft benchmark, not as evidence of end-to-end low-level control or cross-game transfer.

### 11.3 Uncertain or needs re-check
- Re-check Table 2 if later drafting needs exact counts per task family or the full 950-case test breakdown.
- Re-check Appendix A or H if later drafting needs the exact high-level action list or prompt templates.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? No immediate follow-up needed; the full paper has been read for this audit. Reopen the appendix only if we need the exact action vocabulary, task-family counts, or prompt templates.
- Which section to read next if needed: Appendix A/H action and prompt details, plus Table 2 task statistics
- Follow-up question(s): Which task families most strongly separate visual grounding failures from coordination failures?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P1
- Reading depth: deep
- Batch ID: B03
- Outline sections: 2,3,4
- Survey role: representative
- Paper card path: `paper_cards/B03/TeamCraft.md`
- Check status: unchecked
- Next action: draft-section
- Last updated: 2026-04-10
