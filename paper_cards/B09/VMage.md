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
- V-MAGE is a benchmark for vision-centric game play that emphasizes perception-heavy, visually irreducible games rather than symbolic board-state reasoning. It evaluates MLLMs on five human-playable games spanning more than 30 levels and uses a dynamic Elo-style ranking built from gameplay score and valid-action rate. The paper also contrasts standard play with frame-paused play and with text descriptions of the same state, which lets it localize whether failures come from perception, timing, or higher-level reasoning. For this survey, V-MAGE is a strong visual-benchmark paper because it directly operationalizes the claim that raw visual understanding remains a central bottleneck for multimodal game agents.

## 2. Position in our survey
- Why-games relevance: Games can hold planning demands constant while varying how much perception and timing burden remain in the interface.
- Historical stage: ecological agent benchmark
- Narrative level(s): L4 visual agency / L5 cross-game generalization
- Most relevant outline section(s): 2,3,4
- Role in corpus: representative

## 3. Design-space coding
### 3.1 Environment structure
- Information structure: mixed
- Transition structure: mixed
- Agent structure: single-agent
- Social structure: N/A
- Time structure: real-time / hybrid

### 3.2 World structure
- World type(s): adventure / puzzle / other
- Real game / simulated game / designed task-game hybrid: curated suite of real video games
- Benchmark unit: episode / level run

### 3.3 Benchmark scope
- Scope: curated suite
- Number of games / tasks: 5 games and 30+ levels
- Benchmark intent: ecological evaluation / diagnostic evaluation

### 3.4 Modality
- Primary modality: image / video
- Perception burden retained: raw screen interpretation, target localization, scene parsing, and timing
- Perception burden removed: little; the benchmark explicitly avoids collapsing state into symbolic summaries in its main setting

## 4. What this benchmark measures
- Primary capability target: visual understanding for game control
- Secondary capability target(s): timing, long-horizon planning, action validity, and robustness under interface changes
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? yes
- Does it test social reasoning / deception / cooperation? no
- Does it test visual grounding / spatial-temporal reasoning? yes
- Does it test long-horizon autonomy / task completion? yes
- Does it test real-time efficiency? yes
- Does it test cross-game transfer / open-ended generalization? yes
- Why is a game environment especially suitable here? The same game task can be presented with and without visual burden, making perception bottlenecks measurable rather than speculative.

## 5. Interaction paradigm
- Observation channel: gameplay frames in visually rich 2D game environments
- Action channel: game actions selected by the model under a common harness
- Interface type: GUI interaction / structured action space / hybrid
- Agent scaffold allowed: none
- Is there privileged API access? no in the core benchmark; textual descriptions are used only in comparison settings
- How close is the setup to human play? high in the default setting, lower in the paused and text-described ablations
- Main ecological-validity trade-off: the benchmark is strongest when raw frames are used, but much of its scientific value comes from ablations that intentionally intervene on the interface

## 6. Evaluation protocol
- Main score: dynamic Elo-style ranking based on gameplay score and valid-action rate
- Auxiliary score(s): per-level game score, valid-action rate, paused-play results, and text-description results
- Evaluation style: Elo / native score / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: MLLMs are ranked through repeated game runs and compared with stronger interface variants
- Automatic verifiability: high
- Calibration method: shared harness, multiple levels, and dynamic Elo updates from standardized play logs
- Anti-contamination argument: the benchmark centers on live game interaction rather than static puzzle answers
- Reliability or comparability concerns: Elo-style aggregation can hide which failures come from illegal actions versus poor strategy unless the auxiliary metrics are inspected

## 7. Main contributions
- Contribution 1: Builds a visual-game benchmark intentionally targeted at perception-heavy gameplay.
- Contribution 2: Introduces an Elo-style protocol combining outcome quality with valid-action rate.
- Contribution 3: Uses interface ablations to show how much performance improves when perceptual burden is reduced.

## 8. Main findings and failure modes
- Core empirical takeaway: current MLLMs remain far below human play, and the gains from text descriptions show that perception is a major bottleneck.
- Notable model failure mode 1: inaccurate localization of interactable targets
- Notable model failure mode 2: timing and tracking failures in fast-changing scenes
- Notable model failure mode 3: reasoning still breaks down even after perceptual support is added
- Does this paper reveal a benchmark-design limitation as well? yes; it shows that many "game reasoning" claims are actually sensitive to how much perception is abstracted away

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Demonstrates that visual games expose failures not visible in text-only reasoning settings.
- Best use in Section 1 (taxonomy and evolutionary levels): Fits the move toward ecologically realistic multimodal interfaces. Useful for classifying perception-heavy suites and interface-ablation protocols.
- Best use in Section 2 (core capabilities evaluated by games): Strong evidence that visual grounding and strategic control should be analyzed separately.
- Best use in Section 3 (interaction and evaluation paradigm): Excellent comparison case for raw-vision versus textualized play. Helpful reference for combining action validity with outcome quality.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Supports the argument that better visual grounding, not only bigger models, is needed for game agents.

## 10. Relation to nearby papers
- Closest predecessor(s): VideoGameBench, Balrog
- Closest follow-up(s): LMGAME-BENCH, VLMs Play StarCraft II
- Best comparison targets inside our corpus: VideoGameBench, AtariGPT, LMGAME-BENCH, VLMPlayStarCraftII
- What this paper uniquely adds relative to neighbors: It isolates perception bottlenecks by holding the games fixed while swapping the interface between raw visual play and more scaffolded variants.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- The benchmark evaluates five games spanning more than 30 levels.
- The paper reports a dynamic Elo-based ranking built from gameplay score and valid-action rate.
- Performance improves when the emulator is paused or when textual state descriptions are provided, indicating that raw visual understanding is a central failure point.

### 11.2 Our synthesis / interpretation
- V-MAGE is one of the best corpus papers for arguing that perception should be treated as a first-class benchmark variable rather than as background noise.
- It is especially useful when comparing raw visual suites against more scaffolded game benchmarks.

### 11.3 Uncertain or needs re-check
- Re-check the appendix if we later need the exact five game titles and per-game Elo breakdowns.
- Re-check the valid-action-rate definition if we compare it closely with grounding-accuracy metrics in RTS papers.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? Yes for later drafting, because the ablations are central to our interface-design discussion.
- Which section to read next if needed: benchmark protocol / Elo computation / interface ablations
- Follow-up question(s): Which game in V-MAGE most cleanly demonstrates pure perceptual failure after timing is controlled?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P1
- Reading depth: deep
- Batch ID: B09
- Outline sections: 2,3,4
- Survey role: representative
- Paper card path: `paper_cards/B09/VMage.md`
- Next action: draft-section
- Last updated: 2026-04-05
