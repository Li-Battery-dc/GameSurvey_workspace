# WerewolfArena Werewolf Arena

## 0. Metadata
- Date: 2024/07
- Venue: arXiv
- Authors: Suma Bailis, Jane Friedhoff, Feiyang Chen
- Paper link: https://arxiv.org/pdf/2407.13943v1
- Code link:
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: high
- Review gate label: strong

## 1. One-paragraph benchmark summary
- Werewolf Arena turns the classic social deduction game Werewolf into a benchmark for LLM deception, deduction, and persuasion. The environment uses eight players with fixed roles, a rules-based Game Master, memory streams, role-specific actions, and a bidding mechanism that lets agents compete for speaking turns during debate. Rather than focusing only on end-of-game win rates, the paper also analyzes debate dynamics and synthetic vote shifts during conversation. It is a strong anchor for the survey’s social-intelligence branch because it brings hidden roles, persuasion, and partial observability into a live multi-agent setting.

## 2. Position in our survey
- Why-games relevance: It shows how games can expose social inference, deception, and conversational coordination in a controlled but still adversarial setting.
- Historical stage: diagnostic capability probe
- Narrative level(s): L3 social intelligence
- Most relevant outline section(s): 1,2,3,4
- Role in corpus: anchor

## 3. Design-space coding
### 3.1 Environment structure
- Information structure: imperfect
- Transition structure: mixed
- Agent structure: multi-agent
- Social structure: mixed
- Time structure: turn-based

### 3.2 World structure
- World type(s): social deduction
- Real game / simulated game / designed task-game hybrid: real game adapted into an LLM-agent benchmark
- Benchmark unit: full game

### 3.3 Benchmark scope
- Scope: single game
- Number of games / tasks: Werewolf with eight-player role-balanced matches
- Benchmark intent: diagnostic evaluation

### 3.4 Modality
- Primary modality: text
- Perception burden retained: public dialogue, hidden-role reasoning, memory over prior rounds, vote interpretation
- Perception burden removed: face-to-face cues, vocal delivery, and nonverbal signaling

## 4. What this benchmark measures
- Primary capability target: social reasoning under hidden roles
- Secondary capability target(s): deception, persuasion, belief updating, cooperative faction play
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? yes
- Does it test social reasoning / deception / cooperation? yes
- Does it test visual grounding / spatial-temporal reasoning? no
- Does it test long-horizon autonomy / task completion? partially
- Does it test real-time efficiency? no
- Does it test cross-game transfer / open-ended generalization? no
- Why is a game environment especially suitable here? Werewolf naturally combines hidden information, factional incentives, and language-based persuasion with clear win conditions.

## 5. Interaction paradigm
- Observation channel: public debate transcript plus role-dependent private memories
- Action channel: bids to speak, debate utterances, votes, and role-specific night actions
- Interface type: natural language / hybrid
- Agent scaffold allowed: memory
- Is there privileged API access? yes
- How close is the setup to human play? medium; the debate is free-form, but the environment uses synthetic names, capped rounds, and explicit memory updates
- Main ecological-validity trade-off: The benchmark captures social interaction better than formal board-game probes, but it remains a text-only simulated society with a rules-based moderator.

## 6. Evaluation protocol
- Main score: faction win rate
- Auxiliary score(s): role-conditioned win rates, synthetic vote dynamics, qualitative behavior analysis
- Evaluation style: win rate / tournament / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: model-vs-model tournaments plus self-play
- Automatic verifiability: medium to high
- Calibration method: role-balanced pairings within and across model families
- Anti-contamination argument: not central
- Reliability or comparability concerns: small tournament sizes, a simplified text-only environment, and mostly Gemini/GPT comparisons limit statistical strength and cross-paper comparability

## 7. Main contributions
- Contribution 1: Recasts Werewolf as a live multi-agent LLM benchmark with hidden roles.
- Contribution 2: Introduces dynamic turn-taking via bidding instead of fixed speaker order.
- Contribution 3: Adds debate-dynamics analysis through synthetic vote tracking.

## 8. Main findings and failure modes
- Core empirical takeaway: Stronger models differ not only in winning but in how persuasively and suspiciously they speak during debate.
- Notable model failure mode 1: verbose or poorly timed speech can make otherwise strong agents appear suspicious
- Notable model failure mode 2: later-round discussion often becomes repetitive without better dialogue control
- Notable model failure mode 3: role-specific memory and hidden-information handling remain brittle
- Does this paper reveal a benchmark-design limitation as well? yes; the paper shows promise, but the tournament scale is still modest and mainly compares GPT and Gemini families

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Strong example of interactive social reasoning that static benchmarks cannot reproduce.
- Best use in Section 1 (taxonomy and evolutionary levels): Marks the move from formal rule-grounded games to social-intelligence probes. Clear anchor for social deduction and imperfect-information multi-agent play.
- Best use in Section 2 (core capabilities evaluated by games): Direct fit for deception, cooperation, persuasion, and belief tracking.
- Best use in Section 3 (interaction and evaluation paradigm): Useful for memory-enabled text debate with role-specific actions. Relevant for role-balanced tournaments and process-level vote analysis.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Supports the claim that partial observability and social modeling remain hard.

## 10. Relation to nearby papers
- Closest predecessor(s): AvalonBench and earlier LLM social-deduction studies
- Closest follow-up(s): WOLF, Beyond Survival
- Best comparison targets inside our corpus: BeyondSurvival, AvalonBench, LLMHanabi, Wolf
- What this paper uniquely adds relative to neighbors: It emphasizes live conversational dynamics and turn-taking autonomy rather than only post-hoc judgment of deception.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- Each game uses eight players: one Seer, one Doctor, two Werewolves, and four Villagers.
- The environment includes role-specific night actions, a rules-based Game Master, agent memories, and bidding-based debate turns.
- The paper runs intra-family tournaments and analyzes shifting synthetic votes during debate.
- The synthetic votes are analysis-only proxies: they do not affect gameplay and are not stored in player memories.

### 11.2 Our synthesis / interpretation
- Werewolf Arena is a foundational social benchmark in this corpus because it treats dialogue as part of the environment, not just as explanation around the task.
- Its bidding mechanism is especially useful for Section 3 because it adds a conversational-control dimension absent from most turn-based benchmarks.

### 11.3 Uncertain or needs re-check
- Recheck Appendix C if we later need the exact debate-ending alternatives or more detailed moderator logic.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? Completed in this audit; the environment design, bidding analysis, seer analysis, and limitations sections are now checked against the full paper.
- Which section to read next if needed: 3.3 / 5.1 / Appendix C
- Follow-up question(s): How much of the observed performance gap comes from bidding and verbosity rather than deeper role inference?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P0
- Reading depth: deep
- Batch ID: B03
- Outline sections: 1,2,3,4
- Survey role: anchor
- Paper card path: `paper_cards/B03/WerewolfArena.md`
- Check status: unchecked
- Next action: draft-section
- Last updated: 2026-04-10
