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
- MazeEval is a deliberately minimal maze-navigation benchmark for testing spatial reasoning in LLMs without visual input. Models interact through function calls, receiving current coordinates, distances to walls, goal coordinates, and a history of visited positions, then issuing moves in the four cardinal directions. The paper evaluates models in both English and Icelandic and finds that most failures come from looping rather than from basic wall-awareness. For this survey, MazeEval is a useful narrow probe of sequential spatial reasoning and multilingual transfer rather than a broad game benchmark.

## 2. Position in our survey
- Why-games relevance: Simple games can isolate a core cognitive ingredient such as sequential spatial reasoning without confounds from richer interfaces.
- Historical stage: diagnostic capability probe
- Narrative level(s): L2 strategic reasoning
- Most relevant outline section(s): 3,4,6
- Role in corpus: contrast

## 3. Design-space coding
### 3.1 Environment structure
- Information structure: partial but sufficient
- Transition structure: deterministic
- Agent structure: single-agent
- Social structure: N/A
- Time structure: turn-based

### 3.2 World structure
- World type(s): puzzle / maze
- Real game / simulated game / designed task-game hybrid: designed maze benchmark
- Benchmark unit: maze episode

### 3.3 Benchmark scope
- Scope: procedural suite
- Number of games / tasks: mazes from 5x5 to 15x15, with extra tests up to 30x30 and 40x40
- Benchmark intent: diagnostic evaluation

### 3.4 Modality
- Primary modality: symbolic state / text
- Perception burden retained: spatial state tracking and route planning
- Perception burden removed: all visual cues are removed

## 4. What this benchmark measures
- Primary capability target: sequential spatial reasoning with minimal sensory input
- Secondary capability target(s): loop avoidance, multilingual robustness, and path efficiency
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? partially
- Does it test social reasoning / deception / cooperation? no
- Does it test visual grounding / spatial-temporal reasoning? no visual grounding
- Does it test long-horizon autonomy / task completion? partially
- Does it test real-time efficiency? no
- Does it test cross-game transfer / open-ended generalization? partially
- Why is a game environment especially suitable here? Mazes provide a clean sequential decision problem where path quality and failure modes are exactly measurable.

## 5. Interaction paradigm
- Observation channel: coordinates, distances to walls, goal coordinates, and visit history
- Action channel: function calls selecting north, south, east, or west
- Interface type: API / structured action space
- Agent scaffold allowed: history
- Is there privileged API access? yes
- How close is the setup to human play? low; the benchmark intentionally removes visual and embodied richness
- Main ecological-validity trade-off: MazeEval isolates spatial reasoning cleanly, but it is far removed from natural navigation settings

## 6. Evaluation protocol
- Main score: maze success rate
- Auxiliary score(s): step efficiency, wall hits, and backtracking statistics
- Evaluation style: completion rate / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: several frontier models are compared on identical mazes in English and Icelandic
- Automatic verifiability: high
- Calibration method: paired bilingual evaluation on the same mazes and strict limits on revisits and total steps
- Anti-contamination argument: the coordinate-plus-distance formulation had not been publicly released before this benchmark
- Reliability or comparability concerns: the task probes one narrow form of spatial cognition and may overstate weakness or strength relative to richer embodied settings

## 7. Main contributions
- Contribution 1: Introduces a minimal maze benchmark for pure spatial reasoning without visual cues.
- Contribution 2: Uses function calling and explicit movement limits to make behavior easy to analyze.
- Contribution 3: Adds a bilingual evaluation showing strong English-over-Icelandic gaps for many models.

## 8. Main findings and failure modes
- Core empirical takeaway: most models fail abruptly beyond moderate maze sizes, and nearly all failures come from looping.
- Notable model failure mode 1: revisiting the same cells repeatedly despite access to path history
- Notable model failure mode 2: degraded spatial performance in Icelandic relative to English
- Notable model failure mode 3: weak scaling from small mazes to larger ones
- Does this paper reveal a benchmark-design limitation as well? yes; it shows that many spatial-agent claims may depend heavily on language and interface framing

## 9. Why this paper matters for our survey
- Best use in Section 0 (why games): Shows that even stripped-down games can reveal deep sequential reasoning failures.
- Best use in Section 1 (historical evolution): Useful as a minimalist counterpoint to richer embodied or visual game benchmarks.
- Best use in Section 2 (design space): Helps define narrow diagnostic task-games.
- Best use in Section 3 (capability targets): Strong evidence for spatial memory and loop avoidance as distinct targets.
- Best use in Section 4 (interaction paradigm): Good example of a pure function-calling game interface.
- Best use in Section 5 (evaluation protocol): Useful for bilingual paired evaluation and behavior metrics.
- Best use in Section 6/7 (limitations and future): Supports caution about language-dependent "reasoning" claims.

## 10. Relation to nearby papers
- Closest predecessor(s): BabyAI-style navigation probes
- Closest follow-up(s): GameTraversalBenchmark
- Best comparison targets inside our corpus: GameTraversalBenchmark, INGVP, TextQuests
- What this paper uniquely adds relative to neighbors: It removes vision almost entirely, so failures can be read as failures of spatial state integration rather than perception.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- MazeEval gives models coordinates, wall distances, goal coordinates, and visited-position history through function calling.
- The paper evaluates mazes from 5x5 to 15x15 in English and Icelandic and notes extra tests up to 30x30 and 40x40 for o3.
- The paper reports that 100% of failures come from excessive looping rather than from exhausting the overall move budget.

### 11.2 Our synthesis / interpretation
- MazeEval is a clean lower-level probe and is best used as such rather than as a general proxy for full embodied navigation.
- Its multilingual result is especially useful for arguments about language dependence in supposedly abstract reasoning.

### 11.3 Uncertain or needs re-check
- Re-check the exact model list and maze counts by size if we later need a table.
- Re-check whether the history prompt format itself may advantage stronger long-context models.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? Only if later drafting needs the exact bilingual analysis or backtracking plots.
- Which section to read next if needed: methods / cross-linguistic analysis / failure analysis
- Follow-up question(s): Would an explicit map-construction scaffold remove most failures, or are the failures deeper than memory formatting?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P2
- Reading depth: deep
- Batch ID: B11
- Outline sections: 3,4,6
- Survey role: contrast
- Paper card path: `paper_cards/B11/MazeEval.md`
- Next action: draft-section
- Last updated: 2026-04-05
