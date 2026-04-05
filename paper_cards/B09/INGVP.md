# INGVP ING-VP: MLLMs cannot Play Easy Vision-based Games Yet

## 0. Metadata
- Date: 2024/10
- Venue: arXiv
- Authors: Haoran Zhang, Hangyu Guo, Shuyue Guo, Meng Cao, Wenhao Huang, Jiaheng Liu, Ge Zhang
- Paper link: https://arxiv.org/pdf/2410.06555v1.pdf
- Code link: https://github.com/Thisisus7/ING-VP
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: high
- Review gate label: strong

## 1. One-paragraph benchmark summary
- ING-VP is a diagnostic benchmark built around six simple-but-planning-heavy games, each with 50 levels, to test whether multimodal models can handle basic visual game play. The paper systematically varies modality and prompting setup across image-plus-text versus text-only, one-step versus multi-step, and with-versus-without history, which makes it possible to isolate where failures arise. Despite the simplicity of the games, the benchmark finds that current MLLMs still perform extremely poorly and often fall into repetitive loops. For this survey, ING-VP is a strong argument that even easy visual games remain unresolved once perception and sequential planning are combined.

## 2. Position in our survey
- Why-games relevance: Even tiny game worlds can expose the interaction between perception, planning, and repeated action selection better than one-shot reasoning tasks.
- Historical stage: diagnostic capability probe
- Narrative level(s): L4 visual agency
- Most relevant outline section(s): 3,4,6
- Role in corpus: contrast

## 3. Design-space coding
### 3.1 Environment structure
- Information structure: mostly perfect
- Transition structure: deterministic
- Agent structure: single-agent
- Social structure: N/A
- Time structure: turn-based

### 3.2 World structure
- World type(s): puzzle / other
- Real game / simulated game / designed task-game hybrid: designed task-game suite
- Benchmark unit: level episode

### 3.3 Benchmark scope
- Scope: curated suite
- Number of games / tasks: 6 games with 50 levels each, for 300 levels total
- Benchmark intent: diagnostic evaluation

### 3.4 Modality
- Primary modality: mixed
- Perception burden retained: image interpretation in the visual settings, grid understanding, and state tracking
- Perception burden removed: worlds are simple and discrete, with limited action spaces and no real-time pressure

## 4. What this benchmark measures
- Primary capability target: combined visual perception and planning in simple sequential games
- Secondary capability target(s): memory of prior states, benefit of history, and effect of multi-step prompting
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? partially
- Does it test social reasoning / deception / cooperation? no
- Does it test visual grounding / spatial-temporal reasoning? yes
- Does it test long-horizon autonomy / task completion? yes
- Does it test real-time efficiency? no
- Does it test cross-game transfer / open-ended generalization? partially
- Why is a game environment especially suitable here? The tasks are simple enough that poor performance cannot easily be blamed on large action spaces or natural-language ambiguity alone.

## 5. Interaction paradigm
- Observation channel: image-text or text-only descriptions of puzzle-like game states
- Action channel: move choices for each game step
- Interface type: natural language / structured action space / hybrid
- Agent scaffold allowed: history
- Is there privileged API access? limited to the benchmark’s structured state presentation
- How close is the setup to human play? low to medium; the games are intentionally simplified for diagnosis
- Main ecological-validity trade-off: ING-VP sacrifices realism to make perception and planning failures easy to localize

## 6. Evaluation protocol
- Main score: task completion accuracy
- Auxiliary score(s): completion degree and action efficiency
- Evaluation style: completion rate / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: humans and multiple MLLMs are compared across six controlled prompting conditions
- Automatic verifiability: high
- Calibration method: 50 levels per game, fixed settings, and six experimental condition variants
- Anti-contamination argument: the benchmark uses many simple but underrepresented game instances rather than famous single puzzles
- Reliability or comparability concerns: because the games are deliberately easy, failure tells us more about basic competence gaps than about rich ecological play

## 7. Main contributions
- Contribution 1: Builds a 300-level benchmark around six simple visual planning games.
- Contribution 2: Compares image-text and text-only play, one-step and multi-step prompting, and the effect of history.
- Contribution 3: Documents pervasive failure and looping even on easy game instances.

## 8. Main findings and failure modes
- Core empirical takeaway: current MLLMs perform very poorly even on easy vision-based games, with perception and planning errors both contributing heavily.
- Notable model failure mode 1: repeated looping and action repetition
- Notable model failure mode 2: poor visual parsing of simple states
- Notable model failure mode 3: multi-step prompting does not reliably help and can sometimes hurt
- Does this paper reveal a benchmark-design limitation as well? yes; it shows that apparent reasoning improvements can disappear once evaluation requires persistent action rather than one-shot answers

## 9. Why this paper matters for our survey
- Best use in Section 0 (why games): Useful for showing that game interaction reveals failures hidden by static reasoning tests.
- Best use in Section 1 (historical evolution): Fits the diagnostic phase of multimodal game benchmarking.
- Best use in Section 2 (design space): Good example of a deliberately simplified task-game suite.
- Best use in Section 3 (capability targets): Strong evidence for separating perception and planning bottlenecks.
- Best use in Section 4 (interaction paradigm): Helpful contrast to richer video-game interfaces because the world is intentionally stripped down.
- Best use in Section 5 (evaluation protocol): Useful for discussing factorized evaluation across modality and history settings.
- Best use in Section 6/7 (limitations and future): Supports the claim that basic sequential control remains unresolved even before ecological realism is introduced.

## 10. Relation to nearby papers
- Closest predecessor(s): GameplayQA, Sudoku-Bench
- Closest follow-up(s): MazeEval, VGRP-Bench
- Best comparison targets inside our corpus: GameplayQA, MazeEval, LVLMGamePlayers, VGRPBench
- What this paper uniquely adds relative to neighbors: It uses very easy games to argue that the floor of multimodal sequential decision-making is still low.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- ING-VP contains six games with 50 levels each and evaluates 300 levels total.
- The benchmark compares six settings formed by image-text versus text-only, one-step versus multi-step, and with-versus-without history.
- The paper reports accuracy, completion degree, and action efficiency, and finds that models often loop or repeatedly choose ineffective actions.

### 11.2 Our synthesis / interpretation
- ING-VP is especially valuable as a lower-bound benchmark: if models fail here, claims about robust visual game agency should be treated cautiously.
- It supports the survey’s argument that simpler games can still be revealing when the protocol is well controlled.

### 11.3 Uncertain or needs re-check
- Re-check the exact per-game names if we later need a figure caption or table row.
- Re-check whether any individual game benefits materially from history while others do not.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? Probably only if we later need finer detail on which settings most improve or degrade performance.
- Which section to read next if needed: experimental settings / condition ablations / failure analysis
- Follow-up question(s): Does history help because of memory, or only because it partially compensates for perception mistakes?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P2
- Reading depth: deep
- Batch ID: B09
- Outline sections: 3,4,6
- Survey role: contrast
- Paper card path: `paper_cards/B09/INGVP.md`
- Next action: draft-section
- Last updated: 2026-04-05
