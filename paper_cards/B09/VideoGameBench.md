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
- VideoGameBench is a vision-first benchmark that asks VLMs to complete commercial video games using only raw gameplay video and natural-language actions. It covers 23 curated games, including a public development set and a hidden test set with three secret titles, and tracks progress with walkthrough-derived checkpoints rather than only final score. The benchmark is explicitly designed to preserve the latency, perception, and interface burden of real play while also offering a paused `Lite` mode that isolates reasoning from inference delay. For this survey, it is one of the clearest recent anchors for visual game agency under ecologically realistic constraints.

## 2. Position in our survey
- Why-games relevance: Real video games expose the full loop from noisy perception to long-horizon control while still permitting automatic progress checks.
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
- World type(s): adventure / platformer / other
- Real game / simulated game / designed task-game hybrid: curated suite of commercial video games in emulation
- Benchmark unit: game episode

### 3.3 Benchmark scope
- Scope: curated suite
- Number of games / tasks: 23 games total, with 10 public test games, 13 dev games, and 3 secret held-out test games
- Benchmark intent: ecological evaluation

### 3.4 Modality
- Primary modality: video / image
- Perception burden retained: full screen interpretation, progress detection from visuals, timing, and controller-level action selection
- Perception burden removed: no native mouse/keyboard dexterity; actions are exposed through a natural-language control interface

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
- Observation channel: raw gameplay frames from emulated Game Boy, Game Boy Color, and MS-DOS titles
- Action channel: natural-language action commands mapped to emulator controls
- Interface type: natural language / GUI interaction / hybrid
- Agent scaffold allowed: none
- Is there privileged API access? no
- How close is the setup to human play? high in the default mode; the Lite mode pauses the emulator to remove inference-latency pressure
- Main ecological-validity trade-off: checkpoint scoring improves measurement reliability, but progress is still operationalized through walkthrough-derived milestones rather than only native win conditions

## 6. Evaluation protocol
- Main score: percentage of walkthrough checkpoints completed
- Auxiliary score(s): completion on VideoGameBench Lite, per-game success, and latency-sensitive comparisons
- Evaluation style: milestone / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: frontier VLMs are compared on the same games, with walkthrough traces used as the progress reference
- Automatic verifiability: high
- Calibration method: hidden games in the test set, secret titles, and checkpoint hashing from YouTube walkthroughs
- Anti-contamination argument: the secret games and hidden checkpoints reduce direct memorization and answer leakage
- Reliability or comparability concerns: checkpoint design may favor walkthrough-like trajectories, and the default benchmark entangles reasoning quality with inference latency

## 7. Main contributions
- Contribution 1: Introduces a real-game visual benchmark with hidden titles and checkpoint-based progress scoring.
- Contribution 2: Separates ecological play from latency-controlled play through the Lite setting.
- Contribution 3: Provides strong empirical evidence that current VLMs barely make progress on popular games under realistic timing constraints.

## 8. Main findings and failure modes
- Core empirical takeaway: even the best reported model reaches only 0.48% on the full benchmark and 1.6% on the paused Lite variant, showing that popular video games remain largely unsolved.
- Notable model failure mode 1: inference latency prevents timely reactions in the full real-time setting
- Notable model failure mode 2: weak visual grounding causes missed affordances and poor state tracking
- Notable model failure mode 3: long-horizon progress stalls despite access to natural-language action descriptions
- Does this paper reveal a benchmark-design limitation as well? yes; it shows that benchmark conclusions depend strongly on whether real-time latency is treated as part of the task or factored out

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): A strong contemporary example of why games expose coupled perception-planning-control failures.
- Best use in Section 1 (taxonomy and evolutionary levels): Marks a shift from symbolic or text interfaces back to raw commercial-game play. Useful for contrasting real-game visual suites with scaffold-heavy harnesses.
- Best use in Section 2 (core capabilities evaluated by games): Supports claims about visual grounding and long-horizon control as distinct bottlenecks.
- Best use in Section 3 (interaction and evaluation paradigm): Central evidence for preserving human-like visual interfaces. Good reference for checkpoint-based scoring and hidden-game contamination controls.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Supports the claim that current frontier models still fail badly when latency and raw perception are preserved.

## 10. Relation to nearby papers
- Closest predecessor(s): Balrog, Orak
- Closest follow-up(s): LMGAME-BENCH, V-MAGE
- Best comparison targets inside our corpus: Balrog, Orak, LMGAME-BENCH, V-MAGE, AtariGPT
- What this paper uniquely adds relative to neighbors: It keeps the interface closest to human play while explicitly quantifying the effect of inference delay with a matched paused benchmark.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- The paper evaluates 23 games drawn from Game Boy, Game Boy Color, and MS-DOS titles.
- The benchmark includes 10 public test games, 13 development games, and 3 secret held-out games in the test set.
- Progress is measured through walkthrough-derived checkpoints, and the paper reports best-model scores of 0.48% on the full benchmark and 1.6% on VideoGameBench Lite.

### 11.2 Our synthesis / interpretation
- VideoGameBench is one of the strongest corpus papers for arguing that visual-game benchmarking should preserve ecological interface difficulty instead of collapsing it into symbolic state.
- Its paired full-versus-Lite design is especially useful for separating reasoning limits from systems-level latency limits.

### 11.3 Uncertain or needs re-check
- Re-check the appendix if we later need the exact public versus hidden split for every individual title.
- Re-check the checkpoint construction details if we need to compare them directly with judge-based milestone systems in other papers.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? A later reread is worthwhile because this paper can anchor multiple sections on visual agency and protocol design.
- Which section to read next if needed: benchmark construction / checkpoint design / Lite-vs-full evaluation
- Follow-up question(s): Which specific games best isolate latency failure versus perceptual failure?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P1
- Reading depth: deep
- Batch ID: B09
- Outline sections: 2,3,4
- Survey role: representative
- Paper card path: `paper_cards/B09/VideoGameBench.md`
- Next action: draft-section
- Last updated: 2026-04-05
