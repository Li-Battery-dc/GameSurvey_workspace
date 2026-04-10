# ARCAGI3 ARC-AGI-3: A New Challenge for Frontier Agentic Intelligence

## 0. Metadata
- Date: 2026/03
- Venue: arXiv
- Authors: ARC Prize Foundation
- Paper link: https://arxiv.org/pdf/2603.24621v1.pdf
- Code link:
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: high
- Review gate label: strong

## 1. One-paragraph benchmark summary
- ARC-AGI-3 is the official benchmark paper for a human-calibrated interactive reasoning benchmark built from novel abstract turn-based environments. Instead of measuring static puzzle solving, it evaluates whether an agent can explore, infer goals, model environment dynamics, and execute plans efficiently on first contact without instructions. The benchmark uses action efficiency relative to human baselines as its core metric, with a large private holdout and an explicit split between official no-harness reporting and community harness-driven results. For this survey, ARC-AGI-3 is best used as an adjacent contrast paper on interactive benchmark design, adaptive efficiency, and anti-overfitting evaluation policy rather than as a central game benchmark in the narrow sense.

## 2. Position in our survey
- Why-games relevance: Turn-based interactive environments let the benchmark measure exploration, mechanic discovery, and planning efficiency rather than only final-answer accuracy.
- Historical stage: diagnostic capability probe
- Narrative level(s): L2 strategic reasoning / L5 cross-game generalization
- Most relevant outline section(s): 1,2,3,4
- Role in corpus: contrast

## 3. Design-space coding
### 3.1 Environment structure
- Information structure: partial
- Transition structure: mostly deterministic
- Agent structure: single-agent
- Social structure: N/A
- Time structure: turn-based

### 3.2 World structure
- World type(s): puzzle / other
- Real game / simulated game / designed task-game hybrid: designed task-game hybrid with novel abstract environments
- Benchmark unit: environment-level sequence

### 3.3 Benchmark scope
- Scope: curated suite
- Number of games / tasks: 135 environments total (25 public, 55 semi-private, 55 fully private)
- Benchmark intent: diagnostic evaluation

### 3.4 Modality
- Primary modality: image / mixed
- Perception burden retained: frame parsing, object tracking, animation interpretation, and action-effect inference
- Perception burden removed: language understanding, cultural symbols, and real-time reflex control

## 4. What this benchmark measures
- Primary capability target: efficient interactive exploration and goal or mechanic inference
- Secondary capability target(s): causal world-model building, action-efficient planning, and generalization to novel environments
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? yes
- Does it test social reasoning / deception / cooperation? no
- Does it test visual grounding / spatial-temporal reasoning? partially
- Does it test long-horizon autonomy / task completion? yes
- Does it test real-time efficiency? no
- Does it test cross-game transfer / open-ended generalization? yes
- Why is a game environment especially suitable here? A game-like environment can hide mechanics and goals, require safe exploration, and still support exact action-count scoring on first exposure.

## 5. Interaction paradigm
- Observation channel: current 64x64 frame or frame sequence over a 16-color grid
- Action channel: a small discrete action set plus optional cell-coordinate selection and undo
- Interface type: GUI interaction / structured action space / hybrid
- Agent scaffold allowed: none on the official leaderboard; community submissions may use harnesses
- Is there privileged API access? no on the official leaderboard
- How close is the setup to human play? medium; the interface is shared and instruction-free, but the environments are abstract synthetic tasks rather than natural commercial games
- Main ecological-validity trade-off: ARC-AGI-3 preserves first-contact interactive adaptation while intentionally stripping away language, culture, and real-time control to isolate agentic reasoning

## 6. Evaluation protocol
- Main score: RHAE (Relative Human Action Efficiency)
- Auxiliary score(s): per-level efficiency, environment scores, and official-versus-community leaderboard distinctions
- Evaluation style: hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: the human baseline is the second-best first-run human action count per level; official leaderboard runs use a shared prompt and no external tools; community leaderboard accepts self-reported harness results
- Automatic verifiability: high
- Calibration method: each environment is tested on 10 humans and is only included if at least two humans solve it fully on first encounter
- Anti-contamination argument: environments are novel, restricted to core-knowledge priors, split into public and private sets, and the official leaderboard excludes public-set and harness-shaped score inflation
- Reliability or comparability concerns: official scores intentionally discount task-specific harness gains, and the paper mixes benchmark design with a policy choice about what counts as meaningful AGI progress

## 7. Main contributions
- Contribution 1: Introduces ARC-AGI-3 as a large interactive reasoning benchmark with public, semi-private, and fully private environment splits.
- Contribution 2: Defines RHAE, a human-normalized action-efficiency metric that rewards first-contact adaptation rather than brute-force search.
- Contribution 3: Separates official general-purpose API evaluation from harness-driven community results to make overfitting pressures explicit.

## 8. Main findings and failure modes
- Core empirical takeaway: humans solve all included environments, while release-time frontier API models remain below 1% on the official semi-private leaderboard.
- Notable model failure mode 1: weak autonomous goal inference and mechanic discovery without task-specific instructions
- Notable model failure mode 2: context-history management becomes a bottleneck even when raw frame access is not the main issue
- Notable model failure mode 3: benchmark-specific harnesses can solve seen public environments but do not generalize cleanly to unseen ones
- Does this paper reveal a benchmark-design limitation as well? yes; it shows how strongly measured performance can depend on whether evaluation rewards general-purpose agents or benchmark-specific scaffolds

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Minor contrast only; it helps show that interactive environments can measure adaptive efficiency rather than static competence, but it is not a central game-benchmark motivation anchor.
- Best use in Section 1 (taxonomy and evolutionary levels): Useful for the ARC line's shift from static abstract reasoning toward interactive agentic evaluation. It is best framed as a boundary case between puzzle diagnostics and broader interactive agent benchmarks.
- Best use in Section 2 (core capabilities evaluated by games): Strong anchor for exploration, goal inference, and planning under hidden mechanics.
- Best use in Section 3 (interaction and evaluation paradigm): Useful for comparing shared turn-based APIs against richer harnesses and external memory tooling. Important for human-normalized efficiency scoring, private holdouts, and anti-overfitting leaderboard policy.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Supports the claim that future benchmarks need both stronger novelty protection and clearer separation between general intelligence and task-specific harness engineering.

## 10. Relation to nearby papers
- Closest predecessor(s): ARC-AGI-1, ARC-AGI-2
- Closest follow-up(s): ARC Prize harness work and graph-based ARC-AGI-3 baselines
- Best comparison targets inside our corpus: AIGameStore, MazeEval, GameTraversalBenchmark
- What this paper uniquely adds relative to neighbors: It pairs instruction-free interactive play with human-normalized efficiency scoring and an explicit anti-overfitting leaderboard policy.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- ARC-AGI-3 contains 25 public environments, 55 semi-private environments, and 55 fully private environments.
- Agents observe 64x64 16-color frames and act through a small turn-based action space that can include five key actions, undo, and cell-coordinate selection.
- RHAE scores each completed level by the squared ratio between the second-best first-run human action count and the AI action count, then aggregates per environment and across the benchmark.
- Every environment has five levels and is attempted by exactly 10 human participants; inclusion requires at least two first-run humans to solve the full environment. Release-time official scores reported in the paper are 0.37% for Gemini 3.1 Pro Preview, 0.26% for GPT 5.4 (High), 0.25% for Opus 4.6 (Max), and 0.00% for Grok-4.20.

### 11.2 Our synthesis / interpretation
- ARC-AGI-3 is better used in this survey as a benchmark-design and agentic-evaluation contrast than as a core game benchmark in the narrow sense.
- The paper is especially valuable because it makes evaluation policy itself part of the benchmark argument, not just the environment design.
- It is also a useful warning that interactive benchmark scores can be dominated by choices about what kinds of scaffolding are considered legitimate.

### 11.3 Uncertain or needs re-check
- Re-check the exact final levels-per-environment convention if we later need a quantitative table; the design section describes a broader production template while the scoring section standardizes a five-level weighting example.
- Re-check whether the public runtime or community leaderboard code should be cited as the canonical software artifact if we later want a code link.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? No immediate reread is needed; the current card already uses the benchmark-design, scoring, calibration, and release-result sections.
- Which section to read next if needed: environment selection / scoring methodology / official leaderboard policy
- Follow-up question(s): How much future ARC-AGI-3 progress will come from genuinely general agents versus benchmark-shaped harness engineering?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P1
- Reading depth: deep
- Batch ID: B11
- Outline sections: 1,2,3,4
- Survey role: contrast
- Paper card path: `paper_cards/B11/ARCAGI3.md`
- Next action: draft-section
- Check status: unchecked
- Last updated: 2026-04-09
