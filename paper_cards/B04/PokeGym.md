# PokeGym PokeGym: A Visually-Driven Long-Horizon Benchmark for Vision-Language Models

## 0. Metadata
- Date: 2026/04
- Venue: arXiv
- Authors: Ruizhi Zhang, Ye Huang, Yuangang Pan, Chuanfu Shen, Zhilin Liu, Ting Xie, Wen Li, Lixin Duan
- Paper link: https://arxiv.org/pdf/2604.08340v1.pdf
- Code link:
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: high
- Review gate label: strong

## 1. One-paragraph benchmark summary
- PokeGym is a pure-vision game benchmark for long-horizon VLM agents built on Pokémon Legends: Z-A, a visually rich 3D open-world RPG. It defines 30 tasks from 10 quests, each instantiated under Visual-Guided, Step-Guided, and Goal-Only instruction granularities so the benchmark can separate visual grounding, semantic reasoning, and autonomous exploration. Agents act only from RGB observations extracted from the emulator, while an independent evaluator uses AOB memory scanning to verify progress and success without exposing privileged state to the model. For this survey, PokeGym is a strong Level 4 visual-agency paper because it couples raw pixels, long-horizon quest structure, and automated evaluation while also diagnosing a concrete embodied bottleneck: physical deadlock recovery.

## 2. Position in our survey
- Why-games relevance: A 3D RPG quest world forces models to connect perception, navigation, object interaction, and delayed task structure in a way static multimodal tests cannot.
- Historical stage: ecological agent benchmark
- Benchmark level(s): L4 visual agency
- Most relevant outline section(s): 2,3,4
- Role in corpus: representative

## 3. Design-space coding
### 3.1 Structure
- Form: World
- Construction: Embedded
- Construction note: real commercial 3D game played through emulator-based benchmarking
- Benchmark unit: task trajectory

### 3.2 Mechanics profile
- State visibility: partial
- Transition uncertainty: mixed
- Actor configuration: single-agent
- Incentive structure: N/A
- Temporal regime: real-time

### 3.3 Benchmark scope
- Scope: single game
- Number of games / tasks: 1 game, 30 tasks, 10 quests, 3 instruction granularities

### 3.4 Modality
- Observation modality: visual image
- Action modality: mixed
- Perception burden retained: raw RGB observations, changing viewpoints, occlusion, depth reasoning, and quest-conditioned interaction
- Perception burden removed: internal coordinates and quest flags are never exposed to the agent, and action execution is mediated through benchmark-defined control schemes

## 4. What this benchmark measures
- Primary capability target: visually grounded long-horizon task completion in a complex 3D world
- Secondary capability target(s): spatial collision recovery, semantic reasoning from under-specified instructions, and autonomous exploration
- Does it test rule grounding / legal action generation? partially
- Does it test strategic planning under uncertainty? yes
- Does it test social reasoning / deception / cooperation? no
- Does it test visual grounding / spatial-temporal reasoning? yes
- Does it test long-horizon autonomy / task completion? yes
- Does it test real-time efficiency? partially; action timing matters, but the benchmark also uses adaptive pausing in fast combat cases
- Does it test cross-game transfer / open-ended generalization? no
- Why is a game environment especially suitable here? Quest-driven 3D games make perception errors behaviorally consequential because wrong navigation, missed targets, or collision failures directly derail later progress.

## 5. Interaction paradigm
- Observation channel: front-view RGB frame by default, with optional previous-frame reflection and left/right peripheral views
- Action channel: either defined high-level actions or parametric control sequences executed in the emulator
- Interface type: structured action space / hybrid
- Agent scaffold allowed: memory / self-reflection / tool use
- Is there privileged API access? no for the agent; evaluator-only memory scanning is kept separate from the prompt loop
- How close is the setup to human play? medium to high; the benchmark keeps raw pixels and a real 3D world, but action abstraction and adaptive pause mechanisms reduce some native motor burden
- Main ecological-validity trade-off: PokeGym preserves pure visual input and 3D quest structure, but adaptive pausing and benchmark-defined action paradigms keep evaluation tractable rather than fully human-like

## 6. Evaluation protocol
- Main score: success rate (SR)
- Auxiliary score(s): average successful steps, ineffective-move rate, recovery rate, maximum consecutive ineffective moves, action entropy, and failure-category breakdowns
- Evaluation style: success / step / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: 8 main VLMs are evaluated under identical initial states and budgets with 5 trials per setting
- Automatic verifiability: high
- Calibration method: fixed task budgets, standardized save states, three instruction granularities, and AOB-based state extraction over map IDs, coordinates, and quest flags
- Anti-contamination argument: partial; the paper emphasizes strict no-state-leakage and automated verification more than explicit contamination resistance
- Reliability or comparability concerns: the benchmark is tied to one commercial game version, adaptive pause changes the role of latency, and action abstractions shape what counts as control difficulty

## 7. Main contributions
- Contribution 1: Builds a pure-pixel, long-horizon VLM benchmark in a visually complex 3D RPG world.
- Contribution 2: Introduces an automated evaluation pipeline that verifies task success through AOB memory scanning without exposing privileged state to the agent.
- Contribution 3: Uses instruction granularity, deadlock diagnosis, visual-context ablations, and action-paradigm studies to isolate embodied failure modes.

## 8. Main findings and failure modes
- Core empirical takeaway: the dominant bottleneck is not high-level goal specification but low-level physical deadlock recovery in visually grounded 3D interaction.
- Notable model failure mode 1: weaker models often suffer Unaware Deadlocks, hallucinating progress while physically trapped
- Notable model failure mode 2: stronger proprietary models more often exhibit Aware Deadlocks, recognizing the trap but still failing to execute a useful recovery maneuver
- Notable model failure mode 3: execution failures occur even after the target is recognized, with agents getting stuck on nearby geometry or interacting from the wrong position
- Does this paper reveal a benchmark-design limitation as well? yes; the benchmark is compelling for pure-vision 3D evaluation, but its single-game scope and action abstractions limit how far its conclusions should be generalized

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Good modern example of how games make perception, action, and recovery failures observable rather than merely inferable from final answers.
- Best use in Section 2 (core capabilities evaluated by games): Direct support for visual grounding, spatial-temporal reasoning, long-horizon task completion, and recovery-after-error analysis.
- Best use in Section 3 (interaction and evaluation paradigm): Strong evidence for pure-pixel evaluation without privileged state leakage, plus a clear automated-verification design using evaluator-only memory scanning.
- Best use in Section 4 (synthesis, bottlenecks, and future design): One of the best current cards for the claim that embodied VLM bottlenecks often look like spatial intuition and recovery failures rather than only weak top-level planning.

## 10. Relation to nearby papers
- Closest predecessor(s): VideoGameBench, FlashAdventure, Cradle, MineDojo
- Closest follow-up(s): future pure-vision 3D game benchmarks with broader multi-game coverage
- Best comparison targets inside our corpus: VideoGameBench, FlashAdventure, Balrog, MCU, StarDojo
- What this paper uniquely adds relative to neighbors: It combines raw-pixel 3D RPG play, evaluator-only state verification, instruction-granularity probes, and a concrete deadlock taxonomy in one benchmark

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- PokeGym defines 30 tasks derived from 10 quests, with trajectories ranging from 30 to 220 environment steps and three instruction granularities: Visual-Guided, Step-Guided, and Goal-Only.
- Agents operate only on RGB observations, while the evaluator performs AOB memory scanning to recover map IDs, coordinates, and quest flags that are never exposed to the model.
- Across the eight main VLMs, Gemini-3-Pro and GPT-5.2 tie for the top average success rate at 58.70 on the main leaderboard.
- Ineffective moves are significantly negatively correlated with task success across all three instruction granularities, and the failure taxonomy separates Unaware Deadlocks, Aware Deadlocks, Lost trajectories, and Execution Failures.
- In the GPT-5.2 intervention study, a simple forced-back recovery raises average SR from 58.70 to 62.22, outperforming textual deadlock feedback.

### 11.2 Our synthesis / interpretation
- PokeGym is most useful as evidence that raw-visual long-horizon benchmarks expose a spatial-recovery bottleneck that many current VLM evaluations underplay.
- It should be treated as a visual-agency representative rather than as a Pokemon-specialist benchmark, because the paper's main contribution is protocol design for pure-pixel embodied evaluation rather than domain upper bounds.

### 11.3 Uncertain or needs re-check
- Re-check the appendix if later drafting needs exact AOB signature-extraction details, action-space size calculations, or per-task map complexity claims.
- Re-check the extended leaderboard if we later want to cite GPT-5.4 family results instead of the main eight-model table.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? No immediate reread; the full paper already provides enough evidence for setup, results, and failure-diagnosis use in the survey.
- Which section to read next if needed: 4.4 / 4.5 / 4.6 / Appendix D
- Follow-up question(s): Which PokeGym result should anchor Section 4 more strongly: the deadlock taxonomy, the forced-recovery intervention, or the visual-context ablations?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P1
- Reading depth: deep
- Batch ID: B04
- Outline sections: 2,3,4
- Survey role: representative
- Paper card path: `paper_cards/B04/PokeGym.md`
- Check status: unchecked
- Last updated: 2026-04-10
