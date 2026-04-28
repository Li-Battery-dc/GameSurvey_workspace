# ComplexCardGames Can Large Language Models Master Complex Card Games?

## 0. Metadata
- Date: 2025/09
- Venue: arXiv
- Authors: Wei Wang, Fuqing Bie, Junzhe Chen, Dan Zhang, Shiyu Huang, Evgeny Kharlamov, Jie Tang
- Paper link: https://arxiv.org/pdf/2509.01328v4
- Code link: https://github.com/THUDM/LLM4CardGame
- Reading depth: deep
- Card status: finalized
- Confidence in this card: high
- Review gate label: usable

## 1. One-paragraph benchmark summary
- This paper studies whether LLMs can actually learn strong play in complex card games rather than merely survive zero-shot prompting. It evaluates eight card games, builds high-quality trajectory datasets from strong game AIs or expert data, and compares single-game fine-tuning, mixed multi-game fine-tuning, and post-hoc recovery of general capabilities. For this survey, the paper is most useful as a train+eval contrast study that exposes transfer, interference, and capability-retention trade-offs across hard imperfect-information games.

## 2. Position in our survey
- Why-games relevance: Complex card games give a demanding testbed for whether LLMs can acquire nontrivial strategic competence from data rather than from prompt scaffolds alone.
- Historical stage: diagnostic capability probe
- Benchmark level(s): L2 strategic reasoning
- Most relevant outline section(s): 1,2,3,4
- Role in corpus: contrast

## 3. Design-space coding
### 3.1 Structure
- Form: Match
- Construction: Adapted
- Construction note: real card games with benchmarked fine-tuning pipelines
- Benchmark unit: full game / episode

### 3.2 Mechanics profile
- State visibility: mixed
- Transition uncertainty: mixed
- Actor configuration: multi-agent
- Incentive structure: mixed
- Temporal regime: turn-based

### 3.3 Benchmark scope
- Scope: curated suite
- Number of games / tasks: 8 games

### 3.4 Modality
- Observation modality: text or symbolic
- Action modality: semantic
- Perception burden retained: hand-state interpretation, action-history tracking, legal action choice, hidden-information reasoning
- Perception burden removed: raw visual card-table interaction

## 4. What this benchmark measures
- Primary capability target: learning strong card-game policies from expert-style trajectory data
- Secondary capability target(s): cross-game transfer, multi-game interference, retention of non-game capabilities
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? yes
- Does it test social reasoning / deception / cooperation? partially, in team and imperfect-information games
- Does it test visual grounding / spatial-temporal reasoning? no
- Does it test long-horizon autonomy / task completion? partially
- Does it test real-time efficiency? no
- Does it test cross-game transfer / open-ended generalization? yes for within-card-game transfer; no for open-ended generalization
- Why is a game environment especially suitable here? Card games provide hard structured objectives, strong teacher AIs, and controllable transfer relations between similar and dissimilar rulesets.

## 5. Interaction paradigm
- Observation channel: prompts with game rules, state descriptions, history, and legal actions
- Action channel: JSON-style legal action outputs
- Interface type: natural language / structured action space
- Agent scaffold allowed: none
- Is there privileged API access? yes
- How close is the setup to human play? medium; the strategic content is real, but the interface is symbolic and training-centered
- Main ecological-validity trade-off: The setup measures learnability and transfer cleanly, but it says less about human-like play with natural perceptual burdens.

## 6. Evaluation protocol
- Main score: game-specific win rate or reward score against benchmark opponents
- Auxiliary score(s): data-scaling curves, mixed-training transfer results, and general-benchmark retention
- Evaluation style: hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: teacher AIs, benchmark opponents, and pre/post fine-tuning comparisons
- Automatic verifiability: high
- Calibration method: shared datasets, fixed teacher sources, and controlled fine-tuning comparisons
- Anti-contamination argument: not central; the paper is more about learning dynamics than benchmark leakage
- Reliability or comparability concerns: the study mixes benchmarking with a substantial training pipeline, so results reflect both model capability and data construction choices

## 7. Main contributions
- Contribution 1: Evaluates LLM learning on eight complex card games instead of only prompt-based play.
- Contribution 2: Builds high-quality training data from strong game AIs and expert gameplay sources.
- Contribution 3: Measures single-game mastery, multi-game transfer, and general-capability retention together.

## 8. Main findings and failure modes
- Core empirical takeaway: with enough high-quality teacher trajectories, fine-tuned LLMs can approach strong game-AI performance on several complex card games and can jointly handle multiple similar-rule games, but the gains depend heavily on data construction and rule similarity
- Notable model failure mode 1: transfer is strongest between rule-similar games such as DouDizhu and GuanDan or among the poker variants, but it weakens outside those close families
- Notable model failure mode 2: game fine-tuning causes noticeable drops on general benchmarks such as knowledge, math, and coding
- Notable model failure mode 3: even when game performance improves, the paper notes that LLM inference remains slower than specialized game AIs
- Does this paper reveal a benchmark-design limitation as well? yes; it is partly a benchmark paper and partly a domain-adaptation study

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Shows why high-complexity games remain useful capability probes when the question is learning from interaction data rather than zero-shot prompting.
- Best use in Section 1 (taxonomy and evolutionary levels): Level 2 curated-suite contrast for training-heavy card games with text-symbolic observation and semantic JSON actions; not a Level 5 open-ended benchmark.
- Best use in Section 2 (core capabilities evaluated by games): Strong evidence for strategic learning under uncertainty and for transfer/interference patterns governed by rule similarity, such as DouDizhu/GuanDan and poker variants.
- Best use in Section 3 (interaction and evaluation paradigm): Representative symbolic-state train+eval setup for teacher-generated trajectories, legal-action exposure, role/game-specific metrics, and post-training evaluation.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Strong evidence that specialist game tuning can trade off against general benchmark performance, although targeted general-data recovery can partially repair the loss.

## 10. Relation to nearby papers
- Closest predecessor(s): prompt-based poker and card-game evaluations, specialist game-AI training work
- Closest follow-up(s): later multi-game transfer and specialization studies that treat card games as a controlled transfer family
- Best comparison targets inside our corpus: PokerBench, GTOWizardBenchmark, CompleteChessGames, MixingExpertKnowledge
- What this paper uniquely adds relative to neighbors: It makes multi-game transfer, mixed fine-tuning, and general-capability retention first-class evaluation questions within one card-game study.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- The paper evaluates eight card games: DouDizhu, GuanDan, Riichi Mahjong, Uno, Gin Rummy, Leduc Hold'em, Limit Texas Hold'em, and No-limit Texas Hold'em.
- It fine-tunes models on high-quality gameplay interaction data from strong game AIs or expert sources and studies three research questions on single-game mastery, multi-game learning, and general-capability retention.
- Results show positive transfer for similar games, interference for dissimilar ones, and measurable drops on MMLU-Pro, Math-500, and HumanEval after game fine-tuning.

### 11.2 Our synthesis / interpretation
- This card is more important for the survey's discussion of benchmark purpose and training trade-offs than for ecological interaction design.
- It supports the claim that game benchmarks can probe both strategic competence and undesirable specialization.

### 11.3 Uncertain or needs re-check
- Recheck Tables 4-7 and Appendix B if we later need exact per-game score definitions, role-level DouDizhu caveats, or the paper’s latency limitation wording.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? No immediate reread; the main training/evaluation logic is already clear.
- Which section to read next if needed: 3.2 / 4.2 / 4.4
- Follow-up question(s): Which game-pair transfer result best anchors our discussion of positive transfer versus interference?

## 13. Registry sync
- Registry row synced: yes
- Registry status: finalized
- Priority: P2
- Reading depth: deep
- Batch ID: B09
- Outline sections: 1,2,3,4
- Survey role: contrast
- Paper card path: `paper_cards/B09/ComplexCardGames.md`
- Check status: unchecked
- Last updated: 2026-04-28
