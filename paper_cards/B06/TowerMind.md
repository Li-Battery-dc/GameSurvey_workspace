# TowerMind TowerMind: A Tower Defence Game Learning Environment and Benchmark for LLM as Agents

## 0. Metadata
- Date: 2026/01
- Venue: arXiv
- Authors: Dawei Wang, Chengming Zhou, Di Zhao, Xinyuan Liu, Marci Chi Ma, Gary Ushaw, Richard Davison
- Paper link: https://arxiv.org/pdf/2601.05899v1
- Code link:
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: high
- Review gate label: strong

## 1. One-paragraph benchmark summary
- TowerMind is a lightweight tower-defense environment and benchmark for evaluating LLMs as real-time game agents. It keeps the RTS-style coupling of long-term planning and moment-to-moment action choice, but lowers deployment cost and exposes three observation modes: raw pixels, JSON-like textual state, and flattened structured state. The benchmark also explicitly measures invalid-action hallucination alongside task score and includes human and RL baselines. For this survey, TowerMind is a useful multimodal comparison point because it isolates planning, action validity, and privileged-state-interface trade-offs in a compact RTS-derived setting.

## 2. Position in our survey
- Why-games relevance: Tower-defense play creates measurable pressure on planning, timing, spatial allocation, and action validity inside a dynamic but still analyzable game loop.
- Historical stage: ecological agent benchmark
- Narrative level(s): L2 strategic reasoning / L4 visual agency
- Most relevant outline section(s): 3,4,5,6
- Role in corpus: representative

## 3. Design-space coding
### 3.1 Environment structure
- Information structure: perfect
- Transition structure: deterministic
- Agent structure: single-agent
- Social structure: N/A
- Time structure: real-time

### 3.2 World structure
- World type(s): RTS / tower defense
- Real game / simulated game / designed task-game hybrid: designed task-game hybrid built as a research environment
- Benchmark unit: episode

### 3.3 Benchmark scope
- Scope: single game
- Number of games / tasks: 5 benchmark levels in one tower-defense environment
- Benchmark intent: diagnostic evaluation

### 3.4 Modality
- Primary modality: mixed
- Perception burden retained: real-time spatial state interpretation, map reading, timing, and tactical response
- Perception burden removed: textual and structured state formats expose game-state semantics more directly than raw human play

## 4. What this benchmark measures
- Primary capability target: long-term planning plus real-time decision-making in an RTS-derived environment
- Secondary capability target(s): action validity, multimodal understanding, spatial reasoning, and resistance to misleading cues
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? partially
- Does it test social reasoning / deception / cooperation? no
- Does it test visual grounding / spatial-temporal reasoning? yes
- Does it test long-horizon autonomy / task completion? yes
- Does it test real-time efficiency? yes
- Does it test cross-game transfer / open-ended generalization? no
- Why is a game environment especially suitable here? The tower-defense format forces repeated allocation and timing decisions while preserving precise automatic scoring and invalid-action checks.

## 5. Interaction paradigm
- Observation channel: 512x512 RGB frames, textual JSON-like state, or flattened structured state
- Action channel: hybrid action vector with continuous coordinates plus a discrete action type
- Interface type: API / structured action space / hybrid
- Agent scaffold allowed: none
- Is there privileged API access? yes
- How close is the setup to human play? medium; the game loop is human-like, but the text and structured-state interfaces expose privileged semantics
- Main ecological-validity trade-off: TowerMind keeps RTS-like pressure but gains tractability by exposing state in machine-friendly formats and by using a simplified single-player tower-defense setting

## 6. Evaluation protocol
- Main score: environment reward / score normalized to the human baseline
- Auxiliary score(s): valid action rate, per-level normalized performance, RL baseline scores
- Evaluation style: native score / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: five human experts, multiple commercial and open-source LLMs, plus Ape-X DQN and PPO baselines
- Automatic verifiability: high
- Calibration method: five benchmark levels, five random seeds per model, shared zero-shot prompts, and separate language-only versus vision-language settings
- Anti-contamination argument: custom level editing and benchmark customizability are presented as ways to vary tasks and reduce contamination pressure
- Reliability or comparability concerns: results depend strongly on whether the model sees raw vision or privileged state representations, so the benchmark mixes ecological and diagnostic settings

## 7. Main contributions
- Contribution 1: Introduces a lightweight tower-defense environment for LLM and RL evaluation with multimodal observations.
- Contribution 2: Adds hallucination-oriented evaluation through explicit invalid-action tracking.
- Contribution 3: Releases customizable levels and level-editing support for future benchmark variation.

## 8. Main findings and failure modes
- Core empirical takeaway: commercial models outperform open models, but all tested LLMs remain far below human experts on both score and action reliability.
- Notable model failure mode 1: models often choose strategically useless tower placements when levels contain misleading tower points
- Notable model failure mode 2: models rarely show multifinal decision-making, such as combining movement and reward collection efficiently
- Notable model failure mode 3: smaller open models produce many invalid or context-inconsistent actions, especially on harder levels
- Does this paper reveal a benchmark-design limitation as well? yes; the benchmark is informative partly because it exposes a large gap between correctness of legal actions and effectiveness of those actions

## 9. Why this paper matters for our survey
- Best use in Section 0 (why games): Shows why a compact RTS-derived environment can still expose clear planning gaps in frontier models.
- Best use in Section 1 (historical evolution): Useful as a later specialized branch of RTS-style LLM evaluation.
- Best use in Section 2 (design space): Good case for comparing raw-vision, text-state, and structured-state interfaces inside one benchmark.
- Best use in Section 3 (capability targets): Strong evidence on planning, spatial reasoning, and hallucination under dynamic play.
- Best use in Section 4 (interaction paradigm): Useful when discussing privileged observations versus human-like perceptual burden.
- Best use in Section 5 (evaluation protocol): Helpful for the distinction between task performance and valid-action reliability.
- Best use in Section 6/7 (limitations and future): Supports the claim that many agent failures are not only illegal-action failures but also ineffective-action failures.

## 10. Relation to nearby papers
- Closest predecessor(s): RTS-style LLM benchmarks such as TextStarCraft II and LLM-PySC2
- Closest follow-up(s): later visual and ecological game-agent benchmarks that compare multiple input interfaces
- Best comparison targets inside our corpus: [Balrog](D:/research_root/GameSurvey/workspace/paper_cards/B03/Balrog.md), [StarBench](D:/research_root/GameSurvey/workspace/paper_cards/B03/StarBench.md), [PillagerBench](D:/research_root/GameSurvey/workspace/paper_cards/B04/PillagerBench.md), [LMGameBench](D:/research_root/GameSurvey/workspace/paper_cards/B08/LMGameBench.md)
- What this paper uniquely adds relative to neighbors: It combines RTS-like planning pressure with an explicit hallucination metric and side-by-side privileged-state versus vision settings.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- TowerMind is a Unity and ML-Agents-based tower-defense environment with pixel, textual, and structured observations.
- Each action combines two continuous coordinates with one discrete action type, and the benchmark records both score and valid action rate.
- The paper evaluates commercial and open-source LLMs on five levels, compares language-only and vision-language settings, and also reports Ape-X DQN and PPO baselines.

### 11.2 Our synthesis / interpretation
- TowerMind is more useful as a diagnostic multimodal RTS comparison than as a central survey anchor, because its strongest contribution is how cleanly it exposes interface and hallucination trade-offs.
- It is a good example of a benchmark where legality and usefulness diverge, which helps sharpen the survey’s evaluation-protocol discussion.

### 11.3 Uncertain or needs re-check
- If we later need the exact per-level human-normalized scores or the formal level-difficulty equation, re-check Sections 4.2 to 4.3 and Appendix C.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? No immediate reread is required; the benchmark setup, interfaces, and main findings are already clear enough for synthesis.
- Which section to read next if needed: 3.2 / 4.3 / Appendix B
- Follow-up question(s): When we compare multimodal game benchmarks, should TowerMind be grouped with privileged-state diagnostics or with more ecological raw-visual agents?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P2
- Reading depth: deep
- Batch ID: B06
- Outline sections: 3,4,5,6
- Survey role: representative
- Paper card path: `paper_cards/B06/TowerMind.md`
- Next action: draft-section
- Last updated: 2026-04-05
