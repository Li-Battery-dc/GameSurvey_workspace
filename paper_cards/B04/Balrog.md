# Balrog BALROG

## 0. Metadata
- Date: 2024/11
- Venue: ICLR 2025
- Authors: Davide Paglieri, Bartłomiej Cupiał, Samuel Coward, Ulyana Piterbarg, Maciej Wolczyk, Akbir Khan, Eduardo Pignatelli, Łukasz Kuciński, Lerrel Pinto, Rob Fergus, Jakob Nicolaus Foerster, Jack Parker-Holder, Tim Rocktäschel
- Paper link: https://arxiv.org/pdf/2411.13543v2
- Code link: https://github.com/balrog-ai/BALROG
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: high
- Review gate label: strong

## 1. One-paragraph benchmark summary
- BALROG is a benchmark and toolkit for evaluating long-context LLM and VLM agents on six game and RL environment families: BabyAI, Crafter, TextWorld, Baba Is AI, MiniHack, and NetHack. The paper reports zero-shot baselines in which agents output natural-language actions from language-wrapped observations, with optional current-frame images for VLM mode, and scores each environment on a standardized 0-100 progression scale. Because the environments are procedurally generated and range from relatively simple navigation to extremely hard long-horizon play, BALROG is a strong bridge from wrapper-heavy diagnostic evaluation toward harder ecological game suites. For this survey, it is best used as an ecological benchmark with important interface-privilege caveats, not as a pure human-like play benchmark.

## 2. Position in our survey
- Why-games relevance: It uses games to stress sequential planning, exploration, spatial reasoning, and rule discovery under far richer dynamics than static multimodal benchmarks.
- Historical stage: ecological agent benchmark
- Narrative level(s): L4 visual agency
- Most relevant outline section(s): 0,1,2,3,4
- Role in corpus: anchor

## 3. Design-space coding
### 3.1 Environment structure
- Information structure: mixed
- Transition structure: mixed
- Agent structure: single-agent
- Social structure: N/A
- Time structure: turn-based

### 3.2 World structure
- World type(s): puzzle / adventure / sandbox / open-world / other
- Real game / simulated game / designed task-game hybrid: curated suite of existing RL and game environments
- Benchmark unit: episode

### 3.3 Benchmark scope
- Scope: curated suite
- Number of games / tasks: 6 environment families spanning multiple task sets

### 3.4 Modality
- Primary modality: mixed
- Perception burden retained: language descriptions, optional images, long interaction history, exploration and planning demands
- Perception burden removed: some environments rely on text wrappers or combined image-plus-description inputs rather than raw play alone

## 4. What this benchmark measures
- Primary capability target: long-context agentic decision making
- Secondary capability target(s): spatial reasoning, systematic exploration, long-term planning, mechanic inference
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? yes
- Does it test social reasoning / deception / cooperation? no
- Does it test visual grounding / spatial-temporal reasoning? yes
- Does it test long-horizon autonomy / task completion? yes
- Does it test real-time efficiency? no
- Does it test cross-game transfer / open-ended generalization? partially
- Why is a game environment especially suitable here? The suite can keep precise automated scoring while spanning very different planning and observation regimes.

## 5. Interaction paradigm
- Observation channel: language-only descriptions or image-plus-description observations with history
- Action channel: natural-language action strings
- Interface type: natural language / hybrid
- Agent scaffold allowed: none in the reported zero-shot baselines; the released toolkit also supports alternative inference-time strategies such as few-shot prompting
- Is there privileged API access? partially; most environments are exposed through text wrappers, action lists, and invalid-action fallback handling rather than pure raw play
- How close is the setup to human play? low to medium; it preserves sequential gameplay, but the wrappers, action normalization, and fallback actions simplify perception and control
- Main ecological-validity trade-off: BALROG reaches much harder long-context environments than many earlier suites, but it does so through standardized language wrappers rather than end-to-end human-like interfaces

## 6. Evaluation protocol
- Main score: standardized progression across environments
- Auxiliary score(s): per-environment progress metrics and invalid-action trajectory statistics
- Evaluation style: hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: model-only zero-shot baseline leaderboard across environments; no human baseline in the paper
- Automatic verifiability: high
- Calibration method: unified zero-shot protocol, multiple seeds, per-environment normalization to 0-100, and a bespoke NetHack progression metric
- Anti-contamination argument: all six environments are procedurally generated, so exact instances are unlikely to repeat
- Reliability or comparability concerns: wrapper quality, fallback handling for invalid actions, and the choice of language-only versus vision-language observations materially affect results

## 7. Main contributions
- Contribution 1: Packages a diverse suite of hard game environments for LLM/VLM agent evaluation.
- Contribution 2: Standardizes zero-shot agent evaluation while allowing prompt-strategy submissions.
- Contribution 3: Shows that many frontier models plateau far below competent play on the hardest tasks.

## 8. Main findings and failure modes
- Core empirical takeaway: Even strong frontier models make only modest average progress overall, while MiniHack and NetHack remain nearly unsolved.
- Notable model failure mode 1: weak systematic exploration
- Notable model failure mode 2: brittle long-term planning in puzzle and open-world tasks
- Notable model failure mode 3: many models degrade when image observations are added, despite the benchmark's environments being visually grounded
- Does this paper reveal a benchmark-design limitation as well? yes; results depend strongly on wrappers, textification choices, and invalid-action handling

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Strong evidence that games can still challenge frontier multimodal models on long-horizon interaction.
- Best use in Section 1 (taxonomy and evolutionary levels): Represents the move from narrow formal probes toward broader ecological suites, while still exposing heavy interface abstraction.
- Best use in Section 2 (core capabilities evaluated by games): Supports planning, exploration, spatial reasoning, and long-context decision-making claims.
- Best use in Section 3 (interaction and evaluation paradigm): Strong comparison case for language wrappers, optional image observations, per-environment normalization, and invalid-action fallback.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Strong evidence for exploration and planning failures, plus a cautionary case on interface privilege inside "ecological" benchmarks.

## 10. Relation to nearby papers
- Closest predecessor(s): environment-specific benchmark lines such as BabyAI, Crafter, MiniHack, NetHack, and TextWorld, plus earlier rule-grounded agent benchmarks
- Closest follow-up(s): Orak and GameVerse as broader modern suites for visually grounded game agents
- Best comparison targets inside our corpus: FlashAdventure, GameplayQA, StarBench, VideoGameBench
- What this paper uniquely adds relative to neighbors: It is one of the clearest broad-suite baselines for frontier long-context LLMs and VLMs on procedurally generated game environments under a unified protocol.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- BALROG evaluates agents on BabyAI, Crafter, TextWorld, Baba Is AI, MiniHack, and NetHack.
- The reported baselines are zero-shot: agents output natural-language actions from language-wrapped observations, with optional current-frame images in VLM mode.
- Scores are standardized to a 0-100 progression scale, with a bespoke progression metric for NetHack.
- The environments are procedurally generated, and the paper reports strong performance gaps between easier suites and the hardest long-horizon tasks.

### 11.2 Our synthesis / interpretation
- BALROG is best used as a bridge paper: it broadens ecological scope substantially, but its wrappers still make it an interface-privileged benchmark rather than a human-like play benchmark.
- Its paired language-only and VLM settings make it especially useful for discussing how interface design can dominate conclusions about multimodal agent competence.

### 11.3 Uncertain or needs re-check
- Recheck the appendices if we later need exact per-environment task counts, the full observation prompts, or the precise NetHack progression construction.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? No immediate reread; the suite structure and results are already strong enough for synthesis.
- Which section to read next if needed: 3 / 4 / NetHack appendix
- Follow-up question(s): Which BALROG environments are the cleanest cross-paper comparison targets for long-horizon autonomy?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P0
- Reading depth: deep
- Batch ID: B04
- Outline sections: 0,1,2,3,4
- Survey role: anchor
- Paper card path: `paper_cards/B04/Balrog.md`
- Next action: draft-section
- Last updated: 2026-04-10
