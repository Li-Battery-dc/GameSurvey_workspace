# LLMPlayStarCraftII Large Language Models Play StarCraft II: Benchmarks and A Chain of Summarization Approach

## 0. Metadata
- Date: 2023/12
- Venue: NeurIPS 2024
- Authors: Weiyu Ma, Qirui Mi, Yongcheng Zeng, Xue Yan, Yuqiao Wu, Runji Lin, Haifeng Zhang, Jun Wang
- Paper link: https://arxiv.org/pdf/2312.11865v3.pdf
- Code link:
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: high
- Review gate label: strong

## 1. One-paragraph benchmark summary
- This paper introduces TextStarCraft II, a text-based StarCraft II environment for evaluating LLMs on macro strategy, real-time decision-making, and long-horizon planning within a single RTS domain. The environment converts SC2 state into textual observations, lets LLMs choose macro actions, and uses scripted micro policies for low-level execution; the authors also propose Chain of Summarization (CoS) to compress fast-moving game history into manageable reasoning context. The paper evaluates closed and fine-tuned open models against built-in AI, separately studies StarCraft II knowledge via expert-reviewed QA, and runs human-versus-agent matches with a lightweight fine-tuned model. For this survey, it is a key early benchmark in the text-interface SC2 line, but it should be read as macro-level RTS evaluation rather than as evidence of cross-game generalization or full ecological play.

## 2. Position in our survey
- Why-games relevance: Real-time strategy games compress resource management, tech progression, scouting, and long-horizon adaptation into one domain.
- Historical stage: ecological agent benchmark
- Narrative level(s): L2 strategic reasoning
- Most relevant outline section(s): 1,2,3,4
- Role in corpus: representative

## 3. Design-space coding
### 3.1 Environment structure
- Information structure: imperfect
- Transition structure: mixed
- Agent structure: multi-agent
- Social structure: competitive
- Time structure: real-time / hybrid

### 3.2 World structure
- World type(s): RTS
- Real game / simulated game / designed task-game hybrid: StarCraft II through a text interface with scripted micro control
- Benchmark unit: match

### 3.3 Benchmark scope
- Scope: single game
- Number of games / tasks: StarCraft II matches on selected ladder maps against built-in AI and humans
- Benchmark intent: ecological evaluation

### 3.4 Modality
- Primary modality: text / symbolic state
- Perception burden retained: strategic state understanding, resource planning, and scouting interpretation
- Perception burden removed: micro control and raw visual perception are abstracted away

## 4. What this benchmark measures
- Primary capability target: macro-strategic decision making in RTS play
- Secondary capability target(s): long-context summarization, tech progression, and strategic adaptation
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? yes
- Does it test social reasoning / deception / cooperation? no
- Does it test visual grounding / spatial-temporal reasoning? no in the core interface
- Does it test long-horizon autonomy / task completion? yes
- Does it test real-time efficiency? yes
- Does it test cross-game transfer / open-ended generalization? no
- Why is a game environment especially suitable here? SC2 requires layered decision making across economy, tech, and combat over extended time horizons.

## 5. Interaction paradigm
- Observation channel: textualized game state, multi-frame summaries, and strategic history
- Action channel: macro actions for production, construction, research, scouting, and high-level strategy
- Interface type: natural language / API / hybrid
- Agent scaffold allowed: summarization / scripted micro policy
- Is there privileged API access? yes
- How close is the setup to human play? medium-low; the game is authentic, but raw visual and micro burdens are replaced by textual state plus scripted execution
- Main ecological-validity trade-off: TextStarCraft II preserves strategic structure but removes much of the speed and perceptual pressure that make human SC2 difficult

## 6. Evaluation protocol
- Main score: win rate against level-5 built-in AI
- Auxiliary score(s): PBR, RUR, APU, and TR for macro-management analysis, SC2 knowledge QA judged by experts, and human-versus-agent match records
- Evaluation style: win rate / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: multiple LLMs and fine-tuned open models are tested against level-5 built-in AI, plus expert reviews and human matches
- Automatic verifiability: high
- Calibration method: shared maps, fixed race setup, and logged macro metrics
- Anti-contamination argument: no explicit contamination defense beyond preferring interactive SC2 evaluation to static strategy-only questioning
- Reliability or comparability concerns: results depend strongly on the scripted micro layer and the race/opponent configuration

## 7. Main contributions
- Contribution 1: Introduces TextStarCraft II as a text interface for LLM play in SC2.
- Contribution 2: Proposes Chain of Summarization to compress long strategic histories.
- Contribution 3: Shows that closed and fine-tuned open models can beat level-5 built-in AI and that a lightweight fine-tuned model can reach roughly Gold-level human performance in real-time matches.

## 8. Main findings and failure modes
- Core empirical takeaway: with text abstraction and CoS-style history compression, several LLMs can reach competent macro-level SC2 play against built-in AI, but strategic diversity and ecological realism remain limited.
- Notable model failure mode 1: dependence on scripted micro policies and constrained action sets
- Notable model failure mode 2: strategy collapse in fine-tuned models toward narrow unit compositions such as mass stalkers
- Notable model failure mode 3: difficulty understanding task requirements or generating valid commands for weaker open models
- Does this paper reveal a benchmark-design limitation as well? yes; it shows that RTS evaluation outcomes change substantially when micro control and vision are abstracted away

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Demonstrates why RTS games are still central stress tests for long-horizon strategic reasoning.
- Best use in Section 1 (taxonomy and evolutionary levels): A key early RTS benchmark in the LLM-agent literature. Important for text-abstracted RTS benchmarks.
- Best use in Section 2 (core capabilities evaluated by games): Supports planning, adaptation, and resource-management claims.
- Best use in Section 3 (interaction and evaluation paradigm): Strong reference for text-first RTS interfaces and summarization scaffolds. Useful for combining win rate with macro-management metrics.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Supports future work on bringing vision and richer control back into RTS benchmarks.

## 10. Relation to nearby papers
- Closest predecessor(s): AlphaStar-style RL environments
- Closest follow-up(s): StarCraftIIArena, VLMPlayStarCraftII
- Best comparison targets inside our corpus: VLMPlayStarCraftII, StarCraftIIArena, PokerBench, GTOWizardBenchmark
- What this paper uniquely adds relative to neighbors: It established the text-interface benchmark template for later LLM-focused SC2 evaluations.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- The paper introduces TextStarCraft II and the Chain of Summarization method.
- It evaluates proprietary models and fine-tuned open models against level-5 built-in AI and also reports separate human-versus-agent matches.
- The paper reports macro metrics including Population Block Ratio, Resource Utilization Ratio, Average Population Utilization, and Technology Rate.
- In the human-interaction test, a fine-tuned Qwen1.8B model goes 5/10 against a Gold player, 0/10 against Grandmaster and pro players, and 10/10 against a novice.

### 11.2 Our synthesis / interpretation
- This paper is the key starting point for the text-based StarCraft II line in the corpus.
- It is most useful as a historical and methodological anchor rather than as the final word on ecological RTS evaluation.

### 11.3 Uncertain or needs re-check
- If later drafting needs more detail, re-check the appendix logs and figures used for the policy-interpretability discussion and the exact model-by-model win-rate tables.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? Already audited from the full paper; revisit only if we later need appendix-level interpretability examples or exact per-model tables.
- Which section to read next if needed: built-in-AI evaluation tables / human interaction experiments
- Follow-up question(s): How much of the observed competence survives if the scripted micro layer is weakened?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P1
- Reading depth: deep
- Batch ID: B09
- Outline sections: 1,2,3,4
- Survey role: representative
- Paper card path: `paper_cards/B09/LLMPlayStarCraftII.md`
- Next action: draft-section
- Last updated: 2026-04-10
