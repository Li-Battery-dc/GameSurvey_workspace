# ARCAGI3Exploration Graph-Based Exploration for ARC-AGI-3 Interactive Reasoning Tasks

## 0. Metadata
- Date: 2025/12
- Venue: arXiv
- Authors: Evgenii Rudakov, Jonathan Shock, Benjamin Ultan Cowley
- Paper link: https://arxiv.org/pdf/2512.24156v1.pdf
- Code link: https://github.com/dolphin-in-a-coma/arc-agi-3-just-explore
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: medium
- Review gate label: usable

## 1. One-paragraph benchmark summary
- This paper is not the benchmark introduction for ARC-AGI-3, but it is a strong baseline-analysis paper for the benchmark’s interactive reasoning tasks. ARC-AGI-3 presents six game-like environments where agents must discover mechanics through sparse interactive exploration, and this paper studies them with a training-free graph-based explorer that tracks states and actions explicitly. The method substantially outperforms frontier LLM baselines, revealing that systematic state tracking matters more than generic language reasoning in this setting. For this survey, the card is useful as evidence about what ARC-AGI-3 measures and why current LLM agents fail on it, even though the paper is method-centric.

## 2. Position in our survey
- Why-games relevance: Game-like worlds can evaluate few-shot skill acquisition and mechanic discovery under sparse rewards.
- Historical stage: diagnostic capability probe
- Narrative level(s): L2 strategic reasoning / L5 cross-game generalization
- Most relevant outline section(s): 2,3,7
- Role in corpus: peripheral

## 3. Design-space coding
### 3.1 Environment structure
- Information structure: mostly perfect in the released tasks
- Transition structure: deterministic
- Agent structure: single-agent
- Social structure: N/A
- Time structure: turn-based

### 3.2 World structure
- World type(s): puzzle / other
- Real game / simulated game / designed task-game hybrid: interactive reasoning benchmark with novel game-like tasks
- Benchmark unit: level

### 3.3 Benchmark scope
- Scope: curated suite
- Number of games / tasks: 6 games with 8-10 levels each
- Benchmark intent: diagnostic evaluation

### 3.4 Modality
- Primary modality: image / mixed
- Perception burden retained: frame interpretation, state tracking, and action-effect inference
- Perception burden removed: the paper’s baseline uses structured graph search rather than a human-like language interface

## 4. What this benchmark measures
- Primary capability target: interactive rule discovery through exploration
- Secondary capability target(s): sparse-reward planning, state-memory, and level-to-level skill acquisition
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? yes
- Does it test social reasoning / deception / cooperation? no
- Does it test visual grounding / spatial-temporal reasoning? yes
- Does it test long-horizon autonomy / task completion? yes
- Does it test real-time efficiency? partially
- Does it test cross-game transfer / open-ended generalization? yes
- Why is a game environment especially suitable here? The benchmark can hide mechanics and reveal them only through action consequences across progressively harder levels.

## 5. Interaction paradigm
- Observation channel: game frames with sparse level-completion feedback
- Action channel: environment actions over discrete interactive games
- Interface type: GUI interaction / structured action space / hybrid
- Agent scaffold allowed: graph memory / explicit state tracking
- Is there privileged API access? no privileged symbolic rules, though the baseline extracts visual state structure
- How close is the setup to human play? medium; the tasks are game-like, but the reported best baseline is an explicit explorer rather than a human-like player
- Main ecological-validity trade-off: ARC-AGI-3 is novel and adaptive, but the strongest current results come from algorithmic exploration strategies rather than generic agents

## 6. Evaluation protocol
- Main score: number of levels solved, with action count as tiebreaker
- Auxiliary score(s): solved levels by game and by interaction budget
- Evaluation style: completion rate / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: the paper compares random exploration, graph-based ablations, and an LLM+DSL baseline under fixed interaction budgets
- Automatic verifiability: high
- Calibration method: fixed interaction limits such as 4,000 steps and full challenge limits of 8 hours / 10 steps per second
- Anti-contamination argument: the ARC-AGI-3 games are novel and designed around mechanic discovery rather than prior public tasks
- Reliability or comparability concerns: this paper studies ARC-AGI-3 through a baseline method rather than defining the benchmark itself, and one reported challenge submission was affected by a reset-handling bug

## 7. Main contributions
- Contribution 1: Clarifies ARC-AGI-3 as an interactive reasoning benchmark centered on mechanic discovery.
- Contribution 2: Provides a strong training-free graph-exploration baseline that clearly outperforms LLM baselines.
- Contribution 3: Surfaces state tracking and frontier exploration as central capabilities for the benchmark.

## 8. Main findings and failure modes
- Core empirical takeaway: explicit graph-structured exploration dramatically outperforms frontier LLM baselines on ARC-AGI-3.
- Notable model failure mode 1: LLM baselines fail to form and test hypotheses systematically
- Notable model failure mode 2: sparse-reward exploration without memory leads to repeated ineffective actions
- Notable model failure mode 3: very large state spaces make exhaustive exploration computationally intractable
- Does this paper reveal a benchmark-design limitation as well? yes; it shows that benchmarking few-shot interactive reasoning may require non-LLM baselines to understand what the benchmark is truly testing

## 9. Why this paper matters for our survey
- Best use in Section 0 (why games): Shows that games can test adaptive learning rather than just fixed competence.
- Best use in Section 1 (historical evolution): Fits the movement from static ARC tasks to interactive reasoning benchmarks.
- Best use in Section 2 (design space): Useful for mechanic-discovery and sparse-reward benchmark design.
- Best use in Section 3 (capability targets): Strong evidence for state-memory and structured exploration.
- Best use in Section 4 (interaction paradigm): Useful contrast between generic LLM agents and explicit exploration architectures.
- Best use in Section 5 (evaluation protocol): Good example of solve-count plus efficiency scoring.
- Best use in Section 6/7 (limitations and future): Supports hybrid exploration-plus-learning approaches for future interactive reasoning agents.

## 10. Relation to nearby papers
- Closest predecessor(s): ARC-style static reasoning tasks
- Closest follow-up(s): future ARC-AGI-3 solutions
- Best comparison targets inside our corpus: Mars, MazeEval, GameTraversalBenchmark
- What this paper uniquely adds relative to neighbors: It shows, using the same benchmark, that structured exploration can beat frontier language agents even without training.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- ARC-AGI-3 consists of 6 game environments with 8-10 levels each and sparse level-completion feedback.
- The paper reports that its graph-based method solves a median of 30 out of 52 levels in preview evaluation and substantially outperforms frontier LLM-based baselines.
- The benchmark scores number of solved levels with action efficiency as a tiebreaker.

### 11.2 Our synthesis / interpretation
- This paper is best used as supporting evidence about ARC-AGI-3’s demands, not as the canonical benchmark-introduction citation.
- It strengthens the survey’s argument that explicit structure can still dominate generic LLM reasoning in sparse interactive settings.

### 11.3 Uncertain or needs re-check
- Re-check the official ARC-AGI-3 benchmark paper if later drafting needs the primary benchmark citation.
- Re-check the exact discrepancy between official submission results and reruns if we later discuss baseline robustness.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? Only if later survey drafting needs a detailed ARC-AGI-3 case study.
- Which section to read next if needed: benchmark overview / results / discussion of structured exploration
- Follow-up question(s): Which ARC-AGI-3 games most clearly distinguish mechanic discovery from raw search burden?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P3
- Reading depth: deep
- Batch ID: B11
- Outline sections: 2,3,7
- Survey role: peripheral
- Paper card path: `paper_cards/B11/ARCAGI3Exploration.md`
- Next action: draft-section
- Last updated: 2026-04-05
