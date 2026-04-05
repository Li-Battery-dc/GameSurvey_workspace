# FlashAdventure FlashAdventure: A Benchmark for GUI Agents Solving Full Story Arcs in Diverse Adventure Games

## 0. Metadata
- Date: 2025/09
- Venue: EMNLP 2025
- Authors: Jaewoo Ahn, Junseo Kim, Heeseung Yun, Jaehyeon Son, Dongmin Park, Jaewoong Cho, Gunhee Kim
- Paper link: https://arxiv.org/pdf/2509.01052v1
- Code link: https://github.com/ahnjaewoo/FlashAdventure
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: high
- Review gate label: strong

## 1. One-paragraph benchmark summary
- FlashAdventure is a GUI-agent benchmark built from 34 classic Flash adventure games and focused on completing full story arcs rather than short subgoals. The benchmark formulates play as a POMDP over RGB frames and low-level GUI actions, documents substantial long-range observation-behavior gaps, and evaluates agents with success, milestone, and progress metrics. It also introduces CUA-as-a-Judge for automatic milestone verification and COAST as a clue-memory-based baseline framework. In the survey, FlashAdventure is a strong anchor for long-horizon GUI play with memory-dependent task completion.

## 2. Position in our survey
- Why-games relevance: Adventure games create long dependency chains and memory-heavy task structure that static benchmarks rarely capture.
- Historical stage: ecological agent benchmark
- Narrative level(s): L4 visual agency / L5 cross-game generalization
- Most relevant outline section(s): 3,4,6,7
- Role in corpus: representative

## 3. Design-space coding
### 3.1 Environment structure
- Information structure: imperfect
- Transition structure: mixed
- Agent structure: single-agent
- Social structure: N/A
- Time structure: turn-based

### 3.2 World structure
- World type(s): adventure
- Real game / simulated game / designed task-game hybrid: real game suite played through Flash emulation
- Benchmark unit: full task arc

### 3.3 Benchmark scope
- Scope: curated suite
- Number of games / tasks: 34 games
- Benchmark intent: ecological evaluation

### 3.4 Modality
- Primary modality: GUI
- Perception burden retained: raw RGB frames, GUI grounding, hidden internal state, long-horizon clue use
- Perception burden removed: internal engine state and direct symbolic progress access

## 4. What this benchmark measures
- Primary capability target: long-horizon task completion with memory in GUI environments
- Secondary capability target(s): clue retention, subtask planning, partial observability handling
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? yes
- Does it test social reasoning / deception / cooperation? no
- Does it test visual grounding / spatial-temporal reasoning? yes
- Does it test long-horizon autonomy / task completion? yes
- Does it test real-time efficiency? no
- Does it test cross-game transfer / open-ended generalization? yes
- Why is a game environment especially suitable here? Narrative adventure games naturally require remembering clues, revisiting places, and linking distant observations to later actions.

## 5. Interaction paradigm
- Observation channel: RGB game frames and full interaction history
- Action channel: low-level GUI inputs such as clicks
- Interface type: GUI interaction
- Agent scaffold allowed: memory
- Is there privileged API access? no
- How close is the setup to human play? high; the benchmark keeps raw frames, low-level actions, and long story arcs
- Main ecological-validity trade-off: Ecological fidelity is strong, but automated judging still needs a powerful oracle-like computer-use agent.

## 6. Evaluation protocol
- Main score: success rate
- Auxiliary score(s): milestone completion rate, progress score
- Evaluation style: success / milestone / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: human demonstrations plus model baselines
- Automatic verifiability: medium to high
- Calibration method: manually defined milestones and CUA-as-a-Judge milestone checking
- Anti-contamination argument: diverse old Flash games and full story arcs reduce simple overfitting to templated tasks
- Reliability or comparability concerns: milestone definitions require manual curation and the judge depends on a capable computer-use model

## 7. Main contributions
- Contribution 1: Builds a 34-game benchmark focused on full adventure-game story completion.
- Contribution 2: Quantifies the long-term observation-behavior gap in human and agent play.
- Contribution 3: Adds automatic milestone verification and a clue-memory baseline framework.

## 8. Main findings and failure modes
- Core empirical takeaway: Current GUI agents struggle heavily with full story arcs, especially when clues must be remembered and applied hundreds of steps later.
- Notable model failure mode 1: forgetting earlier clues and items before they become relevant
- Notable model failure mode 2: poor subtask generation and weak navigation through long dependencies
- Notable model failure mode 3: brittle GUI grounding across highly varied game interfaces
- Does this paper reveal a benchmark-design limitation as well? yes; automatic judging is practical but still depends on a powerful oracle-like evaluator

## 9. Why this paper matters for our survey
- Best use in Section 0 (why games): Strong example of why games matter for long-horizon agent evaluation.
- Best use in Section 1 (historical evolution): Represents the move toward more ecologically realistic GUI-game benchmarks.
- Best use in Section 2 (design space): Useful anchor for adventure-game and full-story-arc evaluation.
- Best use in Section 3 (capability targets): Direct fit for long-horizon autonomy and memory-dependent task completion.
- Best use in Section 4 (interaction paradigm): Strong example of raw GUI control with little privilege.
- Best use in Section 5 (evaluation protocol): Important for milestone-based progress scoring and computer-use judging.
- Best use in Section 6/7 (limitations and future): Supports the claim that long horizons and memory remain major failure points.

## 10. Relation to nearby papers
- Closest predecessor(s): earlier room-escape and GUI-agent benchmarks
- Closest follow-up(s): broader long-horizon game-agent benchmarks
- Best comparison targets inside our corpus: Balrog, GameVerse, StarBench, MCU
- What this paper uniquely adds relative to neighbors: It is one of the clearest full-story GUI benchmarks with explicit evidence of large observation-behavior gaps.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- FlashAdventure contains 34 Flash adventure games selected for diverse subgenres and full-story solvability.
- Human players average about 1,142 steps and 26 minutes with a 97.1% success rate, indicating the tasks are feasible but long.
- The benchmark uses success, milestone completion, and progress metrics, with CUA-as-a-Judge for automatic milestone verification.

### 11.2 Our synthesis / interpretation
- FlashAdventure is one of the strongest cards in this corpus for arguing that current agents fail on memory-heavy full-task arcs even when individual steps look simple.
- It complements StarBench by shifting the main difficulty from precise moment-to-moment control to sustained long-range coherence.

### 11.3 Uncertain or needs re-check
- Recheck Appendix A.5 or A.7 if we later need exact milestone lists or judge-prompt details.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? No immediate reread; the benchmark role and findings are already clear.
- Which section to read next if needed: 3.4 / 3.5 / 4
- Follow-up question(s): Which FlashAdventure subgenres should anchor the survey's long-horizon GUI comparison table?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P1
- Reading depth: deep
- Batch ID: B03
- Outline sections: 3,4,6,7
- Survey role: representative
- Paper card path: `paper_cards/B03/FlashAdventure.md`
- Next action: draft-section
- Last updated: 2026-04-05
