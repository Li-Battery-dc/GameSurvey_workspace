# SudokuBench Sudoku-Bench: Evaluating creative reasoning with Sudoku variants

## 0. Metadata
- Date: 2025/05
- Venue: arXiv
- Authors: Jeffrey Seely, Yuki Imajuku, Tianyu Zhao, Edoardo Cetin, Llion Jones
- Paper link: https://arxiv.org/pdf/2505.16135v1.pdf
- Code link: https://github.com/SakanaAI/Sudoku-Bench
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: high
- Review gate label: strong

## 1. One-paragraph benchmark summary
- Sudoku-Bench is a curated 100-puzzle benchmark built around modern Sudoku variants rather than vanilla Sudoku alone, designed to test creative multi-step reasoning through puzzle-specific "break-ins" rather than familiar templates. Its core `challenge_100` benchmark is text-only and tool-free: visual elements are serialized into text so the evaluation isolates logical deduction from visual parsing, while a separate SudokuPad harness and associated transcript/action resources are released as extensions rather than as the main reported evaluation track. Baseline results show that frontier LLMs solve fewer than 15% overall and that multi-step interaction helps only modestly on the smallest puzzles, with performance collapsing on larger 9x9 variants. For this survey, Sudoku-Bench is best used as a contrast paper on tightly verifiable creative reasoning and on the design choice to separate pure-reasoning tracks from future tool-use tracks.

## 2. Position in our survey
- Why-games relevance: Variant Sudoku gives tightly verifiable puzzle play where success depends on discovering nontrivial logical break-ins under novel rule combinations.
- Historical stage: diagnostic capability probe
- Narrative level(s): L2 strategic reasoning
- Most relevant outline section(s): 1,2,4
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
- Number of games / tasks: core benchmark `challenge_100` with 15 4x4, 15 6x6, and 70 9x9 puzzles; the release also includes `nikoli_100`, `ctc` (2,565 Sudoku variants), and transcript/action resources
- Benchmark intent: diagnostic evaluation

### 3.4 Modality
- Primary modality: text in the core benchmark, with a separate SudokuPad agentic environment released alongside it
- Perception burden retained: rule interpretation, global consistency, break-in discovery, and long multi-step deduction
- Perception burden removed: the main benchmark textualizes visual elements and does not require natural visual parsing or human-style note-taking

## 4. What this benchmark measures
- Primary capability target: creative logical reasoning under novel rule combinations
- Secondary capability target(s): maintaining global consistency, finding break-ins, and sustaining deductions across long multi-step solves
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? no
- Does it test social reasoning / deception / cooperation? no
- Does it test visual grounding / spatial-temporal reasoning? only indirectly; the core benchmark removes visual parsing, while the released SudokuPad environment could support later visual tracks
- Does it test long-horizon autonomy / task completion? partially; as long multi-step deductive completion rather than embodied trajectories
- Does it test real-time efficiency? no
- Does it test cross-game transfer / open-ended generalization? partially; across novel rule combinations within one puzzle family rather than across broader game genres
- Why is a game environment especially suitable here? Human puzzle creators can keep inventing new rule combinations that resist template memorization while still preserving exact verification and human-interpretable solution structure.

## 5. Interaction paradigm
- Observation channel: textual puzzle specification in the core benchmark; a separate SudokuPad harness can provide board images and annotation tools
- Action channel: full solution outputs in single-shot mode or at least one committed digit placement per round in multi-step mode
- Interface type: natural language / structured action space / hybrid
- Agent scaffold allowed: no tool use in the reported baseline; optional SudokuPad tooling is released separately for later agentic experiments
- Is there privileged API access? no in the core benchmark; the optional SudokuPad harness exposes direct interaction tools
- How close is the setup to human play? low to medium; the puzzle logic is authentic, but the reported benchmark removes normal visual reading and note-taking practices
- Main ecological-validity trade-off: textualizing puzzles and forbidding tools sharpens diagnosis of intrinsic reasoning, but departs from how humans usually solve these variants

## 6. Evaluation protocol
- Main score: solve rate
- Auxiliary score(s): average correct digits in multi-round mode
- Evaluation style: completion rate / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: no human baseline or fixed AI anchor; frontier LLMs are tested on the shared `challenge_100` puzzles in both single-shot and multi-round settings
- Automatic verifiability: high
- Calibration method: curated difficulty ramp across 15 4x4, 15 6x6, and 70 9x9 puzzles, including 50 benchmark-exclusive 9x9 puzzles and 20 difficult Nikoli vanilla Sudokus inside the main set
- Anti-contamination argument: the paper argues that novel variant rules and newly curated puzzles reduce template memorization, but the broader public Sudoku ecosystem and released transcripts mean contamination cannot be ruled out in principle
- Reliability or comparability concerns: the reported baseline is text-only, tool-free, and usually one run per model/puzzle; it isolates reasoning well but is not a full natural-play benchmark

## 7. Main contributions
- Contribution 1: Builds a curated 100-puzzle benchmark of Sudoku variants that target creative reasoning.
- Contribution 2: Releases standardized text representations, a SudokuPad interaction harness, and supporting transcript/action resources for future agentic or imitation-learning work.
- Contribution 3: Shows that current frontier models struggle badly once puzzle size and novelty increase, and that multi-step interaction only modestly improves small-puzzle performance.

## 8. Main findings and failure modes
- Core empirical takeaway: even strong reasoning models solve fewer than 15% overall, and iterative multi-step interaction does little to rescue performance once puzzles require deeper break-ins or larger 9x9 reasoning chains.
- Notable model failure mode 1: confidently producing incorrect solutions
- Notable model failure mode 2: claiming contradictions or missing information where none exists
- Notable model failure mode 3: failing to identify the initial logical break-in needed to reduce the search space
- Does this paper reveal a benchmark-design limitation as well? yes; it shows both that many reasoning benchmarks over-reward memorized templates and that text-only puzzle evaluation measures something narrower than full human puzzle play

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Minor contrast only; it helps show that exact verification does not imply easy reasoning, but it is not a central motivation anchor for game-agent benchmarking.
- Best use in Section 1 (taxonomy and evolutionary levels): Strong contrast for human-curated symbolic puzzle diagnostics that stay narrow in world type while still resisting memorized reasoning templates.
- Best use in Section 2 (core capabilities evaluated by games): Direct support for creative break-in reasoning, global consistency maintenance, and long-form symbolic deduction.
- Best use in Section 3 (interaction and evaluation paradigm): Useful contrast case for textified puzzle interfaces, single-shot versus multi-step evaluation, and the deliberate separation between pure reasoning and tool-use tracks.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Supports a future-design argument for keeping tool-use tracks separate from intrinsic-reasoning tracks instead of mixing them into one headline number.

## 10. Relation to nearby papers
- Closest predecessor(s): classic Sudoku reasoning work and adjacent creativity-oriented reasoning benchmarks such as ARC
- Closest follow-up(s): no direct follow-up in our corpus; the nearest neighbors are symbolic-diagnostic papers such as `VGRPBench`, `CrossWordBench`, and `PuzzlePlex`
- Best comparison targets inside our corpus: CrossWordBench, PuzzleJAX, VGRPBench, DeepPHY
- What this paper uniquely adds relative to neighbors: It focuses on human-curated logical break-ins within one puzzle family, while also exposing how text-only and tool-use tracks can diverge.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- The core `challenge_100` benchmark contains 100 puzzles: 15 4x4, 15 6x6, and 70 9x9; 50 of the 9x9 puzzles were curated exclusively for the benchmark, and 20 challenge puzzles are difficult vanilla Sudokus supplied by Nikoli.
- The release also includes `nikoli_100`, `ctc` with 2,565 Sudoku variants solved on Cracking the Cryptic, and transcript/action data extracted from more than 3,000 published solve videos.
- The reported evaluation uses single-shot and multi-step text interaction; in multi-step mode the model must provide at least one valid digit per round, and the paper keeps only the most recent five model responses in context.
- Frontier LLMs solve fewer than 15% overall, with performance dropping sharply on 6x6 and especially 9x9 puzzles; multi-step interaction improves smaller puzzles only modestly.

### 11.2 Our synthesis / interpretation
- Sudoku-Bench is strongest as a narrow symbolic-reasoning contrast, not as evidence of richer interactive game-agent competence.
- It is especially useful as a counterexample to claims that reasoning benchmarks are nearly saturated, but the survey should keep its text-only evaluation protocol explicit.
- The paper also gives a clean design example of separating intrinsic reasoning evaluation from optional tool-use infrastructure.

### 11.3 Uncertain or needs re-check
- Re-check the exact per-model solve-rate table if we later need quantitative comparison by puzzle size and evaluation mode.
- Re-check which challenge puzzles depend most heavily on visual symmetry or geometry if we later discuss residual visual burden despite textualization.
- If we later cite the broader released resources, re-check whether the surrounding section needs the core `challenge_100` benchmark only or also the transcript/tooling ecosystem.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? No immediate reread is needed; the current audit already depends on dataset design, interaction setup, and the discussion of tool-use.
- Which section to read next if needed: challenge_100 curation / evaluation framework / discussion on tool-use
- Follow-up question(s): If the survey later needs a cleaner comparison table, should we cite only the tool-free `challenge_100` results or explicitly separate them from the broader SudokuPad ecosystem?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P2
- Reading depth: deep
- Batch ID: B08
- Outline sections: 1,2,4
- Survey role: contrast
- Paper card path: `paper_cards/B08/SudokuBench.md`
- Next action: draft-section
- Check status: unchecked
- Last updated: 2026-04-10
