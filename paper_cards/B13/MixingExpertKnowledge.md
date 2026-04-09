# MixingExpertKnowledge Mixing Expert Knowledge: Bring Human Thoughts Back To the Game of Go

## 0. Metadata
- Date: 2025/10
- Venue: NeurIPS 2025
- Authors: Yichuan Ma, Linyang Li, Yongkang Chen, Peiji Li, Jiasheng Ye, Qipeng Guo, Dahua Lin, Kai Chen
- Paper link: https://arxiv.org/pdf/2601.16447v1.pdf
- Code link:
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: medium
- Review gate label: usable

## 1. One-paragraph benchmark summary
- This paper presents LoGos, a Go-specialist general LLM trained by mixing structured Go expertise with long chain-of-thought reasoning data, then refining with RL. It is not mainly a benchmark paper, but it contributes a Go evaluation benchmark, KataGo-Bench-1K, and uses it to show that a general LLM can approach professional Go-level next-move prediction while retaining broad reasoning performance. The paper is relevant to the survey as a specialist upper-bound case and as evidence that benchmarked domain expertise can be injected into a general model when scalable structured knowledge exists. It should not be treated as a broad game benchmark anchor.

## 2. Position in our survey
- Why-games relevance: Go remains a classic domain for evaluating whether structured strategy expertise can be incorporated into general models.
- Historical stage: diagnostic capability probe / specialist comparison
- Narrative level(s): L2 strategic reasoning
- Most relevant outline section(s): 1,4
- Role in corpus: peripheral

## 3. Design-space coding
### 3.1 Environment structure
- Information structure: perfect
- Transition structure: deterministic
- Agent structure: two-player
- Social structure: competitive
- Time structure: turn-based

### 3.2 World structure
- World type(s): board
- Real game / simulated game / designed task-game hybrid: real board game represented as text next-move prediction
- Benchmark unit: board position

### 3.3 Benchmark scope
- Scope: single game
- Number of games / tasks: 1,000 evaluation positions in KataGo-Bench-1K plus tournament-style comparisons
- Benchmark intent: specialist evaluation

### 3.4 Modality
- Primary modality: text / symbolic state
- Perception burden retained: board understanding and next-move reasoning
- Perception burden removed: no visual board input

## 4. What this benchmark measures
- Primary capability target: specialist Go move prediction from a general LLM
- Secondary capability target(s): interaction between domain-specific expertise and general reasoning training
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? no
- Does it test social reasoning / deception / cooperation? no
- Does it test visual grounding / spatial-temporal reasoning? no
- Does it test long-horizon autonomy / task completion? no
- Does it test real-time efficiency? no
- Does it test cross-game transfer / open-ended generalization? no
- Why is a game environment especially suitable here? Go offers an extreme strategy domain where specialist performance ceilings are already well understood.

## 5. Interaction paradigm
- Observation channel: textualized move history and board state
- Action channel: next-move prediction and natural-language commentary in the trained model
- Interface type: natural language / structured action space / hybrid
- Agent scaffold allowed: long CoT and RL fine-tuning
- Is there privileged API access? yes; the game is represented in a machine-friendly textual format
- How close is the setup to human play? low; the evaluation is mostly next-move prediction rather than full board interaction
- Main ecological-validity trade-off: the paper measures specialist competence cleanly, but mostly through move prediction rather than natural game play

## 6. Evaluation protocol
- Main score: accuracy on KataGo-Bench-1K
- Auxiliary score(s): comparative Elo-style tournament analyses and general benchmark retention
- Evaluation style: accuracy / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: LoGos is compared with strong closed-source LLMs and KataGo-Human-SL models across skill levels
- Automatic verifiability: high
- Calibration method: a 1,000-sample benchmark annotated from KataGo plus comparative tournaments
- Anti-contamination argument: the model’s strength is attributed to injected structured expert knowledge rather than broad pretraining alone
- Reliability or comparability concerns: next-move prediction is not the same as full-game play, and the benchmark is highly specialist

## 7. Main contributions
- Contribution 1: Shows a training recipe for mixing structured Go knowledge with general reasoning data.
- Contribution 2: Introduces KataGo-Bench-1K for evaluating Go move prediction in LLMs.
- Contribution 3: Demonstrates that a general LLM can reach Go-specific performance above other general LLMs while retaining broad reasoning ability.

## 8. Main findings and failure modes
- Core empirical takeaway: with expert-knowledge mixing and RL, a general LLM can dramatically improve on Go and approach professional-level benchmark performance.
- Notable model failure mode 1: without domain-specific cold-start data, self-exploration fails to reach even beginner-level strength
- Notable model failure mode 2: naive direct prediction supervision underperforms structured heuristic data construction
- Notable model failure mode 3: the approach depends on access to scalable expert knowledge and carefully designed heuristics
- Does this paper reveal a benchmark-design limitation as well? yes; it shows that specialist benchmarks can be advanced by heavy domain-specific data construction not available for all domains

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Limited; mostly a specialist comparison case.
- Best use in Section 1 (taxonomy and evolutionary levels): Useful for the return of board-game specialists inside the LLM era. Helps distinguish benchmark papers from specialist training-plus-evaluation papers.
- Best use in Section 2 (core capabilities evaluated by games): A case study in expert strategic knowledge injection.
- Best use in Section 3 (interaction and evaluation paradigm): Minor use only. Useful for move-prediction benchmark plus tournament correlation.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Supports discussion of when specialist upper bounds are achievable for LLMs.

## 10. Relation to nearby papers
- Closest predecessor(s): specialized Go engines, chess-specialist LLMs
- Closest follow-up(s): future expert-knowledge-mixing systems
- Best comparison targets inside our corpus: CompleteChessGames, PokerBench, LLMChess
- What this paper uniquely adds relative to neighbors: It focuses on injecting specialist expertise into a general LLM while preserving general benchmarks.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- The paper introduces KataGo-Bench-1K, a 1,000-sample Go benchmark for LLM evaluation.
- LoGos is trained with mixed Go expertise and long-CoT reasoning data, followed by GRPO-based RL.
- The authors report Go benchmark performance above other general LLMs and competitive with strong human-level reference models.

### 11.2 Our synthesis / interpretation
- This is best read as a specialist upper-bound and methodology paper, not as a survey anchor for general game benchmarking.
- It is useful mainly for the survey’s boundary cases on domain-expert systems.

### 11.3 Uncertain or needs re-check
- Re-check the exact benchmark accuracy numbers and tournament Elo mapping if later drafting needs them.
- Re-check whether the "professional-level" claim is benchmark-only or supported by broader full-play evidence.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? Only if we later need a specialist upper-bound discussion.
- Which section to read next if needed: KataGo-Bench setup / self-exploration analysis / data-mixing studies
- Follow-up question(s): How portable is this expert-knowledge-mixing recipe to domains without a strong external engine like KataGo?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P3
- Reading depth: deep
- Batch ID: B13
- Outline sections: 1,4
- Survey role: peripheral
- Paper card path: `paper_cards/B13/MixingExpertKnowledge.md`
- Next action: draft-section
- Last updated: 2026-04-05
