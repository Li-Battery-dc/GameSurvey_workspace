# CrossWordBench CrossWordBench: Evaluating the Reasoning Capabilities of LLMs and LVLMs with Controllable Puzzle Generation

## 0. Metadata
- Date: 2025/03
- Venue: arXiv
- Authors: Jixuan Leng, Chengsong Huang, Langlin Huang, Bill Yuchen Lin, William W. Cohen, Haohan Wang, Jiaxin Huang
- Paper link: https://arxiv.org/pdf/2504.00043v2.pdf
- Code link:
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: high
- Review gate label: strong

## 1. One-paragraph benchmark summary
- CrossWordBench is a controllable crossword benchmark that generates puzzles from public clue-word pairs, dictionary definitions, and adapted benchmark QA data. Its core idea is that crossword solving couples clue answering with visual or structural grid consistency, producing a verifiable multimodal reasoning task that remains difficult even when the underlying clue source is saturated elsewhere. The benchmark supports both direct solving and an interactive mode with grid updates, and it reports separate metrics for word accuracy, letter accuracy, and intersection consistency. For this survey, CrossWordBench is a strong example of how structural constraints can turn familiar QA material into a harder game-like reasoning task.

## 2. Position in our survey
- Why-games relevance: Crossword structure forces local answers to satisfy global consistency constraints, making reasoning more than independent clue retrieval.
- Historical stage: diagnostic capability probe
- Narrative level(s): L2 strategic reasoning / L4 visual agency
- Most relevant outline section(s): 2,3,4,6
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
- Real game / simulated game / designed task-game hybrid: automatically generated crossword puzzles
- Benchmark unit: full puzzle solution / interactive fill step

### 3.3 Benchmark scope
- Scope: curated suite / procedural generator
- Number of games / tasks: generated puzzles across multiple data sources and grid sizes
- Benchmark intent: diagnostic evaluation

### 3.4 Modality
- Primary modality: mixed
- Perception burden retained: clue interpretation and grid-constraint satisfaction; image input is used for LVLM evaluation
- Perception burden removed: the LLM track can use a text grid representation rather than raw image parsing

## 4. What this benchmark measures
- Primary capability target: joint language reasoning and structural constraint satisfaction
- Secondary capability target(s): visual grid parsing, multi-turn correction, and multilingual/generalization analysis
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? no
- Does it test social reasoning / deception / cooperation? no
- Does it test visual grounding / spatial-temporal reasoning? yes
- Does it test long-horizon autonomy / task completion? partially
- Does it test real-time efficiency? no
- Does it test cross-game transfer / open-ended generalization? partially
- Why is a game environment especially suitable here? Crosswords turn many local clue answers into a globally checkable combinatorial object.

## 5. Interaction paradigm
- Observation channel: clues plus either an image grid or a text grid representation
- Action channel: filled crossword answers, optionally step by step in interactive mode
- Interface type: natural language / structured action space / hybrid
- Agent scaffold allowed: tool use in the interactive mode through update functions
- Is there privileged API access? yes in the interactive setting, where grid updates are provided externally
- How close is the setup to human play? medium; the task is authentic, but the benchmark emphasizes controllable puzzle generation and structured outputs
- Main ecological-validity trade-off: generated puzzles improve controllability and scale, but they do not replicate the thematic craftsmanship of human-authored crosswords

## 6. Evaluation protocol
- Main score: word coverage rate
- Auxiliary score(s): letter coverage rate and intersection consistency rate
- Evaluation style: accuracy / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: proprietary and open models are compared in both LLM and LVLM settings, with an interactive mode for LVLMs
- Automatic verifiability: high
- Calibration method: controllable grid size, heuristic puzzle generation, and multiple clue data sources
- Anti-contamination argument: even when clue pairs come from known sources like CommonsenseQA, the generated crossword structures still remain challenging
- Reliability or comparability concerns: generated puzzles may differ from human-authored puzzle quality, and LVLM results depend strongly on grid parsing

## 7. Main contributions
- Contribution 1: Builds a controllable crossword benchmark from public, dictionary, and benchmark-adapted clue sources.
- Contribution 2: Defines structural metrics that separate clue accuracy from grid consistency.
- Contribution 3: Introduces an interactive mode that turns the benchmark into a stepwise agent setting.

## 8. Main findings and failure modes
- Core empirical takeaway: reasoning LLMs outperform conventional LLMs and LVLMs, but performance remains far from solved, especially as grids grow and multimodal parsing is required.
- Notable model failure mode 1: failing to satisfy cross-letter intersection constraints
- Notable model failure mode 2: length mismatches or skipped clues
- Notable model failure mode 3: LVLM failures driven by poor grid parsing and OCR of down words
- Does this paper reveal a benchmark-design limitation as well? yes; it shows that highly saturated QA data can still become challenging once structural constraints are imposed

## 9. Why this paper matters for our survey
- Best use in Section 0 (why games): Demonstrates how game structure can turn familiar question answering into a harder reasoning task.
- Best use in Section 1 (historical evolution): Part of the trend toward controllable generated puzzle benchmarks.
- Best use in Section 2 (design space): Useful for procedural puzzle generation and text-versus-image interface comparisons.
- Best use in Section 3 (capability targets): Supports discussion of global consistency and constraint integration.
- Best use in Section 4 (interaction paradigm): A useful case for comparing LLM and LVLM performance on the same underlying task.
- Best use in Section 5 (evaluation protocol): Strong example of multi-metric scoring beyond task success alone.
- Best use in Section 6/7 (limitations and future): Suggests crossword-like tasks as future multimodal RL environments with verifiable feedback.

## 10. Relation to nearby papers
- Closest predecessor(s): text-centric crossword datasets
- Closest follow-up(s): SudokuBench, VGRPBench
- Best comparison targets inside our corpus: SudokuBench, VGRPBench, GAMEBoT
- What this paper uniquely adds relative to neighbors: It measures not only whether local answers are right, but also whether the whole puzzle is internally consistent.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- CrossWordBench generates puzzles from public clue repositories, dictionary definitions, and adapted benchmark QA data.
- It reports Word Coverage Rate, Letter Coverage Rate, and Intersection Consistency Rate.
- The paper shows that reasoning LLMs outperform LVLMs and that LVLM performance correlates strongly with grid-parsing accuracy.

### 11.2 Our synthesis / interpretation
- CrossWordBench is especially useful for survey claims about structural constraints amplifying benchmark difficulty.
- It is also a good bridge between language-only puzzle solving and multimodal interactive filling.

### 11.3 Uncertain or needs re-check
- Re-check the exact grid sizes used in the main English evaluation if we later need a comparison table.
- Re-check the interactive success step definition if we compare interactive puzzle protocols directly.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? A targeted reread may help later because the metric design is strong survey evidence.
- Which section to read next if needed: benchmark curation / metrics / interactive mode
- Follow-up question(s): Which metric is most predictive of successful full-puzzle solving: WCR, LCR, or ICR?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P2
- Reading depth: deep
- Batch ID: B11
- Outline sections: 2,3,4,6
- Survey role: contrast
- Paper card path: `paper_cards/B11/CrossWordBench.md`
- Next action: draft-section
- Last updated: 2026-04-05
