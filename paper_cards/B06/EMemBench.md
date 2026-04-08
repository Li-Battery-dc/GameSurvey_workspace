# EMemBench EMemBench: Interactive Benchmarking of Episodic Memory for VLM Agents

## 0. Metadata
- Date: 2026/01
- Venue: arXiv
- Authors: Xinze Li, Ziyue Zhu, Siyuan Liu, Yubo Ma, Yuhang Zang, Yixin Cao, Aixin Sun
- Paper link: https://arxiv.org/pdf/2601.16690.pdf
- Code link: https://github.com/InternLM/EMemBench
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: medium
- Review gate label: usable

## 1. One-paragraph benchmark summary
- EMemBench is an interactive benchmark for episodic memory in language and vision-language agents. Rather than evaluating a fixed set of retrospective QA items, it generates questions from each agent's own trajectory in text and visual game environments, with automatically verifiable answers derived from game signals. The benchmark covers a range of memory skills, including recall, induction, temporal reasoning, spatial reasoning, logical reasoning, and adversarial memory queries. For this survey, EMemBench matters because it turns games into controllable memory-generation engines and shows that memory evaluation can be interactive, grounded, and unsaturated.

## 2. Position in our survey
- Why-games relevance: Interactive games create long trajectories with grounded state changes, which makes it possible to ask memory questions that are both meaningful and automatically checkable.
- Historical stage: diagnostic capability probe
- Narrative level(s): L4 visual agency / L5 cross-game generalization
- Most relevant outline section(s): 3,4,6
- Role in corpus: representative

## 3. Design-space coding
### 3.1 Environment structure
- Information structure: mixed
- Transition structure: mixed
- Agent structure: single-agent
- Social structure: N/A
- Time structure: mixed

### 3.2 World structure
- World type(s): adventure / puzzle / other
- Real game / simulated game / designed task-game hybrid: curated suite of interactive text and visual games used as memory generators
- Benchmark unit: trajectory plus generated question set

### 3.3 Benchmark scope
- Scope: curated suite
- Number of games / tasks: 15 text games plus multiple visual-game seeds
- Benchmark intent: diagnostic evaluation

### 3.4 Modality
- Primary modality: mixed
- Perception burden retained: trajectory tracking, event binding, temporal ordering, and spatial grounding
- Perception burden removed: fixed hand-authored QA and unsupported free-form judging

## 4. What this benchmark measures
- Primary capability target: episodic memory for interactive agents
- Secondary capability target(s): induction, temporal reasoning, spatial reasoning, logical recall, and robustness under adversarial questioning
- Does it test rule grounding / legal action generation? no
- Does it test strategic planning under uncertainty? partially
- Does it test social reasoning / deception / cooperation? no
- Does it test visual grounding / spatial-temporal reasoning? yes
- Does it test long-horizon autonomy / task completion? partially
- Does it test real-time efficiency? no
- Does it test cross-game transfer / open-ended generalization? partially
- Why is a game environment especially suitable here? Games provide eventful trajectories with exact underlying state, so memory probes can be generated per agent run instead of memorized from a fixed test set.

## 5. Interaction paradigm
- Observation channel: text-game or visual-game trajectories plus agent memory traces when memory systems are used
- Action channel: ordinary game actions during trajectory generation, followed by memory question answering
- Interface type: API / hybrid
- Agent scaffold allowed: memory
- Is there privileged API access? yes for question generation and answer verification
- How close is the setup to human play? medium-low; the games are interactive, but the benchmark is instrumented around memory diagnosis rather than ordinary play
- Main ecological-validity trade-off: EMemBench gains strong memory supervision by instrumenting trajectories and templated questions, but this makes it more diagnostic than natural end-to-end gameplay

## 6. Evaluation protocol
- Main score: accuracy on trajectory-grounded memory questions
- Auxiliary score(s): breakdown by memory skill, text versus visual setting, and with-memory versus in-context baselines
- Evaluation style: accuracy / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: strong LM and VLM backbones plus a human study
- Automatic verifiability: high
- Calibration method: question templates with controlled answerability and balanced coverage over memory skills
- Anti-contamination argument: questions are generated from each agent's own trajectory rather than drawn from a fixed public benchmark set
- Reliability or comparability concerns: the memory score depends on the benchmark's question-generation templates and on the underlying game distribution

## 7. Main contributions
- Contribution 1: Introduces a trajectory-grounded benchmark for episodic memory in interactive agents.
- Contribution 2: Covers six memory-skill families across both text and visual game settings.
- Contribution 3: Shows that persistent memory helps in text settings but remains less reliable for visually grounded agents.

## 8. Main findings and failure modes
- Core empirical takeaway: results are far from saturated, with induction and spatial reasoning remaining persistent bottlenecks.
- Notable model failure mode 1: poor induction from prior events even when raw recall is stronger
- Notable model failure mode 2: weak spatial memory in visual settings
- Notable model failure mode 3: inconsistent gains from persistent memory for VLM agents
- Does this paper reveal a benchmark-design limitation as well? yes; it shows that many current memory evaluations are too static and too detached from actual agent trajectories

## 9. Why this paper matters for our survey
- Best use in Section 0 (why games): Strong example of games as controllable generators of grounded, dynamic evaluation data.
- Best use in Section 1 (historical evolution): Useful as a specialized later-stage benchmark that repurposes game trajectories for capability diagnosis.
- Best use in Section 2 (design space): Good case where the benchmark unit is not only an episode but also a trajectory-derived question set.
- Best use in Section 3 (capability targets): Direct support for long-horizon memory, spatial reasoning, and trajectory consistency.
- Best use in Section 4 (interaction paradigm): Useful for discussing memory modules as an explicit scaffold variable.
- Best use in Section 5 (evaluation protocol): Strong reference for trajectory-grounded, automatically verified memory evaluation.
- Best use in Section 6/7 (limitations and future): Supports the claim that visually grounded memory remains a major open problem.

## 10. Relation to nearby papers
- Closest predecessor(s): static agent-memory QA benchmarks and trajectory-based agent diagnostics
- Closest follow-up(s): richer memory-focused game and embodied-agent evaluations
- Best comparison targets inside our corpus: TowerMind, ReasoningViaVideo, MineNPCTask, TextQuests
- What this paper uniquely adds relative to neighbors: It uses game trajectories to synthesize personalized memory tests rather than benchmarking only game completion.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- EMemBench generates memory questions from each agent's own trajectory across text and visual game environments.
- It covers single-hop recall, multi-hop recall, induction, temporal, spatial, logical, and adversarial memory skills.
- The paper evaluates memory agents across 15 text games and multiple visual seeds, finds induction and spatial reasoning difficult, and reports a human study confirming benchmark difficulty.

### 11.2 Our synthesis / interpretation
- EMemBench is useful less as a game benchmark in the ordinary win-rate sense and more as a proof that games can generate grounded diagnostic probes for agent memory.
- It helps the survey connect game environments to broader questions about agent instrumentation and benchmark validity.

### 11.3 Uncertain or needs re-check
- Re-check the exact visual-game roster and the strongest memory-agent baselines if we later compare memory systems in detail.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? Yes, because the question-generation pipeline and skill taxonomy likely matter for Section 5.
- Which section to read next if needed: benchmark construction / evaluation / human study
- Follow-up question(s): How transferable are EMemBench's memory scores to open-world game agents rather than curated text and visual environments?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P1
- Reading depth: deep
- Batch ID: B06
- Outline sections: 3,4,6
- Survey role: representative
- Paper card path: `paper_cards/B06/EMemBench.md`
- Next action: draft-section
- Last updated: 2026-04-08
