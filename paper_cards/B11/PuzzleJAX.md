# PuzzleJAX PuzzleJAX: A Benchmark for Reasoning and Learning

## 0. Metadata
- Date: 2025/08
- Venue: arXiv
- Authors: Sam Earle, Graham Todd, Yuchen Li, Ahmed Khalifa, Muhammad Umair Nasir, Zehua Jiang, Andrzej Banburski-Fahey, Julian Togelius
- Paper link: https://arxiv.org/pdf/2508.16821v1.pdf
- Code link:
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: high
- Review gate label: strong

## 1. One-paragraph benchmark summary
- PuzzleJAX is a GPU-accelerated puzzle-game engine and benchmark built by porting PuzzleScript into JAX. Rather than centering one puzzle, it opens a broad space of hundreds of human-authored tile-based puzzle games under a common representation, making it useful both as a benchmark suite and as a generative substrate for new tasks. The benchmark compares search, RL, and LLM-based players and finds that many apparently simple games remain difficult for learning-based agents even when tree search solves them reliably. For this survey, PuzzleJAX is a strong design-space paper for human-authored puzzle suites and generator-based benchmark families.

## 2. Position in our survey
- Why-games relevance: Puzzle games give compact, highly verifiable tests of planning, deduction, and deadlock avoidance.
- Historical stage: diagnostic capability probe
- Narrative level(s): L2 strategic reasoning / L5 cross-game generalization
- Most relevant outline section(s): 2,3,6,7
- Role in corpus: contrast

## 3. Design-space coding
### 3.1 Environment structure
- Information structure: mostly perfect
- Transition structure: deterministic
- Agent structure: single-agent
- Social structure: N/A
- Time structure: turn-based

### 3.2 World structure
- World type(s): puzzle
- Real game / simulated game / designed task-game hybrid: large family of human-authored and DSL-generated tile puzzle games
- Benchmark unit: level episode

### 3.3 Benchmark scope
- Scope: curated suite / generative family
- Number of games / tasks: 500+ validated games from PuzzleScript, with access to thousands more
- Benchmark intent: diagnostic evaluation / train+eval foundation

### 3.4 Modality
- Primary modality: symbolic state
- Perception burden retained: rule understanding, state tracking, deadlock reasoning, and long-range planning
- Perception burden removed: low-level vision and motor control

## 4. What this benchmark measures
- Primary capability target: logical inference and planning in puzzle domains
- Secondary capability target(s): transfer across varied rulesets, exploration under sparse rewards, and sensitivity to deadlock structure
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? no
- Does it test social reasoning / deception / cooperation? no
- Does it test visual grounding / spatial-temporal reasoning? partially in tile form
- Does it test long-horizon autonomy / task completion? yes
- Does it test real-time efficiency? no
- Does it test cross-game transfer / open-ended generalization? yes
- Why is a game environment especially suitable here? Puzzle games can be easy for humans yet algorithmically unforgiving, exposing where agents lack insight instead of brute-force search.

## 5. Interaction paradigm
- Observation channel: tile-grid puzzle states compiled from PuzzleScript-like rules
- Action channel: discrete movement or interaction actions depending on the game
- Interface type: structured action space / API
- Agent scaffold allowed: none
- Is there privileged API access? yes
- How close is the setup to human play? medium; it uses real human-authored games but through standardized symbolic environments
- Main ecological-validity trade-off: PuzzleJAX privileges breadth, fidelity to PuzzleScript, and throughput over human-facing audiovisual presentation

## 6. Evaluation protocol
- Main score: game completion across many puzzle environments
- Auxiliary score(s): search throughput, RL performance, and LLM player comparisons
- Evaluation style: completion rate / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: tree search, RL, and LLM agents are compared over a shared set of human-authored games
- Automatic verifiability: high
- Calibration method: validation against PuzzleScript behavior plus broad cross-game evaluation
- Anti-contamination argument: the benchmark is grounded in many human-authored games and can compile novel rulesets beyond fixed task lists
- Reliability or comparability concerns: some edge-case PuzzleScript features and randomness do not align perfectly with the original engine

## 7. Main contributions
- Contribution 1: Reimplements PuzzleScript in JAX with high throughput and broad feature coverage.
- Contribution 2: Turns a large human-authored puzzle ecosystem into a benchmark family for search, RL, and LLMs.
- Contribution 3: Shows that tree search remains much stronger than current learning-based methods on many puzzle games.

## 8. Main findings and failure modes
- Core empirical takeaway: puzzle games that look simple to humans remain hard for RL and LLM agents, while naive breadth-first search performs surprisingly well.
- Notable model failure mode 1: getting stuck in deadlock states with sparse reward
- Notable model failure mode 2: failure to infer unconventional mechanics across games
- Notable model failure mode 3: overfitting or local-minimum behavior in learning-based approaches
- Does this paper reveal a benchmark-design limitation as well? yes; it shows that fixed single-game benchmarks can hide how fragile methods are across varied rule systems

## 9. Why this paper matters for our survey
- Best use in Section 0 (why games): Supports the argument that small games can still pose deep reasoning challenges.
- Best use in Section 1 (historical evolution): Marks a move from isolated puzzle games to broad generative puzzle families.
- Best use in Section 2 (design space): Excellent for discussing benchmark families defined by DSLs rather than one fixed suite.
- Best use in Section 3 (capability targets): Strong evidence for logical inference, planning, and deadlock handling as distinct targets.
- Best use in Section 4 (interaction paradigm): A clean symbolic-interface contrast to visual puzzle benchmarks.
- Best use in Section 5 (evaluation protocol): Useful for comparing search, RL, and LLMs under the same task family.
- Best use in Section 6/7 (limitations and future): Supports future benchmark designs that are broad enough to resist overfitting.

## 10. Relation to nearby papers
- Closest predecessor(s): Sokoban-like puzzle benchmarks
- Closest follow-up(s): SudokuBench, VGRPBench
- Best comparison targets inside our corpus: SudokuBench, VGRPBench, MazeEval, CrossWordBench
- What this paper uniquely adds relative to neighbors: It contributes a generative puzzle language and a very broad human-authored task family rather than one puzzle format.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- PuzzleJAX ports PuzzleScript to JAX and validates more than 500 human-authored games.
- The benchmark highlights speedups of roughly 2x to 16x over JavaScript implementations.
- Search methods outperform RL and LLM baselines across many games despite the games’ apparent simplicity.

### 11.2 Our synthesis / interpretation
- PuzzleJAX is especially valuable for survey sections on design-space breadth and benchmark generators.
- It also supports a broader point that puzzle difficulty for AI often looks different from puzzle difficulty for humans.

### 11.3 Uncertain or needs re-check
- Re-check the exact validated-game count and the strongest baseline comparisons if we later need a quantitative table.
- Re-check which PuzzleScript features still fail validation in the JAX port.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? A focused reread may be useful later for benchmark-generator discussion.
- Which section to read next if needed: engine fidelity / benchmark games / baseline results
- Follow-up question(s): Which subset of PuzzleJAX games best balances human interpretability and agent difficulty?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P2
- Reading depth: deep
- Batch ID: B11
- Outline sections: 2,3,6,7
- Survey role: contrast
- Paper card path: `paper_cards/B11/PuzzleJAX.md`
- Next action: draft-section
- Last updated: 2026-04-05
