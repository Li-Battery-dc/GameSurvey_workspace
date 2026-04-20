# AvalonBench AvalonBench: Evaluating LLMs Playing the Game of Avalon

## 0. Metadata
- Date: 2023/10
- Venue: NeurIPS 2023 workshop
- Authors: Jonathan Light, Min Cai, Sheng Shen, Ziniu Hu
- Paper link: https://arxiv.org/pdf/2310.05036v3.pdf
- Code link:
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: high
- Review gate label: usable

## 1. One-paragraph benchmark summary
- AvalonBench is an early benchmark for multi-agent LLM play in the social-deduction game Resistance: Avalon. It packages a five-player Avalon environment, naive rule-based action baselines, and ReAct-style LLM agents that act, discuss, and recursively summarize game history across team selection, voting, quest, and assassination phases; in the with-discussion setting, the naive baselines also receive detached LLM-generated dialogue while keeping rule-based decisions. The paper is historically useful because it already exposes a knowing-doing gap: discussion improves identity deduction and assassin-side Merlin kills, but servant-side win rate still stays below the naive baseline. For this survey, AvalonBench is best used as an early prompt-mediated social-deduction probe and interface-design contrast rather than as a mature or highly ecological benchmark platform.

## 2. Position in our survey
- Why-games relevance: Social deduction games force agents to combine hidden information, dialogue, deception, and structured decision phases.
- Historical stage: diagnostic capability probe
- Benchmark level(s): L3 social intelligence
- Most relevant outline section(s): 1,2,3,4
- Role in corpus: representative

## 3. Design-space coding
### 3.1 Game structure
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
- Number of games / tasks: single five-player Avalon game with baseline-bot evaluations, Assassin Set / Servant Set replacements, and a 60-game GPT-3.5 multi-LLM arena

### 3.4 Modality
- Observation modality: text or symbolic
- Action modality: semantic
- Perception burden retained: dialogue interpretation, hidden-role reasoning, and memory over game history
- Perception burden removed: no visual or embodied burden

## 4. What this benchmark measures
- Primary capability target: social reasoning under hidden identities
- Secondary capability target(s): deception, belief tracking, dialogue-conditioned deduction, and role-specific strategy execution
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? yes
- Does it test social reasoning / deception / cooperation? yes
- Does it test visual grounding / spatial-temporal reasoning? no
- Does it test long-horizon autonomy / task completion? partially
- Does it test real-time efficiency? no
- Does it test cross-game transfer / open-ended generalization? no
- Why is a game environment especially suitable here? Avalon compresses hidden information, coordination, and adversarial dialogue into a short, structured interaction loop.

## 5. Interaction paradigm
- Observation channel: game rules, private role information, recursive game summaries, current-round discussion transcripts, and phase-specific request prompts; in bot-comparison runs only mission outcomes, not voting outcomes, are fed back into the recursive summary
- Action channel: team proposals, public approve/reject votes, anonymous quest pass/fail decisions, assassination choices, and fixed-order public discussion turns with the leader opening and closing each round
- Interface type: natural language / structured action space / hybrid
- Agent scaffold allowed: zero-shot CoT / recursive summarization / parser LLM
- Is there privileged API access? yes; the environment supplies structured state, private role information, and parser-mediated action execution
- How close is the setup to human play? medium-low; the game rules are authentic, but discussion is turn-ordered and sentence-limited, actions are routed through a separate parser, and the benchmark compresses history through recursive summaries
- Main ecological-validity trade-off: the benchmark keeps the hidden-role discussion loop, but simplifies play through recursive summaries, parser mediation, scripted speaking order, detached dialogue generation for naive baselines in discussion runs, and restricted voting-history access in bot comparisons

## 6. Evaluation protocol
- Main score: role-conditioned win rate
- Auxiliary score(s): mission win rate, assassination win rate, assassination accuracy, and servant deduction accuracy
- Evaluation style: win rate / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: the LLM replaces either the Assassin or one Servant against naive action bots, with and without discussion; in with-discussion runs the naive bots get detached LLM-generated dialogue but keep rule-based actions; the paper also reports a 60-game GPT-3.5 multi-LLM self-play arena
- Automatic verifiability: high
- Calibration method: repeated games with fixed role setups and separate role-conditioned metrics
- Anti-contamination argument: not central
- Reliability or comparability concerns: LLM runs are small-sample, conclusions depend on naive baseline design and prompt/parser/summarization scaffolding, bot-comparison runs intentionally withhold voting-history information for parity with the baselines, and the same underlying model is reused for action, summary, and dialogue generation

## 7. Main contributions
- Contribution 1: Builds a playable Avalon benchmark with role-aware prompting and baseline bots.
- Contribution 2: Separates action generation, public discussion, recursive history summarization, and parser-based action extraction inside the agent loop.
- Contribution 3: Shows that stronger discussion-conditioned deduction and Merlin identification do not automatically translate into strong role-specific game strategy.

## 8. Main findings and failure modes
- Core empirical takeaway: LLMs can use discussion to infer identities, but often fail to convert that information into robust role-specific strategy; GPT-3.5 with discussion reaches 76.0 servant deduction accuracy yet only 22.2% servant win rate versus the 38.2% naive baseline, while assassin-side gains come mainly through better Merlin kills.
- Notable model failure mode 1: poor simple policy execution when discussion is removed or when the model must match naive role-specific heuristics
- Notable model failure mode 2: evil players leak their own identity or speak inconsistently during discussion
- Notable model failure mode 3: relatively strong deduction accuracy does not translate into stronger servant decisions
- Does this paper reveal a benchmark-design limitation as well? yes; the results are materially conditioned on prompt/parser/summarization design, detached-language naive baselines, and bot comparisons that ignore voting history

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Early evidence that games can expose social reasoning gaps beyond static chat quality.
- Best use in Section 1 (taxonomy and evolutionary levels): Important as an early social-deduction LLM benchmark. Helps define hidden-role, dialogue-heavy game benchmarks.
- Best use in Section 2 (core capabilities evaluated by games): Supports discussion of dialogue-conditioned deduction, deception, and the gap between language understanding and action selection under hidden information.
- Best use in Section 3 (interaction and evaluation paradigm): Useful for role-prompt plus recursive-summary interaction loops, parser-mediated action extraction, and the comparability trade-off created by matching LLM inputs to naive baselines.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Early evidence for a language-understanding-to-strategy-execution gap in social play and for prompt-conditioned multi-agent evaluation.

## 10. Relation to nearby papers
- Closest predecessor(s): early hidden-role or Werewolf-style LLM social-deduction case studies
- Closest follow-up(s): WerewolfArena, Wolf, BeyondSurvival
- Best comparison targets inside our corpus: HumanLevelDiplomacy, WerewolfArena, Wolf, BeyondSurvival
- What this paper uniquely adds relative to neighbors: It is an early concrete Avalon benchmark with recursive history compression, phase-structured public discussion, and explicit evidence that good identity inference can still coexist with weak action policy execution.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- AvalonBench includes a game environment, naive rule-based baseline action policies, and ReAct-style LLM agents for Avalon.
- Because games can involve roughly 15-20 discussion rounds (up to 25), the paper introduces recursive summarization: each new summary is generated from the previous summary, the current-round discussion minutes, and the mission outcome.
- In baseline-comparison runs, the LLM replaces either the Assassin or one Servant, and only mission outcomes rather than voting outcomes are fed back into the recursive summary to match the naive baselines.
- In with-discussion runs, naive agents are extended with a detached LLM for dialogue generation, but their decisions still come from the naive strategy.
- GPT-3.5 with discussion reaches 66.7% total evil win rate and 66.7% assassination accuracy in the Assassin Set.
- GPT-3.5 with discussion as a Servant reaches 22.2% win rate and 76.0 deduction accuracy, versus 38.2% win rate for the naive servant baseline.

### 11.2 Our synthesis / interpretation
- AvalonBench is historically important but methodologically lighter than later social or multi-game benchmark platforms.
- Its safest survey use is as an early L3 benchmark for the knowing-doing gap: dialogue and summary help models track identities, but integrating that information into stable strategic action remains weak.
- The recursive summary mechanism makes the paper useful as an early context-management and within-game memory proxy, but not as a dedicated long-horizon memory benchmark.
- Its safest survey use is as a historical L3 benchmark and interface-design contrast, not as strong evidence of ecological human-like social play.

### 11.3 Uncertain or needs re-check
- Re-check Appendix A only if later drafting needs exact prompt templates or parser prompts.
- Re-check the multi-LLM self-play section if we later want to compare social-deduction failure patterns across self-play and bot-baseline settings, because that evidence is only based on 60 GPT-3.5 games with the same prompt stack.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? No immediate follow-up needed; the full paper has been read for this audit. Reopen the appendix only if we need exact prompt text or dialogue examples.
- Which section to read next if needed: appendix prompts / multi-LLM self-play analysis
- Follow-up question(s): How should later social-deduction benchmarks be compared once they replace naive-bot baselines with stronger evaluation instrumentation?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P1
- Reading depth: deep
- Batch ID: B03
- Outline sections: 1,2,3,4
- Survey role: representative
- Paper card path: `paper_cards/B03/AvalonBench.md`
- Check status: unchecked
- Next action: draft-section
- Last updated: 2026-04-14
