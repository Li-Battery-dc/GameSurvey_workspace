# SmartPlay: A BENCHMARK FOR LLMS AS INTELLIGENT AGENTS

## 0. Metadata
- Date: 2023/10
- Venue: ICLR 2024
- Authors: Yue Wu, Xuan Tang, Tom M. Mitchell, Yuanzhi Li
- Paper link: https://arxiv.org/pdf/2310.01557v5
- Code link: https://github.com/microsoft/SmartPlay
- Reading depth: deep
- Card status: finalized
- Confidence in this card: high
- Review gate label: strong

## 1. One-paragraph benchmark summary
- SmartPlay is an early multi-game benchmark built specifically for evaluating LLMs as interactive agents rather than static text reasoners. It combines six games and up to twenty settings, ranging from simple stochastic decision tasks to long-horizon planning and spatial reasoning environments such as Crafter and Minecraft. The benchmark converts each environment into text observations plus manuals and history, then asks the model to choose from a flat action set. Its main value for this survey is that it explicitly decomposes agent competence into reusable capability axes instead of only reporting overall win rates.

## 2. Position in our survey
- Why-games relevance: It makes the case that games expose planning, randomness, memory, and spatial reasoning in ways static QA benchmarks miss.
- Historical stage: diagnostic capability probe
- Benchmark level(s): L1 rule understanding / L2 strategic reasoning
- Most relevant outline section(s): 0,1,2,3
- Role in corpus: anchor

## 3. Design-space coding
### 3.1 Structure
- Form: Mixed
- Construction: Wrapped
- Construction note: curated suite of adapted existing games and task-games
- Benchmark unit: episode

### 3.2 Mechanics profile
- State visibility: mixed
- Transition uncertainty: mixed
- Actor configuration: single-agent
- Incentive structure: N/A
- Temporal regime: turn-based

### 3.3 Benchmark scope
- Scope: curated suite
- Number of games / tasks: 6 games, up to 20 settings, infinite environment variations

### 3.4 Modality
- Observation modality: text or symbolic
- Action modality: semantic
- Perception burden retained: spatial relations, action history, manual following, stochastic tracking through textualized observations
- Perception burden removed: raw pixels, low-level motor control, full human-like native control

## 4. What this benchmark measures
- Primary capability target: rule-grounded agent competence across planning, memory, randomness, and spatial reasoning
- Secondary capability target(s): long-horizon planning, learning from interaction, error recovery, cross-setting generalization
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? yes
- Does it test social reasoning / deception / cooperation? no
- Does it test visual grounding / spatial-temporal reasoning? partially, through textualized spatial descriptions
- Does it test long-horizon autonomy / task completion? yes
- Does it test real-time efficiency? no
- Does it test cross-game transfer / open-ended generalization? partially
- Why is a game environment especially suitable here? The suite can isolate different agent skills while still preserving sequential decision making and automatically checkable outcomes.

## 5. Interaction paradigm
- Observation channel: text manual + current observation + bounded history
- Action channel: flat categorical game actions expressed as text labels
- Interface type: natural language / structured action space
- Agent scaffold allowed: none
- Is there privileged API access? yes
- How close is the setup to human play? low to medium; game dynamics remain intact but perception and control are heavily simplified
- Main ecological-validity trade-off: The benchmark broadens coverage cheaply by converting 2D/3D play into text, but that removes raw perception and fine-grained action control.

## 6. Evaluation protocol
- Main score: game-specific score, with cross-game comparison reported through human-normalized scores
- Auxiliary score(s): reward, completion rate
- Evaluation style: native score / completion rate / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: multi-model comparison with a small human baseline used for normalized aggregate reporting
- Automatic verifiability: high
- Calibration method: fixed per-game interface parameters and rollout lengths, repeated trials for stochastic games, and optional human-normalized aggregation for cross-game comparison
- Anti-contamination argument: procedurally generated states and large state spaces reduce simple memorization
- Reliability or comparability concerns: textualization choices, history length, and fixed action abstractions change difficulty across games, and the human baseline is small

## 7. Main contributions
- Contribution 1: Defines nine capability axes for LLM agents and maps each game to them.
- Contribution 2: Packages six heterogeneous games behind a unified Gym-like text interface.
- Contribution 3: Reports game-native metrics plus human-normalized aggregate comparisons that expose where current LLM agents still break down.

## 8. Main findings and failure modes
- Core empirical takeaway: GPT-4-class models outperform smaller models but still fall clearly below human baselines on the harder planning and spatial environments.
- Notable model failure mode 1: brittle long-horizon planning in Tower of Hanoi and Crafter
- Notable model failure mode 2: weak 3D spatial reasoning in the Minecraft setting
- Notable model failure mode 3: poor state tracking and recovery after intermediate mistakes
- Does this paper reveal a benchmark-design limitation as well? yes; textifying visual worlds helps measurement but weakens ecological validity

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Direct support for the static-to-interactive evaluation gap: the paper argues that static benchmarks miss long-horizon planning, probabilistic events, spatial reasoning, and learning from interaction, while games provide objectives and feedback that unfold through action.
- Best use in Section 1 (taxonomy and evolutionary levels): Anchor for the transition from Level 1 rule-grounded participation to Level 2 diagnostic agent evaluation. It is a curated mixed-form suite whose text observations, manuals, bounded history, and flat action sets show how early LLM-agent benchmarks converted heterogeneous games into controlled evaluation objects.
- Best use in Section 2 (core capabilities evaluated by games): Strong evidence that game suites can decompose capability targets rather than only report aggregate scores: SmartPlay maps six games to nine capabilities including rule following, planning, odds, learning from interaction, error handling, and 2D/3D spatial reasoning.
- Best use in Section 3 (interaction and evaluation paradigm): Core example of a high-privilege textification pipeline. It fixes manuals, history windows, rollout lengths, action spaces, and trials, then reports reward/completion/score metrics plus human-normalized aggregation; use it to explain how diagnostic clarity trades off against human-like perception and control.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Supports bottleneck claims that even GPT-4-class agents remain far from human baselines on planning, recovery, Crafter-style concurrent objectives, and Minecraft-style 3D spatial navigation, while also showing that textified success is not ecological competence.

## 10. Relation to nearby papers
- Closest predecessor(s): Crafter and Messenger as component environments, plus earlier text-game and general-agent evaluation lines
- Closest follow-up(s): BotzoneBench, BALROG, Orak
- Best comparison targets inside our corpus: BoardGameArena, BotzoneBench, GTBench, LLMChess
- What this paper uniquely adds relative to neighbors: It is one of the clearest early attempts to turn heterogeneous games into a capability-decomposed LLM-agent benchmark.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- SmartPlay contains six games and up to twenty settings with infinite environment variations.
- The paper defines nine capability dimensions and uses a unified OpenAI Gym-like interface with text observations, manuals, bounded history, and flat categorical actions.
- The benchmark defines three native metrics: reward, completion rate, and score; human-normalized scores are used later for cross-game comparison in the results.
- The human baseline is collected from three experienced players using the SmartPlay interface.
- Table 1 fixes per-game inputs, manuals, history lengths, rollout lengths, action spaces, and trial counts; the paper explicitly says changes to these settings should be stated.
- The paper reports GPT-4 variants still underperform human baselines on harder settings, including substantial gaps on Hanoi, Crafter, and Minecraft creative navigation.

### 11.2 Our synthesis / interpretation
- SmartPlay is a strong historical anchor because it treats games as a structured probe of agentic skill rather than only as a leaderboard.
- Its design is best read as high diagnostic control with intentionally reduced ecological realism.

### 11.3 Uncertain or needs re-check
- Recheck Table 1 and the appendix if we later need exact per-environment history windows or the precise human-normalization formula.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? Completed in this audit; the core setup, interface, metrics, and appendix baseline details are now clear enough for survey use.
- Which section to read next if needed: 4.1 / 4.2 / Appendix D
- Follow-up question(s): If we quote exact cross-game human gaps, which table should anchor the comparison?

## 13. Registry sync
- Registry row synced: yes
- Registry status: finalized
- Priority: P0
- Reading depth: deep
- Batch ID: B01
- Outline sections: 0,1,2,3
- Survey role: anchor
- Paper card path: `paper_cards/B01/SmartPlay.md`
- Check status: unchecked
- Next action: draft-section
- Last updated: 2026-04-27
