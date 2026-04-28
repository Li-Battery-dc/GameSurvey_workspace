# NetHackLearningEnvironment The NetHack Learning Environment

## 0. Metadata
- Date: 2020/06
- Venue: NeurIPS 2020 datasets and benchmarks
- Authors: Heinrich Kuttler, Nantas Nardelli, Alexander H. Miller, Roberta Raileanu, Marco Selvatici, Edward Grefenstette, Tim Rocktaschel
- Paper link: https://arxiv.org/pdf/2006.13760.pdf
- Code link: https://github.com/facebookresearch/nle
- Reading depth: deep
- Card status: finalized
- Confidence in this card: high
- Review gate label: usable

## 1. One-paragraph benchmark summary
- The NetHack Learning Environment adapts the classic terminal-based roguelike NetHack into a scalable research benchmark. The paper emphasizes that NetHack combines procedural generation, stochasticity, long horizons, hidden information, resource management, and rich symbolic observations in one difficult but efficiently simulated environment. NLE also provides a task suite, replay tooling, and RL baselines, making it both a benchmark and a long-term research platform rather than a lightweight one-off evaluation set. For this survey, NLE is a major historical precursor for long-horizon, partial-observability, and symbol-mediated game-agent evaluation.

## 2. Position in our survey
- Why-games relevance: NetHack compresses exploration, planning, survival, and partial observability into a single environment that is both hard and automatically evaluable.
- Historical stage: diagnostic capability probe
- Benchmark level(s): L2 strategic reasoning; single-world long-horizon general-agent precursor, not cross-title transfer evidence
- Most relevant outline section(s): 1,2,3,4
- Role in corpus: anchor

## 3. Design-space coding
### 3.1 Structure
- Form: World
- Construction: Wrapped
- Construction note: real game adapted into a research benchmark and task suite
- Benchmark unit: episode

### 3.2 Mechanics profile
- State visibility: partial
- Transition uncertainty: stochastic
- Actor configuration: single-agent
- Incentive structure: N/A
- Temporal regime: turn-based

### 3.3 Benchmark scope
- Scope: single game
- Number of games / tasks: 1 game plus an NLE task suite over procedurally generated runs

### 3.4 Modality
- Observation modality: text or symbolic
- Action modality: semantic / native-control primitive
- Perception burden retained: partial observability, inventory and resource tracking, spatial reasoning, and long-horizon planning
- Perception burden removed: rich graphics and low-level motor control

## 4. What this benchmark measures
- Primary capability target: long-horizon exploration and planning under stochastic partial observability
- Secondary capability target(s): skill acquisition, robustness, and systematic generalization in a difficult game world
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? yes
- Does it test social reasoning / deception / cooperation? no
- Does it test visual grounding / spatial-temporal reasoning? no in the modern visual-agent sense; it studies symbolic spatial reasoning instead
- Does it test long-horizon autonomy / task completion? yes
- Does it test real-time efficiency? no
- Does it test cross-game transfer / open-ended generalization? yes for within-environment systematic generalization over unseen seeds and roles, but not for cross-title transfer
- Why is a game environment especially suitable here? NetHack is rich enough to stress planning and exploration for years while still being cheap to simulate and precisely scored.

## 5. Interaction paradigm
- Observation channel: terminal-style text and symbolic game state
- Action channel: discrete NetHack actions
- Interface type: API / structured action space / hybrid
- Agent scaffold allowed: none in the benchmark core
- Is there privileged API access? yes through environment instrumentation and task suite wrappers
- How close is the setup to human play? medium-low; the original game is preserved, but benchmark wrappers expose machine-friendly arrays and task rewards
- Main ecological-validity trade-off: NLE preserves the difficulty structure of a real game while replacing most human-facing UI friction with symbolic observations and task-specific reward wrappers

## 6. Evaluation protocol
- Main score: task-suite performance and in-game progress
- Auxiliary score(s): baseline RL performance and qualitative agent analysis
- Evaluation style: native score / completion rate / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: distributed deep RL baselines and RND exploration baselines are the main comparison points; the paper references NAO human ascension streaks but does not run a controlled human baseline
- Automatic verifiability: high
- Calibration method: procedurally generated runs, held-out unseen seeds, a standardized task suite, and an explicit recommendation to report average score over 1000 unseen-seed episodes
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
- Best use in Section 0 (lead-in and benchmark motivation): Historical support for games as compact but difficult systems that combine exploration, planning, survival, sparse reward, partial observability, and long-horizon consequences.
- Best use in Section 1 (taxonomy and evolutionary levels): Anchor for the `World` / `Wrapped` / single-game branch of the taxonomy, especially the lineage from RL game environments to later LLM/VLM agent benchmarks; should not be presented as Level 4 visual play because the interface is symbolic terminal/API-mediated.
- Best use in Section 2 (core capabilities evaluated by games): Supports exploration, resource management, stochastic partial-observability, skill acquisition, memory, and systematic generalization over seeds and roles as distinct long-horizon capability targets.
- Best use in Section 3 (interaction and evaluation paradigm): Useful for the interface-privilege ladder: the full NetHack game dynamics are preserved, while observations, actions, task rewards, and replay tooling are exposed through a machine-friendly Gym interface.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Helps explain why hard single worlds require calibration beyond native score alone, including unseen-seed testing, task-suite subgoals, replay analysis, and caveats around score as only a proxy for solving the game.

## 10. Relation to nearby papers
- Closest predecessor(s): ALE, Obstacle Tower, BabyAI, classic roguelike RL environments
- Closest follow-up(s): later long-horizon symbolic-game and text-game evaluation platforms
- Best comparison targets inside our corpus: InteractiveFictionGames, TextQuests, Crafter, TextAtari
- What this paper uniquely adds relative to neighbors: It offers a real, procedurally generated hard game with long-horizon complexity, formal task wrappers, and machine-friendly symbolic observations.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- The paper presents NLE as a scalable, procedurally generated, stochastic, rich, and challenging environment based on NetHack.
- It explicitly motivates the environment as a medium for studying exploration, planning, skill acquisition, and language-conditioned RL.
- The default environment exposes symbolic observations such as glyphs, chars, colors, bottom-line stats, messages, and inventory tensors over 93 available actions.
- The paper provides a task suite and baseline deep RL results, emphasizing that only early-game success is currently demonstrated.
- NLE's full-game solution criterion is consecutive ascension on unseen seeds with randomized character attributes, but the paper recommends score-task comparisons as a nearer-term proxy.
- The paper requires future reports to specify character configuration, NetHack options, allowed actions, hard-coded action sequences, and training seeds, and to forbid test-time save scumming or RNG manipulation.
- Baseline experiments show progress on early tasks such as staircase, pet, eat, gold, score, scout, and oracle, with the oracle task remaining essentially unsolved by the reported agents.

### 11.2 Our synthesis / interpretation
- NLE is a useful historical anchor because it shows how a single hard game can function as a long-term benchmark platform.
- It is best used as a precursor and comparison target rather than as a direct peer to modern LLM benchmark papers.
- It should support the procedural-generalization and hard-world lineage, not claims about human-like multimodal interaction.
- Its symbolic observations and task wrappers make it strong evidence for single-world long-horizon evaluation, but weak evidence for raw visual grounding or native GUI play.

### 11.3 Uncertain or needs re-check
- Re-check the exact NLE task-suite composition and observation interfaces if we later compare it closely with parser-based text benchmarks.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? Audit completed from the full paper; reread only if we later need exact task definitions, observation tensors, or evaluation protocol details.
- Which section to read next if needed: Sections 2.2 to 2.5 and Appendix B to E
- Follow-up question(s): How should NLE be framed relative to text-only long-horizon benchmarks such as Jericho and TextQuests?

## 13. Registry sync
- Registry row synced: yes
- Registry status: finalized
- Priority: P1
- Reading depth: deep
- Batch ID: B05
- Outline sections: 1,2,3,4
- Survey role: anchor
- Paper card path: `paper_cards/B05/NetHackLearningEnvironment.md`
- Check status: unchecked
- Next action: draft-section
- Last updated: 2026-04-27
