# GameArena GameArena: Evaluating LLM Reasoning through Live Computer Games

## 0. Metadata
- Date: 2024/12
- Venue: ICLR 2025
- Authors: Lanxiang Hu, Qiyu Li, Anze Xie, Nan Jiang, Ion Stoica, Haojian Jin, Hao Zhang
- Paper link: https://arxiv.org/pdf/2412.06394v5.pdf
- Code link: https://github.com/lmgame-org
- Reading depth: deep
- Card status: finalized
- Confidence in this card: high
- Review gate label: strong

## 1. One-paragraph benchmark summary
- GameArena is a dynamic benchmark for evaluating reasoning through live human-LLM gameplay rather than static datasets or generic preference voting. It uses three conversational games, Akinator, Taboo, and Bluffing, each chosen to emphasize deductive, abductive, inductive, and multi-hop reasoning under multi-turn interaction. Beyond game outcomes, the paper replays finished sessions and retrospectively queries the same model for ranked candidate lists or truthfulness judgments, turning live gameplay logs into capability-specific reasoning metrics. For this survey, GameArena is a strong bridge between game benchmarking, human-in-the-loop dynamic evaluation, and post-hoc process analysis.

## 2. Position in our survey
- Why-games relevance: Games can gather stepwise reasoning traces from real human interaction while keeping players engaged enough to generate fresh evaluation data.
- Historical stage: diagnostic capability probe
- Benchmark level(s): L2 strategic reasoning / L3 social intelligence
- Most relevant outline section(s): 0,1,3,4
- Role in corpus: representative

## 3. Design-space coding
### 3.1 Structure
- Form: Dialogue
- Construction: Adapted
- Construction note: benchmark suite built from existing human-playable conversational games
- Benchmark unit: game session

### 3.2 Mechanics profile
- State visibility: partial
- Transition uncertainty: mixed
- Actor configuration: multi-agent
- Incentive structure: mixed
- Temporal regime: turn-based

### 3.3 Benchmark scope
- Scope: curated suite
- Number of games / tasks: 3 games with 2,000+ collected sessions

### 3.4 Modality
- Observation modality: text or symbolic
- Action modality: semantic
- Perception burden retained: multi-turn dialogue interpretation and human interaction
- Perception burden removed: no visual or embodied interface

## 4. What this benchmark measures
- Primary capability target: dynamic reasoning in live human interaction
- Secondary capability target(s): deductive, abductive, inductive, and multi-hop reasoning under dialogue constraints
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? partially
- Does it test social reasoning / deception / cooperation? yes
- Does it test visual grounding / spatial-temporal reasoning? no
- Does it test long-horizon autonomy / task completion? partially
- Does it test real-time efficiency? no
- Does it test cross-game transfer / open-ended generalization? no
- Why is a game environment especially suitable here? Games produce fresh, engaging human interaction while constraining evaluation enough to score particular reasoning skills.

## 5. Interaction paradigm
- Observation channel: live human text input under game-specific rules
- Action channel: model questions, answers, guesses, and judgments
- Interface type: natural language
- Agent scaffold allowed: none during gameplay; retrospective replay is added only for evaluation
- Is there privileged API access? no during play; retrospective prompts are used later for analysis
- How close is the setup to human play? high; the benchmark uses real humans interacting with the models in live game sessions
- Main ecological-validity trade-off: the benchmark is highly natural in interaction, but the retrospective reasoning reconstruction is an analysis layer rather than an online capability

## 6. Evaluation protocol
- Main score: game win rate
- Auxiliary score(s): average rounds and capability-specific retrospective metrics derived from intermediate predictions
- Evaluation style: win rate / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: five frontier LLMs are paired with humans across 2,240 sessions; the paper also compares data efficiency and user experience against Chatbot Arena
- Automatic verifiability: mixed; some outcomes are rule-based while some judgments rely on game-specific verification
- Calibration method: random pairing of games and models, DSPy-based system-prompt search with five optimized prompts per game, and retrospective replay under the original prompt/history settings
- Anti-contamination argument: live human game sessions prevent fixed benchmark saturation
- Reliability or comparability concerns: retrospective analysis asks models to reveal hidden intermediate thoughts after the fact, which may not perfectly match their original online reasoning

## 7. Main contributions
- Contribution 1: Introduces a live human-game benchmark focused on reasoning rather than generic preference.
- Contribution 2: Maps three games onto different reasoning types and extracts capability-specific metrics.
- Contribution 3: Shows games can collect more useful reasoning data in the wild than open-ended arena chat.

## 8. Main findings and failure modes
- Core empirical takeaway: dynamic game evaluation produces more targeted reasoning evidence than generic chat arenas, and model rankings on outcome or procedural reasoning metrics can differ from style-biased leaderboards such as Chatbot Arena.
- Notable model failure mode 1: poor strategic questioning in Akinator and Bluffing
- Notable model failure mode 2: difficulty integrating clues across multiple turns in Taboo-like settings
- Notable model failure mode 3: conservative or inconsistent truthfulness judgments in Bluffing, with some models failing to make a final prediction within the round limit
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
- Best comparison targets inside our corpus: GAMEBoT, Clembench, Clembench2024, ThirdParadigm
- What this paper uniquely adds relative to neighbors: It uses live human gameplay to gather dynamic reasoning evidence instead of only offline game simulations.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- GameArena consists of Akinator, Taboo, and Bluffing and was evaluated on over 2,000 game sessions.
- The paper maps Akinator to deductive multi-hop reasoning, Taboo to abductive multi-hop reasoning, and Bluffing to inductive multi-hop reasoning.
- It evaluates 2,240 game sessions collected over 10 weeks and performs retrospective analysis to extract intermediate reasoning signals such as ranked candidate lists or truthfulness judgments.
- The setup evaluates GPT-4o, Claude 3.5 Sonnet, Gemini-1.5 Pro, Mistral Large 2, and LLaMA-3.1 405B, with DSPy prompt search producing five optimized prompts per game.
- GameArena reports 86.9% useful completed sessions versus 4% useful conversations in Chatbot Arena, and a 100-participant user study found higher enjoyment, satisfaction, and willingness to participate.
- The paper reports that procedural reasoning metrics can rank models differently from outcome win rate and from broad preference/ranking benchmarks, making it useful for separating live-game success from reasoning-process signals.

### 11.2 Our synthesis / interpretation
- GameArena is one of the best corpus examples of using games to collect fresh reasoning data in the wild.
- It is especially useful when arguing that dynamic evaluation can be both informative and engaging, but its strongest reasoning claims depend on retrospective replay rather than solely on online outcomes.

### 11.3 Uncertain or needs re-check
- Re-check Table 4 if later drafting uses rank-agreement comparisons with LiveBench-Reasoning, GPQA, or Chatbot Arena.
- Re-check whether a later paragraph should cite outcome rankings, procedural rankings, or both for a given reasoning claim.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? No immediate follow-up needed; the full paper has been read for this audit. Reopen Sections 3 and 4 only if we need the exact retrospective metrics, prompt-optimization setup, or rank-agreement results.
- Which section to read next if needed: retrospective analysis / prompt optimization / ranking comparison tables
- Follow-up question(s): How stable are the retrospective rankings when the replay prompt or system prompt optimizer changes?

## 13. Registry sync
- Registry row synced: yes
- Registry status: finalized
- Priority: P1
- Reading depth: deep
- Batch ID: B07
- Outline sections: 0,1,3,4
- Survey role: representative
- Paper card path: `paper_cards/B07/GameArena.md`
- Check status: unchecked
- Last updated: 2026-04-28
