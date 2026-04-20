# VARP Can VLMs Play Action Role-Playing Games? Take Black Myth Wukong as a Study Case

## 0. Metadata
- Date: 2024/09
- Venue: NeurIPS 2024 Workshop Open-World Agents
- Authors: Peng Chen, Pi Bu, Jun Song, Yuan Gao, Bo Zheng
- Paper link: https://arxiv.org/pdf/2409.12889v2
- Code link: https://varp-agent.github.io/
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: high
- Review gate label: usable

## 1. One-paragraph benchmark summary
- This paper introduces an early visual ARPG benchmark built on the real commercial game Black Myth: Wukong and uses it to ask whether VLM-driven agents can act without relying on game APIs. The benchmark defines 12 in-game tasks, 9 of them combat-heavy, and evaluates success over repeated trials while comparing against human novices. Its agent loop is screen-grounded and ultimately emits keyboard and mouse operations, which makes it useful for the survey's interface discussion, especially on the shift from API-mediated play to visual-centric play. For this survey, however, the paper is stronger as a contrast case on interaction and action design than as a high-rigor evaluation benchmark, because the benchmark is tightly entangled with the VARP scaffold, pauses the game during inference, and relies mainly on coarse task success rates.

## 2. Position in our survey
- Why-games relevance: ARPG play makes the gap between privileged game APIs and human-like visual control concrete because agents must read weakly textual 3D scenes and translate them into timed keyboard-mouse actions.
- Historical stage: ecological agent benchmark
- Benchmark level(s): L4 visual agency
- Most relevant outline section(s): 0,2,3,4
- Role in corpus: contrast

## 3. Design-space coding
### 3.1 Game structure
- Information structure: imperfect
- Transition structure: mixed
- Agent structure: single-agent
- Social structure: N/A
- Time structure: hybrid

### 3.2 Environment structure
- Environment type(s): adventure-quest world / sandbox-open-world
- Real game / simulated game / designed task-game hybrid: real commercial game benchmark
- Benchmark unit: task trajectory / combat encounter

### 3.3 Benchmark scope
- Scope: single game
- Number of games / tasks: 1 game, 12 tasks

### 3.4 Modality
- Observation modality: mixed
- Action modality: native control
- Perception burden retained: raw screenshots, enemy animations, sparse textual cues, UI icons, camera-view interpretation, and 3D navigation obstacles
- Perception burden removed: direct game-state APIs are removed, but OCR, object detection, paused inference, predefined action functions, and optional human-guided retrieval reduce the burden of fully end-to-end play

## 4. What this benchmark measures
- Primary capability target: screen-grounded action selection and combat control in a visual ARPG without direct game-state APIs
- Secondary capability target(s): combo construction, enemy-pattern reading, sparse-cue navigation, and pathfinding under weak textual guidance
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? partially
- Does it test social reasoning / deception / cooperation? no
- Does it test visual grounding / spatial-temporal reasoning? yes
- Does it test long-horizon autonomy / task completion? partially
- Does it test real-time efficiency? partially
- Does it test cross-game transfer / open-ended generalization? no
- Why is a game environment especially suitable here? A real ARPG couples perception, control, and delayed consequences tightly enough that mistakes in scene interpretation or action timing immediately derail task completion.

## 5. Interaction paradigm
- Observation channel: current game screenshots, sampled historical screenshots, OCR-recognized text cues, and Grounding DINO detections for people and objects
- Action channel: executable Python action functions that call keyboard and mouse operations; actions can be predefined, newly generated for enemy-specific combat, or synthesized from retrieved human trajectories
- Interface type: native control / hybrid
- Agent scaffold allowed: memory / reflection / retrieval / planner / tool use
- Is there privileged API access? no game-state API is exposed, but the wrapper still uses substantial assistance through OCR, object detection, paused photo-mode inference, an action library, and optional human-guided retrieval
- How close is the setup to human play? medium; it keeps screenshots plus keyboard-mouse output, but not pure end-to-end play because the agent reasons in a paused loop and acts through curated or generated macro-actions
- Main ecological-validity trade-off: the paper usefully removes engine APIs and foregrounds visual-only play, but it preserves tractability by pausing the game, enriching screenshots with OCR and detector outputs, and letting the framework reason over reusable action functions rather than raw low-level motor sequences alone

## 6. Evaluation protocol
- Main score: per-task success rate
- Auxiliary score(s): average completion time, average inference count, human action-count comparison, and ablations on SOAG and DTSA
- Evaluation style: success rate / human-relative / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: compares VARP driven by GPT-4o, Claude 3.5 Sonnet, and Gemini 1.5 Pro against human novice players; also reports module ablations and a human-guided navigation case study
- Automatic verifiability: medium
- Calibration method: 12 manually defined tasks in the game's first chapter, 5 trials per task, manual difficulty labels, fixed hardware and screen resolution, and photo-mode pausing during inference
- Anti-contamination argument: not a central claim
- Reliability or comparability concerns: success is mostly binary and task-level, task difficulty is manually assigned, the benchmark is tightly coupled to one framework and one game slice, real-time pressure is softened by pausing, and the paper does not provide the kind of backend state-verification later visual benchmarks use

## 7. Main contributions
- Contribution 1: Defines a 12-task Black Myth: Wukong benchmark to probe VLM limits in visual-only ARPG interaction.
- Contribution 2: Releases a 1,000-entry human operation dataset with gameplay video plus mouse-keyboard logs.
- Contribution 3: Proposes the VARP framework with action planning, self-optimizable combat actions, decomposed auxiliaries, and human-guided trajectory retrieval.

## 8. Main findings and failure modes
- Core empirical takeaway: with heavy scaffolding, visual-only VLM agents can handle easy scripted tasks and some medium combat, but very hard combat and unguided 3D navigation remain weak.
- Notable model failure mode 1: second-level keyframe reasoning misses critical enemy attack cues in fast combat
- Notable model failure mode 2: agents struggle with 3D scene perception and pathfinding when the game provides little explicit guidance and contains invisible walls
- Notable model failure mode 3: without action generation or human-guided retrieval, the framework lacks effective responses for enemy-specific combat patterns and hard navigation tasks
- Does this paper reveal a benchmark-design limitation as well? yes; the benchmark is most informative for the API-versus-visual and action-channel debate, but less convincing as a standalone evaluation protocol because the framework and benchmark are not cleanly separated

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Good early evidence that removing APIs exposes a meaningful visual-centric control problem that static or privileged interfaces understate.
- Best use in Section 1 (taxonomy and evolutionary levels): Useful as an early L4 ARPG case study that pushes from API-mediated agents toward screen-grounded play, but should not be treated as a main ecological anchor.
- Best use in Section 2 (core capabilities evaluated by games): Supports visual grounding, enemy-pattern interpretation, sparse-cue navigation, and non-API action definition in action games.
- Best use in Section 3 (interaction and evaluation paradigm): One of the clearest contrast cases for your target questions: it explicitly motivates moving away from APIs, implements keyboard-mouse action macros from screenshots, and then shows how coarse success-rate evaluation still leaves open comparability concerns.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Useful evidence that visual-centric agents still break on frame sparsity, 3D path perception, and action-composition bottlenecks even when semantic APIs are removed.

## 10. Relation to nearby papers
- Closest predecessor(s): Cradle and other early screen-based foundation-model agents, plus RL-based action-game projects cited in the paper
- Closest follow-up(s): later visual-game benchmarks such as StarBench, VideoGameBench, and PokeGym
- Best comparison targets inside our corpus: StarBench, PokeGym, VideoGameBench, Balrog
- What this paper uniquely adds relative to neighbors: It is an unusually explicit early case for the argument that ARPG benchmarking should move away from game APIs toward screenshot-grounded keyboard-mouse control, while also showing how much auxiliary scaffolding is still needed to make that setup work at all

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- The paper motivates its benchmark by arguing that prior game agents often rely on APIs and that this both limits applicability and diverges from human play.
- It defines 12 tasks in Black Myth: Wukong, with 10 basic tasks and 2 challenging tasks, and 75% of them are combat-related.
- The action loop ultimately executes Python functions composed of atomic operations such as light attack, dodge, heavy attack, and restore health, which then operate the keyboard and mouse.
- The implementation uses OCR for text cues, Grounding DINO for detecting people and objects, and pauses the game with photo mode during VLM inference.
- Benchmarking is done with 5 trials per task and success rate as the main metric; task 12, autonomous navigation to Bullguard within 5 minutes, is marked very hard and reaches 0% success without human guidance.
- In the main evaluation, tasks 1 to 8 are reported as nearly solved by both VARP and human novices, task 9 averages 40% success for the VARP agent, task 10 averages 20% for VARP versus 15.63% for human novices, and task 12 rises to 40% only in the human-guided case study.
- Appendix A.5 adds average completion time and average inference count per task, treating one generated executable action as one inference and estimating human combat counts by dividing logged atomic operations by 8.6.

### 11.2 Our synthesis / interpretation
- The paper matters less as a final benchmark protocol than as an early articulation of the visual-centric, non-API problem in game-agent evaluation.
- It should not be described as pure end-to-end human-like play: the benchmark removes game APIs, but the framework still depends on paused inference, OCR and detection aids, curated macro-actions, and optional human-guided retrieval.
- Relative to later B04 papers, its evaluation backend is weak, but its action-channel discussion is unusually valuable because it makes the jump from semantic APIs to screenshot-grounded keyboard-mouse control explicit.

### 11.3 Uncertain or needs re-check
- The paper does not fully specify how much of task success measurement is automated versus manually judged from gameplay outcomes, so later writing should avoid overstating backend verifiability.
- The benchmark is tightly tied to the VARP framework, so cross-paper comparisons should not treat its success rates as directly commensurate with later benchmarks that separate benchmark protocol from agent implementation more cleanly.
- If later drafting needs exact per-model per-task success values from Fig. 3, re-check the figure directly rather than inferring them from the text summary.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? Already done for this audit; no immediate reread is needed unless later writing needs exact figure values or supplementary dataset-composition details.
- Which section to read next if needed: Sec. 3.2 to 3.6 and Appendix A.5
- Follow-up question(s): If we cite this paper in Section 3, should we pair it with StarBench or PokeGym as the cleaner comparison case on non-API play versus evaluation rigor?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P2
- Reading depth: deep
- Batch ID: B04
- Outline sections: 0,2,3,4
- Survey role: contrast
- Paper card path: `paper_cards/B04/VARP.md`
- Check status: unchecked
- Last updated: 2026-04-16
