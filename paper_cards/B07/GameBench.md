# GameBench GameBench: Evaluating Strategic Reasoning Abilities of LLM Agents

## 0. Metadata
- Date: 2024/06
- Venue: arXiv
- Authors: Anthony Costarelli, Mat Allen, Roman Hauksson, Grace Sodunke, Suhas Hariharan, Carlson Cheng, Wenjie Li, Joshua Clymer, Arjun Yadav
- Paper link: https://arxiv.org/pdf/2406.06613v2
- Code link: https://github.com/Joshuaclymer/GameBench
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: high
- Review gate label: usable

## 1. One-paragraph benchmark summary
- GameBench is a multi-player, cross-domain framework for evaluating LLM strategic reasoning through a suite of obscure games chosen to be relatively out-of-distribution. It spans board, card, and social or communicative games, includes both discrete and open-ended action spaces, and evaluates base models plus scaffolds such as CoT and RAP against each other, a random baseline, and humans. Instead of Elo, the paper uses a bootstrapped Bradley-Terry rating model to aggregate cross-game results. For this survey, GameBench is a representative early suite that pushes beyond canonical game-theory tasks toward broader strategic diversity while still remaining text-mediated and scaffold-sensitive.

## 2. Position in our survey
- Why-games relevance: Diverse multi-agent games expose strategy, hidden information, cooperation, and communication in ways that resist simple static-answer evaluation.
- Historical stage: formal container
- Narrative level(s): L2 strategic reasoning / L3 social intelligence
- Most relevant outline section(s): 1,2,3,5,6
- Role in corpus: representative

## 3. Design-space coding
### 3.1 Environment structure
- Information structure: mixed
- Transition structure: mixed
- Agent structure: multi-agent
- Social structure: mixed
- Time structure: mixed

### 3.2 World structure
- World type(s): board / card / social deduction / other
- Real game / simulated game / designed task-game hybrid: curated suite of existing games with unified software interfaces
- Benchmark unit: match

### 3.3 Benchmark scope
- Scope: curated suite
- Number of games / tasks: 9 game environments
- Benchmark intent: diagnostic evaluation

### 3.4 Modality
- Primary modality: text
- Perception burden retained: rule understanding, hidden-information reasoning, communication, and strategic adaptation across games
- Perception burden removed: no raw visual board or GUI burden

## 4. What this benchmark measures
- Primary capability target: cross-domain strategic reasoning in multi-agent games
- Secondary capability target(s): hidden-information handling, non-deterministic play, social deduction, and the effect of reasoning scaffolds
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? yes
- Does it test social reasoning / deception / cooperation? yes
- Does it test visual grounding / spatial-temporal reasoning? no
- Does it test long-horizon autonomy / task completion? partially
- Does it test real-time efficiency? no
- Does it test cross-game transfer / open-ended generalization? partially
- Why is a game environment especially suitable here? Different games package distinct strategic pressures while still yielding pairwise match outcomes that can be aggregated across many agents.

## 5. Interaction paradigm
- Observation channel: text descriptions of game rules, current state, and available actions
- Action channel: textual or structured moves selected by agents in each game environment
- Interface type: API / natural language / hybrid
- Agent scaffold allowed: other
- Is there privileged API access? yes
- How close is the setup to human play? medium-low; the games are genuine, but interaction is standardized through text APIs rather than native interfaces
- Main ecological-validity trade-off: GameBench expands strategic diversity but preserves a highly scaffolded text-first interface

## 6. Evaluation protocol
- Main score: Bradley-Terry agent rating aggregated across games
- Auxiliary score(s): per-game match outcomes and comparisons against random and human baselines
- Evaluation style: tournament / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: GPT-3 and GPT-4 variants with CoT and RAP, random baseline, and human baseline
- Automatic verifiability: high
- Calibration method: weighted match aggregation across games with 10,000 bootstrap samples under an exponential Bradley-Terry model
- Anti-contamination argument: games were chosen to have sparse strategy material online and to be relatively out-of-distribution
- Reliability or comparability concerns: aggregate rankings are sensitive to the included games, and the human dataset is limited

## 7. Main contributions
- Contribution 1: Introduces a cross-domain suite of relatively obscure multi-agent games for strategic-reasoning evaluation.
- Contribution 2: Compares base models with CoT and RAP scaffolds under a common rating framework.
- Contribution 3: Uses Bradley-Terry aggregation to estimate agent skill across games with uncertainty intervals.

## 8. Main findings and failure modes
- Core empirical takeaway: humans outperform all tested agents; CoT helps substantially; RAP also helps; base GPT-3 is roughly random; base GPT-4 can underperform the random baseline.
- Notable model failure mode 1: large sensitivity to scaffold choice rather than robust strategic competence
- Notable model failure mode 2: inconsistent performance across games, suggesting weak transfer of strategy
- Notable model failure mode 3: some aggregate conclusions change materially when a single game is removed
- Does this paper reveal a benchmark-design limitation as well? yes; the authors explicitly note that multigame aggregation can be unstable and that out-of-distribution status is hard to verify conclusively

## 9. Why this paper matters for our survey
- Best use in Section 0 (why games): Shows why multi-agent games can create a harder and less saturable strategic benchmark than static tasks.
- Best use in Section 1 (historical evolution): Useful for the transition from canonical game-theory tasks to more diverse strategic suites.
- Best use in Section 2 (design space): Helps broaden the social and hidden-information portion of the taxonomy.
- Best use in Section 3 (capability targets): Supports discussion of strategic transfer, cooperation, and social deduction.
- Best use in Section 4 (interaction paradigm): Useful comparison point for standardized text APIs and scaffolded play.
- Best use in Section 5 (evaluation protocol): Good reference for rating aggregation and the risks of cross-game leaderboard collapse.
- Best use in Section 6/7 (limitations and future): Strong source on benchmark sensitivity, OOD verification difficulties, and low-resolution human baselines.

## 10. Relation to nearby papers
- Closest predecessor(s): GTBench and smaller game-theory or social-game evaluations
- Closest follow-up(s): broader strategic suites such as GAMABench and TMGBench
- Best comparison targets inside our corpus: [GTBench](D:/research_root/GameSurvey/workspace/paper_cards/B07/GTBench.md), [GAMABench](D:/research_root/GameSurvey/workspace/paper_cards/B07/GAMABench.md), [TMGBench](D:/research_root/GameSurvey/workspace/paper_cards/B07/TMGBench.md), [WerewolfArena](D:/research_root/GameSurvey/workspace/paper_cards/B02/WerewolfArena.md)
- What this paper uniquely adds relative to neighbors: It emphasizes relatively obscure games and cross-game rating methodology rather than only canonical game-theory scenarios.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- GameBench evaluates GPT-3 and GPT-4, with and without CoT and RAP scaffolds, on nine game environments.
- The paper uses an exponential Bradley-Terry model with bootstrap resampling rather than Elo to estimate cross-game agent ratings.
- The reported results show that human baselines outperform all tested LLM agents, while base GPT-4 can perform worse than random.

### 11.2 Our synthesis / interpretation
- GameBench is a useful bridge paper: more diverse than GTBench, but still structurally close to the formal-text benchmark tradition.
- It is especially valuable because it surfaces aggregation instability rather than treating one leaderboard as unquestionable.

### 11.3 Uncertain or needs re-check
- Re-check Section 3 and Appendix H if we later need the exact game list and per-game rating intervals for drafting.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? No immediate reread is needed unless we later want the exact game inventory and game-by-game failure stories.
- Which section to read next if needed: 3.2 / 3.4 / 5
- Follow-up question(s): Should GameBench be positioned mainly as a strategic-diversity benchmark or as an early cautionary case on aggregation and OOD claims?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P1
- Reading depth: deep
- Batch ID: B07
- Outline sections: 1,2,3,5,6
- Survey role: representative
- Paper card path: `paper_cards/B07/GameBench.md`
- Next action: draft-section
- Last updated: 2026-04-05
