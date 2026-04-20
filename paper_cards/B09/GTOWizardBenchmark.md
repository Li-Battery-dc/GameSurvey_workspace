# GTOWizardBenchmark GTO Wizard Benchmark

## 0. Metadata
- Date: 2026/03
- Venue: arXiv
- Authors: Marc-Antoine Provost, Nejc Ilenic, Christopher Solinas, Philippe Beardsell
- Paper link: https://arxiv.org/pdf/2603.23660.pdf
- Code link:
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: high
- Review gate label: strong

## 1. One-paragraph benchmark summary
- GTO Wizard Benchmark introduces a public API and standardized evaluation framework for heads-up no-limit Texas Hold'em. Unlike spot-based benchmarks such as PokerBench, it evaluates agents directly against a fixed superhuman anchor, GTO Wizard AI, and uses AIVAT to reduce variance so that meaningful conclusions can be drawn from many fewer hands. The paper benchmarks frontier LLMs in zero-shot conditions and shows that, despite rapid progress, they remain far below the baseline established by the benchmark's specialist anchor. For this survey, it is a valuable specialist benchmark because it combines a strong fixed opponent with explicit variance-control methodology.

## 2. Position in our survey
- Why-games relevance: Poker provides a formal hidden-information setting where strong solver-like anchors and variance-aware evaluation make strategic competence measurable.
- Historical stage: diagnostic capability probe
- Benchmark level(s): L2 strategic reasoning
- Most relevant outline section(s): 1,2,3,4
- Role in corpus: representative

## 3. Design-space coding
### 3.1 Game structure
- Information structure: imperfect
- Transition structure: stochastic
- Agent structure: multi-agent
- Social structure: competitive
- Time structure: turn-based

### 3.2 World structure
- World type(s): card
- Real game / simulated game / designed task-game hybrid: real game benchmarked through a public API
- Benchmark unit: hand / match

### 3.3 Benchmark scope
- Scope: single game
- Number of games / tasks: heads-up no-limit Texas Hold'em benchmark against fixed AI anchors

### 3.4 Modality
- Observation modality: text or symbolic
- Action modality: semantic
- Perception burden retained: betting history, hidden-state reasoning, action sizing, and strategic planning under uncertainty
- Perception burden removed: no visual table interface and no natural-language interaction burden

## 4. What this benchmark measures
- Primary capability target: strategic reasoning in poker against a superhuman fixed anchor
- Secondary capability target(s): hidden-state reasoning, representation quality, and variance-aware benchmarking
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? yes
- Does it test social reasoning / deception / cooperation? no
- Does it test visual grounding / spatial-temporal reasoning? no
- Does it test long-horizon autonomy / task completion? no
- Does it test real-time efficiency? no
- Does it test cross-game transfer / open-ended generalization? no
- Why is a game environment especially suitable here? Poker allows benchmark designers to measure hidden-information reasoning against a fixed strong anchor while keeping outcomes numerically rigorous.

## 5. Interaction paradigm
- Observation channel: public cards, betting history, stack context, and other structured poker state
- Action channel: fold, call, raise, and bet-size decisions through the public API
- Interface type: API / structured action space
- Agent scaffold allowed: none in the headline zero-shot evaluation
- Is there privileged API access? yes
- How close is the setup to human play? medium-low; the game is real poker, but the benchmark uses a structured API and specialist evaluation stack
- Main ecological-validity trade-off: the benchmark gains comparability and variance control by abstracting away full live-table interaction

## 6. Evaluation protocol
- Main score: luck-adjusted win rate in bb/100 via AIVAT against GTO Wizard AI
- Auxiliary score(s): chips won/lost, detailed luck decomposition metrics, and the anchor validation result against Slumbot
- Evaluation style: tournament / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: models are benchmarked against GTO Wizard AI and Slumbot rather than against humans
- Automatic verifiability: high
- Calibration method: fixed superhuman anchor plus AIVAT variance reduction, with each evaluated model playing 5000 independent hands
- Anti-contamination argument: not central
- Reliability or comparability concerns: dependence on a proprietary anchor and public API may limit long-term independent reproducibility

## 7. Main contributions
- Contribution 1: Introduces a public API benchmark for heads-up no-limit Texas Hold'em.
- Contribution 2: Uses GTO Wizard AI as a fixed superhuman anchor and validates it against Slumbot.
- Contribution 3: Integrates AIVAT to make poker evaluation more statistically efficient.

## 8. Main findings and failure modes
- Core empirical takeaway: frontier LLMs have improved substantially, but all remain far below the benchmark's specialist baseline; the best model in the paper, GPT-5.3 Extra High reasoning, still scores only -16 ± 3.0 bb/100.
- Notable model failure mode 1: weak hidden-state reasoning relative to the superhuman anchor
- Notable model failure mode 2: poor strategic representation in a domain requiring mixed strategies and action sizing
- Notable model failure mode 3: large gap between general reasoning progress and specialist poker competence
- Does this paper reveal a benchmark-design limitation as well? yes; the benchmark is strong on calibration but depends on a proprietary anchor ecosystem

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Good specialist example of games supporting precise quantitative evaluation under uncertainty.
- Best use in Section 1 (taxonomy and evolutionary levels): Useful later-stage refinement of poker benchmarking toward fixed-anchor standardization. Clean single-game imperfect-information specialist benchmark.
- Best use in Section 2 (core capabilities evaluated by games): Supports strategic reasoning and hidden-state planning discussion.
- Best use in Section 3 (interaction and evaluation paradigm): Useful contrast for highly structured API-based evaluation. Strong reference for AI anchors, variance reduction, and standardized calibration.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Supports the need for cross-benchmark comparability and transparent anchor design.

## 10. Relation to nearby papers
- Closest predecessor(s): PokerBench, Slumbot-based poker evaluation, solver-grounded poker AI work
- Closest follow-up(s): future standardized poker and imperfect-information benchmarks
- Best comparison targets inside our corpus: PokerBench, CompleteChessGames, MixingExpertKnowledge, PokeChamp
- What this paper uniquely adds relative to neighbors: It evaluates directly against a fixed superhuman poker anchor and makes variance reduction part of the benchmark design.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- The paper introduces a public API and standardized evaluation framework for heads-up no-limit Texas Hold'em.
- GTO Wizard AI is used as the main benchmark anchor, and the paper states that it defeated Slumbot by 19.4 plus or minus 4.1 bb/100.
- The benchmark integrates AIVAT for variance reduction, which the paper says yields equivalent statistical significance with ten times fewer hands than naive Monte Carlo evaluation.
- Each evaluated LLM plays 5000 independent hands, and the best model in Table 2 is GPT-5.3 Extra High reasoning at -16 ± 3.0 bb/100.

### 11.2 Our synthesis / interpretation
- This is one of the stronger specialist-benchmark cards for Section 3 because calibration and statistical significance are part of the scientific contribution.
- It complements PokerBench well: PokerBench focuses on spot evaluation, while GTO Wizard Benchmark focuses on full-play benchmarking against a fixed anchor.

### 11.3 Uncertain or needs re-check
- If later drafting needs more detail, re-check the appendix prompt template and the detailed luck decomposition metrics beyond AIVAT.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? Already audited from the full paper; revisit only if we later need the appendix prompt or detailed decomposition metrics.
- Which section to read next if needed: detailed evaluation metrics appendix
- Follow-up question(s): How much of the benchmark's value comes from AIVAT and fixed-anchor design rather than from poker itself?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P1
- Reading depth: deep
- Batch ID: B09
- Outline sections: 1,2,3,4
- Survey role: representative
- Paper card path: `paper_cards/B09/GTOWizardBenchmark.md`
- Next action: draft-section
- Last updated: 2026-04-10
