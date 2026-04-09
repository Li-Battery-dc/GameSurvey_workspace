# GAMABench How Far Are We on the Decision-Making of LLMs? Evaluating LLMs' Gaming Ability in Multi-Agent Environments

## 0. Metadata
- Date: 2024/05
- Venue: ICLR 2025
- Authors: Jen-tse Huang, Eric John Li, Man Ho Lam, Tian Liang, Wenxuan Wang, Youliang Yuan, Wenxiang Jiao, Xing Wang, Zhaopeng Tu, Michael R. Lyu
- Paper link: https://arxiv.org/pdf/2403.11807v7
- Code link: https://github.com/CUHK-ARISE/GAMABench
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: high
- Review gate label: usable

## 1. One-paragraph benchmark summary
- GAMABench is a multi-player game-theory benchmark built around eight classical scenarios, but extends them beyond the usual two-player, two-action setting through dynamic parameters, multi-round play, and multi-action choices. It groups games into cooperative, betraying, and sequential categories and uses a dynamic scoring scheme to compare robustness, prompt sensitivity, and generalizability across variants. The paper analyzes both one model family in depth and a broader 13-model leaderboard. For this survey, GAMABench is a representative formal-root benchmark because it keeps the game-theoretic abstraction but broadens player structure and scenario generation to reduce trivial saturation.

## 2. Position in our survey
- Why-games relevance: Classical game-theory scenarios compress many real-world decision dilemmas into tunable, measurable settings that support multi-agent evaluation without requiring rich narrative worlds.
- Historical stage: formal container
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
- World type(s): other
- Real game / simulated game / designed task-game hybrid: designed task-game hybrid based on classical game-theory scenarios
- Benchmark unit: game instance

### 3.3 Benchmark scope
- Scope: curated suite
- Number of games / tasks: 8 game-theory scenarios with dynamically varied parameters
- Benchmark intent: diagnostic evaluation

### 3.4 Modality
- Primary modality: text
- Perception burden retained: long-rule understanding, arithmetic reasoning, theory-of-mind reasoning, and strategic choice under varying player configurations
- Perception burden removed: no perceptual interface or embodied interaction burden

## 4. What this benchmark measures
- Primary capability target: decision-making in multi-agent game-theoretic environments
- Secondary capability target(s): robustness to prompt and temperature changes, generalization across parameterized scenarios, cooperation versus betrayal, and sequential decision-making
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? yes
- Does it test social reasoning / deception / cooperation? yes
- Does it test visual grounding / spatial-temporal reasoning? no
- Does it test long-horizon autonomy / task completion? partially
- Does it test real-time efficiency? no
- Does it test cross-game transfer / open-ended generalization? partially
- Why is a game environment especially suitable here? Parameterized games let the benchmark vary strategic structure while keeping the objective and scoring rules explicit.

## 5. Interaction paradigm
- Observation channel: text prompts describing game rules, current setting, prior outcomes, and player-specific information
- Action channel: JSON-formatted or otherwise structured textual decisions
- Interface type: natural language / hybrid
- Agent scaffold allowed: other
- Is there privileged API access? yes
- How close is the setup to human play? low; GAMABench is primarily a formal prompt-based decision benchmark
- Main ecological-validity trade-off: it gains breadth and parameterized generalization at the cost of removing perceptual and interface realism

## 6. Evaluation protocol
- Main score: dynamic benchmark score aggregated across the eight games
- Auxiliary score(s): robustness analyses over multiple runs, temperature settings, prompt variants, and generalization across different game settings
- Evaluation style: native score / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: the framework supports humans and fixed strategies, but the main reported results focus on LLM cohorts playing the scenarios
- Automatic verifiability: high
- Calibration method: dynamically adjustable game parameters, shared prompt templates, and multi-agent replication within each model family
- Anti-contamination argument: dynamic scenario generation and varied parameters are intended to reduce leakage from memorized classical settings
- Reliability or comparability concerns: because scores are benchmark-specific and heavily parameterized, comparison to other suites is less intuitive than raw win rates

## 7. Main contributions
- Contribution 1: Extends game-theoretic LLM evaluation to multi-player, multi-round, and multi-action settings.
- Contribution 2: Introduces a dynamic scoring scheme and parameterized scenario generation for broader robustness testing.
- Contribution 3: Provides both detailed single-model analysis and a wider 13-model leaderboard.

## 8. Main findings and failure modes
- Core empirical takeaway: GPT-3.5 shows decent robustness but limited generalizability, CoT helps, and Gemini-1.5-Pro leads the reported leaderboard.
- Notable model failure mode 1: weak generalization across altered game settings despite acceptable performance on familiar variants
- Notable model failure mode 2: prompt and temperature changes can alter decision quality meaningfully
- Notable model failure mode 3: many models struggle to balance self-interest against collective welfare across betrayal-oriented games
- Does this paper reveal a benchmark-design limitation as well? yes; its custom scoring scheme is useful inside the benchmark but makes cross-benchmark interpretation less transparent

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Good evidence that parameterized games can create a renewable decision-making benchmark.
- Best use in Section 1 (taxonomy and evolutionary levels): Helps show the move from small canonical games to broader multi-agent scenario generation. Useful for social-structure and multi-player taxonomy discussion.
- Best use in Section 2 (core capabilities evaluated by games): Supports discussion of ToM, arithmetic reasoning, and cooperation-versus-betrayal decisions.
- Best use in Section 3 (interaction and evaluation paradigm): Mainly as a contrast case showing what is lost when all perception is abstracted away. Useful for dynamic scoring, prompt-robustness analysis, and generalizability evaluation.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Supports the argument that benchmark-specific scoring can improve diagnosis while reducing comparability.

## 10. Relation to nearby papers
- Closest predecessor(s): GTBench and two-player game-theory evaluations
- Closest follow-up(s): TMGBench and later broader strategic suites
- Best comparison targets inside our corpus: [GTBench](D:/research_root/GameSurvey/workspace/paper_cards/B07/GTBench.md), [GameBench](D:/research_root/GameSurvey/workspace/paper_cards/B07/GameBench.md), [TMGBench](D:/research_root/GameSurvey/workspace/paper_cards/B07/TMGBench.md), [CKArena](D:/research_root/GameSurvey/workspace/paper_cards/B02/CKArena.md)
- What this paper uniquely adds relative to neighbors: It pushes formal strategic benchmarking toward multi-player, parameterized scenarios without abandoning classical game-theory grounding.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- GAMABench includes eight classical game-theory scenarios organized into cooperative, betraying, and sequential categories.
- The benchmark varies player counts, actions, rounds, temperatures, prompts, and other parameters to study robustness and generalization.
- The paper reports Gemini-1.5-Pro as the top model on the leaderboard, with CoT improving decision-making in the detailed GPT-3.5 analyses.

### 11.2 Our synthesis / interpretation
- GAMABench is less central than GTBench for formal taxonomy, but more useful for showing how the field tried to escape tiny canonical setups without leaving the formal game-theory space.
- It is a helpful reminder that "dynamic" can mean parameter variation rather than richer interfaces or more ecological environments.

### 11.3 Uncertain or needs re-check
- Re-check the appendix if we later need the exact dynamic scoring formula or per-game score normalization details.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? Only if we later need a tighter comparison between GAMABench’s scoring design and GTBench’s tournament-style evaluation.
- Which section to read next if needed: 2 / 3 / Appendix F
- Follow-up question(s): Should GAMABench anchor the survey’s discussion of robustness and parameterized variation inside formal benchmarks?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P1
- Reading depth: deep
- Batch ID: B07
- Outline sections: 1,2,3,4
- Survey role: representative
- Paper card path: `paper_cards/B07/GAMABench.md`
- Next action: draft-section
- Last updated: 2026-04-05
