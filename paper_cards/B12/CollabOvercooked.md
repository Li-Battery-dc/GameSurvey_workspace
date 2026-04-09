# CollabOvercooked Collab-Overcooked: Benchmarking and Evaluating Large Language Models as Collaborative Agents

## 0. Metadata
- Date: 2025/02
- Venue: EMNLP 2025
- Authors: Haochen Sun, Shuwen Zhang, Lujie Niu, Lei Ren, Hao Xu, Hao Fu, Fangkun Zhao, Caixia Yuan, Xiaojie Wang
- Paper link: https://aclanthology.org/2025.emnlp-main.249.pdf
- Code link: https://github.com/YusaeMeow/Collab-Overcooked
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: medium
- Review gate label: usable

## 1. One-paragraph benchmark summary
- Collab-Overcooked is a benchmark for LLM-based multi-agent collaboration built on Overcooked-AI. The key move is to go beyond final task completion and evaluate how agents initiate collaboration, respond to partners, and adapt during multi-step kitchen tasks that require communication and resource exchange. The benchmark contains 30 process-specific tasks across 6 complexity levels and introduces process-oriented trajectory-efficiency metrics rather than only outcome success. For this survey, it is a useful collaborative counterpart to deception-heavy social benchmarks and a strong bridge between pure coordination settings and richer embodied-like teamwork.

## 2. Position in our survey
- Why-games relevance: Overcooked tasks make collaboration pressure concrete because agents must coordinate spatially and temporally under shared goals.
- Historical stage: ecological agent benchmark
- Narrative level(s): L3 social intelligence
- Most relevant outline section(s): 2,3,4
- Role in corpus: representative

## 3. Design-space coding
### 3.1 Environment structure
- Information structure: mixed
- Transition structure: deterministic
- Agent structure: multi-agent
- Social structure: cooperative
- Time structure: hybrid

### 3.2 World structure
- World type(s): other
- Real game / simulated game / designed task-game hybrid: real game adapted into a collaboration benchmark
- Benchmark unit: task episode

### 3.3 Benchmark scope
- Scope: single game
- Number of games / tasks: 30 tasks across 6 complexity levels
- Benchmark intent: diagnostic evaluation / ecological evaluation

### 3.4 Modality
- Primary modality: mixed
- Perception burden retained: task decomposition, communication, local state awareness, and partner coordination
- Perception burden removed: the benchmark simplifies control relative to full human real-time play and emphasizes language-mediated collaboration

## 4. What this benchmark measures
- Primary capability target: collaborative task execution with communication
- Secondary capability target(s): goal interpretation, initiating collaboration, responding to collaboration, and continuous adaptation
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? partially
- Does it test social reasoning / deception / cooperation? yes
- Does it test visual grounding / spatial-temporal reasoning? partially
- Does it test long-horizon autonomy / task completion? yes
- Does it test real-time efficiency? partially
- Does it test cross-game transfer / open-ended generalization? no
- Why is a game environment especially suitable here? Overcooked provides a compact but demanding cooperative setting where communication quality directly affects measurable task efficiency.

## 5. Interaction paradigm
- Observation channel: local environment state, task description, resource availability, and natural-language messages
- Action channel: environment actions plus collaboration messages between agents
- Interface type: natural language / API / hybrid
- Agent scaffold allowed: none in the core benchmark
- Is there privileged API access? yes
- How close is the setup to human play? medium; it preserves the collaborative structure of Overcooked, but the benchmark instruments agent communication and evaluation tightly
- Main ecological-validity trade-off: Collab-Overcooked gains fine-grained collaboration analysis by controlling communication and using benchmark-specific metrics

## 6. Evaluation protocol
- Main score: trajectory-efficiency-oriented collaboration score
- Auxiliary score(s): TES, ITES, and task completion across complexity levels
- Evaluation style: completion rate / process-level / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: 13 LLM agents are compared on the same collaboration tasks
- Automatic verifiability: high
- Calibration method: 30 tasks across 6 complexity levels with process-specific analysis of collaboration behavior
- Anti-contamination argument: not central
- Reliability or comparability concerns: results depend on the benchmark's task decomposition and on the specific communication protocol allowed between agents

## 7. Main contributions
- Contribution 1: Extends Overcooked-AI into a collaboration benchmark with 30 tasks across 6 difficulty levels.
- Contribution 2: Defines collaboration as both initiating and responding to collaboration.
- Contribution 3: Adds trajectory-efficiency metrics to analyze collaboration quality beyond final task success.

## 8. Main findings and failure modes
- Core empirical takeaway: current LLM agents interpret goals reasonably well, but still struggle with active collaboration and continuous adaptation.
- Notable model failure mode 1: failing to proactively request or offer help when task structure demands it
- Notable model failure mode 2: weak adaptation once task context changes during multi-step execution
- Notable model failure mode 3: attention misalignment that degrades collaboration efficiency
- Does this paper reveal a benchmark-design limitation as well? yes; it shows that outcome-only scoring can hide large differences in how collaboration actually happens

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Good evidence that cooperative games reveal interaction failures that static task benchmarks miss.
- Best use in Section 1 (taxonomy and evolutionary levels): Useful bridge from social reasoning benchmarks to collaboration-centered multi-agent evaluation. Strong example of a cooperative single-game benchmark with process metrics.
- Best use in Section 2 (core capabilities evaluated by games): Direct support for cooperation and adaptation.
- Best use in Section 3 (interaction and evaluation paradigm): Helpful for natural-language communication plus structured execution. Important for process-oriented collaboration metrics.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Supports the claim that active collaboration remains much weaker than simple goal interpretation.

## 10. Relation to nearby papers
- Closest predecessor(s): Overcooked-AI, coordination and teamwork benchmarks
- Closest follow-up(s): broader collaborative multi-agent game benchmarks
- Best comparison targets inside our corpus: LLMCoordination, TeamCraft, StrategicHanabi, HumanLevelDiplomacy
- What this paper uniquely adds relative to neighbors: It focuses on fine-grained collaboration process rather than only team outcome or hidden-state reasoning.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- Collab-Overcooked contains 30 tasks across 6 complexity levels and is built on Overcooked-AI.
- The paper defines collaboration capability in terms of initiating collaboration and responding to collaboration, and introduces trajectory-efficiency metrics such as TES and ITES.
- Across 13 LLMs, the authors find strong goal interpretation but notable weaknesses in active collaboration and continuous adaptation.

### 11.2 Our synthesis / interpretation
- This paper is one of the better cards for Section 5 because it demonstrates why process metrics are necessary in multi-agent benchmarks.
- It also helps balance the survey's social-intelligence section away from deception-only benchmarks.

### 11.3 Uncertain or needs re-check
- Re-check the exact definition of the full metric set and whether a third trajectory-efficiency metric is used in the final evaluation tables.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? Yes, because the exact collaboration metrics and task taxonomy matter for comparative synthesis.
- Which section to read next if needed: benchmark design / metrics / results
- Follow-up question(s): How directly do TES and ITES transfer to other cooperative benchmarks outside Overcooked?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P1
- Reading depth: deep
- Batch ID: B12
- Outline sections: 2,3,4
- Survey role: representative
- Paper card path: `paper_cards/B12/CollabOvercooked.md`
- Next action: draft-section
- Last updated: 2026-04-08
