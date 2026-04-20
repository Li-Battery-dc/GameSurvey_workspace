# FlashAdventure FlashAdventure: A Benchmark for GUI Agents Solving Full Story Arcs in Diverse Adventure Games

## 0. Metadata
- Date: 2025/09
- Venue: EMNLP 2025
- Authors: Jaewoo Ahn, Junseo Kim, Heeseung Yun, Jaehyeon Son, Dongmin Park, Jaewoong Cho, Gunhee Kim
- Paper link: https://arxiv.org/pdf/2509.01052v2
- Code link: https://github.com/ahnjaewoo/FlashAdventure
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: high
- Review gate label: strong

## 1. One-paragraph benchmark summary
- FlashAdventure is a native-control benchmark built from 34 classic Flash adventure games and focused on completing full story arcs rather than isolated subtasks. The benchmark formulates play as a POMDP over RGB frames and low-level native-control actions, documents a substantial observation-behavior gap in human play, and evaluates agents with success, milestone-completion, and step metrics. It also introduces CUA-as-a-Judge, a Claude-3.7 computer-use evaluator for milestone verification, and COAST, a clue-memory-based framework for long-horizon planning. In the survey, FlashAdventure is a strong anchor for long-horizon native-control play and memory-dependent task completion, but not for open-ended general-game transfer.

## 2. Position in our survey
- Why-games relevance: Adventure games create long dependency chains and memory-heavy task structure that static benchmarks rarely capture.
- Historical stage: ecological agent benchmark
- Narrative level(s): L4 visual agency
- Most relevant outline section(s): 2,3,4
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

### 3.4 Modality
- Primary modality: GUI
- Perception burden retained: raw RGB frames, GUI grounding, hidden internal state, long-horizon clue use
- Perception burden removed: internal engine state and direct symbolic progress access

## 4. What this benchmark measures
- Primary capability target: long-horizon task completion with memory in GUI environments
- Secondary capability target(s): clue retention, subtask planning, partial observability handling
- Does it test rule grounding / legal action generation? partially
- Does it test strategic planning under uncertainty? yes
- Does it test social reasoning / deception / cooperation? no
- Does it test visual grounding / spatial-temporal reasoning? yes
- Does it test long-horizon autonomy / task completion? yes
- Does it test real-time efficiency? no
- Does it test cross-game transfer / open-ended generalization? partially
- Why is a game environment especially suitable here? Narrative adventure games naturally require remembering clues, revisiting places, and linking distant observations to later actions.

## 5. Interaction paradigm
- Observation channel: RGB game frames and full interaction history
- Action channel: low-level GUI inputs such as clicks
- Interface type: native control
- Agent scaffold allowed: memory; some evaluated baselines also use retrieval or summary modules, while COAST adds explicit clue memory
- Is there privileged API access? no
- How close is the setup to human play? medium to high; the benchmark keeps raw frames, low-level actions, and long story arcs, but still runs under explicit step caps and evaluator access to milestone definitions
- Main ecological-validity trade-off: Ecological fidelity is strong for slow, story-driven native-control play, but the automatic judge has oracle milestone access and the selected genres avoid strict reflex-heavy timing

## 6. Evaluation protocol
- Main score: success rate
- Auxiliary score(s): milestone completion rate, progress score
- Evaluation style: success / milestone / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: human demonstrations plus model baselines
- Automatic verifiability: medium to high
- Calibration method: author-consensus milestone definitions, CUA-as-a-Judge milestone checking, and agreement validation against human judgments
- Anti-contamination argument: not central; the benchmark benefits from diverse legacy Flash titles, but the paper's main reliability case is milestone validation rather than contamination resistance
- Reliability or comparability concerns: milestone definitions are manually curated, the judge is not fully genre-agnostic, and reported experiments are costly single runs on proprietary APIs

## 7. Main contributions
- Contribution 1: Builds a 34-game benchmark focused on full adventure-game story completion.
- Contribution 2: Quantifies the long-term observation-behavior gap in human and agent play.
- Contribution 3: Adds automatic milestone verification and a clue-memory baseline framework.

## 8. Main findings and failure modes
- Core empirical takeaway: Current native-control agents struggle heavily with full story arcs, especially when clues must be remembered and applied hundreds of steps later.
- Notable model failure mode 1: forgetting earlier clues and items before they become relevant
- Notable model failure mode 2: poor subtask generation and weak lateral thinking across long dependencies
- Notable model failure mode 3: brittle GUI grounding across highly varied non-standard interfaces
- Does this paper reveal a benchmark-design limitation as well? yes; automatic judging depends on milestone definitions and is less suitable for reflex-heavy genres

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Strong example of why games matter for long-horizon agent evaluation.
- Best use in Section 1 (taxonomy and evolutionary levels): Represents the move toward more ecologically realistic GUI-game benchmarks, especially for full-story-arc adventure play.
- Best use in Section 2 (core capabilities evaluated by games): Direct fit for long-horizon autonomy and memory-dependent task completion.
- Best use in Section 3 (interaction and evaluation paradigm): Strong example of raw native control with little privilege, plus milestone-based progress scoring and computer-use judging.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Supports the claim that long horizons and memory remain major failure points.

## 10. Relation to nearby papers
- Closest predecessor(s): Cradle, VisEscape, and other GUI-agent or room-escape benchmarks
- Closest follow-up(s): broader long-horizon GUI-game benchmarks and agentic computer-use systems
- Best comparison targets inside our corpus: StarBench, Balrog, GameplayQA, VideoGameBench
- What this paper uniquely adds relative to neighbors: It is one of the clearest full-story native-control benchmarks with explicit human evidence for large observation-behavior gaps and a validated computer-use judge.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- FlashAdventure contains 34 Flash adventure games selected for diverse subgenres and full-story solvability.
- Human players average 1,142 steps and 26 minutes with a 97.1% success rate, showing the games are feasible but long.
- The paper measures an average observation-behavior gap of 251.1 steps in human play for discrete-milestone games.
- CUA-as-a-Judge reaches 94.0% agreement accuracy with human milestone judgments across 300 evaluation samples.

### 11.2 Our synthesis / interpretation
- FlashAdventure is one of the strongest cards in this corpus for arguing that current agents fail on memory-heavy full-task arcs even when individual steps look simple.
- It complements StarBench by shifting the main difficulty from precise moment-to-moment control to sustained long-range coherence and clue use.

### 11.3 Uncertain or needs re-check
- Recheck the appendices if we later need exact per-subgenre milestone lists, judge prompts, or contamination-check details.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? No immediate reread; the benchmark role and findings are already clear.
- Which section to read next if needed: evaluation / CUA-as-a-Judge / limitations
- Follow-up question(s): Which FlashAdventure subgenres should anchor the survey's long-horizon GUI comparison table?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P1
- Reading depth: deep
- Batch ID: B04
- Outline sections: 2,3,4
- Survey role: representative
- Paper card path: `paper_cards/B04/FlashAdventure.md`
- Next action: draft-section
- Last updated: 2026-04-10
