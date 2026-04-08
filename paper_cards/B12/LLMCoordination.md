# LLMCoordination LLM-Coordination: Evaluating and Analyzing Multi-agent Coordination Abilities in Large Language Models

## 0. Metadata
- Date: 2023/10
- Venue: Findings of NAACL 2025
- Authors: Saaket Agashe, Yue Fan, Anthony Reyna, Xin Eric Wang
- Paper link: https://aclanthology.org/2025.findings-naacl.448.pdf
- Code link: https://github.com/eric-ai-lab/llm_coordination
- Reading depth: structured-skim
- Card status: card-reviewed
- Confidence in this card: medium
- Review gate label: usable

## 1. One-paragraph benchmark summary
- LLM-Coordination is a benchmark for pure coordination settings, where agents share goals and must align on mutually beneficial actions. It evaluates models in two ways: Agentic Coordination across four coordination games, and CoordQA, a 198-question multiple-choice diagnostic over environment comprehension, theory-of-mind reasoning, and joint planning. The benchmark is useful because it separates end-to-end coordination behavior from finer-grained diagnostic questions about why coordination succeeds or fails. For this survey, it is a clean mid-level benchmark between very formal game-theoretic tasks and richer collaborative environments such as Overcooked or Minecraft.

## 2. Position in our survey
- Why-games relevance: Pure coordination games expose partner modeling and joint planning in a controlled setting without mixing in adversarial incentives.
- Historical stage: diagnostic capability probe
- Narrative level(s): L3 social intelligence
- Most relevant outline section(s): 1,2,3,5,6
- Role in corpus: representative

## 3. Design-space coding
### 3.1 Environment structure
- Information structure: mixed
- Transition structure: mixed
- Agent structure: multi-agent
- Social structure: cooperative
- Time structure: mixed

### 3.2 World structure
- World type(s): mixed
- Real game / simulated game / designed task-game hybrid: curated coordination-game suite
- Benchmark unit: game episode plus diagnostic question set

### 3.3 Benchmark scope
- Scope: curated suite
- Number of games / tasks: 4 coordination games plus 198 CoordQA questions
- Benchmark intent: diagnostic evaluation

### 3.4 Modality
- Primary modality: mixed
- Perception burden retained: environment understanding, partner modeling, and joint planning
- Perception burden removed: benchmark-specific diagnostics expose coordination reasoning more directly than open-ended live play

## 4. What this benchmark measures
- Primary capability target: multi-agent coordination ability
- Secondary capability target(s): environment comprehension, theory of mind, joint planning, and partner-robust coordination
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? yes
- Does it test social reasoning / deception / cooperation? cooperation
- Does it test visual grounding / spatial-temporal reasoning? partially
- Does it test long-horizon autonomy / task completion? partially
- Does it test real-time efficiency? no
- Does it test cross-game transfer / open-ended generalization? partially
- Why is a game environment especially suitable here? Coordination games let the benchmark isolate cooperative alignment problems that are easy to score but hard to solve.

## 5. Interaction paradigm
- Observation channel: game-state descriptions plus benchmark questions in CoordQA
- Action channel: game actions during Agentic Coordination and multiple-choice answers during CoordQA
- Interface type: natural language / structured action space / hybrid
- Agent scaffold allowed: none
- Is there privileged API access? yes
- How close is the setup to human play? medium-low; the games are interactive, but the diagnostic QA component is explicitly benchmark-instrumented
- Main ecological-validity trade-off: the benchmark gains interpretability by pairing play with QA, but that makes it less ecological than fully end-to-end collaboration settings

## 6. Evaluation protocol
- Main score: Agentic Coordination performance
- Auxiliary score(s): CoordQA accuracy, subskill scores for environment comprehension, theory of mind, and joint planning, plus zero-shot coordination with unseen partners
- Evaluation style: completion rate / accuracy / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: LLM agents are compared with RL baselines and with unseen-partner coordination setups
- Automatic verifiability: high
- Calibration method: four pure coordination games plus a diagnostic QA layer over the same settings
- Anti-contamination argument: not central
- Reliability or comparability concerns: the benchmark mixes end-to-end play with question answering, so different models may look stronger on one layer than the other

## 7. Main contributions
- Contribution 1: Introduces a coordination benchmark centered on pure coordination games.
- Contribution 2: Pairs end-to-end coordination play with CoordQA, a 198-question diagnostic dataset.
- Contribution 3: Shows that LLMs can coordinate well when decisions rely on environment variables but remain weak on partner-belief reasoning.

## 8. Main findings and failure modes
- Core empirical takeaway: LLM agents coordinate surprisingly well in some pure coordination settings, but struggle when success depends on explicitly modeling partners' beliefs and intentions.
- Notable model failure mode 1: weak theory-of-mind reasoning in CoordQA
- Notable model failure mode 2: difficulty with joint planning when partner beliefs matter
- Notable model failure mode 3: stronger performance in environment-driven coordination than in intention-sensitive settings
- Does this paper reveal a benchmark-design limitation as well? yes; it shows that aggregate coordination success alone can hide why models coordinate or fail to coordinate

## 9. Why this paper matters for our survey
- Best use in Section 0 (why games): Clean evidence that games can isolate cooperation challenges under shared incentives.
- Best use in Section 1 (historical evolution): Useful bridge from formal coordination settings to richer social benchmarks.
- Best use in Section 2 (design space): Good example of a curated coordination-game suite with a diagnostic overlay.
- Best use in Section 3 (capability targets): Direct support for cooperation, theory of mind, and joint planning.
- Best use in Section 4 (interaction paradigm): Helpful for mixed end-to-end play plus diagnostic QA evaluation.
- Best use in Section 5 (evaluation protocol): Strong reference for separating holistic coordination outcomes from component-level diagnosis.
- Best use in Section 6/7 (limitations and future): Supports the claim that unseen-partner robustness is not the same as deep partner-belief reasoning.

## 10. Relation to nearby papers
- Closest predecessor(s): GTBench-style coordination tasks and earlier coordination-game studies
- Closest follow-up(s): Collab-Overcooked and broader cooperative-game benchmarks
- Best comparison targets inside our corpus: CollabOvercooked, LLMHanabi, StrategicHanabi, GTBench
- What this paper uniquely adds relative to neighbors: It combines game play with a theory-of-mind and joint-planning diagnostic layer in one benchmark.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- The benchmark contains two tasks: Agentic Coordination across four pure coordination games and CoordQA with 198 multiple-choice questions.
- CoordQA evaluates environment comprehension, theory-of-mind reasoning, and joint planning.
- The paper reports that LLM agents are relatively robust to unseen partners in zero-shot coordination, but struggle more in scenarios requiring active reasoning about partners' beliefs and intentions.

### 11.2 Our synthesis / interpretation
- LLM-Coordination is especially useful for Section 5 because it separates coordination outcome from coordination mechanism.
- It also serves as a clean bridge between formal game-theoretic benchmarks and richer collaborative worlds.

### 11.3 Uncertain or needs re-check
- Re-check the exact four game environments and the strongest RL baseline comparisons if we later need a tighter historical comparison.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? Yes, because the QA construction and zero-shot coordination protocol are likely worth citing directly.
- Which section to read next if needed: benchmark setup / CoordQA / experiments
- Follow-up question(s): Which of the four coordination games most cleanly distinguishes partner-robustness from actual theory-of-mind reasoning?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P1
- Reading depth: structured-skim
- Batch ID: B12
- Outline sections: 1,2,3,5,6
- Survey role: representative
- Paper card path: `paper_cards/B12/LLMCoordination.md`
- Next action: draft-section
- Last updated: 2026-04-08
