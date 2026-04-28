# GameVerse GameVerse: Can VLMs Learn from Video-based Reflection?

## 0. Metadata
- Date: 2026/03
- Venue: arXiv
- Authors: Kuan Zhang, Dongchen Liu, Qiyue Zhao, Jinkun Hou, Xinran Zhang, Qinlei Xie, Miao Liu, Yiming Li
- Paper link: https://arxiv.org/pdf/2603.06656v2
- Code link: https://github.com/THUSI-Lab/GameVerse
- Reading depth: deep
- Card status: finalized
- Confidence in this card: high
- Review gate label: strong

## 1. One-paragraph benchmark summary
- GameVerse is a 15-game VLM benchmark built around a reflect-and-retry gameplay loop rather than one-shot play. During gameplay, agents act from current screenshots using GUI or semantic actions; after failure, they compare their own failure trajectory with expert tutorial videos, generate reflections, and retry with those reflections injected into the prompt. The benchmark mixes intrinsic and milestone-based scoring and compares VLMs against random, human rookie, and human expert baselines. It matters for the survey because it tests whether video-based reflection actually improves visually grounded gameplay and how that improvement depends on model strength, control mode, and game complexity.

## 2. Position in our survey
- Why-games relevance: It uses games to couple perception, action, and post-hoc self-improvement in a way static video benchmarks cannot.
- Historical stage: ecological agent benchmark
- Benchmark level(s): L4 visual agency / L5 cross-game generalization
- Most relevant outline section(s): 1,2,3,4
- Role in corpus: representative

## 3. Design-space coding
### 3.1 Structure
- Form: Mixed
- Construction: Wrapped
- Construction note: suite of real/popular games run through a benchmark harness with visual observations, GUI controls for all games, semantic controls for selected games, and no internal state API for the visual play loop
- Benchmark unit: episode

### 3.2 Mechanics profile
- State visibility: mixed
- Transition uncertainty: mixed
- Actor configuration: single-agent
- Incentive structure: N/A
- Temporal regime: hybrid

### 3.3 Benchmark scope
- Scope: curated suite
- Number of games / tasks: 15 games

### 3.4 Modality
- Observation modality: mixed
- Action modality: mixed
- Perception burden retained: screenshot-based gameplay, GUI consequences, failure trajectories, and expert tutorial videos for reflection
- Perception burden removed: internal game state access

## 4. What this benchmark measures
- Primary capability target: visually grounded play plus reflection-driven improvement
- Secondary capability target(s): cross-game transfer, memory use, milestone completion, action refinement
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? yes
- Does it test social reasoning / deception / cooperation? no
- Does it test visual grounding / spatial-temporal reasoning? yes
- Does it test long-horizon autonomy / task completion? yes
- Does it test real-time efficiency? partially
- Does it test cross-game transfer / open-ended generalization? partially
- Why is a game environment especially suitable here? Games produce meaningful failure trajectories and expert demonstrations that make reflection measurable in a closed loop.

## 5. Interaction paradigm
- Observation channel: current screenshot plus recent action context during play; selected settings also add memory, and reflection uses failure plus expert videos
- Action channel: semantic or native control depending on the game
- Interface type: hybrid
- Agent scaffold allowed: reflection; five games additionally use a memory-aware agent
- Is there privileged API access? no
- How close is the setup to human play? medium; the agent sees real visual trajectories, but the reflection loop is more explicitly instrumented than normal play
- Main ecological-validity trade-off: GameVerse preserves visual interaction and retry behavior, but reflection is injected as prompt text in a single-turn loop rather than learned or interactive adaptation

## 6. Evaluation protocol
- Main score: normalized 100-point score
- Auxiliary score(s): intrinsic game scores, milestone completion, reflection gains versus no-reflection mode, semantic-vs-GUI gaps, and latency-aware comparisons
- Evaluation style: hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: random baseline, human rookie, and human expert comparisons
- Automatic verifiability: medium to high
- Calibration method: intrinsic scoring for 8 games, VLM-based milestone scoring for 7 games, and manual verification of milestones and reported metrics
- Anti-contamination argument: not central; the paper motivates games as a fresher alternative to static datasets but does not treat contamination as its main benchmark claim
- Reliability or comparability concerns: milestone extraction relies on a stronger VLM and manual checking, while reflection gains vary sharply by model strength, action mode, and cognitive category

## 7. Main contributions
- Contribution 1: Introduces a 15-game VLM benchmark organized by a cognitive taxonomy.
- Contribution 2: Adds a video-based reflection and retry protocol rather than fire-and-forget evaluation.
- Contribution 3: Compares failure-only, tutorial-only, and combined reflection sources.

## 8. Main findings and failure modes
- Core empirical takeaway: Reflection usually helps, but the gains concentrate in stronger models and less demanding settings, while humans remain far more robust across the 15-game suite.
- Notable model failure mode 1: weak models fail to internalize useful reflections even when better tutorials are available
- Notable model failure mode 2: gains shrink sharply as cognitive complexity, latency pressure, and real-time demands rise
- Notable model failure mode 3: the semantic-vs-GUI gap shows that high-level reasoning often fails to translate into low-level execution
- Does this paper reveal a benchmark-design limitation as well? yes; the milestone pipeline relies on a stronger VLM and the reflection loop remains a single-turn, prompt-injected intervention

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Strong example of why games expose closed-loop learning demands that static video QA cannot: agents must act from pixels, fail, inspect their trajectory against tutorials, and retry.
- Best use in Section 1 (taxonomy and evolutionary levels): Level 5 curated-suite evidence for cross-game visual-agent evaluation. It should be presented as a fixed 15-game suite with five cognitive categories and three difficulty tiers, not as generated benchmark growth.
- Best use in Section 2 (core capabilities evaluated by games): Useful for Level 4/5 claims about visual grounding, planning, reflection-driven adaptation, and the fact that generalization collapses from easy grid tasks to hard real-time/open-world tasks.
- Best use in Section 3 (interaction and evaluation paradigm): Important example of reflection as an inference-time scaffold and of mixed evaluation: 8 games use intrinsic scores while 7 harder games use VLM-extracted, manually verified milestones from expert videos.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Supports the knowing-doing gap: semantic control averages above GUI control, reflection helps stronger models more, and failures decompose into perception, reasoning, execution, and latency errors.

## 10. Relation to nearby papers
- Closest predecessor(s): visual game-agent suites such as VideoGameBench and BALROG, plus prior tutorial- or reflection-based agent studies
- Closest follow-up(s): StarBench and FlashAdventure as comparison cases for control fidelity and long-horizon native-control play, though not direct reflection benchmarks
- Best comparison targets inside our corpus: AIGameStore, GVGAILLM, Orak, LMGameBench
- What this paper uniquely adds relative to neighbors: It explicitly evaluates reflect-and-retry, dual action spaces, and latency-aware degradation rather than only one-shot control or passive visual understanding.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- GameVerse covers 15 games across five cognitive categories: Tic-Tac-Toe/Baba Is You/2048, Maze/Angry Birds/Slay the Spire, Ace Attorney/Civilization VI/Scene Investigators, Snake/Plants vs. Zombies/Forza Horizon 5, and Mini Metro/Genshin Impact/Red Dead Redemption 2.
- The benchmark evaluates seven VLMs, plus random, human rookie, and human expert baselines; the human baseline study uses 37 participants and 458 gameplay sessions.
- During play, agents act from screenshots using GUI actions for all games and semantic actions for selected games; ten games use a zero-shot agent and five longer/story/open-world games use a memory-aware agent.
- Video-based reflection records a failure trajectory, retrieves an expert walkthrough/tutorial, asks the VLM to contrast failure against expert video, and injects the resulting reflection into the retry prompt.
- Scores are normalized to a 100-point scale, combining intrinsic scoring for 8 games with milestone scoring for 7 harder games; the milestone pipeline uses an advanced VLM and manual verification.
- The paper reports that stronger models gain more from reflection, while gains fall as cognitive difficulty, GUI demands, and real-time pressure increase; semantic control outperforms GUI control on the compared games.
- The paper classifies failures into perception, reasoning, execution, and latency errors.

### 11.2 Our synthesis / interpretation
- GameVerse is useful less as proof that reflection solves visual gameplay and more as evidence that reflection itself is capability-dependent and scaffold-sensitive.
- It helps bridge interaction design and synthesis because it connects tutorial-based scaffolds to persistent brittleness in grounding, latency, and internalization.
- In the Level 5 narrative, it should support cross-game visual-agent breadth and reflective retry, not open-ended/generative benchmark expansion.

### 11.3 Uncertain or needs re-check
- Appendix D is very large; only targeted game details were checked for failure-mode and memory-agent claims. Recheck Appendix D if citing exact per-game prompt templates or raw scores.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? No immediate reread; the reflection protocol and main findings are already usable.
- Which section to read next if needed: Benchmark / Experiment / Appendix A
- Follow-up question(s): Should reflection be treated in the survey as an interaction scaffold, an evaluation intervention, or both?

## 13. Registry sync
- Registry row synced: yes
- Registry status: finalized
- Priority: P1
- Reading depth: deep
- Batch ID: B06
- Outline sections: 1,2,3,4
- Survey role: representative
- Paper card path: `paper_cards/B06/GameVerse.md`
- Check status: unchecked
- Next action: draft-section
- Last updated: 2026-04-27
