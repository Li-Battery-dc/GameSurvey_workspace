# LMGameBench LMGAME-BENCH: How Good are LLMs at Playing Games?

## 0. Metadata
- Date: 2025/05
- Venue: ICLR 2026
- Authors: Lanxiang Hu, Mingjia Huo, Yuxuan Zhang, Haoyang Yu, Eric P. Xing, Ion Stoica, Tajana Rosing, Haojian Jin, Hao Zhang
- Paper link: https://arxiv.org/pdf/2505.15146v2
- Code link: https://github.com/lmgame-org/GamingAgent
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: high
- Review gate label: strong

## 1. One-paragraph benchmark summary
- LMGAME-BENCH is a six-game video-game benchmark built around Super Mario Bros., Tetris, Sokoban, Candy Crush, 2048, and Ace Attorney, all exposed through a unified Gym-style API. The paper's main contribution is not just the suite, but the benchmark harness layered on top of it: optional perception, memory, and reasoning support, bounded contamination checks, and prompt-standardization procedures intended to make rankings more discriminative and interpretable. Across 13 frontier models, the authors compare raw and harnessed play, then use correlation analysis and RL transfer studies to argue that different games load on different capability mixtures. For this survey, the paper is most useful as evidence that benchmark results in games depend heavily on interface design, prompt control, and contamination handling rather than on game choice alone.

## 2. Position in our survey
- Why-games relevance: Video games stress perception, planning, memory, and low-fault-tolerance action in ways that are easy to score yet difficult to saturate.
- Historical stage: diagnostic capability probe
- Benchmark level(s): L2 strategic reasoning / L4 visual agency
- Most relevant outline section(s): 0,1,2,3
- Role in corpus: representative

## 3. Design-space coding
### 3.1 Structure
- Form: Mixed
- Construction: Wrapped
- Construction note: curated suite of established video games with a common harness
- Benchmark unit: game episode

### 3.2 Mechanics profile
- State visibility: mixed
- Transition uncertainty: mixed
- Actor configuration: single-agent
- Incentive structure: N/A
- Temporal regime: hybrid

### 3.3 Benchmark scope
- Scope: curated suite
- Number of games / tasks: 6 games

### 3.4 Modality
- Observation modality: mixed
- Action modality: semantic
- Perception burden retained: screen understanding, long-horizon planning, partial observability, and game-specific control logic
- Perception burden removed: when the harness is enabled, perception modules and memory modules expose more machine-friendly state descriptions

## 4. What this benchmark measures
- Primary capability target: game-agent competence under both raw and harnessed interfaces
- Secondary capability target(s): sensitivity to perception and memory scaffolds, prompt variance, bounded contamination risk, and transfer from game-based RL training
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? yes
- Does it test social reasoning / deception / cooperation? no
- Does it test visual grounding / spatial-temporal reasoning? yes
- Does it test long-horizon autonomy / task completion? yes
- Does it test real-time efficiency? partially
- Does it test cross-game transfer / open-ended generalization? yes
- Why is a game environment especially suitable here? Games combine perception, state tracking, and sequential control in one verifiable loop, making them a compact proxy for broader agentic competence.

## 5. Interaction paradigm
- Observation channel: raw screenshots or extracted textual or symbolic state descriptions, optionally augmented with short trajectory memory and reflection traces
- Action channel: discrete game actions selected turn by turn through the unified Gym-style API
- Interface type: API / structured action space / hybrid
- Agent scaffold allowed: memory / reflection / other
- Is there privileged API access? yes
- How close is the setup to human play? low-to-medium; the games are real, but the strongest settings rely on backend-assisted textualization and memory support
- Main ecological-validity trade-off: the benchmark preserves real commercial or canonical games, but its most informative results come from privileged harness settings that trade human-like play for diagnostic separation

## 6. Evaluation protocol
- Main score: per-game native rewards, including progression rewards or long-horizon rewards depending on the game
- Auxiliary score(s): harness-versus-no-harness comparisons, module ablations, contamination analyses, prompt-variance analyses, benchmark-correlation studies, and RL transfer results
- Evaluation style: native score / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: 13 frontier models are compared with and without harness support, with random-play baselines as the explicit reference point
- Automatic verifiability: high
- Calibration method: standardized prompt optimization with DSPy, module ablations, paired-sample significance tests, and contamination-mitigation interventions for the checked games
- Anti-contamination argument: the paper explicitly checks vision-level contamination in Super Mario Bros and text-level contamination in Ace Attorney, then mitigates the latter with prompt interventions; it does not provide equally strong contamination evidence for every game in the suite
- Reliability or comparability concerns: rankings depend strongly on harness choice, Super Mario Bros is too high-variance for some correlation analyses, and some expensive evaluations are single-run only

## 7. Main contributions
- Contribution 1: Builds a six-game benchmark plus harness for evaluating LLMs and VLMs on video games.
- Contribution 2: Treats perception modules, memory, contamination mitigation, and prompt standardization as part of benchmark infrastructure rather than mere implementation detail.
- Contribution 3: Connects game performance to other benchmark families and to RL transfer on planning and agentic tasks.

## 8. Main findings and failure modes
- Core empirical takeaway: without harnesses, many model-game runs sit near random baselines, while harness support makes the benchmark more discriminative but also reveals how strongly interface assistance shapes rankings.
- Notable model failure mode 1: poor raw visual perception and weak long-horizon control leave many unharnessed runs near zero or near-random performance.
- Notable model failure mode 2: prompt sensitivity remains substantial even after empirical tuning, motivating the paper's DSPy-based standardization step.
- Notable model failure mode 3: RL training on simplified games transfers to cross-game planning and WebShop, but not to math or coding benchmarks such as GSM8K and BIRD.
- Does this paper reveal a benchmark-design limitation as well? yes; it shows that scaffold choice, contamination handling, and prompt protocol can materially change what the benchmark score means

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Supports the claim that games jointly stress perception, memory, and sequential planning in a closed-loop setting.
- Best use in Section 1 (taxonomy and evolutionary levels): Use as a diagnostic-suite example that sits between raw visual game play and heavily scaffolded benchmark infrastructure rather than as a pure ecological benchmark.
- Best use in Section 2 (core capabilities evaluated by games): Useful for showing that one suite can probe different mixtures of spatial reasoning, long-context language understanding, and long-horizon planning.
- Best use in Section 3 (interaction and evaluation paradigm): One of the strongest sources for the claim that observation abstraction, memory support, prompt control, and contamination mitigation all change what a game benchmark is measuring.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Supports the need to disclose interface privilege and bounded contamination evidence instead of treating benchmark scores as directly comparable across setups.

## 10. Relation to nearby papers
- Closest predecessor(s): BALROG and earlier multimodal game-suite benchmarks
- Closest follow-up(s): KORGym and broader benchmark-platform papers
- Best comparison targets inside our corpus: KORGym, Orak, AIGameStore, GVGAILLM
- What this paper uniquely adds relative to neighbors: It turns harness design, contamination mitigation, and prompt standardization into part of the benchmark contribution, then ties those choices to correlation and transfer analyses.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- LMGAME-BENCH evaluates 13 models on six games: Super Mario Bros., Tetris, Sokoban, Candy Crush, 2048, and Ace Attorney.
- The paper introduces optional perception, memory, and reasoning support through a unified gaming harness and compares model performance with and without that support.
- Excluding text-only models, 40% of unharnessed runs fail to beat random-play baselines, whereas 86.7% of harnessed runs beat the random baseline.
- The contamination study is explicit for only two cases: vision-level checks in Super Mario Bros and text-level checks plus prompt-based mitigation in Ace Attorney.
- RL training on simplified Sokoban and Tetris improves cross-game planning performance and WebShop, but does not improve GSM8K or BIRD in the reported experiments.

### 11.2 Our synthesis / interpretation
- LMGAME-BENCH is one of the clearest papers for arguing that benchmark design now includes interface engineering, not just task selection.
- It is more defensible as a Section 3 paradigm paper than as a clean ecological-play benchmark, because the paper's own strongest results depend on privileged harness settings.
- Its contamination contribution is useful for methodology discussion, but the evidence is bounded and should not be inflated into a blanket anti-contamination guarantee for all six games.

### 11.3 Uncertain or needs re-check
- Re-check Appendix C if we later need exact prompt-variance reductions for specific games.
- Re-check Appendix E or F if we later need exact paired-test or effect-size values for harness gains.
- The paper does not provide a full human baseline table, so avoid phrasing that implies a direct human-versus-model benchmark.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? Full paper read completed for this audit; no additional general read is required unless we need appendix-level numerical details.
- Which section to read next if needed: Appendix B / Appendix C / Appendix E / Appendix F
- Follow-up question(s): Use this paper mainly as a Section 3 anchor on interface privilege and calibration, not as the main anchor for cross-game generalization.

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P1
- Reading depth: deep
- Batch ID: B06
- Outline sections: 0,1,2,3
- Survey role: representative
- Paper card path: `paper_cards/B06/LMGameBench.md`
- Check status: unchecked
- Last updated: 2026-04-10
