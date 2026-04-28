# VGRPBench VGRP-Bench: Visual Grid Reasoning Puzzle Benchmark for Large Vision-Language Models

## 0. Metadata
- Date: 2025/03
- Venue: arXiv
- Authors: Yufan Ren, Konstantinos Tertikas, Shalini Maiti, Junlin Han, Tong Zhang, Sabine Süsstrunk, Filippos Kokkinos
- Paper link: https://arxiv.org/pdf/2503.23064v2.pdf
- Code link: https://yufan-ren.com/subpage/VGRP-Bench/
- Reading depth: deep
- Card status: finalized
- Confidence in this card: high
- Review gate label: strong

## 1. One-paragraph benchmark summary
- VGRP-Bench is a visual grid-puzzle benchmark for LVLMs built around 20 customizable puzzle families rather than a fixed scraped set of instances. The paper evaluates off-the-shelf chat and reasoning LVLMs across multiple difficulty levels, separates overall puzzle solving from perception and step-level rule following, and additionally provides text versions of all puzzles to disentangle reasoning failures from vision failures. It also studies two post-training strategies, solution SFT and reasoning SFT, finding meaningful gains on trained easy puzzles but weak transfer to harder or unseen settings. For this survey, VGRP-Bench is best used as a contrast paper on multimodal puzzle diagnostics and on the gap between visual perception, rule understanding, and true puzzle-solving competence rather than as evidence of visual agency proper.

## 2. Position in our survey
- Why-games relevance: Grid puzzles let a benchmark stress perception and rule-based reasoning while keeping exact verification.
- Historical stage: diagnostic capability probe
- Benchmark level(s): L2 multimodal puzzle reasoning; L4 visual-agency boundary case
- Most relevant outline section(s): 2,3,4
- Role in corpus: contrast

## 3. Design-space coding
### 3.1 Structure
- Form: Puzzle
- Construction: Authored
- Construction note: customizable visual reasoning puzzles
- Benchmark unit: full puzzle solution / step

### 3.2 Mechanics profile
- State visibility: full
- Transition uncertainty: deterministic
- Actor configuration: single-agent
- Incentive structure: N/A
- Temporal regime: turn-based

### 3.3 Benchmark scope
- Scope: curated suite
- Number of games / tasks: 20 puzzle families with easy, medium, and hard variants; evaluations use 5 runs of 20 sampled instances each for 100 total samples per reported setting

### 3.4 Modality
- Observation modality: visual image
- Action modality: semantic
- Perception burden retained: grid parsing, clue localization, visual-symbol alignment, and rule interpretation
- Perception burden removed: no naturalistic visual clutter or embodied control beyond puzzle boards

## 4. What this benchmark measures
- Primary capability target: integrated visual perception and logical puzzle solving
- Secondary capability target(s): rule following, local cell grounding, and generalization under puzzle variation
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? no
- Does it test social reasoning / deception / cooperation? no
- Does it test visual grounding / spatial-temporal reasoning? yes
- Does it test long-horizon autonomy / task completion? partially; as multi-step symbolic puzzle completion rather than interactive long-horizon control
- Does it test real-time efficiency? no
- Does it test cross-game transfer / open-ended generalization? partially; across puzzle families and difficulty settings, but not across open-ended game environments
- Why is a game environment especially suitable here? Puzzle boards make errors attributable: a model can fail at seeing, rule following, or solving, and those can be measured separately.

## 5. Interaction paradigm
- Observation channel: puzzle board images, or text versions in comparison settings
- Action channel: structured grid solutions
- Interface type: image input / structured action space / hybrid
- Agent scaffold allowed: none in the main benchmark; post-training variants are explored separately from the benchmark evaluation
- Is there privileged API access? no
- How close is the setup to human play? low to medium; the puzzles are authentic, but the benchmark uses direct board-to-answer generation instead of human-style interactive solving
- Main ecological-validity trade-off: VGRP-Bench is strong on controlled vision-plus-reasoning analysis, but it remains a static puzzle benchmark rather than live interactive game play

## 6. Evaluation protocol
- Main score: puzzle-solving success rate
- Auxiliary score(s): perception accuracy, cell-level evaluation, step-level rule-following accuracy, and taxonomy analyses
- Evaluation style: accuracy / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: no human baseline or fixed AI anchor; closed and open LVLMs are compared, and post-trained variants are measured against pretrained ones
- Automatic verifiability: high
- Calibration method: difficulty levels, clue counts, and puzzle taxonomy
- Anti-contamination argument: puzzles are customizable and generated within the benchmark rather than simply scraped as fixed instances
- Reliability or comparability concerns: text-version results show that perception is only part of the problem, while post-training gains remain puzzle-specific and do not transfer robustly to harder or unseen tasks

## 7. Main contributions
- Contribution 1: Introduces a 20-puzzle-family visual benchmark with a taxonomy over rules and clues.
- Contribution 2: Adds fine-grained perception, cell-level, and step-level evaluations.
- Contribution 3: Studies post-training and shows limited generalization beyond easier seen settings.

## 8. Main findings and failure modes
- Core empirical takeaway: LVLMs struggle even on easy puzzle settings, and while text versions improve results, both off-the-shelf inference and post-training still leave large reasoning gaps.
- Notable model failure mode 1: mislocalizing values or clues on the grid
- Notable model failure mode 2: misunderstanding the role of visual components such as cages versus board numbers
- Notable model failure mode 3: weak transfer to unseen puzzle types or harder variants after fine-tuning
- Does this paper reveal a benchmark-design limitation as well? yes; it shows that whole-puzzle accuracy alone hides whether a model failed at perception, rule understanding, or downstream reasoning

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Minor contrast showing that exact-score multimodal puzzles remain difficult even when they are static and fully verifiable.
- Best use in Section 1 (taxonomy and evolutionary levels): Useful boundary case for separating visual puzzle diagnostics from L4 visual agency: VGRP-Bench keeps image input but removes closed-loop control, timing, and recovery.
- Best use in Section 2 (core capabilities evaluated by games): Direct support for decomposing multimodal puzzle competence into perception, rule following, cell-level grounding, and solution generation.
- Best use in Section 3 (interaction and evaluation paradigm): Strong contrast between image-first and text-control puzzle interfaces, plus a good example of multi-granular evaluation beyond final solve rate.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Supports the claim that narrow post-training on puzzle families does not solve harder-level reasoning or unseen-puzzle generalization.

## 10. Relation to nearby papers
- Closest predecessor(s): symbolic puzzle diagnostics such as `SudokuBench` and visual-game difficulty probes such as `INGVP`
- Closest follow-up(s): no direct follow-up in our corpus; the nearest neighbors are `CrossWordBench`, `SudokuBench`, and `INGVP`
- Best comparison targets inside our corpus: CrossWordBench, SudokuBench, DeepPHY, ReasoningViaVideo
- What this paper uniquely adds relative to neighbors: It is the most explicit puzzle-taxonomy paper in this batch and provides visual-versus-text and cell-versus-step diagnostics rather than only final solve rates.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- VGRP-Bench contains 20 customizable grid-based reasoning puzzles with multiple difficulty levels, and each reported evaluation setting uses 100 total sampled instances from 5 runs of 20 instances each.
- The paper evaluates overall perception and puzzle-solving, plus finer-grained cell-level perception and step-level rule-following performance.
- The benchmark provides text versions of all puzzles, and these improve performance relative to the vision setting without eliminating the core reasoning difficulty.
- The paper studies Solution SFT and Reasoning SFT, reporting gains on trained easy puzzles but weak generalization to harder or unseen settings.

### 11.2 Our synthesis / interpretation
- VGRP-Bench is especially useful for survey claims that puzzle benchmarks should separate visual parsing from downstream reasoning.
- It is also a strong source on the limitations of narrow post-training for multimodal reasoning, since better performance on trained easy puzzles does not imply broader transfer.
- The paper should remain a visual-diagnostic contrast rather than being overstated as a human-like visual-agent benchmark.

### 11.3 Uncertain or needs re-check
- Re-check the exact 20 puzzle families if we later need a taxonomy table.
- Re-check the cross-puzzle generalization appendix if we compare S-SFT and R-SFT in more detail.
- If we later use it in the taxonomy section, re-check whether we want to frame it as a Level-4 precursor or explicitly as a boundary-case diagnostic rather than visual agency itself.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? No immediate reread is needed; the current audit already depends on the evaluation protocol, text-version comparison, and post-training results.
- Which section to read next if needed: taxonomy / fine-grained evaluation / post-training generalization
- Follow-up question(s): If the survey later needs one headline diagnostic lesson, should it cite the text-versus-vision gap or the weak SFT generalization result as the stronger evidence?

## 13. Registry sync
- Registry row synced: yes
- Registry status: finalized
- Priority: P2
- Reading depth: deep
- Batch ID: B08
- Outline sections: 2,3,4
- Survey role: contrast
- Paper card path: `paper_cards/B08/VGRPBench.md`
- Next action: draft-section
- Check status: unchecked
- Last updated: 2026-04-28
