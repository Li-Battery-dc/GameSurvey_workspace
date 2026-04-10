# StarBench StarBench: A Turn-Based RPG Benchmark for Agentic Multimodal Decision-Making and Information Seeking

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
- StarBench evaluates whether VLM agents can translate raw RPG screenshots into precise low-level actions and decide when to seek external help before acting. Built on real-client Honkai: Star Rail battles, it standardizes eight combat tasks across four combat families under two matched regimes: direct control from screenshots to click coordinates and keypresses, and tool-assisted control through a high-level action tuple backed by OCR and detection aids. It also adds an ask-or-act diagnostic in which agents may issue one pre-battle query to a frozen public-help corpus in the tool-assisted regime. For the survey, StarBench is a strong benchmark for comparing human-like GUI control against deliberately privileged assistance inside the same task setup.

## 2. Position in our survey
- Why-games relevance: It captures the pixel-to-action mapping and selective information seeking that static multimodal benchmarks usually abstract away.
- Historical stage: ecological agent benchmark
- Narrative level(s): L4 visual agency
- Most relevant outline section(s): 2,3,4
- Role in corpus: representative

## 3. Design-space coding
### 3.1 Environment structure
- Information structure: mixed
- Transition structure: mixed
- Agent structure: single-agent
- Social structure: N/A
- Time structure: turn-based

### 3.2 World structure
- World type(s): other
- Real game / simulated game / designed task-game hybrid: real client game benchmark
- Benchmark unit: battle

### 3.3 Benchmark scope
- Scope: single game
- Number of games / tasks: 8 battle tasks across 4 combat families
- Benchmark intent: ecological evaluation

### 3.4 Modality
- Primary modality: GUI
- Perception burden retained: raw screenshots, UI grounding, latent combat-state inference, target localization
- Perception burden removed: internal state access beyond the visible UI and optional tool summaries in TA mode

## 4. What this benchmark measures
- Primary capability target: multimodal decision making from pixels to game actions
- Secondary capability target(s): information seeking, UI grounding, target selection, battle tempo management
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? yes
- Does it test social reasoning / deception / cooperation? no
- Does it test visual grounding / spatial-temporal reasoning? yes
- Does it test long-horizon autonomy / task completion? partially
- Does it test real-time efficiency? no
- Does it test cross-game transfer / open-ended generalization? no
- Why is a game environment especially suitable here? RPG combat exposes the full chain from visual parsing to action selection while keeping outcomes and battle objectives measurable.

## 5. Interaction paradigm
- Observation channel: raw screenshots in direct control; screenshots plus detector and OCR-derived textualized observations in tool-assisted mode
- Action channel: either pixel coordinates plus keypress or a high-level `(character, move, target)` tuple
- Interface type: GUI interaction / hybrid
- Agent scaffold allowed: tool use in TA mode; retrieval is added only for the ask-or-act diagnostic
- Is there privileged API access? no engine API access, but TA mode provides privileged detector/OCR outputs and static UI anchors
- How close is the setup to human play? medium; direct-control mode is close to human GUI play, while tool-assisted mode deliberately abstracts away much of the UI-grounding burden
- Main ecological-validity trade-off: The benchmark cleanly compares raw control with structured assistance, but TA substantially simplifies perception-to-action grounding

## 6. Evaluation protocol
- Main score: family-specific native combat metric
- Auxiliary score(s): direct-control versus tool-assisted performance, OCR ablations, and ask-or-act gains
- Evaluation style: native score / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: random policy, autobattle, VLM baselines, and a human expert reference
- Automatic verifiability: high
- Calibration method: fixed client settings, standardized team composition, matched tasks across regimes, and eight trials per task
- Anti-contamination argument: the ask-or-act corpus is frozen and public, but contamination is not the paper's main claim
- Reliability or comparability concerns: results depend on one live-service title, one canonical team setup, OS-level input stability, and a single frozen retrieval pipeline for ask-or-act

## 7. Main contributions
- Contribution 1: Builds a real-client RPG benchmark with both direct-control and tool-assisted regimes.
- Contribution 2: Adds an ask-or-act diagnostic for selective information seeking.
- Contribution 3: Formalizes a clean comparison between low-level GUI control and higher-level action abstraction.

## 8. Main findings and failure modes
- Core empirical takeaway: Direct pixel-to-action play remains far harder than tool-assisted play, while selective help-seeking can improve outcomes when used judiciously.
- Notable model failure mode 1: poor UI grounding in direct control causes missed clicks or ineffective actions
- Notable model failure mode 2: models fail to infer latent combat state from visible cues alone, especially without OCR text
- Notable model failure mode 3: agents do not always know when asking for help is worth the cost
- Does this paper reveal a benchmark-design limitation as well? yes; the TA regime is intentionally privileged enough that ecological and assisted results must be reported separately

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Good evidence that games can expose multimodal action problems beyond plain visual question answering.
- Best use in Section 1 (taxonomy and evolutionary levels): Useful modern example of GUI-grounded real-client play, especially for contrasting raw control with assisted control.
- Best use in Section 2 (core capabilities evaluated by games): Strong for visual grounding, action selection, and information seeking.
- Best use in Section 3 (interaction and evaluation paradigm): Excellent comparison case for ecological versus privileged interfaces, family-specific native metrics, and explicit ask-or-act decisions.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Supports the claim that perception-to-control fidelity is still a major weakness.

## 10. Relation to nearby papers
- Closest predecessor(s): GUI-agent benchmarks, HSR-focused game-agent studies, and earlier VLM game-agent papers
- Closest follow-up(s): later real-client GUI benchmarks such as FlashAdventure
- Best comparison targets inside our corpus: FlashAdventure, VideoGameBench, Balrog, GameplayQA
- What this paper uniquely adds relative to neighbors: It cleanly compares raw pixel control, structured tool assistance, and ask-or-act information seeking within one benchmark on a live client.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- StarBench evaluates eight Honkai: Star Rail battle tasks across four combat families under direct-control and tool-assisted regimes.
- Direct control requires explicit pixel coordinates plus keypresses, while TA uses a structured `(character, move, target)` action tuple.
- TA mode relies on per-task YOLOv8 detection, PaddleOCR text extraction, and static UI anchors rather than engine APIs.
- The ask-or-act diagnostic is available only in TA mode and allows one pre-episode query to a frozen public LightRAG corpus.

### 11.2 Our synthesis / interpretation
- StarBench is one of the clearest papers for discussing interface privilege as an explicit benchmark variable.
- It is especially useful when contrasting visual grounding with higher-level action abstraction.

### 11.3 Uncertain or needs re-check
- Recheck the metric section if we later need the exact per-family formulas or the emulator plans mentioned in the discussion.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? No immediate reread; the interface design and survey value are already clear.
- Which section to read next if needed: interaction protocol / task suite / metrics
- Follow-up question(s): When drafting Section 4, should ask-or-act be grouped under retrieval or under evaluation-time decision policies?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P1
- Reading depth: deep
- Batch ID: B04
- Outline sections: 2,3,4
- Survey role: representative
- Paper card path: `paper_cards/B04/StarBench.md`
- Next action: draft-section
- Last updated: 2026-04-10
