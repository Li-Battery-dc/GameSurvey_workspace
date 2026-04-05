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
- StarBench evaluates whether VLM agents can translate raw RPG screenshots into precise low-level actions and decide when to seek external help before acting. Built on turn-based Honkai: Star Rail battles, it offers two matched regimes: direct control from pixels to click coordinates and keypresses, and tool-assisted control through a higher-level action triple. It also adds an ask-or-act diagnostic in which agents may query a frozen public-help corpus once before a battle. For the survey, StarBench is a strong benchmark for comparing privileged versus ecological interfaces in visual game play.

## 2. Position in our survey
- Why-games relevance: It captures the pixel-to-action mapping and selective information seeking that static multimodal benchmarks usually abstract away.
- Historical stage: ecological agent benchmark
- Narrative level(s): L4 visual agency
- Most relevant outline section(s): 3,4,5,6
- Role in corpus: representative

## 3. Design-space coding
### 3.1 Environment structure
- Information structure: mixed
- Transition structure: deterministic
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
- Observation channel: screenshots, optionally with tool-assisted textualized observations
- Action channel: either pixel coordinates plus keypress or a high-level `(character, move, target)` tuple
- Interface type: GUI interaction / hybrid
- Agent scaffold allowed: retrieval / tool use
- Is there privileged API access? yes, in tool-assisted mode
- How close is the setup to human play? medium; direct-control mode is close to human GUI play, while tool-assisted mode is deliberately more privileged
- Main ecological-validity trade-off: The benchmark cleanly compares raw control with structured assistance, but the latter substantially simplifies the UI-grounding problem.

## 6. Evaluation protocol
- Main score: family-specific native battle objective
- Auxiliary score(s): direct-control versus tool-assisted performance and ask-or-act gains
- Evaluation style: native score / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: model baselines plus human reference
- Automatic verifiability: high
- Calibration method: fixed client, canonical team composition, and matched tasks across regimes
- Anti-contamination argument: the ask-or-act corpus is frozen and public, but contamination is not the paper's main claim
- Reliability or comparability concerns: results depend on one canonical team setup and a single frozen retrieval pipeline for ask-or-act

## 7. Main contributions
- Contribution 1: Builds a real-client RPG benchmark with both direct-control and tool-assisted regimes.
- Contribution 2: Adds an ask-or-act diagnostic for selective information seeking.
- Contribution 3: Formalizes a clean comparison between low-level GUI control and higher-level action abstraction.

## 8. Main findings and failure modes
- Core empirical takeaway: Direct pixel-to-action play remains much harder than tool-assisted play, and selective help-seeking can improve outcomes when used judiciously.
- Notable model failure mode 1: poor UI grounding in direct control causes missed clicks or ineffective actions
- Notable model failure mode 2: models fail to infer latent combat state from visible cues alone
- Notable model failure mode 3: agents do not always know when asking for help is worth the cost
- Does this paper reveal a benchmark-design limitation as well? yes; the tool-assisted regime is powerful enough that comparisons must distinguish ecological and privileged performance explicitly

## 9. Why this paper matters for our survey
- Best use in Section 0 (why games): Good evidence that games can expose multimodal action problems beyond plain visual question answering.
- Best use in Section 1 (historical evolution): Useful modern example of GUI-grounded agent benchmarking.
- Best use in Section 2 (design space): Helps place GUI-based real-client play in the taxonomy.
- Best use in Section 3 (capability targets): Strong for visual grounding, action selection, and information seeking.
- Best use in Section 4 (interaction paradigm): Excellent comparison case for privileged versus ecological interfaces.
- Best use in Section 5 (evaluation protocol): Useful for family-specific battle metrics and ask-or-act evaluation.
- Best use in Section 6/7 (limitations and future): Supports the claim that perception-to-control fidelity is still a major weakness.

## 10. Relation to nearby papers
- Closest predecessor(s): GUI-agent benchmarks and earlier VLM game-agent papers
- Closest follow-up(s): FlashAdventure and related real-client GUI benchmarks
- Best comparison targets inside our corpus: Balrog, GameVerse, FlashAdventure, VideoGameBench
- What this paper uniquely adds relative to neighbors: It cleanly compares raw pixel control, structured tool assistance, and information seeking within one benchmark.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- StarBench evaluates eight Honkai: Star Rail battle tasks under direct-control and tool-assisted regimes.
- Direct control requires pixel coordinates and keypresses, while tool-assisted mode uses a high-level action triple.
- The benchmark includes a single pre-episode ask-or-act choice backed by a frozen retrieval corpus.

### 11.2 Our synthesis / interpretation
- StarBench is one of the clearest papers for discussing interface privilege as an explicit benchmark variable.
- It is especially useful when contrasting visual grounding with higher-level action abstraction.

### 11.3 Uncertain or needs re-check
- Recheck Section 4.4 if we later need the exact metric definitions for each combat family.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? No immediate reread; the interface design and survey value are already clear.
- Which section to read next if needed: 4.1 / 4.2 / 4.4
- Follow-up question(s): When drafting Section 4, should ask-or-act be grouped under retrieval or under evaluation-time decision policies?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P1
- Reading depth: deep
- Batch ID: B03
- Outline sections: 3,4,5,6
- Survey role: representative
- Paper card path: `paper_cards/B03/StarBench.md`
- Next action: draft-section
- Last updated: 2026-04-05
