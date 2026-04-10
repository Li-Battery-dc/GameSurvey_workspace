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
- GAMABench is a multi-player game-theory benchmark built around eight classical scenarios, but extends them beyond the usual two-player, two-action setting through multi-player, multi-round, and multi-action variants with adjustable parameters. It groups games into cooperative, betraying, and sequential categories, rescales game-specific raw scores into a unified 0-100 scheme, and uses those scores to study robustness, prompt sensitivity, and parameter generalizability. The paper analyzes GPT-3.5 in depth with ten same-model agents, then reports a 13-model leaderboard. For this survey, GAMABench is best read as a parameterized formal diagnostic benchmark: its "dynamic" contribution is mainly scenario variation and score adaptation rather than richer interaction interfaces.

## 2. Position in our survey
- Why-games relevance: Classical game-theory scenarios compress many real-world decision dilemmas into tunable, measurable settings that support multi-agent evaluation without requiring rich narrative worlds.
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
- Secondary capability target(s): arithmetic reasoning, theory-of-mind reasoning, robustness to prompt and temperature changes, cooperation versus betrayal, and sequential decision-making
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? yes
- Does it test social reasoning / deception / cooperation? yes
- Does it test visual grounding / spatial-temporal reasoning? no
- Does it test long-horizon autonomy / task completion? no
- Does it test real-time efficiency? no
- Does it test cross-game transfer / open-ended generalization? no
- Why is a game environment especially suitable here? Parameterized games let the benchmark vary strategic structure while keeping the objective and scoring rules explicit.

## 5. Interaction paradigm
- Observation channel: text prompts describing rules, current round, historical outcomes, and player-specific information such as valuations, rank, or hit rate
- Action channel: JSON-formatted bids, proposals, votes, dish choices, targets, or other structured textual decisions
- Interface type: natural language / structured action space / hybrid
- Agent scaffold allowed: none by default; CoT and role prompting in targeted ablations
- Is there privileged API access? yes
- How close is the setup to human play? low; GAMABench is a prompt-based formal decision benchmark with explicit rules, repeated summaries, and structured JSON outputs
- Main ecological-validity trade-off: it gains multi-player breadth and parameter variation at the cost of using heavily mediated prompt interfaces and same-model multi-agent play rather than ecological play loops

## 6. Evaluation protocol
- Main score: rescaled 0-100 gamma-bench score aggregated across eight game-specific raw-score formulas
- Auxiliary score(s): robustness analyses over multiple runs, temperature settings, prompt variants, generalization across alternative parameter settings, and a 13-model leaderboard
- Evaluation style: native score / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: main experiments use ten agents instantiated from the same LLM, with auxiliary appendix experiments against fixed strategies; the framework can also include humans, but no broad human baseline is reported in the main leaderboard
- Automatic verifiability: high
- Calibration method: game-specific raw-score formulas rescaled to 0-100, five runs under default settings, temperature sweeps, prompt-template sweeps, and parameterized setting variation
- Anti-contamination argument: moderate rather than strong; the benchmark uses classical game-theory scenarios, but varying parameters and multi-player settings are intended to reduce simple memorization and leakage
- Reliability or comparability concerns: scores depend on benchmark-specific rescaling, the main setup uses same-model agents rather than mixed-model play, and the fixed 20-round horizon may affect strategic behavior in repeated games

## 7. Main contributions
- Contribution 1: Extends game-theoretic LLM evaluation to multi-player, multi-round, and multi-action settings across eight classical scenarios.
- Contribution 2: Introduces game-specific scoring plus 0-100 rescaling and parameterized scenario variation for robustness and generalizability testing.
- Contribution 3: Provides both detailed GPT-3.5 behavioral analysis and a wider 13-model leaderboard.

## 8. Main findings and failure modes
- Core empirical takeaway: GPT-3.5 is fairly robust across repeated runs and temperature changes but generalizes unevenly across altered settings; CoT improves its overall score from 45.9 to 57.9, whereas role prompting helps only marginally; and Gemini-1.5-Pro leads the reported leaderboard at 69.8.
- Notable model failure mode 1: weak generalization across altered game settings despite acceptable performance on familiar variants
- Notable model failure mode 2: prompt and temperature changes can alter decision quality meaningfully
- Notable model failure mode 3: many models struggle to balance self-interest against collective welfare across betrayal-oriented games
- Does this paper reveal a benchmark-design limitation as well? yes; its custom scoring scheme is useful inside the benchmark but makes cross-benchmark interpretation less transparent

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Limited use only; it can support the claim that parameterized games offer a renewable formal test bed, but it is not a primary motivation anchor.
- Best use in Section 1 (taxonomy and evolutionary levels): Helps show the move from small fixed canonical games to broader multi-player, multi-round, parameterized formal probes.
- Best use in Section 2 (core capabilities evaluated by games): Supports discussion of arithmetic reasoning, theory-of-mind reasoning, cooperation-versus-betrayal choices, and sequential tactical reasoning.
- Best use in Section 3 (interaction and evaluation paradigm): Strong contrast case for prompt-mediated JSON interfaces, repeated-round summaries, game-specific scoring, and robustness or generalizability analysis under parameter changes.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Supports the argument that benchmark-specific scoring and parameter variation improve diagnosis but reduce comparability and still stop short of ecological validity.

## 10. Relation to nearby papers
- Closest predecessor(s): GTBench and two-player game-theory evaluations
- Closest follow-up(s): TMGBench and later broader strategic suites
- Best comparison targets inside our corpus: GameBench, TMGBench, BeyondScaling, OpenGuanDan
- What this paper uniquely adds relative to neighbors: It pushes formal strategic benchmarking toward multi-player, multi-round, parameterized scenarios without abandoning classical game-theory grounding.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- GAMABench includes eight classical game-theory scenarios organized into cooperative, betraying, and sequential categories.
- The default case study uses ten GPT-3.5 (0125) agents, twenty rounds for simultaneous games, temperature 1, and five repeated runs to stabilize estimates.
- The benchmark uses game-specific raw-score formulas that are rescaled to 0-100, then reports robustness under temperature and prompt variation plus generalizability under changed game settings.
- The paper reports that CoT improves GPT-3.5’s overall score from 45.9 to 57.9, while Gemini-1.5-Pro tops the leaderboard at 69.8, followed by LLaMA-3.1-70B at 65.9 and Mixtral-8x22B at 62.4.

### 11.2 Our synthesis / interpretation
- GAMABench is less central than GTBench for formal taxonomy, but more useful for showing how the field tried to escape tiny canonical setups without leaving the prompt-based game-theory space.
- It is a helpful reminder that "dynamic" can mean parameter variation and score adaptation rather than richer interfaces or more ecological environments.

### 11.3 Uncertain or needs re-check
- Re-check Appendix E if we later need the exact rescaling formulas or want to compare scores across games more carefully.
- Re-check Appendix I if we later cite the same-model multi-agent limitation or the fixed 20-round horizon as benchmark caveats.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? Already completed in this audit; no further reread is needed unless we need exact score formulas or appendix-level robustness tables.
- Which section to read next if needed: 3 / Appendix E / Appendix F / Appendix I
- Follow-up question(s): Should GAMABench anchor the survey’s discussion of parameterized formal diagnostics, or serve mainly as a contrast case on custom scoring and same-model self-play?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P1
- Reading depth: deep
- Batch ID: B02
- Outline sections: 1,2,3,4
- Survey role: representative
- Paper card path: `paper_cards/B02/GAMABench.md`
- Check status: unchecked
- Last updated: 2026-04-10
