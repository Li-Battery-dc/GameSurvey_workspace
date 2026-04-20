# StarBench: A Turn-Based RPG Benchmark for Agentic Multimodal Decision-Making and Information Seeking

## 0. Metadata
- Date: 2025/10
- Venue: arXiv
- Authors: Haoran Zhang, Chenhao Zhu, Sicong Guo, Hanzhe Guo, Haiming Li, Donglin Yu
- Paper link: https://arxiv.org/pdf/2510.18483v1
- Code link:
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: high
- Review gate label: strong

## 1. One-paragraph benchmark summary
- StarBench is a real-client Honkai: Star Rail benchmark that holds tasks and metrics fixed while varying only the interaction regime. Across eight battles in four combat families, it compares direct control, where a VLM sees only a 1920x1080 screenshot and must emit low-level click coordinates plus keypresses, against tool-assisted control, where the same screenshot is paired with a semantic action tuple and optional YOLO/OCR textification. A second diagnostic lets the agent decide once per episode whether to ask a frozen LightRAG help corpus for a short hint before acting. For this survey, StarBench is an anchor paper because it cleanly separates raw native control, semantic action abstraction, and evaluation-time information seeking inside one benchmark.

## 2. Position in our survey
- Why-games relevance: It makes the full pixel -> action -> outcome loop auditable while also exposing the human-like question of when an agent should seek outside information instead of acting immediately.
- Historical stage: ecological agent benchmark
- Narrative level(s): L4 visual agency
- Most relevant outline section(s): 0,1,2,3,4
- Role in corpus: anchor

## 3. Design-space coding
### 3.1 Environment structure
- Information structure: mixed
- Transition structure: mixed
- Agent structure: single-agent
- Social structure: N/A
- Time structure: turn-based

### 3.2 World structure
- World type(s): other (turn-based RPG combat)
- Real game / simulated game / designed task-game hybrid: real commercial game client benchmark
- Benchmark unit: battle / episode

### 3.3 Benchmark scope
- Scope: single game
- Number of games / tasks: 1 game, 8 battle tasks, 4 combat families

### 3.4 Modality
- Primary modality: GUI
- Perception burden retained: raw screenshot parsing, partial observability, turn-order and resource tracking, weakness/status interpretation, and target localization
- Perception burden removed: in TA, detector boxes, OCR text, static UI anchors, and an optional retrieved hint reduce the grounding burden substantially

## 4. What this benchmark measures
- Primary capability target: pixel-to-action grounding under matched low-level and semantic-control protocols
- Secondary capability target(s): selective information seeking, UI affordance grounding, resource and timing management, and target prioritization
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? yes
- Does it test social reasoning / deception / cooperation? no
- Does it test visual grounding / spatial-temporal reasoning? yes
- Does it test long-horizon autonomy / task completion? partially
- Does it test real-time efficiency? no
- Does it test cross-game transfer / open-ended generalization? no
- Why is a game environment especially suitable here? Turn-based RPG combat mixes native scoring, partial observability, and visually grounded action timing, so perception mistakes show up immediately as illegal, mistimed, or strategically poor actions.

## 5. Interaction paradigm
- Observation channel: DC uses the raw screenshot only; TA uses the same screenshot plus optional structured tokens from a per-task YOLOv8 detector and PaddleOCR; Ask persists one textual hint across the episode
- Action channel: DC emits click coordinates `(x, y)` plus a keypress, while TA emits `(character, move, target)` with move in `{Basic, Skill, Release Ultimate, Hold Ultimate}`
- Interface type: native control / hybrid
- Agent scaffold allowed: static UI maps, per-task detection, OCR, and optional one-shot LightRAG help; ReAct and Reflexion appear only as evaluated prompt variants
- Is there privileged API access? no game-engine API is exposed, but TA is still privileged because it exposes detector/OCR outputs and fixed actionable regions
- How close is the setup to human play? medium to high overall; DC is close to human native control, while TA and Ask deliberately move toward semantic assistance
- Main ecological-validity trade-off: Holding tasks and metrics fixed makes interface privilege explicit. TA is valuable because it isolates higher-level decision quality, but it should not be conflated with direct human-like control.

## 6. Evaluation protocol
- Main score: family-specific native HSR metrics: Echo of War uses success, steps, and reward; Memory of Chaos uses remaining cycles; Pure Fiction uses score under an AV budget; Apocalyptic Shadow uses the native composite boss score
- Auxiliary score(s): DC vs TA vs TA-no-OCR comparisons, ask rate/effect/efficiency, and human / AutoBattle baselines
- Evaluation style: native score / completion / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: random policy in TA, AutoBattle, a 10-participant human reference, and VLM baselines from GPT-4o-mini, Claude 3.5 Sonnet, and Gemini 1.5 Flash, plus ReAct / Reflexion prompt variants
- Automatic verifiability: high for the recorded metrics, with practical reproducibility caveats from live-client execution
- Calibration method: fixed Quantum-aligned team, 8 trials per task, fixed 1920x1080 client settings with 0.5 s inter-event delay, matched tasks across regimes, and fail-stop rules after 10 consecutive invalid outputs / actions
- Anti-contamination argument: not the main claim, but the help corpus is public-only and frozen, and the live-service game drift reduces the usefulness of static memorized knowledge
- Reliability or comparability concerns: single-title scope, one standardized team, live-client timing and input noise, per-task detector dependence in TA, and ask-or-act being available only in TA

## 7. Main contributions
- Contribution 1: Defines a real-client RPG benchmark with 8 battles across 4 HSR combat families under matched direct-control and tool-assisted regimes.
- Contribution 2: Makes the raw-control vs semantic-action comparison explicit without relying on engine APIs.
- Contribution 3: Adds a method-agnostic Ask-or-Act diagnostic over a fixed public corpus and decision logs.

## 8. Main findings and failure modes
- Core empirical takeaway: With tasks and metrics held fixed, current VLMs collapse in direct control but become meaningfully competent in tool-assisted play; OCR helps further, and asking is beneficial only when calibrated.
- Notable model failure mode 1: DC exposes a grounding gap, with models clicking non-UI regions or default targets and falling into no-op / basic-attack loops.
- Notable model failure mode 2: TA without OCR still leaves models misreading HP, skill-point, and readiness text, leading to illegal or mistimed actions.
- Notable model failure mode 3: Ask policies differ by model and task type: GPT-4o-mini gets the strongest absolute uplift, Claude is more efficient on Echo of War at a lower ask rate, and Gemini asks frequently with little payoff.
- Does this paper reveal a benchmark-design limitation as well? yes; TA and Ask are intentionally privileged tracks, and live-client execution still introduces reproducibility noise.

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Use Table 1 and the related-work framing to introduce the API / simulator / macro trade-off, then use StarBench as the clean matched case showing why that trade-off matters for human-like play.
- Best use in Section 1 (taxonomy and evolutionary levels): Anchor Level 4 because it compares raw native control and semantic action abstraction inside one benchmark rather than across unrelated papers.
- Best use in Section 2 (core capabilities evaluated by games): Direct support for visual grounding, affordance detection, resource tracking, target selection, and information seeking under partial observability.
- Best use in Section 3 (interaction and evaluation paradigm): Probably the strongest single paper in the corpus for the action-channel trade-off: screenshot -> OS primitives vs semantic tuple, plus family-native metric design and Ask-or-Act evaluation.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Anchor for the claim that current VLMs more often know what to do than they can ground and execute, and for the argument that dual-track protocols are better than collapsing ecological and assisted play into one score.

## 10. Relation to nearby papers
- Closest predecessor(s): VARP and other early non-API real-client agents, plus API-mediated game-agent lines discussed in the paper's related-work table
- Closest follow-up(s): PokeGym and neighboring GUI-control benchmarks such as FlashAdventure and VideoGameBench
- Best comparison targets inside our corpus: Balrog, VARP, FlashAdventure, VideoGameBench
- What this paper uniquely adds relative to neighbors: It keeps the same task suite and native metrics while comparing direct raw control, semantic tool-assisted control, and ask-or-act information seeking.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- Table 1 contrasts prior benchmarks by real client status, observation channel, action interface, tool assistance, direct-control track, and ask-or-act support; StarBench is the only listed setting combining a real-client low-level direct-control track, a matched tool-assisted track, and ask-or-act.
- In DC, the agent receives a 1920x1080 screenshot only and must output `(x, y)` coordinates plus a keypress; actions are executed through `pyautogui`, out-of-range coordinates are clipped, and empty or non-numeric outputs become no-ops.
- In TA, the agent emits `(c, m, t)`, where `m` is one of `Basic`, `Skill`, `Release Ultimate`, or `Hold Ultimate`; a static UI map plus per-task YOLOv8 detections trained on about 400 labeled battle images and PaddleOCR both textify the UI and parameterize target clicks.
- Ask-or-Act is available only in TA: one pre-episode LightRAG query is allowed over a fixed 1.14 MB public corpus, the returned hint persists through the episode, and the system does not return coordinates, macros, or action strings.
- The task suite contains 5 Echo of War bosses (Cocolia, Phantylia, Swarm King, Theater, Feixiao), 1 Upper-Stage Memory of Chaos battle (Xianzhou), 1 Upper-Stage Pure Fiction battle (Cliched), and 1 Upper-Stage Apocalyptic Shadow battle (Stardevourer).
- Metrics are family-specific: Echo of War reports completion steps and a reward combining HP-safety / healing and normalized damage; Memory of Chaos reports remaining cycles from the AV schedule; Pure Fiction sums score within `AVmax = 450`; Apocalyptic Shadow uses the native composite score from HP depletion plus remaining AV; Ask-or-Act reports ask rate, per-ask Effect against the immediately previous episode on the same task, and Efficiency normalized by expected asks with `T = 8`.
- In DC, GPT-4o-mini, Claude 3.5 Sonnet, and Gemini 1.5 Flash all score 0% success on every Echo of War boss and collapse to `-inf` / `0` / `0` on Memory of Chaos / Pure Fiction / Apocalyptic Shadow in Table 5.
- In TA, GPT-4o-mini reaches 100% success on Cocolia, Phantylia, Theater, and Feixiao and 50% on Swarm King; Claude reaches 100%, 87.5%, 87.5%, and 62.5% on four of those bosses, while Gemini remains mostly weak.
- Removing OCR while keeping YOLO boxes hurts GPT-4o-mini from 100% to 62.5% on Cocolia, from 100% to 37.5% on Phantylia, and from 100% to 25% on Theater and Feixiao; Claude shows parallel drops.
- Ask-or-Act differs strongly by model: GPT-4o-mini has the largest Effect on Echo of War (82.8), Pure Fiction (10800), and Apocalyptic Shadow (3002), Claude has the best Echo-of-War Efficiency (27.4) with AR 22.5%, and Gemini asks very frequently on Echo of War (AR 97.5%) with much lower payoff (Effect 47.4, Efficiency 6.1).
- The paper reports that models tend to ask on the first trial of a task; on explicit-goal tasks they often ask only after failure, while on implicit-goal tasks such as Pure Fiction or Memory of Chaos they ask more proactively.

### 11.2 Our synthesis / interpretation
- StarBench is the clearest anchor in the corpus for separating grounding failure from higher-level planning failure, because only the interface changes while tasks and metrics stay fixed.
- Its related-work framing is useful beyond Level 4: it gives us a compact way to discuss API, simulator, and macro privilege before moving into more specific benchmark comparisons.
- Ask-or-Act should be cited as an evaluation-time decision policy layered on top of a privileged interaction regime, not as evidence that retrieval alone solves visual control.

### 11.3 Uncertain or needs re-check
- Because the benchmark runs on a live-service client and the paper's emulator is future work, later drafting should not overstate exact reproducibility beyond the fixed settings already reported.
- TA uses per-task detectors trained on limited labeled images, so if we later compare StarBench to broader generalization benchmarks we should keep the claim narrow to matched interface diagnosis rather than detector-free transfer.
- If later prose needs the full Echo-of-War reward notation or exact per-family values beyond the headline numbers above, re-check Sec. 4.4 and Tables 4-6 directly.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? Already completed for this audit; the paper's survey value depends on Section 2, Table 1, Section 4, and Tables 4-6 rather than abstract-level claims.
- Which section to read next if needed: Sec. 2.3 and Table 1 for interface-trade-off framing; Sec. 4.4 and Tables 4-6 for task and metric detail
- Follow-up question(s): When drafting the API / interface trade-off, pair StarBench with VARP for the non-API motivation and with Balrog or Orak for the broader interface-privilege contrast.

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P0
- Reading depth: deep
- Batch ID: B04
- Outline sections: 0,1,2,3,4
- Survey role: anchor
- Paper card path: `paper_cards/B04/StarBench.md`
- Next action: draft-section
- Last updated: 2026-04-16
