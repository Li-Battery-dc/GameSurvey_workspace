# LLMCoordination LLM-Coordination: Evaluating and Analyzing Multi-agent Coordination Abilities in Large Language Models

## 0. Metadata
- Date: 2025/04
- Venue: Findings of NAACL 2025
- Authors: Saaket Agashe, Yue Fan, Anthony Reyna, Xin Eric Wang
- Paper link: https://aclanthology.org/2025.findings-naacl.448.pdf
- Code link: https://github.com/eric-ai-lab/llm_coordination
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: high
- Review gate label: usable

## 1. One-paragraph benchmark summary
- LLM-Coordination is a benchmark for pure coordination settings, where agents share payoffs and must align on mutually beneficial actions. It evaluates models in two linked ways: Agentic Coordination, where scaffolded LLM agents play four coordination games end to end, and CoordQA, a 198-question multiple-choice diagnostic over environment comprehension, theory-of-mind reasoning, and joint planning. The paper is especially useful because it makes the coordination trade-off legible: LLM agents can do surprisingly well when decisions mainly depend on environment state, but they remain much weaker when success requires active reasoning about partners' beliefs and intentions. For this survey, it is best treated as a controlled, text-state coordination benchmark rather than an ecological collaboration benchmark.

## 2. Position in our survey
- Why-games relevance: Pure coordination games expose partner modeling and joint planning in a controlled setting without mixing in adversarial incentives.
- Historical stage: diagnostic capability probe
- Narrative level(s): L3 social intelligence
- Most relevant outline section(s): 1,2,3,4
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
- Primary modality: text / symbolic state
- Perception burden retained: environment understanding, partner modeling, and joint planning over textualized game states
- Perception burden removed: raw visual grounding, raw grid parsing, and low-level control are abstracted away; the benchmark often supplies processed state information equivalent to RL observations

## 4. What this benchmark measures
- Primary capability target: multi-agent coordination ability
- Secondary capability target(s): environment comprehension, theory of mind, joint planning, and partner-robust coordination
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? yes
- Does it test social reasoning / deception / cooperation? yes; cooperation without adversarial incentives
- Does it test visual grounding / spatial-temporal reasoning? no
- Does it test long-horizon autonomy / task completion? partially
- Does it test real-time efficiency? no
- Does it test cross-game transfer / open-ended generalization? no
- Why is a game environment especially suitable here? Coordination games let the benchmark isolate cooperative alignment problems that are easy to score but hard to solve.

## 5. Interaction paradigm
- Observation channel: processed textual state descriptions, partner/action history, and benchmark questions in CoordQA
- Action channel: selection from legal high-level actions during Agentic Coordination, then multiple-choice answers during CoordQA
- Interface type: natural language / structured action space / hybrid
- Agent scaffold allowed: memory / reasoning / grounding / answer verification / ToM intermediate reasoning
- Is there privileged API access? yes
- How close is the setup to human play? medium-low; the games are interactive, but observations are heavily textualized and the grounding layer filters infeasible actions
- Main ecological-validity trade-off: the benchmark gains interpretability and reproducibility through text-state descriptions, action filtering, and CoordQA, but that makes it substantially less ecological than raw-interface collaboration settings

## 6. Evaluation protocol
- Main score: Agentic Coordination performance across the four games
- Auxiliary score(s): CoordQA accuracy, subskill scores for environment comprehension, theory of mind, and joint planning, zero-shot coordination with unseen partners, and ablations on ToM reasoning / verification
- Evaluation style: completion rate / accuracy / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: LLM agents are compared against MARL baselines in self-play and cross-play; Overcooked cross-play uses human-proxy behavior-cloning partners and Hanabi cross-play uses OBL partners
- Automatic verifiability: high
- Calibration method: four pure coordination games plus a 66-scenario / 198-question diagnostic QA layer; MCQ answers are scored by fuzzy string matching and agentic experiments use repeated trials per setup
- Anti-contamination argument: not central
- Reliability or comparability concerns: the benchmark mixes end-to-end play with question answering, relies on substantial prompt/scaffold design, and uses manually curated unambiguous edge cases; its observations are also more privileged than human play

## 7. Main contributions
- Contribution 1: Introduces a coordination benchmark centered on pure coordination games.
- Contribution 2: Pairs end-to-end coordination play with CoordQA, a 198-question diagnostic dataset over 66 curated scenarios.
- Contribution 3: Separates environment-driven coordination strength from partner-belief and joint-planning weaknesses through self-play, cross-play, and QA analyses.

## 8. Main findings and failure modes
- Core empirical takeaway: Zero-shot LLM agents, especially GPT-4-turbo, can match or surpass trained RL baselines in environment-driven coordination settings such as Overcooked and remain robust in unseen-partner cross-play, but they are much weaker in Hanabi and on CoordQA items that require active theory-of-mind reasoning and joint planning.
- Notable model failure mode 1: weak theory-of-mind reasoning and implicit-partner modeling are the main bottlenecks, especially in Hanabi
- Notable model failure mode 2: joint planning remains weak even when environment comprehension is relatively strong; the paper reports that even the best LLM stays below 40% on Joint Planning questions
- Notable model failure mode 3: performance depends materially on auxiliary scaffold steps such as answer verification and explicit ToM reasoning
- Notable model failure mode 4: LLM agents are far slower and more computationally expensive than RL baselines, limiting real-time applicability
- Does this paper reveal a benchmark-design limitation as well? yes; it shows that aggregate coordination success alone can hide why models coordinate or fail to coordinate

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Clean evidence that games can isolate cooperation challenges under shared incentives instead of conflating them with adversarial strategy.
- Best use in Section 1 (taxonomy and evolutionary levels): Useful bridge from formal coordination settings to richer social benchmarks. Good example of a curated coordination-game suite with a diagnostic overlay.
- Best use in Section 2 (core capabilities evaluated by games): Direct support for cooperation, theory of mind, and joint planning.
- Best use in Section 3 (interaction and evaluation paradigm): Strong reference for text-state, scaffolded agentic play plus diagnostic QA, and for separating holistic coordination outcomes from component-level diagnosis.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Supports the claim that unseen-partner robustness is not the same as deep partner-belief reasoning.

## 10. Relation to nearby papers
- Closest predecessor(s): GTBench-style coordination tasks and earlier coordination-game studies
- Closest follow-up(s): Collab-Overcooked and broader cooperative-game benchmarks
- Best comparison targets inside our corpus: CollabOvercooked, LLMHanabi, StrategicHanabi, GameArena
- What this paper uniquely adds relative to neighbors: It combines game play, unseen-partner cross-play, and a theory-of-mind / joint-planning diagnostic layer inside one coordination benchmark.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- The benchmark contains two tasks: Agentic Coordination across four pure coordination games and CoordQA with 198 multiple-choice questions built from 66 curated scenarios.
- The four games are Hanabi Challenge, Overcooked-AI, Collab Capture, and Collab Escape.
- The agent framework includes memory, reasoning, and grounding; Hanabi additionally uses answer verification, and Hanabi plus CollabEscape benefit from an explicit ToM-reasoning step.
- The paper states that Overcooked observations are supplied as processed textual state descriptions equivalent to what an RL agent would access in state representations.
- In self-play, GPT-4-turbo matches or exceeds RL baselines across multiple Overcooked layouts, but in Hanabi it scores `13.33` versus roughly `24` for the strongest RL baselines.
- In Hanabi cross-play, GPT-4-turbo scores `15.00` with OBL-1 and `12.00` with OBL-4, while the SAD baseline drops from `23.66` in self-play to `11.33` and `8.00` with the same unseen partners.

### 11.2 Our synthesis / interpretation
- LLM-Coordination is especially useful for Section 3 and Section 4 because it separates coordination outcome from coordination mechanism.
- Its safest survey framing is as a text-state, privileged, scaffolded coordination benchmark rather than as evidence of human-like collaborative play.
- It serves as a clean bridge between formal game-theoretic coordination settings and richer collaboration benchmarks by showing exactly where environment reasoning stops being enough.

### 11.3 Uncertain or needs re-check
- Re-check exact per-model numeric CoordQA accuracies from Figure 3 if we later need a fine-grained historical comparison across closed and open models.
- Re-check whether later follow-up work reuses the same Collab Capture / Collab Escape scenarios or treats them as one-off benchmark environments.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? No immediate follow-up needed; the full paper has been read for this audit. Reopen the benchmark setup or experiment sections only if we need exact per-game tables or prompt details.
- Which section to read next if needed: benchmark setup / CoordQA / experiments
- Follow-up question(s): Which of the four coordination games most cleanly distinguishes partner-robustness from actual theory-of-mind reasoning?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P1
- Reading depth: deep
- Batch ID: B12
- Outline sections: 1,2,3,4
- Survey role: representative
- Paper card path: `paper_cards/B12/LLMCoordination.md`
- Check status: unchecked
- Next action: draft-section
- Last updated: 2026-04-09
