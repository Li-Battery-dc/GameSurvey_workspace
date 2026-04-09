# NetHackLearningEnvironment The NetHack Learning Environment

## 0. Metadata
- Date: 2020/06
- Venue: NeurIPS 2020 datasets and benchmarks
- Authors: Heinrich Kuttler, Nantas Nardelli, Alexander H. Miller, Roberta Raileanu, Marco Selvatici, Edward Grefenstette, Tim Rocktaschel
- Paper link: https://arxiv.org/pdf/2006.13760.pdf
- Code link: https://github.com/facebookresearch/nle
- Reading depth: structured-skim
- Card status: card-reviewed
- Confidence in this card: medium
- Review gate label: usable

## 1. One-paragraph benchmark summary
- The NetHack Learning Environment adapts the classic terminal-based roguelike NetHack into a scalable research benchmark. The paper emphasizes that NetHack combines procedural generation, stochasticity, long horizons, hidden information, resource management, and rich symbolic observations in one difficult but efficiently simulated environment. NLE also provides a task suite and baseline results, making it both a benchmark and a long-term research environment. For this survey, NLE is a major historical precursor for long-horizon, partial-observability, and text or symbol-mediated game-agent evaluation.

## 2. Position in our survey
- Why-games relevance: NetHack compresses exploration, planning, survival, and partial observability into a single environment that is both hard and automatically evaluable.
- Historical stage: ecological agent benchmark
- Narrative level(s): L2 strategic reasoning / L5 cross-game generalization
- Most relevant outline section(s): 1,2,3,4
- Role in corpus: anchor

## 3. Design-space coding
### 3.1 Environment structure
- Information structure: imperfect
- Transition structure: stochastic
- Agent structure: single-agent
- Social structure: N/A
- Time structure: turn-based

### 3.2 World structure
- World type(s): adventure / other
- Real game / simulated game / designed task-game hybrid: real game adapted into a research benchmark and task suite
- Benchmark unit: episode

### 3.3 Benchmark scope
- Scope: procedural-infinite
- Number of games / tasks: 1 game plus an NLE task suite over procedurally generated runs
- Benchmark intent: train+eval foundation

### 3.4 Modality
- Primary modality: text / symbolic state
- Perception burden retained: partial observability, inventory and resource tracking, spatial reasoning, and long-horizon planning
- Perception burden removed: rich graphics and low-level motor control

## 4. What this benchmark measures
- Primary capability target: long-horizon exploration and planning under stochastic partial observability
- Secondary capability target(s): skill acquisition, robustness, and systematic generalization in a difficult game world
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? yes
- Does it test social reasoning / deception / cooperation? no
- Does it test visual grounding / spatial-temporal reasoning? partially
- Does it test long-horizon autonomy / task completion? yes
- Does it test real-time efficiency? no
- Does it test cross-game transfer / open-ended generalization? partially
- Why is a game environment especially suitable here? NetHack is rich enough to stress planning and exploration for years while still being cheap to simulate and precisely scored.

## 5. Interaction paradigm
- Observation channel: terminal-style text and symbolic game state
- Action channel: discrete NetHack actions
- Interface type: natural language / structured action space / hybrid
- Agent scaffold allowed: none in the benchmark core
- Is there privileged API access? yes through environment instrumentation and task suite wrappers
- How close is the setup to human play? medium; the original game is preserved, but benchmark wrappers expose machine-friendly state and tasks
- Main ecological-validity trade-off: NLE preserves the difficulty structure of a real game while simplifying perception relative to modern visual or embodied environments

## 6. Evaluation protocol
- Main score: task-suite performance and in-game progress
- Auxiliary score(s): baseline RL performance and qualitative agent analysis
- Evaluation style: native score / completion rate / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: distributed deep RL baselines and exploration baselines are the main comparison points
- Automatic verifiability: high
- Calibration method: procedurally generated runs and a standardized task suite
- Anti-contamination argument: not central
- Reliability or comparability concerns: NLE is primarily an RL benchmark, so direct comparison to language-model agents depends strongly on the chosen observation interface

## 7. Main contributions
- Contribution 1: Adapts NetHack into a scalable learning environment for AI research.
- Contribution 2: Provides a task suite and baseline results for a notoriously hard game.
- Contribution 3: Frames NetHack as an ideal medium for exploration, planning, skill acquisition, and language-conditioned RL.

## 8. Main findings and failure modes
- Core empirical takeaway: even strong distributed RL baselines make only early-stage progress, underscoring the environment's difficulty.
- Notable model failure mode 1: weak exploration in the face of sparse rewards and high stochasticity
- Notable model failure mode 2: difficulty sustaining long-horizon survival and planning
- Notable model failure mode 3: brittle systematic generalization across procedurally generated runs
- Does this paper reveal a benchmark-design limitation as well? yes; it is highly valuable as a hard benchmark, but it is not natively an LLM benchmark and so requires careful translation into the current survey frame

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Strong historical example of games as hard, multi-skill benchmark environments.
- Best use in Section 1 (taxonomy and evolutionary levels): Important precursor in the long-horizon game-agent lineage. Useful for procedural, single-game, terminal-mediated benchmarks.
- Best use in Section 2 (core capabilities evaluated by games): Supports exploration, planning, and long-horizon robustness claims.
- Best use in Section 3 (interaction and evaluation paradigm): Helpful contrast against later natural-language or GUI-heavy interfaces. Good reference for task-suite calibration in a single hard game.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Helps explain why later LLM-agent work often seeks more instrumented interfaces over similarly hard worlds.

## 10. Relation to nearby papers
- Closest predecessor(s): ALE, Obstacle Tower, BabyAI, classic roguelike RL environments
- Closest follow-up(s): Jericho-derived text-game benchmarks and later long-horizon game-agent evaluations
- Best comparison targets inside our corpus: InteractiveFictionGames, TextQuests, Crafter, MineNPCTask
- What this paper uniquely adds relative to neighbors: It offers a real, procedurally generated hard game with long-horizon complexity but without relying on rich visual interfaces.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- The paper presents NLE as a scalable, procedurally generated, stochastic, rich, and challenging environment based on NetHack.
- It explicitly motivates the environment as a medium for studying exploration, planning, skill acquisition, and language-conditioned RL.
- The paper provides a task suite and baseline deep RL results, emphasizing that only early-game success is currently demonstrated.

### 11.2 Our synthesis / interpretation
- NLE is a useful historical anchor because it shows how a single hard game can function as a long-term benchmark platform.
- It is best used as a precursor and comparison target rather than as a direct peer to modern LLM benchmark papers.

### 11.3 Uncertain or needs re-check
- Re-check the exact NLE task-suite composition and observation interfaces if we later compare it closely with parser-based text benchmarks.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? A targeted reread is worthwhile if we later want to position NLE more precisely in the historical-evolution section.
- Which section to read next if needed: task suite / environment design / baseline experiments
- Follow-up question(s): How should NLE be framed relative to text-only long-horizon benchmarks such as Jericho and TextQuests?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P1
- Reading depth: structured-skim
- Batch ID: B10
- Outline sections: 1,2,3,4
- Survey role: anchor
- Paper card path: `paper_cards/B10/NetHackLearningEnvironment.md`
- Next action: draft-section
- Last updated: 2026-04-08
