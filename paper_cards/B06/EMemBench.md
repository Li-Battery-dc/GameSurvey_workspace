# EMemBench EMemBench: Interactive Benchmarking of Episodic Memory for VLM Agents

## 0. Metadata
- Date: 2026/01
- Venue: arXiv
- Authors: Xinze Li, Ziyue Zhu, Siyuan Liu, Yubo Ma, Yuhang Zang, Yixin Cao, Aixin Sun
- Paper link: https://arxiv.org/pdf/2601.16690.pdf
- Code link: https://github.com/InternLM/EMemBench
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: high
- Review gate label: usable

## 1. One-paragraph benchmark summary
- EMemBench is a programmatic benchmark generator for episodic memory in interactive agents. Instead of evaluating memory with a fixed question set over prewritten histories, it lets an agent play interactive games, logs both observable and hidden game signals, and then generates verifiable questions from that specific trajectory. The benchmark is built on 15 Jericho interactive-fiction games plus the Crafter visual survival environment, balances seven ability families, and adds controls such as answerability preconditions, query-horizon limits, fixed seeds, and open-book versus closed-book human studies. For this survey, EMemBench is a strong representative of game-based memory diagnostics, but it should be used as evidence about trajectory-grounded evaluation rather than as a general game-performance benchmark.

## 2. Position in our survey
- Why-games relevance: Interactive games create individualized, eventful trajectories with exact underlying state, making it possible to generate grounded memory questions that are automatically answerable and verifiable.
- Historical stage: diagnostic capability probe
- Narrative level(s): L4 visual agency
- Most relevant outline section(s): 2,3,4
- Role in corpus: representative

## 3. Design-space coding
### 3.1 Environment structure
- Information structure: mixed
- Transition structure: mixed
- Agent structure: single-agent
- Social structure: N/A
- Time structure: mixed

### 3.2 World structure
- World type(s): adventure / open-world / other
- Real game / simulated game / designed task-game hybrid: curated suite using Jericho text games and Crafter as trajectory generators for memory evaluation
- Benchmark unit: trajectory plus generated QA set

### 3.3 Benchmark scope
- Scope: curated suite
- Number of games / tasks: 15 Jericho text games plus the Crafter visual game; Table 1 reports about 80 questions per trajectory on average, and the visual setting is averaged over 5 fixed seeds
- Benchmark intent: diagnostic evaluation

### 3.4 Modality
- Primary modality: mixed
- Perception burden retained: trajectory tracking, event binding, temporal ordering, spatial grounding, and partial observability in the underlying environments
- Perception burden removed: fixed hand-authored question sets and subjective post-hoc judging of answers

## 4. What this benchmark measures
- Primary capability target: episodic memory for interactive agents
- Secondary capability target(s): single-hop recall, multi-hop recall, induction, temporal reasoning, spatial reasoning, logical reasoning, and adversarial memory queries
- Does it test rule grounding / legal action generation? no
- Does it test strategic planning under uncertainty? no
- Does it test social reasoning / deception / cooperation? no
- Does it test visual grounding / spatial-temporal reasoning? yes
- Does it test long-horizon autonomy / task completion? partially
- Does it test real-time efficiency? no
- Does it test cross-game transfer / open-ended generalization? no
- Why is a game environment especially suitable here? Games provide long, structured trajectories with exact state logs, so the benchmark can derive memory questions from what the specific agent actually experienced.

## 5. Interaction paradigm
- Observation channel: Jericho text-game trajectories or Crafter visual observations and HUD signals, plus structured logging used for question generation and verification
- Action channel: normal game actions during trajectory generation, followed by post-episode question answering
- Interface type: API / hybrid
- Agent scaffold allowed: memory
- Is there privileged API access? yes for question generation and ground-truth computation; question answering itself is constrained to the agent's observable history plus its own memory
- How close is the setup to human play? medium-low; the underlying interaction is real, but the benchmark is instrumented around memory diagnosis rather than ordinary end-task play
- Main ecological-validity trade-off: EMemBench gains strong, individualized supervision by logging hidden state and generating templated questions, but that instrumentation makes it more diagnostic than naturalistic gameplay evaluation

## 6. Evaluation protocol
- Main score: overall ACC and F1 on trajectory-grounded questions
- Auxiliary score(s): per-ability breakdown, text versus visual results, query-horizon-control results, and open-book versus closed-book human studies
- Evaluation style: accuracy / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: strong LLM and VLM backbones are compared in direct in-context and memory-agent settings; humans are evaluated in both open-book and closed-book protocols
- Automatic verifiability: high
- Calibration method: answerability preconditions, balanced question-type distributions, query-horizon control, fixed environment and generation seeds, and optional paraphrase variants
- Anti-contamination argument: strong; questions are generated from each agent's own trajectories rather than drawn from a fixed public test set
- Reliability or comparability concerns: the template library defines what counts as memory ability, and the visual setting is currently centered on Crafter rather than a broader visual-game roster

## 7. Main contributions
- Contribution 1: Reframes episodic-memory evaluation as experience-conditioned benchmark generation rather than fixed-history QA.
- Contribution 2: Couples interactive gameplay with deterministic question generation and verifiable ground truth across seven memory abilities.
- Contribution 3: Shows that induction and spatially grounded memory remain major bottlenecks, especially in the visual setting.

## 8. Main findings and failure modes
- Core empirical takeaway: the benchmark is far from saturated, and induction plus spatial reasoning remain the hardest abilities, especially for visually grounded agents.
- Notable model failure mode 1: agents struggle to induce reusable patterns from prior events even when simpler recall is stronger
- Notable model failure mode 2: visual spatial memory is weak, suggesting difficulty binding transient observations into a stable episode-level representation
- Notable model failure mode 3: explicit persistent memory helps text-game settings more consistently than the visual setting, where gains are small or unstable
- Does this paper reveal a benchmark-design limitation as well? yes; it makes clear that fixed-history memory QA misses the memory-formation process that interactive agents actually need

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): A strong example of games serving as controllable generators of grounded, individualized evaluation data.
- Best use in Section 1 (taxonomy and evolutionary levels): Useful as a later-stage diagnostic branch where game trajectories are repurposed to measure memory rather than win rate or task completion.
- Best use in Section 2 (core capabilities evaluated by games): Direct support for long-horizon memory, temporal reasoning, and spatially grounded recall in interactive settings.
- Best use in Section 3 (interaction and evaluation paradigm): A strong reference for benchmark instrumentation, answerability control, and the effect of explicit memory modules.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Supports the claim that visually grounded episodic memory remains a major unresolved bottleneck.

## 10. Relation to nearby papers
- Closest predecessor(s): long-context memory QA benchmarks, StoryBench-style memory evaluation, and other memory-agent benchmarks that operate on fixed histories
- Closest follow-up(s): richer multimodal or open-world memory evaluations that extend trajectory-grounded QA beyond Jericho and Crafter
- Best comparison targets inside our corpus: `MineNPCTask`, `TextQuests`, `FlashAdventure`, `MCU`
- What this paper uniquely adds relative to neighbors: It generates verifiable memory tests from each agent's own trajectory and adds fairness controls such as query-horizon limits and open-book versus closed-book human studies.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- EMemBench builds on Jericho for text games and Crafter for the visual setting, and Table 1 summarizes the benchmark as covering 16 environments in total.
- The benchmark groups questions into seven ability families: single-hop, multi-hop, induction, spatial, temporal, logical, and adversarial.
- For visual games, the paper reports averages over five fixed seeds `{1, 42, 43, 100, 123}`; for text games, results are averaged over 15 games, and question generation uses seed 42.
- The paper includes both open-book and closed-book human studies and explicitly introduces query-horizon control to reduce unfairness from different trajectory lengths.

### 11.2 Our synthesis / interpretation
- EMemBench is one of the clearest examples in the corpus of how game environments can be repurposed into a benchmark generator rather than just a task suite.
- Its survey value is strongest in Sections 2 to 4, where it helps connect game benchmarks to broader questions about agent instrumentation, memory modules, and evaluation validity.

### 11.3 Uncertain or needs re-check
- If we later compare memory-agent architectures in detail, re-check the exact prompting and retrieval settings for Mem0, LangMem, and A-MEM.
- If we need broader claims about visual memory benchmarking, note that the visual branch currently depends on Crafter rather than on multiple distinct visual games.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? No immediate reread is required unless we later need exact prompting details for the memory-agent baselines or the full template inventory.
- Which section to read next if needed: 3 / 4 / human-study section / Appendix F
- Follow-up question(s): When we draft the memory subsection, should EMemBench anchor the discussion of trajectory-grounded evaluation design, or should that role be split with MineNPC-Task and FlashAdventure?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P1
- Reading depth: deep
- Batch ID: B06
- Outline sections: 2,3,4
- Survey role: representative
- Paper card path: `paper_cards/B06/EMemBench.md`
- Check status: unchecked
- Last updated: 2026-04-09
