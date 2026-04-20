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
- V-MAGE is a vision-centric game evaluation framework over five modified human-playable Pygame games and 30+ evaluation environments. Its core claim is not that the benchmark is text-free, but that game state is not reduced to a privileged symbolic API: models must still interpret screenshots and short frame histories in visually irreducible scenes, while prompts provide rules, action formats, and baseline history text. The suite uses manually engineered levels, often easier or more diagnostic than standard human difficulty, to isolate positioning, tracking, timing, and visual grounding before reintroducing harder settings. For this survey, V-MAGE is best used as a controlled visual-diagnostic benchmark with a pairwise Elo ranking over model scores plus valid-action rate, complemented by separate human raw-score baselines, text-state ablations, and unit tests for core visual abilities.

## 2. Position in our survey
- Why-games relevance: Games can hold planning demands constant while varying how much perception and timing burden remain in the interface.
- Historical stage: diagnostic capability probe
- Benchmark level(s): L4 visual agency
- Most relevant outline section(s): 1,2,3,4
- Role in corpus: representative

## 3. Design-space coding
### 3.1 Game structure
- Information structure: perfect
- Transition structure: mixed
- Agent structure: single-agent
- Social structure: N/A
- Time structure: hybrid

### 3.2 World structure
- World type(s): adventure / other
- Real game / simulated game / designed task-game hybrid: designed task-game hybrid built from modified open-source Pygame games with manually redesigned benchmark levels
- Benchmark unit: episode / level run

### 3.3 Benchmark scope
- Scope: curated suite
- Number of games / tasks: 5 games and 30+ levels

### 3.4 Modality
- Observation modality: mixed
- Action modality: native control
- Perception burden retained: raw screen interpretation, object localization, multi-frame tracking, temporal action choice, and continuous visual grounding in non-grid scenes
- Perception burden removed: there is no privileged game-state API in the core setting, but rules, action schemas, and baseline reasoning/action history are already textualized; inference-speed penalties are removed by default because the environment pauses during model processing

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
- Observation channel: current screenshot plus up to three prior screenshots, wrapped with task-specific rule prompts and baseline history text describing earlier reasoning and action outcomes
- Action channel: the model emits one action from a task-specific discrete action set, which the agent wrapper parses and semantically validates before execution
- Interface type: native control / prompt-mediated discrete action space / hybrid
- Agent scaffold allowed: recent-frame history / reasoning history / lightweight agent wrapper / semantic action parser
- Is there privileged API access? no privileged game-state API is exposed to the model, but the interaction is not pure-pixel because prompts include rule text, output-format constraints, and baseline history text
- How close is the setup to human play? medium: screenshot grounding is preserved, but the loop is prompt-mediated, built on modified mini-games, and paused during inference
- Main ecological-validity trade-off: V-MAGE preserves visually grounded state tracking better than textified game benchmarks, but it simplifies control into prompted discrete actions, removes latency pressure, and uses custom diagnostic level variants rather than only native game difficulty

## 6. Evaluation protocol
- Main score: dynamic Elo rating among models based on pairwise comparison of gameplay score and valid-action rate
- Auxiliary score(s): per-level raw scores, no-history variants, text-description ablations, unit tests for core visual abilities, and human raw-score baselines
- Evaluation style: Elo / native score / human-relative ratio / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: Elo is computed from pairwise model-vs-model comparisons plus a random baseline, with 100 rounds per level and 10^4 shuffled recalculations; five human participants are evaluated separately by average raw score on the same environments and are not Elo opponents
- Automatic verifiability: high
- Calibration method: shared game-agent-model pipeline, manually difficulty-stratified levels, randomized pairwise matches, a random-action baseline, separate human score baselines, and Elo stabilization over repeated permutations
- Anti-contamination argument: not a central claim; the paper relies more on interactive evaluation design than on hidden-content or leakage defenses
- Reliability or comparability concerns: Elo can hide absolute task success, valid-action rate partly reflects prompt-format compliance, the human reference uses only N=5 and lives on raw-score rather than Elo scale, and frame pausing means the benchmark diagnoses dynamic reasoning more than deployment-speed constraints

## 7. Main contributions
- Contribution 1: Builds a vision-centric benchmark over five modified continuous-space games with manually engineered diagnostic levels.
- Contribution 2: Introduces a dynamic Elo protocol that ranks models by pairwise comparison of gameplay score together with valid-action rate.
- Contribution 3: Separates score-based human baselines from Elo rankings and adds no-history, text-state, and unit-test analyses to localize failure sources.

## 8. Main findings and failure modes
- Core empirical takeaway: current MLLMs can approach human scores on the easiest diagnostic levels, but the gap widens sharply on harder dynamic tasks; text-state ablations and larger models help, yet tracking, timing, and downstream planning deficits remain well below human performance.
- Notable model failure mode 1: inaccurate localization of interactable targets
- Notable model failure mode 2: multi-frame tracking and timing collapse on dynamic tasks such as Pong and FlappyBird
- Notable model failure mode 3: anchoring bias makes models over-rely on prior reasoning and ignore subtle visual updates across near-duplicate frames
- Does this paper reveal a benchmark-design limitation as well? yes; it shows that many "game reasoning" claims depend heavily on whether the benchmark preserves visual irreducibility and whether latency is factored out

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Demonstrates that dynamic games expose perception and tracking failures that static multimodal benchmarks miss.
- Best use in Section 1 (taxonomy and evolutionary levels): Best treated as a diagnostic branch inside the visual-agency lineage, especially for level-engineered visual probes rather than full ecological play.
- Best use in Section 2 (core capabilities evaluated by games): Strong support for separating visual grounding, tracking, and timing from downstream reasoning quality.
- Best use in Section 3 (interaction and evaluation paradigm): A useful contrast case for screenshot-grounded but prompt-mediated interaction, paused dynamic evaluation, and the separation between Elo ranking and human raw-score baselines.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Good evidence that perception bottlenecks matter, but that fixing perception alone does not resolve reasoning and anchoring failures.

## 10. Relation to nearby papers
- Closest predecessor(s): INGVP, Balrog, LVLMGamePlayers
- Closest follow-up(s): VideoGameBench, StarBench, FlashAdventure
- Best comparison targets inside our corpus: LVLMGamePlayers, VideoGameBench, AtariGPT, Balrog
- What this paper uniquely adds relative to neighbors: It couples visually irreducible continuous-space mini-games with explicit level engineering, mixed screenshot-plus-prompt interaction, Elo-by-score ranking, and separate human score baselines rather than only reporting one fixed native game difficulty.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- V-MAGE wraps five modified open-source Pygame games: Race, SuperMario, FlappyBird, Pong, and TempestRun; Appendix C.3 lists the source repositories.
- In the baseline setting, model input includes the current screenshot, up to three previous screenshots, task-specific rule and action prompts, and textual history describing prior reasoning and action outcomes.
- Level design is manual and diagnostic: Race has 6 levels that shift from map view to driver view and add acceleration; SuperMario has 10 levels culminating in a 1:1 World 1-1 replica; FlappyBird has 7 levels where early levels remove gravity and add DOWN or KEEP actions; Pong has 3 levels varying paddle width, ball speed, and ball size; TempestRun has 4 levels varying role speed, cell length, and obstacle randomness.
- Models are ranked with a dynamic Elo procedure based on gameplay score and valid-action rate, using 100 pairwise rounds per game level and 10^4 shuffled recalculations for stabilization.
- The human baseline comes from five participants' average raw scores on the same environments, reported separately from Elo tables.
- The default framework pauses the game during inference, and supplementary text-state ablations improve performance but still leave models far below human scores on simple benchmarked levels.

### 11.2 Our synthesis / interpretation
- V-MAGE is one of the best corpus papers for arguing that perception should be treated as a first-class benchmark variable rather than as background noise.
- It should be described as a screenshot-grounded but prompt-mediated visual diagnostic suite, not as a pure-pixel or text-free benchmark.
- Its main survey value is in L4 taxonomy and Section 3 interaction-evaluation analysis: it preserves visually irreducible front-end scenes while still relying on prompt scaffolding, engineered levels, and separate Elo versus human-score calibration.
- It is not strong evidence for open-ended cross-game generalization or fully ecological full-game play.

### 11.3 Uncertain or needs re-check
- Re-check the appendix if we later need the exact contribution of valid-action rate in close Elo comparisons or more precise per-model variance estimates.
- Human baselines use N=5 and raw-score scales that differ by game, so later draft prose should not compare human reference magnitudes directly with Elo values.
- If we later summarize the benchmark size precisely, re-check whether "30+ environments" should count only core levels or also the no-history variants.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? Already done for this audit; further rereading is only needed if the draft later needs appendix-level Elo or level-design detail.
- Which section to read next if needed: Appendix C for level and prompt details, then Appendix D and E for Elo construction, unit tests, and text-state ablations
- Follow-up question(s): Which V-MAGE comparisons best illustrate the gap between perception repair and downstream reasoning repair?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P1
- Reading depth: deep
- Batch ID: B04
- Outline sections: 1,2,3,4
- Survey role: representative
- Paper card path: `paper_cards/B04/VMage.md`
- Check status: unchecked
- Last updated: 2026-04-16
