# INGVP ING-VP: MLLMs cannot Play Easy Vision-based Games Yet

## 0. Metadata
- Date: 2024/10
- Venue: arXiv
- Authors: Haoran Zhang, Hangyu Guo, Shuyue Guo, Meng Cao, Wenhao Huang, Jiaheng Liu, Ge Zhang
- Paper link: https://arxiv.org/pdf/2410.06555v1.pdf
- Code link: https://github.com/Thisisus7/ING-VP
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: high
- Review gate label: strong

## 1. One-paragraph benchmark summary
- ING-VP is a diagnostic benchmark built around six simple-but-planning-heavy games, each with 50 levels, to test whether MLLMs can solve basic spatial-planning games from either visual states or text-state representations. The paper systematically varies inference conditions across one-step versus multi-step reasoning, image-based versus text-only state input, and with-versus-without history, making it possible to isolate where failures arise. Most levels are algorithmically generated and verified, and the benchmark evaluates completion with accuracy, completion degree, and action efficiency rather than only final success. For this survey, ING-VP is a strong lower-bound benchmark: if models fail badly here, claims about robust visual game agency need to be treated cautiously.

## 2. Position in our survey
- Why-games relevance: Even tiny game worlds can expose the interaction between perception, planning, and repeated action selection better than one-shot reasoning tasks.
- Historical stage: diagnostic capability probe
- Benchmark level(s): L2 strategic reasoning / L4 visual agency
- Most relevant outline section(s): 2,3,4
- Role in corpus: contrast

## 3. Design-space coding
### 3.1 Game structure
- Information structure: mixed
- Transition structure: deterministic
- Agent structure: single-agent
- Social structure: N/A
- Time structure: turn-based

### 3.2 Environment structure
- Environment type(s): abstract puzzle
- Real game / simulated game / designed task-game hybrid: designed task-game suite
- Benchmark unit: level episode

### 3.3 Benchmark scope
- Scope: curated suite
- Number of games / tasks: 6 games with 50 levels each, for 300 levels total

### 3.4 Modality
- Observation modality: mixed
- Action modality: semantic
- Perception burden retained: image interpretation in the visual settings, grid understanding, and state tracking
- Perception burden removed: worlds are simple and discrete, with limited action spaces and no real-time pressure

## 4. What this benchmark measures
- Primary capability target: combined visual perception and planning in simple sequential games
- Secondary capability target(s): memory of prior states, benefit of history, and effect of multi-step prompting
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? no
- Does it test social reasoning / deception / cooperation? no
- Does it test visual grounding / spatial-temporal reasoning? yes
- Does it test long-horizon autonomy / task completion? limited
- Does it test real-time efficiency? no
- Does it test cross-game transfer / open-ended generalization? partially
- Why is a game environment especially suitable here? The tasks are simple enough that poor performance cannot easily be blamed on large action spaces or natural-language ambiguity alone.

## 5. Interaction paradigm
- Observation channel: either image states or textual state descriptions, plus game instructions and optionally prior dialogue history
- Action channel: move choices for each game step
- Interface type: natural language / structured action space / hybrid
- Agent scaffold allowed: history / undo option in selected with-history settings
- Is there privileged API access? yes in the text-only comparison settings; no in the image-state settings
- How close is the setup to human play? low to medium; the games are intentionally simplified for diagnosis
- Main ecological-validity trade-off: ING-VP sacrifices realism to make perception and planning failures easy to localize

## 6. Evaluation protocol
- Main score: task completion accuracy
- Auxiliary score(s): completion degree and action efficiency
- Evaluation style: completion rate / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: multiple MLLMs are evaluated across six controlled prompting conditions; the paper discusses human ease qualitatively rather than reporting a full formal human benchmark table
- Automatic verifiability: high
- Calibration method: 50 levels per game, fixed settings, and six experimental condition variants
- Anti-contamination argument: most levels are algorithmically generated and verified, and the benchmark modifies tasks such as N-Queens so models cannot solve them purely by memorized templates
- Reliability or comparability concerns: because the games are deliberately easy and capped at short solution lengths, failure tells us more about basic competence gaps than about rich ecological play; the benchmark also omits difficulty grading

## 7. Main contributions
- Contribution 1: Builds a 300-level benchmark around six simple visual planning games.
- Contribution 2: Compares image-text and text-only play, one-step and multi-step prompting, and the effect of history.
- Contribution 3: Documents pervasive failure and looping even on easy game instances.

## 8. Main findings and failure modes
- Core empirical takeaway: current MLLMs perform very poorly even on easy vision-based planning games, with the best model reaching only 3.37% accuracy overall.
- Notable model failure mode 1: repeated looping and action repetition
- Notable model failure mode 2: poor visual parsing of relative positions, even when objects themselves are recognized
- Notable model failure mode 3: multi-step prompting does not reliably help and can sometimes hurt
- Does this paper reveal a benchmark-design limitation as well? yes; it shows that apparent reasoning improvements can disappear once evaluation requires persistent action rather than one-shot answers

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Useful for showing that game interaction reveals failures hidden by static reasoning tests.
- Best use in Section 1 (taxonomy and evolutionary levels): Fits the diagnostic phase of multimodal game benchmarking. Good example of a deliberately simplified visual-planning task suite rather than a full visual-agency benchmark.
- Best use in Section 2 (core capabilities evaluated by games): Strong evidence for separating perception and planning bottlenecks.
- Best use in Section 3 (interaction and evaluation paradigm): Helpful contrast to richer video-game interfaces because the world is intentionally stripped down. Useful for discussing factorized evaluation across modality and history settings.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Supports the claim that basic sequential control remains unresolved even before ecological realism is introduced.

## 10. Relation to nearby papers
- Closest predecessor(s): SmartPlay, AtariGPT, GameTraversalBenchmark
- Closest follow-up(s): LVLMGamePlayers, VGRPBench, MazeEval
- Best comparison targets inside our corpus: LVLMGamePlayers, Balrog, GameplayQA, StarBench
- What this paper uniquely adds relative to neighbors: It uses very easy games to argue that the floor of multimodal sequential decision-making is still low.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- ING-VP contains six games with 50 levels each and evaluates 300 levels total: Sokoban, Maze, Sudoku, 8-queens, Tower of Hanoi, and 15-puzzle.
- The benchmark compares six settings formed by image-state versus text-only input, one-step versus multi-step reasoning, and with-versus-without history in the multi-step setting.
- The paper reports accuracy, completion degree, and action efficiency, and finds that models often loop or repeatedly choose ineffective actions.

### 11.2 Our synthesis / interpretation
- ING-VP is especially valuable as a lower-bound benchmark: if models fail here, claims about robust visual game agency should be treated cautiously.
- It supports the survey’s argument that simpler games can still be revealing when the protocol is well controlled.
- Its strongest survey role is as a Section 3 contrast case for modality ablations and history ablations, not as an ecological visual-agent anchor.

### 11.3 Uncertain or needs re-check
- Re-check the per-game condition table in Appendix C if we later need a table-ready statement about which games benefit most from text-only versus image-state input.
- Re-check whether the omission of previous images in with-history settings should be foregrounded when comparing ING-VP to other history-enabled benchmarks.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? Already done for this audit; further rereading is only needed if the draft later needs the per-game Appendix C tables or prompt details.
- Which section to read next if needed: Section 4.3 and Appendix C for per-game setting breakdowns and prompt wording
- Follow-up question(s): Which comparison best shows that text-state access helps more than step-by-step decomposition?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P2
- Reading depth: deep
- Batch ID: B04
- Outline sections: 2,3,4
- Survey role: contrast
- Paper card path: `paper_cards/B04/INGVP.md`
- Check status: unchecked
- Last updated: 2026-04-10
