# Batch B05: long-horizon-memory-open-worlds

## Why This Batch Exists
- Consolidate the papers whose main survey value is long-horizon autonomy, memory, repair, and open-world or sandbox continuity.
- Support Section 2.5 and the later synthesis on persistent failure modes.

## Suggested Drafting Order

| Order | paper_id | Title | Survey role | Outline anchors | Why this paper is in the batch |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | InteractiveFictionGames | Interactive Fiction Games: A Colossal Adventure | anchor | 0,1,2,3,4 | Highly cited text-game precursor and Jericho anchor for the survey's taxonomy and lineage discussion. |
| 2 | NetHackLearningEnvironment | The NetHack Learning Environment | anchor | 1,2,3,4 | Foundational hard game environment for long-horizon, partial-observability, and general-agent discussions. |
| 3 | TextQuests | TextQuests: How Good are LLMs at Text-Based Video Games? | representative | 2,3,4 | Interactive fiction benchmark stressing textual exploration memory and long-context action selection. |
| 4 | TextAtari | TextAtari: 100K Frames Game Playing with Language Agents | contrast | 2,3,4 | Textified Atari benchmark links compact language state to very long control horizons. |
| 5 | Crafter | Benchmarking the Spectrum of Agent Capabilities | anchor | 0,1,2,3,4 | Crafter is a foundational single-environment general-capability benchmark and precursor for later game-agent suites. |
| 6 | MCU | MCU: An Evaluation Framework for Open-Ended Game Agents | representative | 0,1,2,3,4 | Open-ended Minecraft benchmark with task composition and human-aligned evaluation. |
| 7 | Mars | Mars: Situated Inductive Reasoning in an Open-World Environment | contrast | 2,3,4 | Open-world situated reasoning environment is useful for embodied comparison but only partly benchmark-centric. [uncertain: scope] |
| 8 | MineNPCTask | MineNPC-Task: Task Suite for Memory-Aware Minecraft Agents | representative | 2,3,4 | Minecraft task suite centered on memory-aware mixed-initiative play, useful for the long-horizon memory discussion. |
| 9 | StarDojo | StarDojo: Benchmarking Open-Ended Behaviors of Agentic Multimodal LLMs in Production-Living Simulations with Stardew Valley | representative | 2,3,4 | Production-living simulation benchmark expanding open-ended multimodal behavior and long-horizon evaluation. |
| 10 | EMemBench | EMemBench: Interactive Benchmarking of Episodic Memory for VLM Agents | representative | 2,3,4 | Interactive game-based episodic-memory benchmark for VLM agents that sharpens the memory diagnostic branch. |

## Expected Survey Payoff
- Tie text games, roguelikes, Minecraft tasks, and production-living simulations into one long-horizon narrative.
- Keep memory, trajectory length, and recovery-after-error evidence together.

## Questions To Resolve While Drafting
- Which failures are really memory failures versus interface or exploration failures?
- How far can this batch support open-world claims without over-claiming ecological realism?

## Batch Use Note
- Use this batch to draft Section 2.5 and the long-horizon failure analysis in Section 4.1.
