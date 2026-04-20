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
- PuzzleJAX is primarily a GPU-accelerated reimplementation of PuzzleScript in JAX, paired with a large validated collection of human-authored tile-based puzzle games and preliminary agent experiments. The paper reports 951 collected PuzzleScript games, of which 414 validate fully and 156 partially under the authors' replay-based fidelity check, and frames this as a benchmark space of 500+ diverse environments rather than a tightly frozen leaderboard suite. Its empirical section compares breadth-first search, PPO, and prompted LLM agents on a smaller subset of example games, showing that symbolic puzzle domains that look simple to humans still break current learning-based agents through deadlocks, weak rule tracking, and poor long-range planning. For this survey, PuzzleJAX is best used as a contrast paper on symbolic puzzle-family breadth, automatic verifiability, and generator-backed benchmark design rather than as a human-like game-agent benchmark.

## 2. Position in our survey
- Why-games relevance: Puzzle games give compact, highly verifiable tests of rule tracking, planning, and deadlock avoidance while keeping scoring and success conditions explicit.
- Historical stage: diagnostic capability probe
- Narrative level(s): L2 strategic reasoning / L5 cross-game generalization
- Most relevant outline section(s): 1,2,4
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
- Real game / simulated game / designed task-game hybrid: large family of human-authored PuzzleScript games plus a DSL that can compile new tile-puzzle rulesets
- Benchmark unit: level episode

### 3.3 Benchmark scope
- Scope: procedural-infinite
- Number of games / tasks: 951 collected PuzzleScript games; 414 fully valid and 156 partially valid under the paper's replay-based validation, with the paper framing 500+ diverse environments and access to thousands of PuzzleScript-style games

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
- Does it test visual grounding / spatial-temporal reasoning? only in symbolic grid form, not as raw visual grounding
- Does it test long-horizon autonomy / task completion? partially; within level-scale puzzle completion rather than open-ended task arcs
- Does it test real-time efficiency? no
- Does it test cross-game transfer / open-ended generalization? partially; mostly transfer within a shared symbolic puzzle DSL rather than across broader game modalities
- Why is a game environment especially suitable here? Puzzle games make success conditions explicit while still requiring agents to discover multi-step plans, mechanic interactions, and deadlock-avoiding action sequences.

## 5. Interaction paradigm
- Observation channel: symbolic tile-grid states; LLM agents additionally receive ASCII state, legend, rules, and action meanings
- Action channel: discrete movement or interaction actions depending on the game
- Interface type: structured action space / API
- Agent scaffold allowed: none beyond prompt-packaged rules, legend, and action descriptions for LLM agents
- Is there privileged API access? yes
- How close is the setup to human play? low to medium; it uses real human-authored games but strips play down to standardized symbolic states with explicit rule access
- Main ecological-validity trade-off: PuzzleJAX prioritizes symbolic fidelity, throughput, and cross-game comparability over human-like perception, rule discovery, or audiovisual interaction

## 6. Evaluation protocol
- Main score: validation fidelity to original PuzzleScript behavior plus per-level win/completion on a smaller subset of example games
- Auxiliary score(s): JAX-versus-JavaScript throughput, BFS search depth/coverage, PPO training behavior, and LLM win rate across 12 games
- Evaluation style: completion rate / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: no human baseline; breadth-first search, PPO, and prompted LLM agents are probed on selected games and levels
- Automatic verifiability: high
- Calibration method: replay-based state-equivalence validation against PuzzleScript plus multi-method comparisons on representative games
- Anti-contamination argument: the paper argues that the large human-authored PuzzleScript space and the ability to compile novel rulesets reduce simple overfitting, but it does not provide a formal contamination audit
- Reliability or comparability concerns: only part of the collected PuzzleScript corpus validates fully in PuzzleJAX, and the agent experiments are exploratory rather than a fixed benchmark protocol over the whole corpus

## 7. Main contributions
- Contribution 1: Reimplements PuzzleScript in JAX with high throughput and broad feature coverage.
- Contribution 2: Turns a large human-authored puzzle ecosystem into a benchmark family for search, RL, and LLMs.
- Contribution 3: Shows that tree search remains much stronger than current learning-based methods on many puzzle games.

## 8. Main findings and failure modes
- Core empirical takeaway: symbolic puzzle games that look simple to humans remain hard for PPO and prompted LLM agents, while naive breadth-first search often solves them when state spaces stay tractable.
- Notable model failure mode 1: getting stuck in deadlock states with sparse reward
- Notable model failure mode 2: failure to infer unconventional mechanics across games
- Notable model failure mode 3: overfitting or local-minimum behavior in learning-based approaches
- Does this paper reveal a benchmark-design limitation as well? yes; it shows both the value and the difficulty of scaling beyond fixed single-game probes without sacrificing validation coverage or protocol stability

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Minor contrast only; it helps show that seemingly small symbolic games can still expose hard reasoning failures, but it is not a central motivation anchor.
- Best use in Section 1 (taxonomy and evolutionary levels): Strong contrast for a DSL-backed puzzle-family benchmark that broadens beyond a single game while staying inside a narrow symbolic world type.
- Best use in Section 2 (core capabilities evaluated by games): Direct support for logical inference, rule transfer, deadlock handling, and long-range puzzle planning as distinct evaluation targets.
- Best use in Section 3 (interaction and evaluation paradigm): Useful contrast case for privileged symbolic interfaces, explicit rule access, replay-based validation, and search-versus-learning comparisons on the same task family.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Supports the claim that broader benchmark spaces can reduce overfitting pressure, but only if validation coverage and frozen evaluation protocols stay explicit.

## 10. Relation to nearby papers
- Closest predecessor(s): PuzzleScript itself and earlier single-puzzle families such as Sokoban-like benchmarks
- Closest follow-up(s): no direct follow-up in our corpus; the nearest later neighbors are symbolic-diagnostic puzzle papers such as `SudokuBench` and `PuzzlePlex`
- Best comparison targets inside our corpus: CrossWordBench, SudokuBench, VGRPBench, MazeEval
- What this paper uniquely adds relative to neighbors: It contributes a high-throughput PuzzleScript-compatible engine plus a large validated human-authored puzzle corpus, giving the survey a generator-backed symbolic benchmark contrast rather than a single puzzle format.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- The paper reimplements PuzzleScript in JAX and reports speedups ranging from 2x to 16x over the JavaScript engine on tested games.
- The authors collect 951 PuzzleScript games and report 414 fully valid plus 156 partially valid games under replay-based validation against original PuzzleScript behavior.
- Breadth-first search is evaluated with a 1 million-step cap on a subset of games; PPO is trained on individual levels with heuristic-shaped reward; LLM agents are run 10 times per level with a 100-step cap across 12 games.
- Most tested LLM/game pairs have 0% win rate, while BFS often solves tractable games that still defeat PPO or prompted LLMs.

### 11.2 Our synthesis / interpretation
- PuzzleJAX is most defensible as a contrast case for symbolic diagnostic benchmark families, not as evidence of human-like game play.
- The paper is useful because it separates two ideas that surveys often blur together: a reusable engine/DSL contribution and a standardized benchmark protocol.
- It also supports the broader survey point that puzzle difficulty for AI can differ sharply from apparent human simplicity.

### 11.3 Uncertain or needs re-check
- If we later build a quantitative comparison table, re-check the exact split between fully valid and partially valid games and whether we want to cite the paper's "500+ environments" phrasing or the appendix counts.
- Re-check which PuzzleScript features still fail validation in the JAX port before using PuzzleJAX as evidence for faithful engine portability rather than benchmark breadth.
- Survey-boundary caution remains: this paper fits best as a narrow symbolic contrast, not as a core ecological game-agent benchmark.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? No immediate reread is needed; the current audit already depends on the engine, validation, and baseline sections.
- Which section to read next if needed: validation appendix / search and LLM result sections
- Follow-up question(s): If the survey later needs a frozen symbolic benchmark table, which validated PuzzleJAX subset is stable and representative enough to cite?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P2
- Reading depth: deep
- Batch ID: B08
- Outline sections: 1,2,4
- Survey role: contrast
- Paper card path: `paper_cards/B08/PuzzleJAX.md`
- Next action: draft-section
- Check status: unchecked
- Last updated: 2026-04-10
