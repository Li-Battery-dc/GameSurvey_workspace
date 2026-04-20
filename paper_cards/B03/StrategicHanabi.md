# StrategicHanabi Sparks of Cooperative Reasoning: LLMs as Strategic Hanabi Agents

## 0. Metadata
- Date: 2026/01
- Venue: arXiv
- Authors: Mahesh Ramesh, Kaousheik Jayakumar, Aswinkumar Ramkumar, Pavan Thodima, Aniket Rege, Emmanouil-Vasileios Vlatakis-Gkaragkounis
- Paper link: https://arxiv.org/pdf/2601.18077v2.pdf
- Code link:
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: medium
- Review gate label: usable

## 1. One-paragraph benchmark summary
- Sparks of Cooperative Reasoning uses Hanabi as a large-scale benchmark for cooperative reasoning under incomplete information. The paper evaluates 17 LLMs across 2-5 player settings, compares three progressively scaffolded setups (`basic`/Watson, `best`/Sherlock, and multi-turn `Mycroft`), and then turns the resulting trajectories into HanabiLogs and HanabiRewards for post-training. Its core value is that it treats benchmark scores, scaffold sensitivity, cross-play, and learnability as one connected cooperative-reasoning story rather than as isolated experiments. For this survey, it is a representative cooperative benchmark-plus-training-resource paper rather than a mere side contrast to deception benchmarks.

## 2. Position in our survey
- Why-games relevance: Hanabi makes hidden-state coordination and recursive partner modeling concrete while remaining fully scoreable.
- Historical stage: diagnostic capability probe
- Benchmark level(s): L3 social intelligence
- Most relevant outline section(s): 2,3,4
- Role in corpus: representative

## 3. Design-space coding
### 3.1 Game structure
- Information structure: imperfect
- Transition structure: deterministic
- Agent structure: multi-agent
- Social structure: cooperative
- Time structure: turn-based

### 3.2 World structure
- World type(s): card
- Real game / simulated game / designed task-game hybrid: real game adapted into an LLM benchmark
- Benchmark unit: full game

### 3.3 Benchmark scope
- Scope: single game
- Number of games / tasks: Hanabi games across 2-5 players with 17 evaluated models

### 3.4 Modality
- Observation modality: text or symbolic
- Action modality: semantic
- Perception burden retained: hidden information, partner coordination, hint interpretation, and state tracking
- Perception burden removed: physical card handling and face-to-face table interaction

## 4. What this benchmark measures
- Primary capability target: cooperative reasoning under incomplete information
- Secondary capability target(s): theory of mind, working-memory reliability, scaffold robustness, and fine-tuning potential
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? yes
- Does it test social reasoning / deception / cooperation? yes
- Does it test visual grounding / spatial-temporal reasoning? no
- Does it test long-horizon autonomy / task completion? yes
- Does it test real-time efficiency? no
- Does it test cross-game transfer / open-ended generalization? partially
- Why is a game environment especially suitable here? Hanabi requires reasoning about what teammates know, which makes cooperative cognition measurable through actual score and move quality.

## 5. Interaction paradigm
- Observation channel: textualized Hanabi state, HLE explicit knowledge, hint history, and scaffold-specific deductive or working-memory context
- Action channel: legal Hanabi actions plus move ratings and reasoning traces in scaffolded settings
- Interface type: natural language / structured action space / hybrid
- Agent scaffold allowed: memory / planner / other
- Is there privileged API access? yes
- How close is the setup to human play? low to medium; the game is real Hanabi, but explicit deductive context, legal action lists, and HLE feedback are more privileged than ordinary play
- Main ecological-validity trade-off: the benchmark cleanly probes cooperative reasoning, but stronger scaffolds move the setting away from raw, minimally assisted play by injecting engine-derived deductions

## 6. Evaluation protocol
- Main score: average Hanabi score out of 25 across player counts and scaffold settings
- Auxiliary score(s): scaffold comparisons, cross-play analysis, fine-tuning gains, and transfer to non-Hanabi cooperation or reasoning tasks
- Evaluation style: native score / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: same-model self-play teams are the main protocol; human play and specialist Hanabi agents are external references, and cross-play appears as an ablation
- Automatic verifiability: high
- Calibration method: evaluation across 2-5 players and across Watson, Sherlock, and Mycroft scaffold settings
- Anti-contamination argument: not central
- Reliability or comparability concerns: rankings depend materially on scaffold choice, engine-provided deductions are not human-like, and HanabiRewards uses LLM-provided move utilities that are not strictly verifiable

## 7. Main contributions
- Contribution 1: Evaluates 17 LLMs on Hanabi across multiple player counts and scaffold settings.
- Contribution 2: Releases HanabiLogs and HanabiRewards to support supervised and RL-style improvement.
- Contribution 3: Shows that fine-tuning on cooperative trajectories can improve both Hanabi play and some out-of-domain cooperative or reasoning tasks.

## 8. Main findings and failure modes
- Core empirical takeaway: top reasoning models reach roughly 15-18/25 with explicit scaffolds, but still trail specialist agents and strong human play, and they lose about 2-4 points when forced to track state implicitly in the multi-turn setting.
- Notable model failure mode 1: unreliable internal state tracking without explicit memory support
- Notable model failure mode 2: brittle partner coordination despite strong language-model competence
- Notable model failure mode 3: heavy dependence on scaffold design and training data for robust gains
- Does this paper reveal a benchmark-design limitation as well? yes; it highlights how much cooperative-benchmark results can change when memory and context engineering change

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Good evidence that cooperative games reveal hidden-state reasoning limits that ordinary QA misses.
- Best use in Section 1 (taxonomy and evolutionary levels): Supportive contrast inside the cooperation branch rather than a level-defining taxonomy anchor.
- Best use in Section 2 (core capabilities evaluated by games): Directly supports cooperation, ToM, and working-memory claims.
- Best use in Section 3 (interaction and evaluation paradigm): Helpful when discussing context engineering and memory scaffolds. Useful for comparing native score with scaffolded and trainable evaluation setups.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Supports the claim that social competence often depends on explicit memory support.

## 10. Relation to nearby papers
- Closest predecessor(s): LLM-Hanabi, earlier Hanabi AI work, cooperative ToM evaluations
- Closest follow-up(s): trainable cooperative-game benchmarks and broader coordination suites
- Best comparison targets inside our corpus: CollabOvercooked, LLMCoordination, WerewolfArena, LLMHanabi
- What this paper uniquely adds relative to neighbors: It combines cooperative benchmarking with scaffold ablations and training resources rather than treating Hanabi as a single frozen evaluation setup.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- The paper evaluates 17 state-of-the-art LLMs on Hanabi across 2-5 players.
- It compares minimal prompting with scaffolded settings named Watson, Sherlock, and Mycroft.
- The best reasoning models score roughly 15-18/25, while specialist agents and strong human play remain above 20/25.
- The authors release HanabiLogs with 1,520 annotated trajectories and HanabiRewards with 560 games carrying move-level utilities.
- RL fine-tuning a 4B Qwen model on HanabiRewards improves Hanabi performance by up to 156% and transfers to external cooperation and temporal-reasoning tasks.

### 11.2 Our synthesis / interpretation
- This paper is more than a raw benchmark card: it shows that cooperative results depend heavily on scaffold design and that benchmark trajectories can be repurposed for post-training.
- It is useful as a bridge from pure evaluation to benchmark-plus-training-resource work in cooperative games.

### 11.3 Uncertain or needs re-check
- Re-check the exact cross-play protocol and the strongest out-of-domain transfer numbers if we later use them in Section 7.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? Completed in this audit; the experiment setup, benchmark results, cross-play, fine-tuning, and future-work sections are now checked against the full paper and source.
- Which section to read next if needed: method / evaluation / appendices on HanabiLogs and HanabiRewards
- Follow-up question(s): How much of the gain comes from memory scaffolding versus domain-specific fine-tuning?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P1
- Reading depth: deep
- Batch ID: B03
- Outline sections: 2,3,4
- Survey role: representative
- Paper card path: `paper_cards/B03/StrategicHanabi.md`
- Check status: unchecked
- Next action: draft-section
- Last updated: 2026-04-10
