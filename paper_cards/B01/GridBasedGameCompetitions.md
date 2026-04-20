# GridBasedGameCompetitions Evaluating Large Language Models with Grid-Based Game Competitions: An Extensible LLM Benchmark and Leaderboard

## 0. Metadata
- Date: 2024
- Venue: Journal of Cognitive Systems 2024
- Authors: Oguzhan Topsakal, Colby J. Edell, Jackson B. Harper
- Paper link: https://dergipark.org.tr/en/download/article-file/4483558
- Code link: https://github.com/research-outcome/LLM-Game-Benchmark
- Reading depth: structured-skim
- Card status: card-reviewed
- Confidence in this card: medium
- Review gate label: usable

## 1. One-paragraph benchmark summary
- This paper introduces an open-source web benchmark and leaderboard for three deterministic grid games: Tic-Tac-Toe, Connect Four, and Gomoku. It evaluates seven LLMs plus a random-play baseline across list, illustration, and image prompt formats over 2,310 simulated matches, tracking wins, disqualifications, invalid moves, and missed win or block opportunities. The main empirical pattern is that symbolic list prompts are handled best, while illustration and especially image prompts produce more rule failures and missed strategic moves as game complexity increases. For this survey, the paper is best used as a narrow controlled probe of legal-move generation, board-state interpretation, and prompt-format sensitivity rather than as a broad game-agent benchmark.

## 2. Position in our survey
- Why-games relevance: Small deterministic games make rule comprehension and action validity easy to verify, which is useful for controlled LLM comparison.
- Historical stage: diagnostic capability probe
- Narrative level(s): L1 rule following / L2 strategic reasoning
- Most relevant outline section(s): 1,2,3
- Role in corpus: contrast

## 3. Design-space coding
### 3.1 Environment structure
- Information structure: perfect
- Transition structure: deterministic
- Agent structure: multi-agent
- Social structure: competitive
- Time structure: turn-based

### 3.2 World structure
- World type(s): board
- Real game / simulated game / designed task-game hybrid: benchmark of real grid games under standardized prompting
- Benchmark unit: match

### 3.3 Benchmark scope
- Scope: game family
- Number of games / tasks: 3 games, 3 prompt types, 2,310 simulated matches, 7 LLMs plus random play

### 3.4 Modality
- Primary modality: mixed
- Perception burden retained: rule following, board-state interpretation, and strategic move selection
- Perception burden removed: list prompts remove most perceptual burden and expose the board almost symbolically

## 4. What this benchmark measures
- Primary capability target: legal move generation, board-state interpretation, and simple strategic reasoning
- Secondary capability target(s): prompt-format robustness, visual input handling, and missed win or block opportunities
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? no
- Does it test social reasoning / deception / cooperation? no
- Does it test visual grounding / spatial-temporal reasoning? partially
- Does it test long-horizon autonomy / task completion? no
- Does it test real-time efficiency? no
- Does it test cross-game transfer / open-ended generalization? no
- Why is a game environment especially suitable here? Grid games keep rules explicit and outcomes exact, which makes invalid-action and prompt-format comparisons easy to interpret.

## 5. Interaction paradigm
- Observation channel: prompt text plus either occupied-cell lists, symbolic board illustrations, or attached board images; invalid-move warnings and remaining-invalid-move counts are injected during play
- Action channel: JSON row and column move proposals
- Interface type: natural language / structured action space / image / hybrid
- Agent scaffold allowed: none
- Is there privileged API access? no
- How close is the setup to human play? low
- Main ecological-validity trade-off: the benchmark is highly controlled, but direct symbolic state exposure, retry warnings after invalid moves, and tiny solved games make it more diagnostic of interface handling than of broader game-agent competence

## 6. Evaluation protocol
- Main score: win, draw, and disqualification outcomes across repeated pairwise matches
- Auxiliary score(s): invalid moves, total moves, and missed win or block opportunities per valid move by game and prompt type
- Evaluation style: win rate / tournament / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: seven-way model-vs-model play plus a random-play baseline; each pairing is repeated five times for each game and prompt combination, with Llama3-70B excluded from image-prompt tests
- Automatic verifiability: high
- Calibration method: shared prompt structure across games, five repeats per combination, fixed invalid-move thresholds by game, and a rule that disqualification does not count as a win for the opponent
- Anti-contamination argument: weak; the paper assumes the tested models were not explicitly trained for these games and only proposes future custom or altered games as a mitigation
- Reliability or comparability concerns: the game family is tiny and canonical, only five repeats are run per combination, prompt modality confounds strategic competence, and there is no human baseline

## 7. Main contributions
- Contribution 1: Builds an open-source web simulator, artifact pipeline, and leaderboard around simple grid games.
- Contribution 2: Compares list, illustration, and image prompts inside the same benchmark family under a shared protocol.
- Contribution 3: Reports how wins, disqualifications, invalid moves, and missed strategic opportunities change with game complexity and prompt format.

## 8. Main findings and failure modes
- Core empirical takeaway: list prompts are consistently easiest, while illustration and especially image prompts lead to more disqualifications, invalid moves, and missed win or block opportunities as the games become more complex.
- Notable model failure mode 1: many invalid moves come from selecting already occupied cells, and some models also produce JSON-format errors
- Notable model failure mode 2: blocking the opponent degrades more than spotting one's own winning moves, especially under illustration and image prompts
- Notable model failure mode 3: benchmark outcomes depend heavily on modality support, including the inability to run Llama3-70B on image prompts
- Does this paper reveal a benchmark-design limitation as well? yes; prompt representation and multimodal support can dominate what appears to be strategic competence in simple board games

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Limited supporting example that games provide exact legal-action checks and a clear random-play contrast.
- Best use in Section 1 (taxonomy and evolutionary levels): Useful as a small deterministic board-game probe, but too narrow to act as a main historical anchor.
- Best use in Section 2 (core capabilities evaluated by games): Supports discussion of rule following, board-state encoding, and simple deterministic strategy rather than rich planning.
- Best use in Section 3 (interaction and evaluation paradigm): Strongest use case. Helpful for comparing symbolic versus illustrative versus image inputs, JSON action formatting, invalid-move handling, and leaderboard-style aggregation.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Supports the caution that tiny canonical games and multimodal interface burdens can confound claims about genuine strategic competence.

## 10. Relation to nearby papers
- Closest predecessor(s): earlier Tic-Tac-Toe-only board-game evaluations and GTBench-style formal game probes
- Closest follow-up(s): broader formal suites and leaderboard benchmarks with richer games or wider task diversity
- Best comparison targets inside our corpus: GTBench, SmartPlay, BotzoneBench, LLMChess
- What this paper uniquely adds relative to neighbors: It cleanly isolates prompt-format effects inside a tiny solved-game family and packages the setup as an open-source simulation and leaderboard workflow.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- The benchmark uses Tic-Tac-Toe, Connect Four, and Gomoku with list, illustration, and image prompt formats.
- The study evaluates Claude 3.5 Sonnet, Claude 3 Sonnet, Gemini 1.5 Flash, Gemini 1.5 Pro, GPT-4 Turbo, GPT-4o, and Llama3-70B plus a random-play baseline; Llama3-70B is not used for image prompts.
- Each pairing is repeated five times per game and prompt combination, with invalid-move limits of three for Tic-Tac-Toe, six for Connect Four, and fifteen for Gomoku; the full study reports 2,310 simulated matches.
- The reported leaderboard aggregates win ratios, wins, disqualifications, invalid moves, and total moves, and the paper also analyzes missed win or block opportunities per valid move.
- List prompts are generally easiest, while illustration and image prompts lead to more failures as game complexity increases; the paper notes no out-of-bounds errors and attributes many invalid moves to already occupied spaces.

### 11.2 Our synthesis / interpretation
- This is best treated as a narrow controlled contrast case at the lower end of the design space, not as a rich benchmark of long-horizon game agency.
- Its real survey value is methodological: it shows how much representation choice, multimodal support, and retry or disqualification protocol can matter before moving to richer games.

### 11.3 Uncertain or needs re-check
- The PDF clearly supports year-level citation as a 2024 JCS paper, but it does not establish a month-level publication date; use year-level citation unless publisher metadata is needed.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? No immediate follow-up needed; this card was re-audited against the full paper.
- Which section to read next if needed: the GitHub leaderboard artifacts if we later need exact per-model aggregate snapshots beyond the paper figures
- Follow-up question(s): If we cite this paper in Section 3, should we foreground prompt-format sensitivity or the invalid-move and missed-opportunity metrics?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P2
- Reading depth: structured-skim
- Batch ID: B01
- Outline sections: 1,2,3
- Survey role: contrast
- Paper card path: `paper_cards/B01/GridBasedGameCompetitions.md`
- Check status: unchecked
- Last updated: 2026-04-10
