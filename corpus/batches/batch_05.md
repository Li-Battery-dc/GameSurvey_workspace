# Batch B05: long-horizon-memory-open-worlds

## Why This Batch Exists
- Consolidate the papers whose main survey value is long-horizon autonomy, memory, repair, and single-environment historical lineage.
- Keep supporting long-horizon evidence here after moving Level 5-strong generalization/open-ended papers into B06.
- Support the later synthesis on persistent failure modes, memory, repair, and single-world evaluation limits.

## Suggested Drafting Order

| Order | paper_id | Title | Survey role | Outline anchors | Why this paper is in the batch |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | InteractiveFictionGames | Interactive Fiction Games: A Colossal Adventure | anchor | 0,1,2,3,4 | Highly cited text-game precursor and Jericho anchor for the survey's taxonomy and lineage discussion. |
| 2 | NetHackLearningEnvironment | The NetHack Learning Environment | anchor | 1,2,3,4 | Foundational hard game environment for long-horizon, partial-observability, and general-agent discussions. |
| 3 | Crafter | Benchmarking the Spectrum of Agent Capabilities | anchor | 0,1,2,3,4 | Foundational single-environment general-capability benchmark and precursor for later game-agent suites; useful as lineage, not strong cross-game evidence. |
| 4 | Mars | Mars: Situated Inductive Reasoning in an Open-World Environment | contrast | 2,3,4 | Open-world situated reasoning environment is useful for novelty/adaptation comparison but only partly benchmark-centric. [uncertain: scope] |
| 5 | MineNPCTask | MineNPC-Task: Task Suite for Memory-Aware Minecraft Agents | representative | 2,3,4 | Minecraft task suite centered on memory-aware mixed-initiative play, useful for the long-horizon memory and repair discussion. |
| 6 | EMemBench | EMemBench: Interactive Benchmarking of Episodic Memory for VLM Agents | representative | 2,3,4 | Interactive game-based episodic-memory benchmark for VLM agents that sharpens the memory diagnostic branch. |

## Expected Survey Payoff
- Preserve the long-horizon lineage from text games, roguelikes, and single-world survival settings.
- Keep memory, repair, trajectory length, and recovery-after-error evidence together without overloading the Level 5 batch.

## Questions To Resolve While Drafting
- Which failures are really memory failures versus interface or exploration failures?
- How far can this batch support open-world and long-horizon claims without over-claiming cross-game generalization?

## Batch Use Note
- Use this batch to draft long-horizon memory/repair claims and the failure analysis in Section 4.1; use B06 for Level 5 generalization/open-endedness.
