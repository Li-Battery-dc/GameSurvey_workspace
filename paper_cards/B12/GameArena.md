# GameArena GameArena: Evaluating LLM Reasoning through Live Computer Games

## 0. Metadata
- Date: 2024/12
- Venue: ICLR 2025
- Authors: Lanxiang Hu, Qiyu Li, Anze Xie, Nan Jiang, Ion Stoica, Haojian Jin, Hao Zhang
- Paper link: https://arxiv.org/pdf/2412.06394v5.pdf
- Code link: https://github.com/lmgame-org
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: high
- Review gate label: strong

## 1. One-paragraph benchmark summary
- GameArena is a dynamic benchmark for evaluating reasoning through live human-LLM game play rather than static datasets or generic preference voting. It uses three social games, Akinator, Taboo, and Bluffing, each chosen to emphasize different reasoning types such as deductive, abductive, inductive, and multi-hop reasoning. Beyond game outcomes, it retroactively reconstructs intermediate reasoning signals from game histories to score specific reasoning capabilities. For this survey, GameArena is a strong bridge between game benchmarking and in-the-wild dynamic evaluation.

## 2. Position in our survey
- Why-games relevance: Games can gather stepwise reasoning traces from real human interaction while keeping players engaged enough to generate fresh evaluation data.
- Historical stage: diagnostic capability probe
- Narrative level(s): L2 strategic reasoning / L3 social intelligence
- Most relevant outline section(s): 0,1,2,3,4
- Role in corpus: representative

## 3. Design-space coding
### 3.1 Environment structure
- Information structure: imperfect
- Transition structure: mixed
- Agent structure: multi-agent / human-model interaction
- Social structure: mixed
- Time structure: turn-based

### 3.2 World structure
- World type(s): social deduction / guessing / other
- Real game / simulated game / designed task-game hybrid: benchmark suite built from existing human-playable conversational games
- Benchmark unit: game session

### 3.3 Benchmark scope
- Scope: curated suite
- Number of games / tasks: 3 games with 2,000+ collected sessions
- Benchmark intent: diagnostic evaluation / live evaluation

### 3.4 Modality
- Primary modality: text
- Perception burden retained: multi-turn dialogue interpretation and human interaction
- Perception burden removed: no visual or embodied interface

## 4. What this benchmark measures
- Primary capability target: dynamic reasoning in live human interaction
- Secondary capability target(s): deductive, abductive, inductive, and multi-hop reasoning under dialogue constraints
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? yes
- Does it test social reasoning / deception / cooperation? yes
- Does it test visual grounding / spatial-temporal reasoning? no
- Does it test long-horizon autonomy / task completion? partially
- Does it test real-time efficiency? no
- Does it test cross-game transfer / open-ended generalization? partially
- Why is a game environment especially suitable here? Games produce fresh, engaging human interaction while constraining evaluation enough to score particular reasoning skills.

## 5. Interaction paradigm
- Observation channel: live human text input under game-specific rules
- Action channel: model questions, answers, guesses, and judgments
- Interface type: natural language
- Agent scaffold allowed: retrospective analysis
- Is there privileged API access? no during play; retrospective prompts are used later for analysis
- How close is the setup to human play? high; the benchmark uses real humans interacting with the models in live game sessions
- Main ecological-validity trade-off: the benchmark is highly natural in interaction, but the retrospective reasoning reconstruction is an analysis layer rather than an online capability

## 6. Evaluation protocol
- Main score: game win rate
- Auxiliary score(s): average rounds and capability-specific retrospective metrics derived from intermediate predictions
- Evaluation style: win rate / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: multiple frontier LLMs play against humans, and user studies compare GameArena with Chatbot Arena
- Automatic verifiability: mixed; some outcomes are rule-based while some judgments rely on game-specific verification
- Calibration method: randomized prompts, multiple models, and retrospective analysis under fixed replay conditions
- Anti-contamination argument: live human game sessions prevent fixed benchmark saturation
- Reliability or comparability concerns: retrospective analysis asks models to reveal hidden intermediate thoughts after the fact, which may not perfectly match their original online reasoning

## 7. Main contributions
- Contribution 1: Introduces a live human-game benchmark focused on reasoning rather than generic preference.
- Contribution 2: Maps three games onto different reasoning types and extracts capability-specific metrics.
- Contribution 3: Shows games can collect more useful reasoning data in the wild than open-ended arena chat.

## 8. Main findings and failure modes
- Core empirical takeaway: dynamic game evaluation produces more targeted reasoning evidence than generic chat arenas, and model rankings can differ from style-biased leaderboards.
- Notable model failure mode 1: poor strategic questioning in Akinator and Bluffing
- Notable model failure mode 2: difficulty integrating clues across multiple turns in Taboo-like settings
- Notable model failure mode 3: inconsistent rule following or weak hidden-state tracking during live play
- Does this paper reveal a benchmark-design limitation as well? yes; it shows that human preference arenas conflate reasoning with stylistic preference and need more structured alternatives

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Strong argument that games can make evaluation engaging enough to generate fresh dynamic data.
- Best use in Section 1 (taxonomy and evolutionary levels): Useful in the shift from static test suites and preference arenas to live interactive reasoning benchmarks. Helps define human-in-the-loop dynamic game benchmarks.
- Best use in Section 2 (core capabilities evaluated by games): Strong source for mapping games to distinct reasoning types.
- Best use in Section 3 (interaction and evaluation paradigm): An anchor for natural-language-only live interaction. Useful for retrospective analysis of intermediate reasoning signals.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Supports future benchmarks that combine human freshness with stronger automatic verification.

## 10. Relation to nearby papers
- Closest predecessor(s): Chatbot Arena
- Closest follow-up(s): other live-eval platforms
- Best comparison targets inside our corpus: AvalonBench, GAMEBoT, DSGBench
- What this paper uniquely adds relative to neighbors: It uses live human gameplay to gather dynamic reasoning evidence instead of only offline game simulations.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- GameArena consists of Akinator, Taboo, and Bluffing and was evaluated on over 2,000 game sessions.
- It performs retrospective analysis to extract intermediate reasoning signals such as ranked candidate lists or truthfulness judgments.
- A user study with 100 participants reported better engagement than Chatbot Arena.

### 11.2 Our synthesis / interpretation
- GameArena is one of the best corpus examples of using games to collect fresh reasoning data in the wild.
- It is especially useful when arguing that dynamic evaluation can be both informative and engaging.

### 11.3 Uncertain or needs re-check
- Re-check the exact model ranking differences against Chatbot Arena if later drafting uses them explicitly.
- Re-check the percentage of "useful" sessions versus Chatbot Arena for a quantitative comparison.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? Yes later, especially for the retrospective-analysis methodology.
- Which section to read next if needed: game design / retrospective analysis / user study
- Follow-up question(s): How stable are retrospective reasoning metrics across different replay prompts?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P1
- Reading depth: deep
- Batch ID: B12
- Outline sections: 0,1,2,3,4
- Survey role: representative
- Paper card path: `paper_cards/B12/GameArena.md`
- Next action: draft-section
- Last updated: 2026-04-05
