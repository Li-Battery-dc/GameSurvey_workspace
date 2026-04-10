# CollabOvercooked Collab-Overcooked: Benchmarking and Evaluating Large Language Models as Collaborative Agents

## 0. Metadata
- Date: 2025/02
- Venue: EMNLP 2025
- Authors: Haochen Sun, Shuwen Zhang, Lujie Niu, Lei Ren, Hao Xu, Hao Fu, Fangkun Zhao, Caixia Yuan, Xiaojie Wang
- Paper link: https://aclanthology.org/2025.emnlp-main.249.pdf
- Code link: https://github.com/YusaeMeow/Collab-Overcooked
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: high
- Review gate label: usable

## 1. One-paragraph benchmark summary
- Collab-Overcooked is a benchmark for LLM-based multi-agent collaboration built on Overcooked-AI. Its key move is to force collaboration through resource isolation and asymmetric task knowledge, then evaluate not only whether tasks finish but also whether agents correctly initiate collaboration, respond to partner requests, and adapt during sequential kitchen workflows. The benchmark contains 30 process-specific tasks across 6 complexity levels and introduces process-oriented metrics built around TES, ITES, Progress Completeness, Initiating Capability, and Responding Capability. For this survey, it is a strong cooperation-focused counterpart to deception-heavy social benchmarks and a useful bridge from pure coordination tasks to more interactive teamwork settings.

## 2. Position in our survey
- Why-games relevance: Overcooked tasks make collaboration pressure concrete because agents must coordinate spatially and temporally under shared goals.
- Historical stage: diagnostic capability probe
- Narrative level(s): L3 social intelligence
- Most relevant outline section(s): 1,2,3,4
- Role in corpus: representative

## 3. Design-space coding
### 3.1 Environment structure
- Information structure: mixed
- Transition structure: deterministic
- Agent structure: multi-agent
- Social structure: cooperative
- Time structure: turn-based

### 3.2 World structure
- World type(s): other
- Real game / simulated game / designed task-game hybrid: real game adapted into a collaboration benchmark
- Benchmark unit: task episode

### 3.3 Benchmark scope
- Scope: single game
- Number of games / tasks: 30 tasks across 6 complexity levels
- Benchmark intent: diagnostic evaluation

### 3.4 Modality
- Primary modality: text / symbolic state
- Perception burden retained: task decomposition, communication, state tracking, and partner coordination under asymmetric information
- Perception burden removed: visual perception and native game-interface control are abstracted into text prompts and predefined action primitives

## 4. What this benchmark measures
- Primary capability target: collaborative task execution with communication
- Secondary capability target(s): goal interpretation, initiating collaboration, responding to collaboration, and continuous adaptation
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? partially
- Does it test social reasoning / deception / cooperation? yes
- Does it test visual grounding / spatial-temporal reasoning? no
- Does it test long-horizon autonomy / task completion? partially
- Does it test real-time efficiency? partially
- Does it test cross-game transfer / open-ended generalization? no
- Why is a game environment especially suitable here? Overcooked provides a compact but demanding cooperative setting where communication quality directly affects measurable task efficiency.

## 5. Interaction paradigm
- Observation channel: text prompts containing game rules, task description, current kitchen state, available action space, and natural-language partner messages
- Action channel: predefined action primitives in `func(args)` format plus natural-language collaboration messages
- Interface type: natural language / API / hybrid
- Agent scaffold allowed: memory / reflection
- Is there privileged API access? yes; the environment broadcasts global state, validates action primitives, and exposes task-specific structured prompts
- How close is the setup to human play? medium-low; it preserves interactive teamwork, but uses text state broadcasts, forced collaboration designs, and predefined action primitives
- Main ecological-validity trade-off: Collab-Overcooked gains fine-grained collaboration analysis by forcing interdependence and using process metrics, but this stronger diagnostic control reduces ecological realism

## 6. Evaluation protocol
- Main score: success rate and Progress Completeness across task complexity levels
- Auxiliary score(s): TES, ITES, Initiating Capability, Responding Capability, and human-versus-model comparisons
- Evaluation style: completion rate / process-level / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: 13 LLM agents are evaluated with a shared in-context agent architecture, and 10 human participants provide a performance ceiling under time constraints
- Automatic verifiability: high
- Calibration method: 30 tasks across 6 complexity levels, 10 repetitions per task, identical agent architecture across models, and process-specific collaboration analysis
- Anti-contamination argument: not central
- Reliability or comparability concerns: results depend on manually annotated RATs, long prompt stacks with memory/reflection, and a relatively simple baseline architecture that leaves room for stronger agent designs

## 7. Main contributions
- Contribution 1: Extends Overcooked-AI into a collaboration benchmark with 30 tasks across 6 difficulty levels.
- Contribution 2: Defines collaboration as both initiating and responding to collaboration.
- Contribution 3: Adds TES/ITES-derived process metrics to analyze collaboration quality beyond final task success.

## 8. Main findings and failure modes
- Core empirical takeaway: current LLM agents interpret goals reasonably well, but still struggle with active collaboration and continuous adaptation; most models respond to collaboration better than they initiate it, and performance drops sharply with task complexity.
- Notable model failure mode 1: failing to proactively request or offer help when task structure demands it
- Notable model failure mode 2: weak adaptation once task context changes during multi-step execution
- Notable model failure mode 3: attention misalignment that degrades collaboration efficiency
- Does this paper reveal a benchmark-design limitation as well? yes; it shows that outcome-only scoring can hide large differences in how collaboration actually happens, but its own evaluation depends on exhaustively specified RATs and long prompt-based agent loops

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Good evidence that cooperative games reveal interaction failures that static task benchmarks miss.
- Best use in Section 1 (taxonomy and evolutionary levels): Useful bridge from social reasoning benchmarks to collaboration-centered multi-agent evaluation. Strong example of a cooperative single-game benchmark with process metrics.
- Best use in Section 2 (core capabilities evaluated by games): Direct support for cooperation and adaptation.
- Best use in Section 3 (interaction and evaluation paradigm): Helpful for text-state interaction, predefined action primitives, and process-oriented collaboration metrics such as PC, IC, and RC.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Supports the claim that active collaboration remains much weaker than simple goal interpretation.

## 10. Relation to nearby papers
- Closest predecessor(s): Overcooked-AI, coordination and teamwork benchmarks
- Closest follow-up(s): broader collaborative multi-agent game benchmarks
- Best comparison targets inside our corpus: HumanLevelDiplomacy, StrategicHanabi, LLMCoordination, TeamCraft
- What this paper uniquely adds relative to neighbors: It focuses on fine-grained collaboration process, forced interdependence, and initiating-versus-responding capability rather than only team outcome or hidden-state reasoning.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- Collab-Overcooked contains 30 tasks across 6 complexity levels and is built on Overcooked-AI.
- The paper defines collaboration capability in terms of initiating collaboration and responding to collaboration, and introduces TES/ITES-derived metrics including Progress Completeness, Initiating Capability, and Responding Capability.
- Across 13 LLMs and a 10-person human evaluation, the authors find strong goal interpretation but notable weaknesses in active collaboration and continuous adaptation, with human performance remaining far more stable at high complexity.

### 11.2 Our synthesis / interpretation
- This paper is one of the stronger corpus sources for showing why process metrics are necessary in multi-agent benchmarks.
- It also helps balance the survey's social-intelligence section away from deception-only benchmarks, but it should be framed as a text-state diagnostic collaboration benchmark rather than as a visual or highly ecological one.

### 11.3 Uncertain or needs re-check
- Re-check Appendix B if later drafting needs the exact TES/ITES formulation or the full RAT annotation details.
- Re-check the attention-analysis appendix if later drafting wants to attribute failures specifically to prompt-part attention misalignment.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? No immediate follow-up needed; the full paper has been read for this audit. Reopen Sections 3 to 5 or Appendix B only if we need exact metric formulas, RAT details, or human-ceiling analysis.
- Which section to read next if needed: metrics / benchmark design / human evaluation appendix
- Follow-up question(s): How transferable are PC, IC, and RC to cooperative benchmarks that do not have exhaustively annotatable action trajectories?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P1
- Reading depth: deep
- Batch ID: B03
- Outline sections: 1,2,3,4
- Survey role: representative
- Paper card path: `paper_cards/B03/CollabOvercooked.md`
- Check status: unchecked
- Next action: draft-section
- Last updated: 2026-04-10
