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
- LMGAME-BENCH is a six-game benchmark for testing LLMs and VLMs on classical video games under both raw and scaffolded settings. Its main contribution is not only the game suite itself, but the gaming harness around it: perception modules, memory and reflection support, contamination checks, and prompt-standardization procedures that make game evaluation more discriminative and interpretable. The paper also analyzes how game performance relates to other benchmark families and shows that RL training on some games transfers to planning and agentic tasks such as BlocksWorld and WebShop. For this survey, LMGAME-BENCH is one of the strongest diagnostic-suite papers because it treats interface scaffolding, contamination, and prompt variance as benchmark-design variables rather than implementation details.

## 2. Position in our survey
- Why-games relevance: Video games stress perception, planning, memory, and low-fault-tolerance action in ways that are easy to score yet difficult to saturate.
- Historical stage: ecological agent benchmark
- Narrative level(s): L2 strategic reasoning / L4 visual agency / L5 cross-game generalization
- Most relevant outline section(s): 0,1,2,3,5
- Role in corpus: representative

## 3. Design-space coding
### 3.1 Environment structure
- Information structure: mixed
- Transition structure: mixed
- Agent structure: single-agent
- Social structure: N/A
- Time structure: mixed

### 3.2 World structure
- World type(s): platformer / puzzle / adventure / other
- Real game / simulated game / designed task-game hybrid: curated suite of established video games with a common harness
- Benchmark unit: game episode

### 3.3 Benchmark scope
- Scope: curated suite
- Number of games / tasks: 6 games
- Benchmark intent: diagnostic evaluation / train+eval foundation

### 3.4 Modality
- Primary modality: mixed
- Perception burden retained: screen understanding, long-horizon planning, partial observability, and game-specific control logic
- Perception burden removed: when the harness is enabled, perception modules and memory modules expose more machine-friendly state descriptions

## 4. What this benchmark measures
- Primary capability target: game-agent competence under both raw and scaffolded interfaces
- Secondary capability target(s): effect of perception and memory scaffolds, contamination sensitivity, prompt sensitivity, and transfer from RL game training
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? yes
- Does it test social reasoning / deception / cooperation? no
- Does it test visual grounding / spatial-temporal reasoning? yes
- Does it test long-horizon autonomy / task completion? yes
- Does it test real-time efficiency? partially
- Does it test cross-game transfer / open-ended generalization? yes
- Why is a game environment especially suitable here? Games combine perception, state tracking, and sequential control in one verifiable loop, making them a compact proxy for broader agentic competence.

## 5. Interaction paradigm
- Observation channel: game screenshots, extracted symbolic or textual state representations, and optional memory/reflection traces
- Action channel: game actions chosen turn by turn through the gaming harness
- Interface type: GUI interaction / API / hybrid
- Agent scaffold allowed: memory / reflection / other
- Is there privileged API access? yes
- How close is the setup to human play? medium; the games are real, but the harness can substantially reduce perceptual burden
- Main ecological-validity trade-off: LMGAME-BENCH spans real games, yet its strongest results often come from harnessed settings that blend ecological play with diagnostic abstraction

## 6. Evaluation protocol
- Main score: normalized per-game benchmark score
- Auxiliary score(s): harness-versus-no-harness comparisons, contamination analyses, prompt-variance analyses, benchmark-correlation studies, and RL transfer results
- Evaluation style: native score / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: 13 state-of-the-art models are compared with and without harness support, plus random-play baselines and human-level proficiency gaps
- Automatic verifiability: high
- Calibration method: standardized prompts, DSPy-based prompt optimization, contamination checks, and module ablations for perception and memory
- Anti-contamination argument: the paper explicitly tests vision-level contamination in Super Mario Bros and text-level contamination in Ace Attorney, then introduces mitigation procedures
- Reliability or comparability concerns: the benchmark meaningfully changes when the harness is enabled, so backbone comparisons depend on interface choices as much as on raw model ability

## 7. Main contributions
- Contribution 1: Builds a six-game benchmark plus harness for evaluating LLMs and VLMs on video games.
- Contribution 2: Treats perception modules, memory, contamination mitigation, and prompt standardization as benchmark infrastructure.
- Contribution 3: Connects game performance to other benchmark families and to RL transfer on planning or agentic tasks.

## 8. Main findings and failure modes
- Core empirical takeaway: without harnesses, many runs are near random; with harnesses, performance gaps become clearer, but even top models remain far below human-level play.
- Notable model failure mode 1: poor raw visual perception and long-horizon planning drive many near-random runs
- Notable model failure mode 2: prompt sensitivity remains large even among empirically tuned prompts
- Notable model failure mode 3: contamination can distort apparent ability, especially in games with public transcripts or iconic visual assets
- Does this paper reveal a benchmark-design limitation as well? yes; the benchmark shows that scaffold choice can dominate model ranking, which complicates comparisons unless the interface is reported explicitly

## 9. Why this paper matters for our survey
- Best use in Section 0 (why games): Strong evidence that games stress a composition of abilities usually benchmarked in isolation.
- Best use in Section 1 (historical evolution): Represents the move from simply using games to building benchmark-plus-harness ecosystems around them.
- Best use in Section 2 (design space): Useful for discussing real-game suites, scaffolded interfaces, and contamination-aware benchmark design.
- Best use in Section 3 (capability targets): Covers perception, planning, memory, and some transfer.
- Best use in Section 4 (interaction paradigm): One of the best sources on how much the interface itself shapes game-agent performance.
- Best use in Section 5 (evaluation protocol): Strong reference for prompt variance, contamination studies, and module ablations.
- Best use in Section 6/7 (limitations and future): Supports the claim that future benchmarks must expose scaffolds and contamination checks, not hide them.

## 10. Relation to nearby papers
- Closest predecessor(s): BALROG and earlier video-game suite benchmarks
- Closest follow-up(s): KORGym and broader benchmark-platform papers
- Best comparison targets inside our corpus: [Balrog](D:/research_root/GameSurvey/workspace/paper_cards/B03/Balrog.md), [Orak](D:/research_root/GameSurvey/workspace/paper_cards/B05/Orak.md), [KORGym](D:/research_root/GameSurvey/workspace/paper_cards/B08/KORGym.md), [GAMEBoT](D:/research_root/GameSurvey/workspace/paper_cards/B08/GAMEBoT.md)
- What this paper uniquely adds relative to neighbors: It makes benchmark infrastructure itself part of the scientific claim by analyzing harnessing, contamination, and prompt standardization together.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- LMGAME-BENCH evaluates 13 models on six games and introduces harness modules for perception, memory, and prompt optimization.
- The paper reports that 40% of unharnessed game runs fail to beat random baselines, whereas 86.7% of harnessed runs do so.
- RL training on some games improves both in-domain gaming performance and some out-of-domain planning or agentic benchmarks.

### 11.2 Our synthesis / interpretation
- LMGAME-BENCH is one of the clearest papers for arguing that benchmark design now includes interface engineering, not just task selection.
- It is especially valuable because it does not treat contamination and prompt variance as afterthoughts.

### 11.3 Uncertain or needs re-check
- Re-check Sections 3.2 and 3.3 if we later need the exact low-rank factorization findings or the strongest transfer numbers into BlocksWorld and WebShop.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? A targeted reread is likely worthwhile later because this paper can support multiple survey sections.
- Which section to read next if needed: 2.2 / 3.2 / 3.3
- Follow-up question(s): Should LMGAME-BENCH or Orak anchor the survey’s discussion of scaffold-heavy game benchmark platforms?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P1
- Reading depth: deep
- Batch ID: B08
- Outline sections: 0,1,2,3,5
- Survey role: representative
- Paper card path: `paper_cards/B08/LMGameBench.md`
- Next action: draft-section
- Last updated: 2026-04-05
