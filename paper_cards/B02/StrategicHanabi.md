# StrategicHanabi Sparks of Cooperative Reasoning: LLMs as Strategic Hanabi Agents

## 0. Metadata
- Date: 2026/01
- Venue: arXiv
- Authors: Mahesh Ramesh, Kaousheik Jayakumar, Aswinkumar Ramkumar, Pavan Thodima, Aniket Rege, Emmanouil-Vasileios Vlatakis-Gkaragkounis
- Paper link: https://arxiv.org/pdf/2601.18077.pdf
- Code link:
- Reading depth: deep
- Card status: card-draft
- Confidence in this card: medium
- Review gate label: usable

## 1. One-paragraph benchmark summary
- Sparks of Cooperative Reasoning uses Hanabi as a large-scale benchmark for cooperative reasoning under incomplete information. The paper evaluates 17 LLMs across 2-5 player settings, compares several prompt-and-memory scaffolds, and releases training resources in the form of HanabiLogs and HanabiRewards. Its core value is that it treats cooperative play quality, scaffold robustness, and learnability as connected questions rather than measuring one static prompt setting. For this survey, it is a useful counterpart to both deception-oriented social benchmarks and the narrower ToM-focused Hanabi papers already in the corpus.

## 2. Position in our survey
- Why-games relevance: Hanabi makes hidden-state coordination and recursive partner modeling concrete while remaining fully scoreable.
- Historical stage: diagnostic capability probe
- Narrative level(s): L3 social intelligence
- Most relevant outline section(s): 2,3,5,6
- Role in corpus: contrast

## 3. Design-space coding
### 3.1 Environment structure
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
- Benchmark intent: diagnostic evaluation / train+eval foundation

### 3.4 Modality
- Primary modality: text / symbolic state
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
- Observation channel: textualized Hanabi state, hint history, public game context, and scaffold-specific memory context
- Action channel: legal Hanabi actions and generated reasoning traces under scaffolded settings
- Interface type: natural language / structured action space / hybrid
- Agent scaffold allowed: memory / other
- Is there privileged API access? yes
- How close is the setup to human play? medium; the game is preserved, but scaffold engineering and textual state exposure reduce ordinary play friction
- Main ecological-validity trade-off: the benchmark cleanly probes cooperative reasoning, but stronger scaffolds move the setting away from raw, minimally assisted play

## 6. Evaluation protocol
- Main score: Hanabi game score
- Auxiliary score(s): scaffold comparisons, cross-play analysis, fine-tuning gains, and transfer to non-Hanabi cooperation or reasoning tasks
- Evaluation style: native score / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: model cross-play plus comparison to specialist human experts
- Automatic verifiability: high
- Calibration method: evaluation across 2-5 players and across Watson, Sherlock, and Mycroft scaffold settings
- Anti-contamination argument: not central
- Reliability or comparability concerns: the benchmark is informative, but rankings depend materially on scaffold choice and on whether models are evaluated zero-shot or after domain-specific training

## 7. Main contributions
- Contribution 1: Evaluates 17 LLMs on Hanabi across multiple player counts and scaffold settings.
- Contribution 2: Releases HanabiLogs and HanabiRewards to support supervised and RL-style improvement.
- Contribution 3: Shows that fine-tuning on cooperative trajectories can improve both Hanabi play and some out-of-domain cooperative or reasoning tasks.

## 8. Main findings and failure modes
- Core empirical takeaway: top models improve with stronger scaffolds, but even the best scores remain well below specialist human experts.
- Notable model failure mode 1: unreliable internal state tracking without explicit memory support
- Notable model failure mode 2: brittle partner coordination despite strong language-model competence
- Notable model failure mode 3: heavy dependence on scaffold design and training data for robust gains
- Does this paper reveal a benchmark-design limitation as well? yes; it highlights how much cooperative-benchmark results can change when memory and context engineering change

## 9. Why this paper matters for our survey
- Best use in Section 0 (why games): Good evidence that cooperative games reveal hidden-state reasoning limits that ordinary QA misses.
- Best use in Section 1 (historical evolution): Useful for the cooperative branch of social benchmark evolution.
- Best use in Section 2 (design space): Strong single-game cooperative imperfect-information case.
- Best use in Section 3 (capability targets): Directly supports cooperation, ToM, and working-memory claims.
- Best use in Section 4 (interaction paradigm): Helpful when discussing context engineering and memory scaffolds.
- Best use in Section 5 (evaluation protocol): Useful for comparing native score with scaffolded and trainable evaluation setups.
- Best use in Section 6/7 (limitations and future): Supports the claim that social competence often depends on explicit memory support.

## 10. Relation to nearby papers
- Closest predecessor(s): LLM-Hanabi, earlier Hanabi AI work, cooperative ToM evaluations
- Closest follow-up(s): trainable cooperative-game benchmarks and broader coordination suites
- Best comparison targets inside our corpus: LLMHanabi, WerewolfArena, LLMCoordination, CollabOvercooked
- What this paper uniquely adds relative to neighbors: It combines cooperative benchmarking with scaffold ablations and training resources rather than treating Hanabi as a single frozen evaluation setup.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- The paper evaluates 17 state-of-the-art LLMs on Hanabi across 2-5 players.
- It compares minimal prompting with scaffolded settings named Watson, Sherlock, and Mycroft.
- The authors report that the best models score around 15/25, still trailing specialist human experts above 20/25, and release HanabiLogs plus HanabiRewards.

### 11.2 Our synthesis / interpretation
- This paper is a stronger systems-and-benchmark card than LLM-Hanabi because it makes scaffold dependence and learnability explicit.
- It is useful as a bridge from pure evaluation to benchmark-plus-training-resource work in cooperative games.

### 11.3 Uncertain or needs re-check
- Re-check the exact cross-play protocol and the strongest out-of-domain transfer numbers if we later use them in Section 7.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? Yes, because the scaffold design and transfer results likely matter for later synthesis.
- Which section to read next if needed: method / evaluation / appendices on HanabiLogs and HanabiRewards
- Follow-up question(s): How much of the gain comes from memory scaffolding versus domain-specific fine-tuning?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-draft
- Priority: P1
- Reading depth: deep
- Batch ID: B02
- Outline sections: 2,3,5,6
- Survey role: contrast
- Paper card path: `paper_cards/B02/StrategicHanabi.md`
- Next action: review-card
- Last updated: 2026-04-06
