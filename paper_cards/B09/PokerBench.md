# PokerBench PokerBench: Training Large Language Models to become Professional Poker Players

## 0. Metadata
- Date: 2025/01
- Venue: AAAI 2025
- Authors: Richard Zhuang, Akshat Gupta, Richard Yang, Aniket Rahane, Zhengyu Li, Gopala Anumanchipalli
- Paper link: https://arxiv.org/pdf/2501.08328v2.pdf
- Code link:
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: high
- Review gate label: strong

## 1. One-paragraph benchmark summary
- PokerBench is a specialist poker benchmark and accompanying training set for evaluating LLM decision quality on Texas no-limit hold'em spots rather than full end-to-end table play. The benchmark contains 1,000 pre-flop and 10,000 post-flop scenarios labeled with GTO references, and it scores both action accuracy and exact-match wager accuracy. The paper then validates the benchmark by showing that higher-scoring fine-tuned checkpoints also win more in 50k-hand heads-up matches, while a smaller 1,000-hand test against GPT-4 exposes the gap between GTO-style spot accuracy and exploitative live play. For this survey, PokerBench is best used as a specialist contrast on solver-grounded diagnostic evaluation, not as a broad social or ecological benchmark.

## 2. Position in our survey
- Why-games relevance: Poker combines hidden information, opponent modeling, and strategic trade-offs in a fully formalized setting with exact solver references.
- Historical stage: diagnostic capability probe
- Benchmark level(s): L2 strategic reasoning
- Most relevant outline section(s): 1,2,3,4
- Role in corpus: contrast

## 3. Design-space coding
### 3.1 Game structure
- Information structure: imperfect
- Transition structure: stochastic
- Agent structure: multi-agent
- Social structure: competitive
- Time structure: turn-based

### 3.2 World structure
- World type(s): card
- Real game / simulated game / designed task-game hybrid: benchmark of real poker decision spots derived from solver analysis
- Benchmark unit: decision spot

### 3.3 Benchmark scope
- Scope: single game
- Number of games / tasks: 11,000 spots covering pre-flop and post-flop play

### 3.4 Modality
- Observation modality: text or symbolic
- Action modality: semantic
- Perception burden retained: betting history, hidden-information reasoning, and wager selection
- Perception burden removed: no visual table interface or live timing burden

## 4. What this benchmark measures
- Primary capability target: GTO-aligned poker decision making
- Secondary capability target(s): betting-size precision, balanced strategy selection, and the relation between spot-level accuracy and match play
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? yes
- Does it test social reasoning / deception / cooperation? no
- Does it test visual grounding / spatial-temporal reasoning? no
- Does it test long-horizon autonomy / task completion? no
- Does it test real-time efficiency? no
- Does it test cross-game transfer / open-ended generalization? no
- Why is a game environment especially suitable here? Poker has exact strategic references and forces reasoning under hidden information and mixed strategies.

## 5. Interaction paradigm
- Observation channel: textualized poker spot descriptions including hole cards, board, and action history
- Action channel: fold/call/raise-style decisions with explicit sizes
- Interface type: natural language / structured action space / hybrid
- Agent scaffold allowed: none in the benchmark evaluation
- Is there privileged API access? yes; the benchmark presents solver-clean spot state rather than a raw table interface
- How close is the setup to human play? low; it captures strategic decision structure but removes table interaction, timing, and full multi-hand adaptation
- Main ecological-validity trade-off: PokerBench gains fast, reproducible solver-grounded evaluation by abstracting away live table dynamics and most exploitative adaptation

## 6. Evaluation protocol
- Main score: action accuracy and exact match accuracy
- Auxiliary score(s): 50k-hand heads-up bb/100 between fine-tuned checkpoints and a 1,000-hand matchup against GPT-4
- Evaluation style: accuracy / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: pretrained and fine-tuned LLMs are compared on solver-labeled spots, then selected checkpoints are compared in simulated heads-up play
- Automatic verifiability: high
- Calibration method: curated pre-flop and post-flop spot sampling grounded in GTOWizard and WASM-Postflop solver outputs, plus match-play validation
- Anti-contamination argument: no strong explicit contamination claim beyond using diverse solver-generated spots instead of a small public quiz set
- Reliability or comparability concerns: spot accuracy measures closeness to GTO decisions, not full exploitative or ecological skill; live validation is heads-up and therefore narrower than the 6-max spot benchmark

## 7. Main contributions
- Contribution 1: Introduces an 11,000-spot poker benchmark with separate pre-flop and post-flop evaluation.
- Contribution 2: Uses exact action and size metrics grounded in GTO solver outputs.
- Contribution 3: Validates the benchmark by relating checkpoint scores to stronger simulated match performance while also surfacing limits of simple supervised fine-tuning.

## 8. Main findings and failure modes
- Core empirical takeaway: current pretrained LLMs are far from GTO poker play, with GPT-4 reaching 65.54% action accuracy and 53.55% exact-match accuracy overall, while fine-tuning can lift Llama-3-8B to 80.64% and 78.26% respectively.
- Notable model failure mode 1: poor bet-size precision even when the action category is correct
- Notable model failure mode 2: weak post-flop decision quality relative to solver-grounded references
- Notable model failure mode 3: simple supervised fine-tuning can improve benchmark accuracy without yielding fully robust exploitative play against off-distribution strategies
- Does this paper reveal a benchmark-design limitation as well? yes; it argues that full-game poker evaluation alone is too costly during development, but also shows that spot-level GTO accuracy and live-play exploitability are not identical

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Supports the use of games to evaluate hidden-information strategy.
- Best use in Section 1 (taxonomy and evolutionary levels): A specialist benchmark reflecting a move from full-play engines to faster diagnostic spot evaluation. Useful for decision-spot versus full-trajectory benchmark distinctions inside single-game specialists.
- Best use in Section 2 (core capabilities evaluated by games): Strong evidence on uncertainty, balance, and opponent-aware play.
- Best use in Section 3 (interaction and evaluation paradigm): A strong contrast case for structured text-state inputs, solver-grounded action-level metrics, and the difference between spot evaluation and match-play validation.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Supports the idea that specialist domains may need both cheap diagnostic spot evaluation and more ecological match-play checks.

## 10. Relation to nearby papers
- Closest predecessor(s): solver-based poker AI work and earlier GPT-4 poker spot analyses
- Closest follow-up(s): GTOWizardBenchmark and later specialist poker evaluations with stronger calibration stacks
- Best comparison targets inside our corpus: GTOWizardBenchmark, CompleteChessGames, MixingExpertKnowledge, PokeChamp
- What this paper uniquely adds relative to neighbors: It pairs a solver-grounded spot benchmark and training set with explicit match-play validation, then shows that the two evaluation views align only partially

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- PokerBench contains 1,000 pre-flop spots and 10,000 post-flop spots for 6-max NLH.
- It evaluates both Action Accuracy and Exact Match Accuracy using GTOWizard pre-flop labels and WASM-Postflop solver outputs.
- GPT-4 is the best pretrained model in Table 2 with 65.54% action accuracy and 53.55% exact-match accuracy overall.
- The paper shows that higher-scoring Llama-3-8B checkpoints win more over 50k-hand heads-up matches, while GPT-4 beats the best fine-tuned checkpoint over a separate 1,000-hand test.

### 11.2 Our synthesis / interpretation
- PokerBench is a strong specialist benchmark for imperfect-information reasoning because it makes solver-grounded action quality auditable and then partially validates that score with live play.
- It is best used as a contrast to broader cross-game papers and as evidence that benchmark design in specialist domains may need both spot metrics and gameplay checks.

### 11.3 Uncertain or needs re-check
- If later drafting needs more detail, re-check the appendix style analysis around GPT-4's off-GTO "donking" behavior and how strongly that specific failure mode generalizes.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? Already audited from the full paper; revisit only if the survey needs appendix-level style analysis.
- Which section to read next if needed: gameplay analysis appendix
- Follow-up question(s): How should the survey phrase the gap between GTO-style spot accuracy and exploitative live-play strength without overstating either side?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P2
- Reading depth: deep
- Batch ID: B09
- Outline sections: 1,2,3,4
- Survey role: contrast
- Paper card path: `paper_cards/B09/PokerBench.md`
- Next action: draft-section
- Last updated: 2026-04-10
