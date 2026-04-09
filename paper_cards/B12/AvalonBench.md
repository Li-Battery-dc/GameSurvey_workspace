# AvalonBench AvalonBench: Evaluating LLMs Playing the Game of Avalon

## 0. Metadata
- Date: 2023/10
- Venue: NeurIPS 2023 workshop
- Authors: Jonathan Light, Min Cai, Sheng Shen, Ziniu Hu
- Paper link: https://arxiv.org/pdf/2310.05036v3.pdf
- Code link:
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: medium
- Review gate label: usable

## 1. One-paragraph benchmark summary
- AvalonBench is an early benchmark for multi-agent LLM play in the social-deduction game Resistance: Avalon. It provides a game engine, rule-based baseline bots, and ReAct-style LLM agents that act, discuss, and summarize history across the game phases of team selection, voting, questing, and assassination. The benchmark is narrow and somewhat prompt-heavy, but it is important historically because it exposes that LLMs can sound socially competent in discussion while still making weak strategic decisions. For this survey, AvalonBench is best used as an early multi-agent social-game probe rather than a mature benchmark platform.

## 2. Position in our survey
- Why-games relevance: Social deduction games force agents to combine hidden information, dialogue, deception, and structured decision phases.
- Historical stage: diagnostic capability probe
- Narrative level(s): L3 social intelligence
- Most relevant outline section(s): 1,2,3,4
- Role in corpus: representative

## 3. Design-space coding
### 3.1 Environment structure
- Information structure: imperfect
- Transition structure: deterministic
- Agent structure: multi-agent
- Social structure: mixed
- Time structure: turn-based

### 3.2 World structure
- World type(s): social deduction
- Real game / simulated game / designed task-game hybrid: digital environment for an existing tabletop social deduction game
- Benchmark unit: full game

### 3.3 Benchmark scope
- Scope: single game
- Number of games / tasks: Avalon games in five-player settings with multiple role configurations
- Benchmark intent: diagnostic evaluation

### 3.4 Modality
- Primary modality: text
- Perception burden retained: dialogue interpretation, hidden-role reasoning, and memory over game history
- Perception burden removed: no visual or embodied burden

## 4. What this benchmark measures
- Primary capability target: social reasoning under hidden identities
- Secondary capability target(s): deception, suspicion tracking, dialogue generation, and role-specific decision making
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? yes
- Does it test social reasoning / deception / cooperation? yes
- Does it test visual grounding / spatial-temporal reasoning? no
- Does it test long-horizon autonomy / task completion? partially
- Does it test real-time efficiency? no
- Does it test cross-game transfer / open-ended generalization? no
- Why is a game environment especially suitable here? Avalon compresses hidden information, coordination, and adversarial dialogue into a short, structured interaction loop.

## 5. Interaction paradigm
- Observation channel: role information, summaries of prior rounds, discussion transcripts, and phase prompts
- Action channel: team choices, votes, quest decisions, assassination choices, and discussion messages
- Interface type: natural language / structured action space / hybrid
- Agent scaffold allowed: summarization
- Is there privileged API access? yes; the environment provides parsed state and role information
- How close is the setup to human play? medium; game logic is authentic, but communication and memory are heavily prompt-mediated
- Main ecological-validity trade-off: the benchmark captures real social deduction structure, but the heavy use of summaries and prompt parsers simplifies some cognitive burdens

## 6. Evaluation protocol
- Main score: win rate in role-specific settings
- Auxiliary score(s): assassination win rate and deduction accuracy for servant roles
- Evaluation style: win rate / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: LLM agents are compared against deterministic baseline bots in assassin and servant settings, with and without discussion
- Automatic verifiability: high
- Calibration method: repeated games with fixed role setups and separate role-conditioned metrics
- Anti-contamination argument: live multi-agent play and discussion are harder to memorize than static QA benchmarks
- Reliability or comparability concerns: benchmark conclusions depend strongly on the handcrafted baseline bots, prompt design, and summary quality

## 7. Main contributions
- Contribution 1: Builds a playable Avalon benchmark with role-aware prompting and baseline bots.
- Contribution 2: Separates action, discussion, and history summarization within the LLM agent loop.
- Contribution 3: Shows that fluent discussion does not imply strong social-game strategy.

## 8. Main findings and failure modes
- Core empirical takeaway: LLMs often infer identities reasonably well from discussion but still lose due to poor strategic actions and unreliable deception.
- Notable model failure mode 1: weak role-specific action selection despite good verbal analysis
- Notable model failure mode 2: leaking evil identity through unnatural or inconsistent dialogue
- Notable model failure mode 3: over-reliance on prompts and summaries rather than grounded strategic tracking
- Does this paper reveal a benchmark-design limitation as well? yes; it shows that social-game evaluation can be confounded by prompt scaffolding and bot quality

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Early evidence that games can expose social reasoning gaps beyond static chat quality.
- Best use in Section 1 (taxonomy and evolutionary levels): Important as an early social-deduction LLM benchmark. Helps define hidden-role, dialogue-heavy game benchmarks.
- Best use in Section 2 (core capabilities evaluated by games): Supports discussion of deduction, deception, and cooperation under uncertainty.
- Best use in Section 3 (interaction and evaluation paradigm): Useful for role-prompt plus summary-based interaction loops. Good example of role-conditioned win-rate analysis.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Supports later calls for stronger multi-agent evaluation and less prompt-dependent setups.

## 10. Relation to nearby papers
- Closest predecessor(s): Werewolf-style social deduction studies
- Closest follow-up(s): GameArena, DSGBench
- Best comparison targets inside our corpus: WerewolfArena, Wolf, GameArena, DSGBench
- What this paper uniquely adds relative to neighbors: It is an early concrete implementation of phase-structured LLM social-deduction play with separate discussion and action loops.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- AvalonBench includes a game environment, rule-based bots, and ReAct-style LLM agents for Avalon.
- It evaluates assassin and servant settings and reports win-rate-style metrics plus servant deduction accuracy.
- The paper finds that GPT-3.5 improves with discussion in some settings but still underperforms baseline strategies overall.

### 11.2 Our synthesis / interpretation
- AvalonBench is historically important but methodologically lighter than later social or multi-game benchmark platforms.
- It is most useful as a contrast case showing that discussion fluency is not the same as strategic social intelligence.

### 11.3 Uncertain or needs re-check
- Re-check the exact role distributions and game counts if later drafting needs them.
- Re-check whether later versions or forks of the environment changed the baseline bot assumptions.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? Only selectively later if we need exact role-metric definitions.
- Which section to read next if needed: benchmark setup / baseline strategies / results analysis
- Follow-up question(s): Which observed errors come from social reasoning limits versus prompt/parser brittleness?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P1
- Reading depth: deep
- Batch ID: B12
- Outline sections: 1,2,3,4
- Survey role: representative
- Paper card path: `paper_cards/B12/AvalonBench.md`
- Next action: draft-section
- Last updated: 2026-04-05
