# VideoGameBench VideoGameBench: Can Vision-Language Models complete popular video games?

## 0. Metadata
- Date: 2025/05
- Venue: arXiv
- Authors: Alex L. Zhang, Thomas L. Griffiths, Karthik R. Narasimhan, Ofir Press
- Paper link: https://arxiv.org/pdf/2505.18134v2.pdf
- Code link: https://github.com/alexzhang13/videogamebench
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: high
- Review gate label: strong

## 1. One-paragraph benchmark summary
- VideoGameBench is a raw-visual game benchmark that evaluates whether VLM agents can make measurable progress in commercial 1990s video games using only game frames plus high-level objective and control descriptions. The benchmark contains 23 curated games split into a 13-game development set and a 10-game test set, with three secret test games hosted on a private server to discourage narrow optimization to known titles. Progress is scored with walkthrough-derived checkpoints rather than only final win states, and the paper also introduces a paused `Lite` subset to separate reaction-time limits from planning limits. For this survey, it is a strong visual-agency paper because it preserves perception, timing pressure, and long-horizon control while still keeping progress automatically measurable.

## 2. Position in our survey
- Why-games relevance: Real video games expose the full loop from noisy perception to long-horizon control while still permitting automatic progress checks.
- Historical stage: ecological agent benchmark
- Narrative level(s): L4 visual agency / L5 cross-game generalization (secondary)
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
- World type(s): adventure / platformer / other
- Real game / simulated game / designed task-game hybrid: curated suite of commercial video games in emulation
- Benchmark unit: full game run / episode

### 3.3 Benchmark scope
- Scope: curated suite
- Number of games / tasks: 23 games total, with 13 dev games and a 10-game test split that includes 7 public titles plus 3 secret held-out games
- Benchmark intent: ecological evaluation

### 3.4 Modality
- Primary modality: image / short frame history
- Perception burden retained: raw screen interpretation, timing pressure, object localization, navigation, and low-level controller or mouse-keyboard choice
- Perception burden removed: native human motor execution is abstracted into structured language actions and emulator commands

## 4. What this benchmark measures
- Primary capability target: end-to-end visual game completion under real-time constraints
- Secondary capability target(s): long-horizon planning, scene understanding, control timing, and cross-game transfer
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? yes
- Does it test social reasoning / deception / cooperation? no
- Does it test visual grounding / spatial-temporal reasoning? yes
- Does it test long-horizon autonomy / task completion? yes
- Does it test real-time efficiency? yes
- Does it test cross-game transfer / open-ended generalization? yes
- Why is a game environment especially suitable here? It couples perception, control, and delayed rewards in a way that static multimodal tasks do not.

## 5. Interaction paradigm
- Observation channel: raw game frames, plus game-specific objective and control instructions and recent trajectory context
- Action channel: structured language actions for keyboard, mouse, or Game Boy button sequences
- Interface type: structured action space / hybrid
- Agent scaffold allowed: memory / ReAct-style scratchpad
- Is there privileged API access? no
- How close is the setup to human play? medium-high: it preserves raw frames and timing pressure, but uses prompted control descriptions, a ReAct agent scaffold, and structured action emission instead of native human motor play
- Main ecological-validity trade-off: the benchmark keeps the raw visual interface, but still relies on structured action APIs, walkthrough-derived checkpoints, and a scaffold with textual memory to make evaluation tractable

## 6. Evaluation protocol
- Main score: percentage of walkthrough checkpoints completed
- Auxiliary score(s): VideoGameBench Lite scores, per-game checkpoint progress, and practice-game performance
- Evaluation style: milestone / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: frontier VLMs are compared on the same test games; the paper separately validates the interface by having a human complete early levels using the same information available to the agent
- Automatic verifiability: high
- Calibration method: equal weighting across games, secret held-out test titles, walkthrough-timestamp checkpoints, and runtime caps tied to walkthrough length
- Anti-contamination argument: dev/test separation, secret games, and strict no-tools/no-overlay rules reduce benchmark gaming, but the paper explicitly notes that pretraining exposure to guides and walkthroughs remains possible
- Reliability or comparability concerns: checkpoint progress is coarse and walkthrough-shaped, only one run per model is reported in the main benchmark, and default-mode scores entangle reasoning with latency

## 7. Main contributions
- Contribution 1: Introduces a 23-game commercial-video-game benchmark with a 10-game test split that includes secret held-out titles.
- Contribution 2: Proposes automated checkpoint-based progress tracking from YouTube walkthroughs using perceptual hashing.
- Contribution 3: Adds VideoGameBench Lite to isolate reaction-time effects and shows that current VLMs still barely progress even when latency is removed.

## 8. Main findings and failure modes
- Core empirical takeaway: no tested VLM completes a benchmark game; the best full-benchmark result is Gemini 2.5 Pro at 0.48% overall, while the Lite subset raises the best overall score only to 1.6%.
- Notable model failure mode 1: inference latency prevents timely reactions in the full real-time setting
- Notable model failure mode 2: models exhibit a knowing-doing gap, often recognizing what to do but failing to execute it correctly in control space
- Notable model failure mode 3: state confusion and repetitive action loops stall long-horizon progress even when the environment is paused
- Does this paper reveal a benchmark-design limitation as well? yes; it shows that benchmark conclusions depend strongly on whether real-time latency is treated as part of the task or factored out

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): A contemporary ecological example of why games reveal coupled perception, control, and memory failures that static multimodal tests understate.
- Best use in Section 1 (taxonomy and evolutionary levels): A late-stage visual-agency benchmark that helps distinguish raw-screen game play from older symbolic or scaffold-heavier visual setups.
- Best use in Section 2 (core capabilities evaluated by games): Direct support for visual grounding, time-sensitive action, and long-horizon progress tracking in the same benchmark.
- Best use in Section 3 (interaction and evaluation paradigm): One of the batch's strongest references for the trade-off between raw ecological interfaces, structured action APIs, checkpoint scoring, and latency-controlled ablations.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Strong evidence that raw-vision evaluation still surfaces severe latency, control, and state-tracking failures even for frontier VLMs.

## 10. Relation to nearby papers
- Closest predecessor(s): LVLMGamePlayers, Balrog, GameArena
- Closest follow-up(s): FlashAdventure, StarBench, GameplayQA
- Best comparison targets inside our corpus: Balrog, VMage, LVLMGamePlayers, AtariGPT, FlashAdventure
- What this paper uniquely adds relative to neighbors: It combines raw commercial-game play, secret held-out titles, automated walkthrough-based progress tracking, and a matched Lite ablation for latency.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- The paper defines a 23-game benchmark spanning Game Boy, Game Boy Color, and MS-DOS titles, split into 13 dev games and a 10-game test set with 7 public titles plus 3 secret games.
- Agents receive raw game frames plus basic objective and control instructions, and the baseline VG-Agent uses a ReAct-style scaffold with textual memory.
- Progress is measured by matching gameplay frames to walkthrough-derived checkpoints via perceptual hashing, and the best reported overall scores are 0.48% on the full benchmark and 1.6% on VideoGameBench Lite.

### 11.2 Our synthesis / interpretation
- VideoGameBench is one of the strongest corpus papers for arguing that visual-game benchmarking should preserve ecological interface difficulty instead of collapsing play into symbolic state.
- Its full-versus-Lite pairing makes it especially useful in Section 3 and Section 4, where we need to separate reasoning limitations from systems-level latency limitations.
- Its support for Level 5 is secondary: the secret games and multi-title split matter for generalization, but the paper is primarily an L4 visual-agency anchor.

### 11.3 Uncertain or needs re-check
- Re-check Appendix C and D if we later need per-game checkpoint counts, runtime caps, or cost details for tighter cross-benchmark comparison.
- If we compare interface burden across visual papers, re-check how much the Game Boy and MS-DOS prompt differences should be foregrounded as benchmark heterogeneity.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? Already done for the current audit; no immediate reread is required unless we need appendix-level protocol detail in the draft.
- Which section to read next if needed: Appendix C and D on checkpoint construction, runtime caps, and prompt/interface details
- Follow-up question(s): Which of the reported failures should be attributed to latency, and which persist clearly in the Lite setting?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P1
- Reading depth: deep
- Batch ID: B09
- Outline sections: 2,3,4
- Survey role: representative
- Paper card path: `paper_cards/B09/VideoGameBench.md`
- Check status: unchecked
- Last updated: 2026-04-09
