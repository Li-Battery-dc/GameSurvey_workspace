# VMage V-MAGE: A Game Evaluation Framework for Assessing Vision-Centric Capabilities in Multimodal Large Language Models

## 0. Metadata
- Date: 2025/04
- Venue: arXiv
- Authors: Xiangxi Zheng, Linjie Li, Zhengyuan Yang, Ping Yu, Alex Jinpeng Wang, Rui Yan, Yuan Yao, Lijuan Wang
- Paper link: https://arxiv.org/pdf/2504.06148v2.pdf
- Code link: https://github.com/CSU-JPG/V-MAGE
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: high
- Review gate label: strong

## 1. One-paragraph benchmark summary
- V-MAGE is a vision-centric game evaluation framework that tests MLLMs on five visually irreducible, continuous-space video games spanning more than 30 levels. Instead of commercial full games, it uses modified human-playable Pygame environments with difficulty-stratified levels to isolate capabilities such as positioning, tracking, timing, and visual grounding under dynamic interaction. Model rankings are computed with a dynamic Elo protocol based on gameplay score and valid-action rate, and the paper supplements the benchmark with human baselines, text-state ablations, and unit tests for core visual abilities. For this survey, V-MAGE is valuable as a diagnostic visual-game benchmark that makes perception and multi-frame reasoning failures explicit without collapsing the task into symbolic state.

## 2. Position in our survey
- Why-games relevance: Games can hold planning demands constant while varying how much perception and timing burden remain in the interface.
- Historical stage: diagnostic capability probe
- Narrative level(s): L4 visual agency
- Most relevant outline section(s): 2,3,4
- Role in corpus: representative

## 3. Design-space coding
### 3.1 Environment structure
- Information structure: perfect
- Transition structure: mixed
- Agent structure: single-agent
- Social structure: N/A
- Time structure: hybrid

### 3.2 World structure
- World type(s): other (platformer / racing / arcade / runner)
- Real game / simulated game / designed task-game hybrid: designed task-game hybrid built from modified open-source Pygame games
- Benchmark unit: episode / level run

### 3.3 Benchmark scope
- Scope: curated suite
- Number of games / tasks: 5 games and 30+ levels
- Benchmark intent: diagnostic evaluation

### 3.4 Modality
- Primary modality: image / short frame history
- Perception burden retained: raw screen interpretation, object localization, multi-frame tracking, and temporally sensitive action choice
- Perception burden removed: inference-speed penalties are removed by default because the environment pauses during model processing

## 4. What this benchmark measures
- Primary capability target: vision-grounded control and multi-frame reasoning in dynamic games
- Secondary capability target(s): positioning, tracking, timing, action validity, and robustness under text-state ablations
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? limited
- Does it test social reasoning / deception / cooperation? no
- Does it test visual grounding / spatial-temporal reasoning? yes
- Does it test long-horizon autonomy / task completion? limited
- Does it test real-time efficiency? no
- Does it test cross-game transfer / open-ended generalization? limited
- Why is a game environment especially suitable here? The same game family can be varied across difficulty levels and interface conditions, making perception and multi-frame reasoning bottlenecks measurable rather than speculative.

## 5. Interaction paradigm
- Observation channel: current and recent gameplay frames plus task-specific rule prompts
- Action channel: structured game actions generated through an agent wrapper and semantically validated before execution
- Interface type: GUI interaction / structured action space / hybrid
- Agent scaffold allowed: recent-frame history / reasoning history / lightweight agent wrapper
- Is there privileged API access? no in the core benchmark; textual descriptions are used only in comparison settings
- How close is the setup to human play? medium: raw visual interaction is preserved, but the tasks are modified Pygame environments and the default setup pauses the game during inference
- Main ecological-validity trade-off: V-MAGE preserves dynamic visual control, but it sacrifices raw latency pressure and uses simplified game environments to obtain cleaner diagnosis

## 6. Evaluation protocol
- Main score: dynamic Elo-style ranking based on gameplay score and valid-action rate
- Auxiliary score(s): per-level raw scores, human-baseline comparisons, text-description ablations, and unit tests for core visual abilities
- Evaluation style: Elo / native score / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: models are paired for 100 rounds per game level, Elo is stabilized across repeated shuffles, and five human participants provide a baseline on the same environment
- Automatic verifiability: high
- Calibration method: shared game-agent-model pipeline, difficulty-stratified levels, randomized pairwise matches, and Elo stabilization over repeated permutations
- Anti-contamination argument: not a central claim; the paper relies more on interactive evaluation design than on hidden-content or leakage defenses
- Reliability or comparability concerns: Elo can hide absolute task success, valid-action rate partly reflects formatting compliance, and frame pausing means the benchmark diagnoses dynamic reasoning more than deployment-speed constraints

## 7. Main contributions
- Contribution 1: Builds a vision-centric benchmark over five continuous-space games with more than 30 difficulty-stratified levels.
- Contribution 2: Introduces a dynamic Elo protocol that compares models using gameplay score together with valid-action rate.
- Contribution 3: Uses human baselines, text-state ablations, and core-ability unit tests to diagnose where current MLLMs fail.

## 8. Main findings and failure modes
- Core empirical takeaway: current MLLMs approach human scores only on simple levels, but the human-model gap widens sharply on harder dynamic tasks; text-state ablations improve results yet still do not close the gap.
- Notable model failure mode 1: inaccurate localization of interactable targets
- Notable model failure mode 2: multi-frame tracking and timing collapse on dynamic tasks such as Pong and FlappyBird
- Notable model failure mode 3: anchoring bias makes models over-rely on prior reasoning and ignore subtle visual updates across near-duplicate frames
- Does this paper reveal a benchmark-design limitation as well? yes; it shows that many "game reasoning" claims depend heavily on whether the benchmark preserves visual irreducibility and whether latency is factored out

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Demonstrates that dynamic games expose perception and tracking failures that static multimodal benchmarks miss.
- Best use in Section 1 (taxonomy and evolutionary levels): Best treated as a diagnostic branch inside the visual-agency lineage rather than as a full ecological benchmark.
- Best use in Section 2 (core capabilities evaluated by games): Strong support for separating visual grounding, tracking, and timing from downstream reasoning quality.
- Best use in Section 3 (interaction and evaluation paradigm): A useful contrast case for paused dynamic evaluation, multi-frame inputs, and Elo-style aggregation over difficulty-stratified levels.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Good evidence that perception bottlenecks matter, but that fixing perception alone does not resolve reasoning and anchoring failures.

## 10. Relation to nearby papers
- Closest predecessor(s): INGVP, Balrog, LVLMGamePlayers
- Closest follow-up(s): VideoGameBench, StarBench, FlashAdventure
- Best comparison targets inside our corpus: LVLMGamePlayers, VideoGameBench, AtariGPT, Balrog
- What this paper uniquely adds relative to neighbors: It couples visually irreducible continuous-space games with difficulty-stratified levels, human baselines, and diagnostic ablations rather than only reporting raw benchmark scores.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- The benchmark evaluates five games, namely FlappyBird, Race, SuperMario, Pong, and TempestRun, across more than 30 levels.
- Models are ranked with a dynamic Elo procedure based on gameplay score and valid-action rate, using 100 pairwise rounds per game level and stabilization over repeated shuffles.
- The default framework pauses the game during inference, and supplementary text-state ablations improve performance but still leave most models well below human baselines on harder levels.

### 11.2 Our synthesis / interpretation
- V-MAGE is one of the best corpus papers for arguing that perception should be treated as a first-class benchmark variable rather than as background noise.
- It is especially useful when comparing raw visual suites against more scaffolded or more text-reducible game benchmarks.
- Its survey value is mainly in L4 and Section 3 diagnostics; it is not strong evidence for open-ended cross-game generalization.

### 11.3 Uncertain or needs re-check
- Re-check the appendix if we later need the exact level mappings for each ability test or more precise per-model variance estimates.
- Re-check how heavily formatting-validity influences Elo outcomes if we compare V-MAGE directly with benchmarks that score only environment success.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? Already done for this audit; further rereading is only needed if the draft later needs appendix-level Elo or level-design detail.
- Which section to read next if needed: Appendix D and E on Elo construction, unit tests, and text-state ablations
- Follow-up question(s): Which V-MAGE comparisons best illustrate the gap between perception repair and downstream reasoning repair?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P1
- Reading depth: deep
- Batch ID: B04
- Outline sections: 2,3,4
- Survey role: representative
- Paper card path: `paper_cards/B04/VMage.md`
- Check status: unchecked
- Last updated: 2026-04-10
