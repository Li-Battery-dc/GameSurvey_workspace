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
- BALROG is a broad benchmark and framework for evaluating long-context LLMs and VLMs as sequential decision-making agents across challenging game environments. It bundles environments such as BabyAI, Crafter, TextWorld, Baba Is AI, MiniHack, and NetHack, and evaluates zero-shot agents that produce natural-language actions from either language-only or vision-language observations. The benchmark explicitly decouples models from prompting strategies and reports standardized progression across tasks. For this survey, BALROG is a core visual/ecological anchor because it covers a wide range from simple navigation to very hard long-horizon environments.

## 2. Position in our survey
- Why-games relevance: It uses games to stress sequential planning, exploration, spatial reasoning, and rule discovery under far richer dynamics than static multimodal benchmarks.
- Historical stage: ecological agent benchmark
- Narrative level(s): L4 visual agency
- Most relevant outline section(s): 0,2,3,4,5,6
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
- Benchmark intent: ecological evaluation

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
- Agent scaffold allowed: none
- Is there privileged API access? yes
- How close is the setup to human play? medium; the benchmark keeps sequential gameplay but often supplements raw observations with language wrappers
- Main ecological-validity trade-off: BALROG reaches harder environments than many earlier suites, but still relies on wrapper descriptions and standardized action prompting.

## 6. Evaluation protocol
- Main score: standardized progression across environments
- Auxiliary score(s): task-specific progress metrics and invalid-action trajectory statistics
- Evaluation style: hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: model-only baseline leaderboard across environments
- Automatic verifiability: high
- Calibration method: unified zero-shot protocol with multiple seeds and per-environment progress normalization
- Anti-contamination argument: diverse games and hard exploration tasks reduce simple benchmark memorization value
- Reliability or comparability concerns: wrapper quality and the choice of language-only versus vision-language format materially affect results

## 7. Main contributions
- Contribution 1: Packages a diverse suite of hard game environments for LLM/VLM agent evaluation.
- Contribution 2: Standardizes zero-shot agent evaluation while allowing prompt-strategy submissions.
- Contribution 3: Shows that many frontier models plateau far below competent play on the hardest tasks.

## 8. Main findings and failure modes
- Core empirical takeaway: Even strong frontier models make only modest average progress, and the hardest environments such as MiniHack and NetHack remain largely unsolved.
- Notable model failure mode 1: weak systematic exploration
- Notable model failure mode 2: brittle long-term planning in puzzle and open-world tasks
- Notable model failure mode 3: vision inputs sometimes degrade performance rather than helping
- Does this paper reveal a benchmark-design limitation as well? yes; results can depend on language wrappers and fallback handling for invalid actions

## 9. Why this paper matters for our survey
- Best use in Section 0 (why games): Strong evidence that games can still challenge frontier multimodal models on long-horizon interaction.
- Best use in Section 1 (historical evolution): Represents the shift toward broader ecological suites after earlier symbolic/formal benchmarks.
- Best use in Section 2 (design space): Useful overview paper for mixed environment structure and modality.
- Best use in Section 3 (capability targets): Supports planning, exploration, and spatial reasoning claims.
- Best use in Section 4 (interaction paradigm): Good comparison case for language wrappers versus image-plus-language observations.
- Best use in Section 5 (evaluation protocol): Relevant for standardized progression metrics and invalid-action handling.
- Best use in Section 6/7 (limitations and future): Strong evidence for persistent exploration and planning failures.

## 10. Relation to nearby papers
- Closest predecessor(s): SmartPlay and earlier RL-game benchmark suites
- Closest follow-up(s): Orak, GameVerse
- Best comparison targets inside our corpus: SmartPlay, Orak, GameVerse, FlashAdventure
- What this paper uniquely adds relative to neighbors: It is one of the clearest broad-suite baselines for frontier LLMs and VLMs on long-context game environments.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- BALROG evaluates agents on BabyAI, Crafter, TextWorld, Baba Is AI, MiniHack, and NetHack.
- Agents output natural-language actions from either language-only or vision-language observations under a unified protocol.
- The reported results show moderate progress on easier suites and near-flat performance on the hardest environments.

### 11.2 Our synthesis / interpretation
- BALROG is best used as a central bridge from symbolic game probes to more ecological agent benchmarks.
- The benchmark’s use of both language and vision formats makes it especially useful when discussing privileged interfaces.

### 11.3 Uncertain or needs re-check
- Recheck the appendices if we later need exact per-environment task counts or the precise standardized-progression definition.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? No immediate reread; the suite structure and results are already strong enough for synthesis.
- Which section to read next if needed: 2.1 / 3.1 / 4.1
- Follow-up question(s): Which BALROG environments are the cleanest cross-paper comparison targets for long-horizon autonomy?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P0
- Reading depth: deep
- Batch ID: B03
- Outline sections: 0,2,3,4,5,6
- Survey role: anchor
- Paper card path: `paper_cards/B03/Balrog.md`
- Next action: draft-section
- Last updated: 2026-04-05
