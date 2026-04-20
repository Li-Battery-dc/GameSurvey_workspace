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
- Review gate label: usable

## 1. One-paragraph benchmark summary
- VideoGameBench is a raw-visual benchmark that asks VLM agents to make measurable progress in commercial 1990s video games using only raw frames plus high-level objective and control descriptions. It defines 23 curated games split into a 13-game development set and a 10-game test set, including three secret evaluation games on a private server. Progress is scored by matching gameplay frames to walkthrough-scraped checkpoint frames with perceptual hashes and mapping the furthest matched checkpoint to walkthrough time, which makes the benchmark automatically scorable but also checkpoint-shaped and threshold-sensitive. The paper's paused `Lite` setting is useful for relaxing reaction pressure, but because it effectively turns play into a turn-based interaction it is best treated as a compromise ablation rather than a clean replica of the real-time task; for this survey, the paper is a supporting Level 4 case on raw-visual control, very low frontier VLM scores, and checkpoint-based evaluation design.

## 2. Position in our survey
- Why-games relevance: Real video games expose the full loop from noisy perception to long-horizon control while still permitting partial automatic scoring through walkthrough-frame checkpoints.
- Historical stage: ecological agent benchmark
- Benchmark level(s): L4 visual agency
- Most relevant outline section(s): 2,3,4
- Role in corpus: representative

## 3. Design-space coding
### 3.1 Game structure
- Information structure: mixed
- Transition structure: mixed
- Agent structure: single-agent
- Social structure: N/A
- Time structure: hybrid

### 3.2 Environment structure
- Environment type(s): adventure-quest world
- Real game / simulated game / designed task-game hybrid: curated suite of commercial video games in emulation
- Benchmark unit: full game run / episode

### 3.3 Benchmark scope
- Scope: curated suite
- Number of games / tasks: 23 games total, with 13 dev games and a 10-game test split that includes 7 public titles plus 3 secret held-out games

### 3.4 Modality
- Observation modality: visual image
- Action modality: native control
- Perception burden retained: raw screen interpretation, timing pressure, object localization, navigation, and low-level controller or mouse-keyboard choice
- Perception burden removed: native human motor execution is abstracted into structured language actions and emulator commands

## 4. What this benchmark measures
- Primary capability target: end-to-end visual game completion under real-time constraints
- Secondary capability target(s): long-horizon planning, scene understanding, control timing, and limited cross-game generalization
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? yes
- Does it test social reasoning / deception / cooperation? no
- Does it test visual grounding / spatial-temporal reasoning? yes
- Does it test long-horizon autonomy / task completion? yes
- Does it test real-time efficiency? yes
- Does it test cross-game transfer / open-ended generalization? partially
- Why is a game environment especially suitable here? It couples perception, control, and delayed consequences in a way that static multimodal tasks do not, while still exposing recognizable milestone states that can be tracked automatically.

## 5. Interaction paradigm
- Observation channel: raw game frames, plus game-specific objective and control instructions and recent trajectory context; in `Lite`, the paused setup also changes how DOS and Game Boy frame histories are packaged
- Action channel: structured language actions for keyboard, mouse, or Game Boy button sequences; the `Lite` Game Boy prompt further reduces each decision step to a single action tuple
- Interface type: structured action space / hybrid
- Agent scaffold allowed: memory / ReAct-style scratchpad
- Is there privileged API access? no
- How close is the setup to human play? medium: it preserves raw frames and native game dynamics, but uses prompted control descriptions, a ReAct-style memory scaffold, and structured action emission instead of human motor input
- Main ecological-validity trade-off: the benchmark keeps raw pixels and commercial games, but still abstracts control into language-formatted actions, scores progress through walkthrough-frame matching, and uses a paused `Lite` setting that relaxes the real-time loop

## 6. Evaluation protocol
- Main score: percentage of game completed estimated from the furthest matched walkthrough checkpoint
- Auxiliary score(s): VideoGameBench Lite scores, per-game checkpoint progress, and practice-game performance
- Evaluation style: milestone / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: model-only benchmark on the test games; a co-author is only used to verify that the interface can reach early checkpoints in Kirby's Dream Land and Doom II under the same information restrictions
- Automatic verifiability: medium-high
- Calibration method: equal weighting across games, secret held-out test titles, walkthrough-timestamp checkpoints, per-checkpoint hash-threshold tuning, and runtime caps tied to walkthrough length
- Anti-contamination argument: dev/test separation, secret games, and strict no-tools/no-overlay rules reduce benchmark gaming, but the paper explicitly notes that pretraining exposure to guides and walkthroughs remains possible
- Reliability or comparability concerns: checkpoint progress is coarse and walkthrough-shaped; full-screen perceptual-hash matching requires manual threshold tuning and can fail when differences are local, HUD-dependent, or resolution-dependent; only one run per model is reported in the main benchmark; and `Lite` is not a clean latency-only ablation because it pauses the game and changes some prompt or observation details

## 7. Main contributions
- Contribution 1: Introduces a 23-game commercial-video-game benchmark with a 10-game test split that includes secret held-out titles.
- Contribution 2: Proposes walkthrough-frame checkpoint tracking by matching gameplay frames to scraped longplay images with perceptual hashes.
- Contribution 3: Adds VideoGameBench Lite, a paused setting that relaxes reaction-time pressure, and shows that current VLMs still barely progress even under that easier protocol.

## 8. Main findings and failure modes
- Core empirical takeaway: no tested VLM completes a benchmark game; scores remain near zero in both settings, with Gemini 2.5 Pro reaching 0.48% overall on the 10-game test split and the best Lite score only reaching 1.6% over three paused games.
- Notable model failure mode 1: inference latency makes actions stale in the full real-time setting before the model can execute what it intended
- Notable model failure mode 2: models show a knowing-doing gap and visual misprocessing, often stating the correct objective but emitting badly grounded control actions
- Notable model failure mode 3: planning and memory failures create state confusion, forgotten objectives, and repeated loops even in the paused `Lite` setting
- Does this paper reveal a benchmark-design limitation as well? yes; conclusions depend both on the paused-versus-real-time protocol and on heuristic walkthrough-frame checkpoint detection rather than direct state verification

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): A supporting ecological example of why games reveal coupled perception, control, and memory failures that static multimodal tests understate.
- Best use in Section 1 (taxonomy and evolutionary levels): A supporting Level 4 case that distinguishes raw-screen game play from more abstract visual setups, without needing to treat it as a primary generalization anchor.
- Best use in Section 2 (core capabilities evaluated by games): Useful evidence for visual grounding, time-sensitive action, and the fact that some failures persist after reaction deadlines are relaxed.
- Best use in Section 3 (interaction and evaluation paradigm): Best used for the front-end/back-end split: raw pixels plus structured control on the interaction side, walkthrough-frame pHash checkpoint matching on the evaluation side, and `Lite` as a compromised pause-based latency ablation.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Concrete evidence for stale actions, knowing-doing gaps, visual misreads, and looped planning failures, but not a paper to overuse for broader transfer claims.

## 10. Relation to nearby papers
- Closest predecessor(s): LVLMGamePlayers, Balrog, GameArena
- Closest follow-up(s): FlashAdventure, StarBench, GameplayQA
- Best comparison targets inside our corpus: LVLMGamePlayers, FlashAdventure, AtariGPT, Balrog
- What this paper uniquely adds relative to neighbors: It combines raw commercial-game play, secret held-out titles, heuristic walkthrough-frame checkpoint matching, and a paused `Lite` comparison that exposes both latency and protocol-design trade-offs.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- The paper defines a 23-game benchmark spanning Game Boy, Game Boy Color, and MS-DOS titles, split into 13 dev games and a 10-game test set with 7 public titles plus 3 secret games.
- Agents receive raw game frames plus basic objective and control instructions, and the baseline VG-Agent uses a ReAct-style scaffold with textual memory.
- VideoGameBench Lite pauses the emulator while the agent is deciding, which the paper says effectively turns real-time play into a turn-based interaction; in the reported setup, DOS Lite uses five past frames spaced 0.1 seconds apart while Game Boy Lite uses the most recent frame.
- Progress is measured by scraping checkpoint frames from longplay walkthroughs, matching emulator frames to those checkpoint images with perceptual hashes, and mapping the furthest matched checkpoint to the walkthrough timestamp.
- The checkpoint detector uses a baseline Hamming threshold of under 12 with per-checkpoint tuning, and the appendix notes limitations when checkpoint differences are local to part of the image, or when HUD state or resolution differs from the walkthrough.
- The best reported overall scores are 0.48% on the full benchmark and 1.6% on VideoGameBench Lite, and the paper's qualitative analysis attributes low performance to latency, knowing-doing gaps, visual misprocessing, and weak planning or memory management.

### 11.2 Our synthesis / interpretation
- VideoGameBench is better used as a supporting Level 4 evidence card than as a top visual-agency anchor, because its main survey value comes from a narrow but clear combination of raw-visual control, very low scores, and explicit qualitative failure analysis.
- Its evaluation protocol is best described as walkthrough-frame template matching with perceptual hashes, which makes it useful for Section 3 discussions about backend scoring but weaker than direct state-verifiable evaluation as a methodological anchor.
- Its full-versus-`Lite` pairing is still useful in Section 3 and Section 4, but mainly as a relaxed-reaction-pressure comparison rather than as a clean causal separation of reasoning from execution.

### 11.3 Uncertain or needs re-check
- Re-check Appendix C and D if we later need per-game checkpoint counts, runtime caps, or cost details for tighter cross-benchmark comparison.
- If we compare `Lite` numerically against other real-time papers, re-check how much its pause mechanism and prompt or frame-packaging changes matter beyond latency alone.
- If we make strong claims about evaluation robustness, re-check the released implementation details for per-checkpoint thresholds and any crop-based matching changes beyond the paper text.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? Already done for the current audit; no immediate reread is required unless we need appendix-level protocol detail in the draft.
- Which section to read next if needed: Appendix C and D on checkpoint construction, runtime caps, and prompt/interface details
- Follow-up question(s): How much of the gap between the main benchmark and `Lite` should be attributed to pausing itself versus the accompanying prompt and observation changes?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P2
- Reading depth: deep
- Batch ID: B04
- Outline sections: 2,3,4
- Survey role: representative
- Paper card path: `paper_cards/B04/VideoGameBench.md`
- Check status: unchecked
- Last updated: 2026-04-15
