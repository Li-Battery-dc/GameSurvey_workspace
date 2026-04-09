# GridBasedGameCompetitions Evaluating Large Language Models with Grid-Based Game Competitions: An Extensible LLM Benchmark and Leaderboard

## 0. Metadata
- Date: 2025
- Venue: Journal of Cognitive Systems 2025
- Authors: Oguzhan Topsakal, Colby J. Edell, Jackson B. Harper
- Paper link: https://doi.org/10.52876/jcs.1611181
- Code link: https://github.com/research-outcome/LLM-Game-Benchmark
- Reading depth: structured-skim
- Card status: card-reviewed
- Confidence in this card: medium
- Review gate label: usable

## 1. One-paragraph benchmark summary
- This paper proposes a simple, extensible leaderboard benchmark based on grid games such as Tic-Tac-Toe, Connect Four, and Gomoku. Its main contribution is not game novelty but a controlled comparison of prompt formats: list-based state descriptions, illustrative board renderings, and image inputs. Across 2,310 simulated matches, the authors show that even simple deterministic board games reveal meaningful differences in invalid moves, missed opportunities, and sensitivity to input modality. For this survey, the paper is a useful narrow precursor for formal rule-following and prompt-format analysis rather than a central benchmark anchor.

## 2. Position in our survey
- Why-games relevance: Small deterministic games make rule comprehension and action validity easy to verify, which is useful for controlled LLM comparison.
- Historical stage: formal container
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
- Number of games / tasks: 3 games, 3 prompt types, 2,310 simulated matches
- Benchmark intent: diagnostic evaluation

### 3.4 Modality
- Primary modality: mixed
- Perception burden retained: rule following, board-state interpretation, and strategic move selection
- Perception burden removed: list prompts remove most perceptual burden and expose the board almost symbolically

## 4. What this benchmark measures
- Primary capability target: legal move generation and simple strategic reasoning
- Secondary capability target(s): prompt-format sensitivity, visual board interpretation, and missed-opportunity behavior
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? no
- Does it test social reasoning / deception / cooperation? no
- Does it test visual grounding / spatial-temporal reasoning? partially
- Does it test long-horizon autonomy / task completion? no
- Does it test real-time efficiency? no
- Does it test cross-game transfer / open-ended generalization? no
- Why is a game environment especially suitable here? Grid games keep rules explicit and outcomes exact, which makes invalid-action and prompt-format comparisons easy to interpret.

## 5. Interaction paradigm
- Observation channel: list-form state descriptions, illustrative board renderings, or image inputs
- Action channel: proposed board moves
- Interface type: natural language / image / hybrid
- Agent scaffold allowed: none
- Is there privileged API access? yes in the list-prompt condition
- How close is the setup to human play? low to medium depending on prompt type
- Main ecological-validity trade-off: the benchmark is highly controlled, but its games are so simple that it says more about prompt sensitivity than about broader game-agent competence

## 6. Evaluation protocol
- Main score: win and validity outcomes across matches
- Auxiliary score(s): disqualifications, invalid moves, and missed opportunities by game and prompt type
- Evaluation style: win rate / tournament / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: model-vs-model play among Claude 3.5 Sonnet, GPT-4 Turbo, and Llama3-70B
- Automatic verifiability: high
- Calibration method: shared rules across three games and side-by-side prompt-type comparisons
- Anti-contamination argument: the paper suggests extending to new games and dynamic rule changes to reduce leakage pressure
- Reliability or comparability concerns: the game set is tiny and canonical, so contamination and ceiling effects remain plausible concerns

## 7. Main contributions
- Contribution 1: Builds an extensible benchmark and leaderboard around simple grid games.
- Contribution 2: Compares list, illustration, and image prompts inside the same benchmark family.
- Contribution 3: Reports how invalid moves and missed opportunities scale with game complexity and input format.

## 8. Main findings and failure modes
- Core empirical takeaway: simpler games such as Tic-Tac-Toe are handled more reliably, while Connect Four and Gomoku expose more invalid actions and missed winning chances.
- Notable model failure mode 1: higher disqualification and invalid-move rates under illustration and image prompts
- Notable model failure mode 2: weaker play as board complexity increases
- Notable model failure mode 3: prompt-format sensitivity even in deterministic perfect-information games
- Does this paper reveal a benchmark-design limitation as well? yes; it shows that benchmark outcomes in simple games can be driven heavily by representation choice

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Modest supporting example that games offer exact rule-verification and strategy probes.
- Best use in Section 1 (taxonomy and evolutionary levels): Useful as a narrow formal precursor rather than a main historical anchor. Clean example of perfect-information deterministic board-game benchmarking.
- Best use in Section 2 (core capabilities evaluated by games): Supports rule-following and simple strategic-planning discussion.
- Best use in Section 3 (interaction and evaluation paradigm): Helpful for prompt-format and visual-versus-symbolic interface comparisons. Useful for discussing invalid-move metrics and leaderboard design.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Supports the need for richer games once simple deterministic settings saturate.

## 10. Relation to nearby papers
- Closest predecessor(s): SmartPlay, GTBench, early board-game LLM evaluations
- Closest follow-up(s): broader formal suites and leaderboard benchmarks
- Best comparison targets inside our corpus: GTBench, GameBench, SmartPlay, TMGBench
- What this paper uniquely adds relative to neighbors: It isolates prompt-format effects very cleanly within a small family of board games.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- The benchmark uses Tic-Tac-Toe, Connect Four, and Gomoku with list, illustration, and image prompt formats.
- The study reports 2,310 simulated matches among leading LLMs and tracks invalid moves, disqualifications, and missed opportunities.
- The paper finds that list prompts are generally easiest, while illustration and image prompts lead to more failures.

### 11.2 Our synthesis / interpretation
- This is best treated as a narrow contrast case that clarifies the lower end of the design space.
- Its real survey value is methodological: it shows how much representation choice can matter even before moving to richer games.

### 11.3 Uncertain or needs re-check
- Re-check the exact tournament setup and whether the paper includes human or scripted baselines before using it in a calibration discussion.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? Probably only if we later need a clean prompt-format contrast example in the formal section.
- Which section to read next if needed: benchmark design / results
- Follow-up question(s): Is this benchmark better discussed as a rule-following probe or as a prompt-format study with game wrappers?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P2
- Reading depth: structured-skim
- Batch ID: B07
- Outline sections: 1,2,3
- Survey role: contrast
- Paper card path: `paper_cards/B07/GridBasedGameCompetitions.md`
- Next action: draft-section
- Last updated: 2026-04-08
