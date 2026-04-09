# AtariGPT Atari-GPT: Benchmarking Multimodal Large Language Models as Low-Level Policies in Atari Games

## 0. Metadata
- Date: 2024/08
- Venue: arXiv
- Authors: Nicholas R. Waytowich, Devin White, MD Sunbeam, Vinicius G. Goecks
- Paper link: https://arxiv.org/pdf/2408.15950v2.pdf
- Code link: https://github.com/nwayt001/atari-gpt
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: medium
- Review gate label: usable

## 1. One-paragraph benchmark summary
- Atari-GPT evaluates multimodal LLMs as low-level control policies on seven Atari games from the Arcade Learning Environment. Instead of testing high-level advice or textual planning only, the paper prompts models to output actual game actions from recent gameplay frames and compares them with human, DQN, and random baselines. The benchmark is narrower than recent multi-game visual suites, but it is still useful because it directly asks whether frontier multimodal models can act as Atari policies under partial temporal context. For this survey, it serves as a contrast case showing that even iconic RL environments remain difficult for general multimodal models.

## 2. Position in our survey
- Why-games relevance: Atari provides a compact way to test whether multimodal models can close the gap between visual understanding and low-level control.
- Historical stage: ecological agent benchmark
- Narrative level(s): L4 visual agency
- Most relevant outline section(s): 2,3,4
- Role in corpus: contrast

## 3. Design-space coding
### 3.1 Environment structure
- Information structure: mixed
- Transition structure: mixed
- Agent structure: single-agent
- Social structure: N/A
- Time structure: real-time

### 3.2 World structure
- World type(s): arcade / other
- Real game / simulated game / designed task-game hybrid: standardized arcade game suite in ALE
- Benchmark unit: game episode

### 3.3 Benchmark scope
- Scope: curated suite
- Number of games / tasks: 7 Atari games
- Benchmark intent: ecological evaluation

### 3.4 Modality
- Primary modality: image
- Perception burden retained: raw visual input and short temporal context over recent frames
- Perception burden removed: the interface is simplified to action selection rather than full human controller dexterity

## 4. What this benchmark measures
- Primary capability target: frame-conditioned control policy quality
- Secondary capability target(s): spatial reasoning, temporal tracking, and robustness across different arcade genres
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? partially
- Does it test social reasoning / deception / cooperation? no
- Does it test visual grounding / spatial-temporal reasoning? yes
- Does it test long-horizon autonomy / task completion? partially
- Does it test real-time efficiency? yes
- Does it test cross-game transfer / open-ended generalization? partially
- Why is a game environment especially suitable here? Atari gives a controlled, automatically scored test of whether multimodal models can act rather than only describe.

## 5. Interaction paradigm
- Observation channel: current frame plus recent gameplay frames from ALE
- Action channel: JSON or structured action output selecting an Atari move
- Interface type: structured action space / hybrid
- Agent scaffold allowed: none
- Is there privileged API access? no
- How close is the setup to human play? medium; the models see raw frames, but interaction is mediated through structured action generation
- Main ecological-validity trade-off: the benchmark preserves visual control but uses a limited temporal window and simplified prompting compared with richer game-agent setups

## 6. Evaluation protocol
- Main score: normalized game performance relative to human and random baselines
- Auxiliary score(s): per-game scores and comparisons to DQN baselines
- Evaluation style: native score
- Human baseline / AI anchor / self-play / model-vs-model setup: multimodal LLMs are compared with human, random, and DQN references
- Automatic verifiability: high
- Calibration method: fixed rollout protocol over 1000 timesteps with 8-frame skipping and consistent frame history
- Anti-contamination argument: evaluation is interactive and low-level rather than a static vision QA task
- Reliability or comparability concerns: the short evaluation horizon and restricted temporal context may under-measure long-horizon competence while still being strongly affected by latency

## 7. Main contributions
- Contribution 1: Frames Atari as a low-level multimodal control benchmark for LLMs.
- Contribution 2: Compares multiple frontier multimodal models against human, DQN, and random anchors.
- Contribution 3: Identifies visual-spatial reasoning and timing as major blockers for policy quality.

## 8. Main findings and failure modes
- Core empirical takeaway: multimodal LLMs beat random play on average but remain far below both humans and classical RL baselines.
- Notable model failure mode 1: weak spatial-temporal reasoning over fast-moving objects
- Notable model failure mode 2: inference latency relative to game dynamics
- Notable model failure mode 3: unstable policy quality across different Atari genres
- Does this paper reveal a benchmark-design limitation as well? yes; it shows that using LLMs as direct low-level policies is informative but also heavily system-limited

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Shows that interactive visual control exposes limitations not visible in static multimodal benchmarks.
- Best use in Section 1 (taxonomy and evolutionary levels): A useful transition from classical RL game environments to multimodal LLM evaluation. A narrow but concrete example of low-level policy benchmarking.
- Best use in Section 2 (core capabilities evaluated by games): Supports discussion of spatial-temporal reasoning and reactive control.
- Best use in Section 3 (interaction and evaluation paradigm): Contrasts structured action outputs with natural-language action interfaces. Good for discussing normalized human-relative score reporting.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Supports the argument that frontier MLLMs still trail classical game agents in reactive environments.

## 10. Relation to nearby papers
- Closest predecessor(s): Balrog, GameplayQA
- Closest follow-up(s): VideoGameBench, V-MAGE
- Best comparison targets inside our corpus: Balrog, VideoGameBench, VMage, LMGAME-BENCH
- What this paper uniquely adds relative to neighbors: It asks frontier MLLMs to operate directly as low-level Atari policies rather than as planners over a more abstracted harness.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- The benchmark evaluates seven Atari games from ALE.
- The rollout protocol uses 1000 timesteps, 8-frame skipping, and recent-frame context.
- Reported average normalized performance is 23.2% for GPT-4o, 18.36% for GPT-4V, 12.36% for Claude 3 Haiku, and 8.5% for Gemini 1.5 Flash.

### 11.2 Our synthesis / interpretation
- Atari-GPT is not the strongest benchmark-design paper in the corpus, but it is useful as a clean contrast showing that popular RL domains are still challenging for multimodal LLMs.
- It is especially helpful when discussing how much "general" multimodal intelligence still lags specialized control systems.

### 11.3 Uncertain or needs re-check
- Re-check the exact seven Atari titles if we later need a detailed comparison table.
- Re-check whether the models were allowed any task-specific prompt variations beyond the main shared protocol.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? Only if later survey drafting needs the exact per-game failure patterns or rollout details.
- Which section to read next if needed: evaluation setup / per-game results / discussion
- Follow-up question(s): How much of the remaining gap comes from latency versus policy weakness after perception?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P2
- Reading depth: deep
- Batch ID: B09
- Outline sections: 2,3,4
- Survey role: contrast
- Paper card path: `paper_cards/B09/AtariGPT.md`
- Next action: draft-section
- Last updated: 2026-04-05
