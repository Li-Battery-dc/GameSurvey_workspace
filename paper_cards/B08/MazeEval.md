# MazeEval MazeEval: A Benchmark for Testing Sequential Decision-Making in Language Models

## 0. Metadata
- Date: 2025/07
- Venue: arXiv
- Authors: Hafsteinn Einarsson
- Paper link: https://arxiv.org/pdf/2507.20395v1.pdf
- Code link:
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: high
- Review gate label: usable

## 1. One-paragraph benchmark summary
- MazeEval is a deliberately minimal coordinate-based maze-navigation benchmark for testing spatial reasoning in LLMs without visual input. Models act through function calls, receiving current coordinates, goal coordinates, distance-to-wall information in each cardinal direction, and a complete history of previously visited states, then choosing one of four moves. The paper evaluates identical mazes in English and Icelandic and finds a sharp language gap for most models, while nearly all failures arise from looping rather than from immediate misunderstandings of walls or move legality. For this survey, MazeEval is best used as a narrow probe of sequential spatial reasoning, privileged state interfaces, and multilingual robustness rather than as a broad embodied or game-agent benchmark.

## 2. Position in our survey
- Why-games relevance: Simple games can isolate a core cognitive ingredient such as sequential spatial reasoning without confounds from richer interfaces.
- Historical stage: diagnostic capability probe
- Benchmark level(s): L2 strategic reasoning
- Most relevant outline section(s): 2,3,4
- Role in corpus: contrast

## 3. Design-space coding
### 3.1 Structure
- Form: Puzzle
- Construction: Authored
- Construction note: designed maze benchmark
- Benchmark unit: maze episode

### 3.2 Mechanics profile
- State visibility: partial
- Transition uncertainty: deterministic
- Actor configuration: single-agent
- Incentive structure: N/A
- Temporal regime: turn-based

### 3.3 Benchmark scope
- Scope: single game
- Number of games / tasks: five DFS-generated mazes for each size from 5x5 to 15x15, with additional exploratory tests for O3 at 30x30 and 40x40

### 3.4 Modality
- Observation modality: text or symbolic
- Action modality: semantic
- Perception burden retained: spatial state tracking and route planning
- Perception burden removed: all visual cues are removed

## 4. What this benchmark measures
- Primary capability target: sequential spatial reasoning with minimal sensory input
- Secondary capability target(s): loop avoidance, multilingual robustness, and path efficiency
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? no
- Does it test social reasoning / deception / cooperation? no
- Does it test visual grounding / spatial-temporal reasoning? no visual grounding
- Does it test long-horizon autonomy / task completion? partially
- Does it test real-time efficiency? no
- Does it test cross-game transfer / open-ended generalization? partially; mostly across larger mazes and a second language within the same task family
- Why is a game environment especially suitable here? Mazes provide a clean sequential decision problem where path quality and failure modes are exactly measurable.

## 5. Interaction paradigm
- Observation channel: coordinates, distances to walls, goal coordinates, and visit history
- Action channel: function calls selecting north, south, east, or west
- Interface type: API / structured action space
- Agent scaffold allowed: full visit history is provided by the environment at every step
- Is there privileged API access? yes
- How close is the setup to human play? low; the benchmark intentionally removes visual and embodied richness
- Main ecological-validity trade-off: MazeEval isolates spatial reasoning cleanly, but it is far removed from natural navigation settings because the agent receives structured coordinates, wall distances, and a persistent visit log instead of human-like perception

## 6. Evaluation protocol
- Main score: maze success rate
- Auxiliary score(s): step efficiency, wall hits, and backtracking statistics
- Evaluation style: completion rate / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: several frontier models are compared on identical mazes in English and Icelandic
- Automatic verifiability: high
- Calibration method: paired bilingual evaluation on the same mazes and strict limits on revisits and total steps
- Anti-contamination argument: the coordinate-plus-distance formulation had not been publicly released before this benchmark
- Reliability or comparability concerns: the task probes one narrow form of spatial cognition, uses only five mazes per size with early stopping after total failure at a size, and may overstate weakness or strength relative to richer embodied settings

## 7. Main contributions
- Contribution 1: Introduces a minimal maze benchmark for pure spatial reasoning without visual cues.
- Contribution 2: Uses function calling and explicit movement limits to make behavior easy to analyze.
- Contribution 3: Adds a bilingual evaluation showing strong English-over-Icelandic gaps for many models.

## 8. Main findings and failure modes
- Core empirical takeaway: most models fail abruptly beyond moderate maze sizes, and nearly all failures come from looping despite the benchmark providing explicit visit history and distance information.
- Notable model failure mode 1: revisiting the same cells repeatedly despite access to path history
- Notable model failure mode 2: degraded spatial performance in Icelandic relative to English
- Notable model failure mode 3: weak scaling from small mazes to larger ones
- Does this paper reveal a benchmark-design limitation as well? yes; it shows that many spatial-agent claims may depend heavily on language and interface framing

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Minor contrast only; it shows that even stripped-down sequential tasks can reveal severe reasoning failures, but it is not a central motivation anchor for game benchmarking writ large.
- Best use in Section 1 (taxonomy and evolutionary levels): Minor boundary-case contrast for highly stripped-down task-games that preserve sequential decision-making while removing nearly all ecological content.
- Best use in Section 2 (core capabilities evaluated by games): Strong evidence for spatial memory and loop avoidance as distinct targets.
- Best use in Section 3 (interaction and evaluation paradigm): Good example of a pure function-calling game interface. Useful for bilingual paired evaluation and behavior metrics.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Supports caution about language-dependent "reasoning" claims.

## 10. Relation to nearby papers
- Closest predecessor(s): BabyAI-style navigation probes
- Closest follow-up(s): GameTraversalBenchmark
- Best comparison targets inside our corpus: GameTraversalBenchmark, ReasoningViaVideo, EvoEmpirBench, DeepPHY
- What this paper uniquely adds relative to neighbors: It removes vision almost entirely, so failures can be read as failures of spatial state integration rather than perception.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- MazeEval gives models coordinates, wall distances, goal coordinates, and complete visited-position history through a function-calling interface.
- The paper generates five DFS mazes per size from 5x5 to 15x15, evaluates the same mazes in English and Icelandic, and reports extra exploratory tests up to 30x30 and 40x40 for O3.
- The benchmark terminates runs if a cell is revisited ten times, and the paper reports that 100% of failures came from excessive looping rather than from exhausting the overall move budget.

### 11.2 Our synthesis / interpretation
- MazeEval is a clean lower-level probe and is best used as such rather than as a general proxy for full embodied navigation.
- Its multilingual result is especially useful for arguments about language dependence in supposedly abstract reasoning.
- The benchmark is also a useful caution that strong structure and history support do not eliminate core state-tracking failures.

### 11.3 Uncertain or needs re-check
- Re-check the exact model list and maze counts by size if we later need a table.
- Re-check whether the history prompt format itself may advantage stronger long-context models.
- The paper text appears inconsistent about whether seven or eight models were evaluated; re-check the final count if we later cite it explicitly.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? No immediate reread is needed; the current audit already depends on the interface design, bilingual comparison, and failure analysis.
- Which section to read next if needed: cross-linguistic analysis / efficiency plots / failure analysis
- Follow-up question(s): Would an explicit map-construction scaffold remove most failures, or do the language gaps suggest something deeper than memory formatting?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P2
- Reading depth: deep
- Batch ID: B08
- Outline sections: 2,3,4
- Survey role: contrast
- Paper card path: `paper_cards/B08/MazeEval.md`
- Next action: draft-section
- Check status: unchecked
- Last updated: 2026-04-10
