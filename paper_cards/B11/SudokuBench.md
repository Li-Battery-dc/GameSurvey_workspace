# SudokuBench Sudoku-Bench: Evaluating creative reasoning with Sudoku variants

## 0. Metadata
- Date: 2025/05
- Venue: arXiv
- Authors: Jeffrey Seely, Yuki Imajuku, Tianyu Zhao, Edoardo Cetin, Llion Jones
- Paper link: https://arxiv.org/pdf/2505.16135v1.pdf
- Code link:
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: high
- Review gate label: strong

## 1. One-paragraph benchmark summary
- Sudoku-Bench is a 100-puzzle benchmark built around modern Sudoku variants rather than vanilla Sudoku alone. It deliberately targets creative reasoning by using puzzles whose rules may include visual constraints and puzzle-specific natural-language descriptions, while also providing a precise text representation that isolates reasoning from visual extraction errors. The benchmark evaluates both single-shot and multi-round solving and shows that even leading models solve fewer than 15% overall, with performance collapsing on larger and more novel puzzles. For this survey, Sudoku-Bench is a strong anchor for puzzle benchmarks that stress break-in discovery and structured reasoning rather than memorized templates.

## 2. Position in our survey
- Why-games relevance: Variant Sudoku gives tightly verifiable problems where success depends on discovering nontrivial logical break-ins.
- Historical stage: diagnostic capability probe
- Narrative level(s): L2 strategic reasoning
- Most relevant outline section(s): 2,3,6
- Role in corpus: contrast

## 3. Design-space coding
### 3.1 Environment structure
- Information structure: perfect
- Transition structure: deterministic
- Agent structure: single-agent
- Social structure: N/A
- Time structure: turn-based

### 3.2 World structure
- World type(s): puzzle
- Real game / simulated game / designed task-game hybrid: curated set of human-designed logic puzzles
- Benchmark unit: full puzzle solution

### 3.3 Benchmark scope
- Scope: curated suite
- Number of games / tasks: 100 puzzles across 4x4, 6x6, and 9x9 variants
- Benchmark intent: diagnostic evaluation

### 3.4 Modality
- Primary modality: text in the main benchmark, with tool support for visual interaction through SudokuPad
- Perception burden retained: rule interpretation, logical consistency, and search over tightly coupled constraints
- Perception burden removed: main evaluation textualizes visual elements to isolate reasoning from perception

## 4. What this benchmark measures
- Primary capability target: creative logical reasoning under novel rule combinations
- Secondary capability target(s): maintaining global consistency, finding break-ins, and limited interactive correction
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? no
- Does it test social reasoning / deception / cooperation? no
- Does it test visual grounding / spatial-temporal reasoning? partially in the optional visual interface
- Does it test long-horizon autonomy / task completion? partially
- Does it test real-time efficiency? no
- Does it test cross-game transfer / open-ended generalization? yes
- Why is a game environment especially suitable here? Human puzzle creators can keep inventing new rule combinations that resist template memorization while preserving exact verification.

## 5. Interaction paradigm
- Observation channel: textual puzzle specification or optional SudokuPad board interaction
- Action channel: full solution outputs or committed digit placements in multi-round mode
- Interface type: natural language / structured action space / hybrid
- Agent scaffold allowed: tool use in the provided SudokuPad interface, though baseline evaluation is tool-free
- Is there privileged API access? no in the main text-only setting
- How close is the setup to human play? medium; the logic is authentic, but the main benchmark textualizes the puzzles for current models
- Main ecological-validity trade-off: isolating reasoning from perception sharpens diagnosis, but it also removes part of how humans naturally experience Sudoku variants

## 6. Evaluation protocol
- Main score: solve rate
- Auxiliary score(s): average correct digits in multi-round mode
- Evaluation style: completion rate / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: frontier models are tested on shared puzzles in both single-shot and multi-round settings
- Automatic verifiability: high
- Calibration method: curated puzzle difficulty ramp with 15 4x4, 15 6x6, and 70 9x9 puzzles
- Anti-contamination argument: variant rules and newly curated puzzles reduce template memorization compared with standard Sudoku
- Reliability or comparability concerns: the text representation removes visual parsing difficulty, so results focus on reasoning rather than fully natural puzzle play

## 7. Main contributions
- Contribution 1: Builds a curated 100-puzzle benchmark of Sudoku variants that target creative reasoning.
- Contribution 2: Provides both text representations and SudokuPad-based tooling.
- Contribution 3: Shows that current frontier models struggle badly once puzzle size and novelty increase.

## 8. Main findings and failure modes
- Core empirical takeaway: even strong reasoning models solve fewer than 15% overall, with performance near zero on many 9x9 variants.
- Notable model failure mode 1: confidently producing incorrect solutions
- Notable model failure mode 2: claiming contradictions or missing information where none exists
- Notable model failure mode 3: failing to identify the initial logical break-in needed to reduce the search space
- Does this paper reveal a benchmark-design limitation as well? yes; it shows that many reasoning benchmarks reward known templates rather than the discovery of novel constraint structures

## 9. Why this paper matters for our survey
- Best use in Section 0 (why games): Supports the argument that games and puzzles can give exact verification without trivializing reasoning.
- Best use in Section 1 (historical evolution): A modern example of human-designed puzzle benchmarking rather than mass-generated textbook QA.
- Best use in Section 2 (design space): Useful for text-versus-visual puzzle interface comparisons.
- Best use in Section 3 (capability targets): Strong evidence for creative break-in reasoning and global consistency maintenance.
- Best use in Section 4 (interaction paradigm): Helpful for discussing when visual structure should be textualized and when it should not.
- Best use in Section 5 (evaluation protocol): Good example of single-shot versus iterative solving.
- Best use in Section 6/7 (limitations and future): Supports the case for future tool-use tracks distinct from pure reasoning tracks.

## 10. Relation to nearby papers
- Closest predecessor(s): classic Sudoku and ARC-style reasoning benchmarks
- Closest follow-up(s): VGRPBench, CrossWordBench
- Best comparison targets inside our corpus: VGRPBench, CrossWordBench, PuzzleJAX
- What this paper uniquely adds relative to neighbors: It focuses on human-curated logical break-ins rather than generic grid parsing or broad puzzle taxonomies.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- Sudoku-Bench contains 100 puzzles: 15 4x4, 15 6x6, and 70 9x9.
- The benchmark supports both single-shot solving and multi-round play where the model commits at least one digit per round.
- The paper reports that even top models solve fewer than 15% overall and that most success comes from the smallest puzzles.

### 11.2 Our synthesis / interpretation
- Sudoku-Bench is one of the strongest corpus papers for creative constraint reasoning rather than generic logic QA.
- It is especially useful as a counterexample to claims that reasoning benchmarks are nearly saturated.

### 11.3 Uncertain or needs re-check
- Re-check the exact best-model solve rates by size if we later need a comparison table.
- Re-check which puzzles most depend on visual symmetry or geometry if we discuss residual visual burden.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? Yes selectively, especially if we draft a subsection on puzzle break-ins and tool-use tracks.
- Which section to read next if needed: dataset curation / evaluation framework / failure analysis
- Follow-up question(s): Which subset of Sudoku-Bench is best for separating creative reasoning from brute-force search?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P2
- Reading depth: deep
- Batch ID: B11
- Outline sections: 2,3,6
- Survey role: contrast
- Paper card path: `paper_cards/B11/SudokuBench.md`
- Next action: draft-section
- Last updated: 2026-04-05
