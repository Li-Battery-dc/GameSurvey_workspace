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
- GameBench is a cross-domain benchmark for evaluating LLM strategic reasoning through nine relatively obscure multiplayer games selected to span abstract strategy, hidden information, language communication, social deduction, cooperation, and nondeterminism. It includes both discrete and open-ended action spaces, evaluates GPT-3 and GPT-4 base agents together with CoT and GPT-4-RAP scaffolds, and aggregates uneven match data with a weighted, bootstrapped exponential Bradley-Terry model. The benchmark moves beyond canonical game-theory scenarios toward broader strategic diversity, but still relies on text-heavy APIs and explicitly acknowledges that its out-of-distribution claim is only heuristic rather than verified.

## 2. Position in our survey
- Why-games relevance: Diverse multi-agent games expose strategy, hidden information, cooperation, and communication in ways that resist simple static-answer evaluation.
- Historical stage: diagnostic capability probe
- Narrative level(s): L2 strategic reasoning / L3 social intelligence
- Most relevant outline section(s): 1,2,3,4
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
- Primary modality: mixed
- Perception burden retained: rule understanding, hidden-information reasoning, communication, strategic adaptation across games, and image-based board perception in Hive
- Perception burden removed: most games still remove raw GUI interaction and low-level action execution

## 4. What this benchmark measures
- Primary capability target: cross-domain strategic reasoning in multi-agent games
- Secondary capability target(s): hidden-information handling, non-deterministic play, language-mediated coordination or deduction, and the effect of reasoning scaffolds
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? yes
- Does it test social reasoning / deception / cooperation? yes
- Does it test visual grounding / spatial-temporal reasoning? partially
- Does it test long-horizon autonomy / task completion? no
- Does it test real-time efficiency? no
- Does it test cross-game transfer / open-ended generalization? no
- Why is a game environment especially suitable here? Different games package distinct strategic pressures while still yielding pairwise match outcomes that can be aggregated across many agents.

## 5. Interaction paradigm
- Observation channel: game rules, current state, and available actions exposed through a Python game API, with Hive using image state for GPT-4 and text descriptions for GPT-3 and RAP
- Action channel: either selecting from available actions or producing open-ended text actions, depending on the game
- Interface type: API / natural language / hybrid
- Agent scaffold allowed: CoT / RAP
- Is there privileged API access? yes
- How close is the setup to human play? low; the games are genuine, but interaction is standardized through rule text, explicit state exposure, and available-action APIs rather than native interfaces
- Main ecological-validity trade-off: GameBench expands strategic diversity and includes some open-ended play, but it still depends on privileged state or action exposure and duplicated same-model teammates in some cooperative settings

## 6. Evaluation protocol
- Main score: weighted, bootstrapped exponential Bradley-Terry ratings aggregated across games
- Auxiliary score(s): per-game ratings, average score tables, and comparisons against random and human baselines
- Evaluation style: tournament / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: GPT-3 and GPT-4 variants, GPT-4-RAP, a random-action baseline, and a sparse human baseline collected from a co-creator plus a friend for Codenames
- Automatic verifiability: high
- Calibration method: inverse-frequency game weighting, 10,000 bootstrap samples, and maximum-likelihood fitting of an exponential Bradley-Terry model
- Anti-contamination argument: explicit but unverified; the authors filtered for games without obvious guides or forums, then later note that GPT-4 still appears to know many game rules and that OOD status is unresolved
- Reliability or comparability concerns: aggregate rankings are sensitive to the included games, human data are sparse, match counts are uneven, and some cooperative team games duplicate the same agent across teammates

## 7. Main contributions
- Contribution 1: Introduces a cross-domain suite of relatively obscure multi-agent games for strategic-reasoning evaluation.
- Contribution 2: Compares base models with CoT and GPT-4-RAP scaffolds under a common rating framework.
- Contribution 3: Uses weighted Bradley-Terry aggregation with bootstrap uncertainty to estimate agent skill across uneven cross-game data.

## 8. Main findings and failure modes
- Core empirical takeaway: the sparse human baseline outperforms all tested agents; CoT is the strongest scaffold overall; GPT-4-RAP improves over base GPT-4 but usually trails GPT-4-CoT; base GPT-3 is roughly random; and base GPT-4 can underperform the random baseline because of severe failure on Sea Battle.
- Notable model failure mode 1: large sensitivity to scaffold choice rather than robust strategic competence
- Notable model failure mode 2: inconsistent performance across games, suggesting weak transfer of strategy
- Notable model failure mode 3: some aggregate conclusions change materially when a single game is removed
- Does this paper reveal a benchmark-design limitation as well? yes; the authors explicitly note that multigame aggregation can be unstable and that out-of-distribution status is hard to verify conclusively

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Limited use only; it can illustrate why multi-agent strategic play is harder to saturate than static tasks, but it is not a primary lead-in anchor.
- Best use in Section 1 (taxonomy and evolutionary levels): Useful for the transition from canonical game-theory tasks to broader diagnostic strategic suites with social and communicative coverage.
- Best use in Section 2 (core capabilities evaluated by games): Supports discussion of hidden information, cooperation, social deduction, open-ended communication, and scaffold-sensitive strategic reasoning.
- Best use in Section 3 (interaction and evaluation paradigm): Strong comparison point for standardized game APIs, available-action exposure, multimodal exceptions such as Hive, and rating aggregation that is visibly sensitive to benchmark composition.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Strong source on aggregation instability, unresolved OOD validation, and the weakness of low-resolution human baselines.

## 10. Relation to nearby papers
- Closest predecessor(s): GTBench and smaller game-theory or social-game evaluations
- Closest follow-up(s): broader strategic suites such as GAMABench and TMGBench
- Best comparison targets inside our corpus: GTBench, GAMABench, TMGBench, WerewolfArena
- What this paper uniquely adds relative to neighbors: It emphasizes obscure real games, communicative and social play, and benchmark-level aggregation questions rather than only canonical game-theory scenarios.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- GameBench evaluates GPT-3 and GPT-4 on nine games, adds CoT to both models, and reports GPT-4-RAP results; GPT-3-RAP data were not collected because the model repeatedly refused RAP-style prediction prompts.
- The benchmark API exposes game rules, current state, and available actions; Hive uses images for GPT-4 but is textualized for GPT-3 and RAP.
- The paper uses inverse-frequency weighting plus 10,000 bootstrap samples under an exponential Bradley-Terry model rather than Elo to estimate cross-game agent ratings.
- The reported results show that the human baseline outperforms all tested LLM agents, but the human data are sparse and come from a co-creator of the benchmark, plus a friend for Codenames.

### 11.2 Our synthesis / interpretation
- GameBench is a useful bridge paper: more diverse and socially expressive than GTBench, but still structurally close to the text-API benchmark tradition rather than ecological play.
- It is especially valuable because it surfaces aggregation instability and weak OOD validation rather than treating one multigame leaderboard as unquestionable.

### 11.3 Uncertain or needs re-check
- Re-check Appendix H if we later need exact per-game confidence intervals or the Sea Battle sensitivity story in figure form.
- Re-check Appendix D if we later want to cite the duplicated-agent setup in cooperative team games or the exact multimodal handling of Hive.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? Already completed in this audit; no further reread is needed unless we later need exact per-game counts or human-subject caveats.
- Which section to read next if needed: 3.4 / 4 / Appendix D / Appendix H
- Follow-up question(s): Should GameBench be framed mainly as a cross-domain strategic suite or primarily as a cautionary case on aggregation and OOD validation?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P1
- Reading depth: deep
- Batch ID: B07
- Outline sections: 1,2,3,4
- Survey role: representative
- Paper card path: `paper_cards/B07/GameBench.md`
- Check status: unchecked
- Last updated: 2026-04-09
