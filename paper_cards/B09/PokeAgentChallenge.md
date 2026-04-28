# PokeAgentChallenge The PokeAgent Challenge: Competitive and Long-Context Learning at Scale

## 0. Metadata
- Date: 2025/12
- Venue: NeurIPS 2025 competition
- Authors: Seth Karten, Jake Grigsby, Tersoo Upaa, Junik Bae, Seonghun Hong, Hyunyoung Jeong, Jaeyoon Jung, Kun Kerdthaisong, Gyungbo Kim, Hyeokgi Kim, Yujin Kim, Eunju Kwon, Dongyu Liu, Patrick Mariglia, Sangyeon Park, Benedikt Schink, Xianwei Shi, Anthony Sistilli, Joseph Twin, Arian Urdu, Matin Urdu, Qiao Wang, Ling Wu, Wenli Zhang, Kunsheng Zhou, Stephanie Milani, Kiran Vodrahalli, Amy Zhang, Fei Fang, Yuke Zhu, Chi Jin
- Paper link: https://arxiv.org/pdf/2603.15563v2
- Code link:
- Reading depth: deep
- Card status: finalized
- Confidence in this card: high
- Review gate label: strong

## 1. One-paragraph benchmark summary
- The PokeAgent Challenge turns Pokemon into a two-track living benchmark that jointly stresses competitive partial observability and long-horizon sequential planning. Its Battling Track runs agents on a dedicated Pokemon Showdown server and evaluates them with Full-History Bradley-Terry, Glicko-1, and GXE, while its Speedrunning Track standardizes long-context play in Pokemon Emerald with metrics such as completion percentage, time, and action count. For this survey, it is one of the strongest bridge papers between specialist game AI, LLM harnesses, and competition-backed benchmarking.

## 2. Position in our survey
- Why-games relevance: Pokemon naturally combines hidden information, strategic adversaries, and extremely long action horizons in a way few other benchmarks do.
- Historical stage: ecological agent benchmark
- Benchmark level(s): L2 strategic reasoning / L4 visual agency
- Most relevant outline section(s): 1,2,3,4
- Role in corpus: contrast

## 3. Design-space coding
### 3.1 Structure
- Form: Match
- Construction: Wrapped
- Construction note: real game benchmark wrappers around Pokemon battling and RPG play
- Benchmark unit: battle or speedrun episode

### 3.2 Mechanics profile
- State visibility: partial
- Transition uncertainty: stochastic
- Actor configuration: mixed
- Incentive structure: mixed
- Temporal regime: hybrid

### 3.3 Benchmark scope
- Scope: game family
- Number of games / tasks: 2 benchmark tracks within the Pokemon ecosystem

### 3.4 Modality
- Observation modality: mixed
- Action modality: mixed
- Perception burden retained: hidden information, opponent modeling, long-horizon planning, visual interaction in speedrunning
- Perception burden removed: some standardized harness friction, especially on the battling track

## 4. What this benchmark measures
- Primary capability target: strategic reasoning under partial observability plus long-context planning at scale
- Secondary capability target(s): harness design, metagame adaptation, specialist-versus-generalist comparison
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? yes
- Does it test social reasoning / deception / cooperation? no; it stresses adversarial opponent modeling rather than language-mediated social reasoning
- Does it test visual grounding / spatial-temporal reasoning? yes, in the speedrunning track
- Does it test long-horizon autonomy / task completion? yes
- Does it test real-time efficiency? yes, especially in the speedrunning track where wall-clock latency is part of the benchmark
- Does it test cross-game transfer / open-ended generalization? no
- Why is a game environment especially suitable here? Pokemon combines adversarial decision making and very long sequential play inside a culturally stable, data-rich ecosystem.

## 5. Interaction paradigm
- Observation channel: structured battle states on Showdown and visual frames plus limited state information for speedrunning
- Action channel: legal battle actions or environment control commands through the challenge harnesses
- Interface type: hybrid
- Agent scaffold allowed: other (submission-dependent; strong systems use search, RL, memory, planners, or multi-agent harnesses)
- Is there privileged API access? mixed; yes on battling and partially on speedrunning through limited state exposure
- How close is the setup to human play? medium; the benchmark preserves real game structure but often relies on standardized harnesses and battle-state abstractions
- Main ecological-validity trade-off: The benchmark is unusually realistic in domain complexity, but performance is strongly shaped by harness quality.

## 6. Evaluation protocol
- Main score: Full-History Bradley-Terry for battling and completion progress/time for speedrunning
- Auxiliary score(s): Glicko-1, GXE, completion time, and action count
- Evaluation style: leaderboard / competition / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: community submissions and organizer baselines drive the main evaluation; speedrunning also reports human world-record splits as an upper bound rather than a matched baseline
- Automatic verifiability: high
- Calibration method: dedicated evaluation server, large battle datasets, public leaderboards, and standardized task rules
- Anti-contamination argument: partial; the paper argues Pokemon battling is nearly orthogonal to standard LLM benchmarks and that evolving metagames force adaptation, but harness and domain familiarity still matter
- Reliability or comparability concerns: results depend heavily on harness design, and the two tracks measure very different kinds of capability

## 7. Main contributions
- Contribution 1: Introduces a dual-track benchmark spanning competitive battling and RPG speedrunning.
- Contribution 2: Releases very large public battle data resources, sample teams, and strong baselines.
- Contribution 3: Converts the NeurIPS 2025 challenge into a living benchmark with continuing evaluation infrastructure.

## 8. Main findings and failure modes
- Core empirical takeaway: specialist RL and search methods remain much stronger than generalist LLM approaches, and long-horizon Pokemon play still requires substantial harness support
- Notable model failure mode 1: raw frontier models do not make meaningful speedrunning progress without sophisticated orchestration
- Notable model failure mode 2: common CLI-style agent harnesses lose coherence over the thousands of sequential decisions required for speedrunning
- Notable model failure mode 3: Pokemon exposes capabilities that standard LLM benchmarks fail to predict well
- Does this paper reveal a benchmark-design limitation as well? yes; benchmark difficulty is excellent, but comparing systems is hard when harness complexity varies so much

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Shows how one human game franchise can preserve multiple dynamic pressures: adversarial hidden-information battles and long-horizon RPG navigation.
- Best use in Section 1 (taxonomy and evolutionary levels): Strong example of `Mixed` form and game-family scope, where competition infrastructure hardens into a living benchmark with separate battle and speedrunning tracks.
- Best use in Section 2 (core capabilities evaluated by games): Direct evidence for Level 2 partial-observability strategy in Battling and Level 4 visual/long-context agency in Speedrunning; do not collapse the two tracks into one capability score.
- Best use in Section 3 (interaction and evaluation paradigm): Strong protocol card for dedicated evaluation servers, FH-BT/Glicko/GXE rating choices, harness x model attribution, milestone speedrun metrics, and latency/action-count trade-offs.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Supports the claim that benchmark difficulty, living leaderboards, and harness comparability must be discussed together because raw frontier models fail without domain-specific orchestration.

## 10. Relation to nearby papers
- Closest predecessor(s): PokeChamp, specialist Pokemon agents, long-horizon game-agent demonstrations
- Closest follow-up(s): living game competitions and benchmark leaderboards
- Best comparison targets inside our corpus: PokerBench, PokeChamp, GTOWizardBenchmark, CompleteChessGames
- What this paper uniquely adds relative to neighbors: It puts adversarial partial observability and long-context RPG play inside one benchmark ecosystem.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- The benchmark has two tracks: Battling on Pokemon Showdown and Speedrunning in Pokemon Emerald.
- The battling track uses Glicko-1, GXE, and a Full-History Bradley-Terry rating as its primary skill metric, while the speedrunning track uses completion-oriented metrics.
- The released resources include 4M human demonstrations, 18M synthetic/self-play battles, 200K+ curated teams, and 100K+ community battles; the NeurIPS challenge drew more than 100 competing teams.

### 11.2 Our synthesis / interpretation
- This card is especially useful for discussing benchmark quality under strong harness effects rather than as a clean "raw model" comparison.
- It also strengthens the survey's argument that living competitive ecosystems create difficult-to-saturate evaluation targets.

### 11.3 Uncertain or needs re-check
- Battling and speedrunning scores are not directly commensurate, so the paper should support cross-track synthesis only at the capability level, not through one combined ranking.
- Recheck Sections 3.2, 4.2, and 5 if we later need the exact FH-BT fitting procedure or the official speedrunning boundary conditions.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? A targeted reread may be worthwhile later because the rating design and harness details matter for protocol drafting.
- Which section to read next if needed: 3.2 / 4.2 / Appendix D
- Follow-up question(s): Should FH-BT become a named protocol example in Section 3.2?

## 13. Registry sync
- Registry row synced: yes
- Registry status: finalized
- Priority: P2
- Reading depth: deep
- Batch ID: B09
- Outline sections: 1,2,3,4
- Survey role: contrast
- Paper card path: `paper_cards/B09/PokeAgentChallenge.md`
- Check status: unchecked
- Last updated: 2026-04-28
