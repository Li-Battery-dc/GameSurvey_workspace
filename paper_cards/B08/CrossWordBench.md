# CrossWordBench CrossWordBench: Evaluating the Reasoning Capabilities of LLMs and LVLMs with Controllable Puzzle Generation

## 0. Metadata
- Date: 2025/03
- Venue: arXiv
- Authors: Jixuan Leng, Chengsong Huang, Langlin Huang, Bill Yuchen Lin, William W. Cohen, Haohan Wang, Jiaxin Huang
- Paper link: https://arxiv.org/pdf/2504.00043v2.pdf
- Code link: https://github.com/SeanLeng1/CrossWordBench
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: high
- Review gate label: strong

## 1. One-paragraph benchmark summary
- CrossWordBench is a controllable crossword benchmark that generates puzzles from three clue sources: public multilingual repositories, WordNet-style dictionary definitions, and adapted benchmark QA data such as CommonsenseQA. Its core contribution is not human-authored crossword craftsmanship, but a scalable structural-constraint benchmark where clue answering must satisfy crossing-letter consistency in either text or image format. The paper evaluates over 20 LLMs and LVLMs in direct zero-shot solving, plus a smaller agentic interactive mode for LVLMs that updates grid images step by step, and reports word-, letter-, and intersection-level metrics rather than only full-puzzle success. For this survey, CrossWordBench is best used as a contrast paper on multimodal structural reasoning and on how crossword constraints can make even saturated QA material nontrivial again without becoming a full ecological game-agent benchmark.

## 2. Position in our survey
- Why-games relevance: Crossword structure forces local answers to satisfy global consistency constraints, making reasoning more than independent clue retrieval.
- Historical stage: diagnostic capability probe
- Benchmark level(s): L2 strategic reasoning
- Most relevant outline section(s): 1,2,3,4
- Role in corpus: contrast

## 3. Design-space coding
### 3.1 Structure
- Form: Puzzle
- Construction: Generated
- Construction note: automatically generated crossword puzzles
- Benchmark unit: full puzzle solution / interactive fill step

### 3.2 Mechanics profile
- State visibility: full
- Transition uncertainty: deterministic
- Actor configuration: single-agent
- Incentive structure: N/A
- Temporal regime: turn-based

### 3.3 Benchmark scope
- Scope: single game
- Number of games / tasks: main English evaluation uses 100 7x7 and 100 14x14 puzzles; additional sets include 100 Chinese 7x7, 100 English Simple 7x7, and 50 CommonsenseQA-derived 7x7 puzzles

### 3.4 Modality
- Observation modality: mixed
- Action modality: semantic
- Perception burden retained: clue interpretation and grid-constraint satisfaction; image input is required for the LVLM track
- Perception burden removed: the LLM track can use a text grid representation rather than raw image parsing, so the benchmark does not require human-like visual play in its strongest setting

## 4. What this benchmark measures
- Primary capability target: joint language reasoning and structural constraint satisfaction
- Secondary capability target(s): visual grid parsing for LVLMs, exploiting crossing-letter constraints, and limited stepwise correction in the interactive mode
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? no
- Does it test social reasoning / deception / cooperation? no
- Does it test visual grounding / spatial-temporal reasoning? partially; it tests static grid parsing and clue-grid alignment rather than dynamic visual control
- Does it test long-horizon autonomy / task completion? partially; multi-clue puzzle completion is sequential, but still far from embodied long-horizon agency
- Does it test real-time efficiency? no
- Does it test cross-game transfer / open-ended generalization? partially; across clue sources, languages, and grid sizes within one crossword format
- Why is a game environment especially suitable here? Crosswords turn many local clue answers into a globally checkable combinatorial object.

## 5. Interaction paradigm
- Observation channel: clues plus either an image grid or a text grid representation
- Action channel: filled crossword answers, optionally step by step in interactive mode
- Interface type: natural language / structured action space / hybrid
- Agent scaffold allowed: none in direct zero-shot solving; the interactive VLM mode adds external grid-update functions and feedback
- Is there privileged API access? yes in the interactive setting, where grid updates are provided externally
- How close is the setup to human play? low to medium; crossword logic is authentic, but the benchmark uses generated puzzles and structured prompting instead of human-authored themed puzzle experiences
- Main ecological-validity trade-off: controllable generated puzzles improve scale, multimodal comparison, and structural diagnosis, but they do not replicate the thematic craftsmanship or open-ended interaction of human-authored crosswords

## 6. Evaluation protocol
- Main score: word coverage rate
- Auxiliary score(s): letter coverage rate and intersection consistency rate
- Evaluation style: accuracy / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: no human baseline or fixed AI anchor; proprietary and open models are compared in both LLM and LVLM settings, with an additional interactive mode for LVLMs
- Automatic verifiability: high
- Calibration method: controllable grid sizes (7x7 and 14x14 in English), multiple clue-source categories, and grid-generation choices such as crossing density and prefill ratio
- Anti-contamination argument: even when clue pairs come from known sources like CommonsenseQA, the generated crossword structures still remain challenging because models must satisfy grid constraints rather than answer clues independently
- Reliability or comparability concerns: generated puzzles may differ from human-authored crossword quality, main experiments focus on the English sets, and LVLM results depend strongly on grid-parsing accuracy

## 7. Main contributions
- Contribution 1: Builds a controllable crossword benchmark from public, dictionary, and benchmark-adapted clue sources.
- Contribution 2: Defines structural metrics that separate clue accuracy from grid consistency.
- Contribution 3: Introduces an interactive LVLM mode with external grid updates, creating a bounded function-calling style agent setting.

## 8. Main findings and failure modes
- Core empirical takeaway: reasoning LLMs clearly outperform non-reasoning models and LVLMs, but performance remains far from solved, especially as grids grow, multimodal parsing is required, or models must recover from early mistakes.
- Notable model failure mode 1: failing to satisfy cross-letter intersection constraints
- Notable model failure mode 2: length mismatches or skipped clues
- Notable model failure mode 3: LVLM failures driven by poor grid parsing and OCR of down words
- Does this paper reveal a benchmark-design limitation as well? yes; it shows both that structural constraints can revive saturated QA sources and that multimodal reasoning scores can collapse for reasons as basic as grid parsing

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Minor contrast only; it shows how structured puzzles can make familiar QA-style knowledge interactively harder, but it is not a central motivation paper for game-agent benchmarking.
- Best use in Section 1 (taxonomy and evolutionary levels): Strong contrast for controllable generated puzzle benchmarks that sit closer to symbolic reasoning probes than to ecological game environments.
- Best use in Section 2 (core capabilities evaluated by games): Direct support for global consistency, crossing-constraint integration, and multimodal clue-grid reasoning.
- Best use in Section 3 (interaction and evaluation paradigm): Strong case for comparing text-grid and image-grid interfaces on the same underlying task, and for using multi-metric scoring beyond one headline accuracy number.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Useful for arguing that future multimodal benchmarks need verifiable feedback and better separation between reasoning failure and perception failure.

## 10. Relation to nearby papers
- Closest predecessor(s): text-centric crossword datasets such as Cryptonite and earlier crossword QA formulations
- Closest follow-up(s): no direct follow-up in our corpus; the nearest neighbors are symbolic or multimodal puzzle probes such as `SudokuBench`, `VGRPBench`, and `PuzzleJAX`
- Best comparison targets inside our corpus: SudokuBench, PuzzleJAX, VGRPBench, DeepPHY
- What this paper uniquely adds relative to neighbors: It measures not only whether local answers are right, but also whether the whole puzzle is internally consistent across text and image interfaces.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- CrossWordBench generates puzzles from three clue sources: public multilingual repositories, dictionary definitions, and adapted benchmark QA data such as single-word-answer CommonsenseQA questions.
- The main English evaluation uses 100 7x7 and 100 14x14 puzzles; additional evaluations cover 100 Chinese 7x7, 100 English Simple 7x7, and 50 CommonsenseQA-derived 7x7 puzzles.
- The paper reports Word Coverage Rate (WCR), Letter Coverage Rate (LCR), and Intersection Consistency Rate (ICR), and uses Interactive Success Step (ISS) for the interactive LVLM setting.
- Reasoning LLMs outperform non-reasoning models, LVLM performance correlates strongly with grid-parsing accuracy, and most models in interactive mode fail on the very first step for most 7x7 English puzzles.

### 11.2 Our synthesis / interpretation
- CrossWordBench is especially useful for survey claims about structural constraints amplifying benchmark difficulty even when clue sources themselves are familiar.
- It is a good bridge between language-only puzzle solving and multimodal grid parsing, but it should remain a contrast case rather than being overcast as visual agency proper.
- The benchmark is also a clean example of separating reasoning failure from perception failure through distinct metrics and analyses.

### 11.3 Uncertain or needs re-check
- Re-check the exact grid-generation settings such as prefill ratio if we later need a benchmark-construction comparison table.
- Re-check the interactive-mode protocol details if we later compare agentic puzzle interfaces directly against other function-calling settings.
- If we later cite the CommonsenseQA adaptation as an anti-contamination argument, re-check how strongly we want to frame it as robustness to source saturation versus merely added structural difficulty.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? No immediate reread is needed; the current audit already depends on benchmark construction, metric design, and the interactive mode analysis.
- Which section to read next if needed: benchmark curation / metric definitions / interactive mode
- Follow-up question(s): If the survey later needs one headline structural metric, should it emphasize ICR as the clearest evidence that models are or are not using crossing constraints?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P2
- Reading depth: deep
- Batch ID: B08
- Outline sections: 1,2,3,4
- Survey role: contrast
- Paper card path: `paper_cards/B08/CrossWordBench.md`
- Next action: draft-section
- Check status: unchecked
- Last updated: 2026-04-27
