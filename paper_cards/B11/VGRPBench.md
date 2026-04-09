# VGRPBench VGRP-Bench: Visual Grid Reasoning Puzzle Benchmark for Large Vision-Language Models

## 0. Metadata
- Date: 2025/03
- Venue: arXiv
- Authors: Yufan Ren, Konstantinos Tertikas, Shalini Maiti, Junlin Han, Tong Zhang, Sabine Süsstrunk, Filippos Kokkinos
- Paper link: https://arxiv.org/pdf/2503.23064v2.pdf
- Code link: https://yufan-ren.com/subpage/VGRP-Bench/
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: high
- Review gate label: strong

## 1. One-paragraph benchmark summary
- VGRP-Bench is a large visual puzzle benchmark for LVLMs built around 20 customizable grid-based reasoning puzzles. It emphasizes the combination of grid perception, rule-following, and multi-step solving, and it supplements whole-puzzle accuracy with cell-level and step-level evaluations. The paper also explores post-training with solution SFT and reasoning SFT, showing improvement on easier settings but weak generalization to harder or unseen puzzles. For this survey, VGRP-Bench is a strong reference for visual puzzle taxonomies and fine-grained multimodal evaluation.

## 2. Position in our survey
- Why-games relevance: Grid puzzles let a benchmark stress perception and rule-based reasoning while keeping exact verification.
- Historical stage: diagnostic capability probe
- Narrative level(s): L4 visual agency
- Most relevant outline section(s): 2,3,4
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
- Real game / simulated game / designed task-game hybrid: customizable visual reasoning puzzles
- Benchmark unit: full puzzle solution / step

### 3.3 Benchmark scope
- Scope: curated suite
- Number of games / tasks: 20 puzzle families with easy, medium, and hard variants
- Benchmark intent: diagnostic evaluation

### 3.4 Modality
- Primary modality: image / mixed
- Perception burden retained: grid parsing, clue localization, and visual-symbol alignment
- Perception burden removed: no naturalistic visual clutter beyond puzzle boards

## 4. What this benchmark measures
- Primary capability target: integrated visual perception and logical puzzle solving
- Secondary capability target(s): rule following, local cell grounding, and generalization under puzzle variation
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? no
- Does it test social reasoning / deception / cooperation? no
- Does it test visual grounding / spatial-temporal reasoning? yes
- Does it test long-horizon autonomy / task completion? partially
- Does it test real-time efficiency? no
- Does it test cross-game transfer / open-ended generalization? yes
- Why is a game environment especially suitable here? Puzzle boards make errors attributable: a model can fail at seeing, rule following, or solving, and those can be measured separately.

## 5. Interaction paradigm
- Observation channel: puzzle board images, or text versions in comparison settings
- Action channel: structured grid solutions
- Interface type: image input / structured action space / hybrid
- Agent scaffold allowed: none in the main benchmark; post-training variants are explored
- Is there privileged API access? no
- How close is the setup to human play? medium; the puzzles are authentic-like, but benchmarked through direct answer generation
- Main ecological-validity trade-off: VGRP-Bench is strong on controlled vision-plus-reasoning analysis, but it is still far from live interactive game play

## 6. Evaluation protocol
- Main score: puzzle-solving success rate
- Auxiliary score(s): perception accuracy, cell-level evaluation, step-level rule-following accuracy, and taxonomy analyses
- Evaluation style: accuracy / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: closed and open LVLMs are compared, and post-trained variants are measured against pretrained ones
- Automatic verifiability: high
- Calibration method: difficulty levels, clue counts, and puzzle taxonomy
- Anti-contamination argument: puzzles are customizable and generated within the benchmark rather than simply scraped fixed instances
- Reliability or comparability concerns: post-training gains can be puzzle-specific and do not transfer robustly to harder or unseen tasks

## 7. Main contributions
- Contribution 1: Introduces a 20-puzzle-family visual benchmark with a taxonomy over rules and clues.
- Contribution 2: Adds fine-grained perception, cell-level, and step-level evaluations.
- Contribution 3: Studies post-training and shows limited generalization beyond easier seen settings.

## 8. Main findings and failure modes
- Core empirical takeaway: LVLMs struggle even on easy puzzle settings, and scaling or post-training only partially closes the gap.
- Notable model failure mode 1: mislocalizing values or clues on the grid
- Notable model failure mode 2: misunderstanding the role of visual components such as cages versus board numbers
- Notable model failure mode 3: weak transfer to unseen puzzle types or harder variants after fine-tuning
- Does this paper reveal a benchmark-design limitation as well? yes; it shows that whole-puzzle accuracy alone hides whether a model failed at perception or reasoning

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Shows how puzzles can turn multimodal reasoning into an exactly scored benchmark.
- Best use in Section 1 (taxonomy and evolutionary levels): A useful waypoint in the shift to purpose-built LVLM game benchmarks. Strong source on puzzle taxonomy and customizable benchmark construction.
- Best use in Section 2 (core capabilities evaluated by games): Supports decomposition into perception, rule following, and solution generation.
- Best use in Section 3 (interaction and evaluation paradigm): Good contrast between image-first and text-first puzzle interfaces. Strong reference for multi-granular evaluation.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Supports the claim that post-training on narrow puzzle families does not solve generalization.

## 10. Relation to nearby papers
- Closest predecessor(s): SudokuBench
- Closest follow-up(s): CrossWordBench, MazeEval
- Best comparison targets inside our corpus: SudokuBench, CrossWordBench, PuzzleJAX
- What this paper uniquely adds relative to neighbors: It is the most explicit puzzle-taxonomy paper in this batch and gives fine-grained visual diagnostics rather than only final solve rates.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- VGRP-Bench contains 20 customizable grid-based reasoning puzzles with multiple difficulty levels.
- The paper evaluates puzzle solving, perception, cell-level, and step-level rule-following performance.
- It also studies Solution SFT and Reasoning SFT and reports gains on easy puzzles but weak generalization to harder or unseen settings.

### 11.2 Our synthesis / interpretation
- VGRP-Bench is especially useful for survey claims that puzzle benchmarks should separate visual parsing from downstream reasoning.
- It is also a strong source on the limitations of narrow post-training for visual reasoning.

### 11.3 Uncertain or needs re-check
- Re-check the exact 20 puzzle families if we later need a taxonomy table.
- Re-check the cross-puzzle generalization appendix if we compare S-SFT and R-SFT in more detail.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? A later reread is worthwhile for the taxonomy and post-training sections.
- Which section to read next if needed: evaluation protocol / taxonomy / post-training results
- Follow-up question(s): Which fine-grained metric best predicts eventual puzzle success under harder difficulty?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P2
- Reading depth: deep
- Batch ID: B11
- Outline sections: 2,3,4
- Survey role: contrast
- Paper card path: `paper_cards/B11/VGRPBench.md`
- Next action: draft-section
- Last updated: 2026-04-05
