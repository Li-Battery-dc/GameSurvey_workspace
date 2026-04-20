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
- TowerMind is a lightweight tower-defense environment built to benchmark LLMs on long-term planning and real-time decision-making in an RTS-derived setting. It supports three observation modes - raw pixels, JSON-formatted textual state, and flattened structured state - and evaluates both task score and valid action rate, treating invalid actions as hallucination-like failures. The environment also adds moving fog of war, misleading tower points, and random gold drops, so the task is not purely deterministic even though the map layout is fixed. For this survey, TowerMind is best used as a compact diagnostic benchmark for interface trade-offs, action validity, and effectiveness under dynamic play, not as a close proxy for fully human-like RTS play.

## 2. Position in our survey
- Why-games relevance: Tower-defense play creates repeated, automatically scored decisions about spatial allocation, timing, and resource use inside a dynamic game loop where legality and usefulness can diverge.
- Historical stage: diagnostic capability probe
- Benchmark level(s): L2 strategic reasoning / L4 visual agency
- Most relevant outline section(s): 2,3,4
- Role in corpus: representative

## 3. Design-space coding
### 3.1 Game structure
- Information structure: imperfect
- Transition structure: mixed
- Agent structure: single-agent
- Social structure: N/A
- Time structure: real-time

### 3.2 World structure
- World type(s): RTS
- Real game / simulated game / designed task-game hybrid: designed task-game hybrid built as a research environment
- Benchmark unit: episode

### 3.3 Benchmark scope
- Scope: single game
- Number of games / tasks: 5 built-in benchmark levels in one tower-defense environment

### 3.4 Modality
- Observation modality: mixed
- Action modality: native control
- Perception burden retained: real-time map reading, timing pressure, spatial allocation, partial observability from moving fog of war, and action-outcome coupling
- Perception burden removed: textual and structured modes expose privileged game-state semantics that humans do not receive directly

## 4. What this benchmark measures
- Primary capability target: long-term planning and real-time decision-making under dynamic, partially observable play
- Secondary capability target(s): action validity, multimodal state understanding, spatial allocation, and resistance to misleading affordances
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? yes
- Does it test social reasoning / deception / cooperation? no
- Does it test visual grounding / spatial-temporal reasoning? yes
- Does it test long-horizon autonomy / task completion? yes
- Does it test real-time efficiency? yes
- Does it test cross-game transfer / open-ended generalization? no
- Why is a game environment especially suitable here? The tower-defense format forces repeated decisions about where, when, and how to act while preserving automatic scoring and explicit checks for invalid actions.

## 5. Interaction paradigm
- Observation channel: 512 x 512 x 3 pixel observations, JSON-formatted textual state, or flattened structured state; units and enemies hidden by fog of war are removed from observations
- Action channel: a hybrid action vector `(x, y, c)` with continuous 2D coordinates and one discrete action type over 12 actions
- Interface type: API / structured action space / hybrid
- Agent scaffold allowed: none
- Is there privileged API access? yes
- How close is the setup to human play? low to medium; the raw-pixel mode is closer to human play, but the text and structured-state modes expose privileged semantics
- Main ecological-validity trade-off: TowerMind preserves a real-time RTS-like control problem while simplifying the domain to single-player tower defense and offering machine-friendly state formats

## 6. Evaluation protocol
- Main score: raw environment score / reward, ranging from -20 to 0 in the benchmark levels
- Auxiliary score(s): valid action rate, level-wise score normalized against the human baseline in reported tables, and a separate RL benchmark with Ape-X DQN and PPO
- Evaluation style: native score / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: five human experts establish the main baseline; commercial and open LLMs are evaluated zero-shot under language-only and vision-language settings; Ape-X DQN and PPO are reported separately as RL baselines
- Automatic verifiability: high
- Calibration method: five built-in benchmark levels with an explicit difficulty metric, five random seeds per model, identical prompts across models, and side-by-side language-only versus vision-language evaluation
- Anti-contamination argument: weak but present; the paper argues custom levels and the level editor can reduce contamination pressure, but does not present a strong benchmark-wide leakage defense
- Reliability or comparability concerns: results are highly sensitive to whether the model sees raw pixels or privileged state representations, and valid-action reliability is easier than actually choosing effective actions

## 7. Main contributions
- Contribution 1: Introduces a lightweight tower-defense environment for evaluating long-term planning and decision-making in LLM agents.
- Contribution 2: Measures both task score and valid action rate, making hallucination-like invalid actions a first-class evaluation target.
- Contribution 3: Provides multimodal observations, a difficulty-controlled five-level benchmark, and a level editor for future customization.

## 8. Main findings and failure modes
- Core empirical takeaway: even the strongest models remain far below human experts, and the main gap is not only in legal action generation but also in choosing actions that are actually useful.
- Notable model failure mode 1: models waste resources on misleading tower points or otherwise fail to validate whether a plausible action meaningfully helps the level
- Notable model failure mode 2: models show weak multifinality in decision-making, struggling to coordinate subgoals such as combat, gold collection, and hero control
- Notable model failure mode 3: open models in particular produce many invalid or state-inconsistent actions, and valid action rate worsens as levels become harder
- Does this paper reveal a benchmark-design limitation as well? yes; it shows that benchmark conclusions change sharply with interface privilege, so raw score alone is not comparable across observation modes

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): A compact example showing why interactive games expose effectiveness gaps that static correctness benchmarks miss.
- Best use in Section 1 (taxonomy and evolutionary levels): A specialized RTS-derived diagnostic branch that sits between formal strategy probes and richer visual-agent benchmarks.
- Best use in Section 2 (core capabilities evaluated by games): Direct evidence for real-time decision-making, spatial allocation, and the distinction between legal actions and useful actions.
- Best use in Section 3 (interaction and evaluation paradigm): Strong evidence for the privileged-interface versus ecological-validity trade-off because the same environment supports pixel, textual, and structured observations.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Supports the claim that current models can often act legally without acting effectively, and that misleading affordances remain a serious failure source.

## 10. Relation to nearby papers
- Closest predecessor(s): TextStarCraft II, LLM-PySC2, and other RTS-style LLM benchmarks built on heavier StarCraft II infrastructure
- Closest follow-up(s): later multimodal RTS and visual-agent benchmarks that test more ecological control loops
- Best comparison targets inside our corpus: AtariGPT, Balrog, GameplayQA, StarBench
- What this paper uniquely adds relative to neighbors: It is a lightweight RTS-derived benchmark that explicitly separates invalid-action failures from ineffective-action failures while exposing the effect of privileged versus non-privileged observation modes.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- TowerMind provides three observation modes: pixel-based, JSON-formatted textual observations, and flattened structured state.
- The environment includes moving fog of war, random gold drops, and misleading tower points; units and enemies inside fog are removed from observations and friendly units there become inactive.
- Each action is represented as `(x, y, c)` with continuous coordinates plus one discrete action type over 12 actions, and the benchmark reports both score and valid action rate.
- The paper defines five built-in benchmark levels, evaluates commercial and open LLMs against five human experts, and reports a separate RL benchmark using Ape-X DQN and PPO.

### 11.2 Our synthesis / interpretation
- TowerMind is a strong diagnostic benchmark for planning, real-time action selection, and interface design, but it should not be framed as direct evidence of human-like RTS play.
- Its most survey-relevant contribution is not raw performance ranking; it is the clean demonstration that action legality and action usefulness are distinct evaluation targets.

### 11.3 Uncertain or needs re-check
- If we later need the exact normalized human-relative scores or the full level-difficulty formula, re-check Section 4.2, Appendix C, and the human-baseline tables.
- If we compare it in detail against StarCraft II benchmarks, re-check Appendix B for the exact observation fields and invalid-action error-code mapping.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? No immediate reread is required; the setup, interfaces, and main findings are already clear enough for drafting support.
- Which section to read next if needed: 3.2 / 4.2 / Appendix B / Appendix C
- Follow-up question(s): When we write the real-time decision subsection, should TowerMind be grouped with RTS lineage papers or with multimodal diagnostic benchmarks built around interface trade-offs?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P2
- Reading depth: deep
- Batch ID: B04
- Outline sections: 2,3,4
- Survey role: representative
- Paper card path: `paper_cards/B04/TowerMind.md`
- Check status: unchecked
- Last updated: 2026-04-10
