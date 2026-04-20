# TextArena TextArena

## 0. Metadata
- Date: 2025/04
- Venue: arXiv
- Authors: Leon Guertler, Bobby Cheng, Simon Yu, Bo Liu, Leshem Choshen, Cheston Tan
- Paper link: https://arxiv.org/pdf/2504.11442.pdf
- Code link: https://github.com/TextArena/TextArena
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: medium
- Review gate label: usable

## 1. One-paragraph benchmark summary
- TextArena is an open-source suite of competitive text games for training and evaluating agentic behavior in LLMs. The paper describes an initial release of 57+ environments and notes that the collection had already grown to 74 games by publication, spanning single-player, two-player, and multi-player setups. It ties those environments to a public online-play system with real-time TrueSkill ratings against both humans and submitted models, explicitly targeting dynamic soft skills such as negotiation, theory of mind, and deception that are usually under-measured in static NLP benchmarks. For this survey, TextArena is one of the clearest recent papers on how text-game suites can become living benchmark platforms rather than static one-shot evaluations.

## 2. Position in our survey
- Why-games relevance: Competitive games generate dynamic, multi-turn pressure on strategy and social behavior while still producing clear outcomes and public leaderboards.
- Historical stage: open-ended general-game benchmark
- Narrative level(s): L2 strategic reasoning / L3 social intelligence / L5 cross-game generalization
- Most relevant outline section(s): 1,2,3,4
- Role in corpus: representative

## 3. Design-space coding
### 3.1 Environment structure
- Information structure: mixed
- Transition structure: mixed
- Agent structure: mixed
- Social structure: mixed
- Time structure: turn-based

### 3.2 World structure
- World type(s): board / card / social deduction / other
- Real game / simulated game / designed task-game hybrid: curated suite of text-based games under a shared framework
- Benchmark unit: match / episode

### 3.3 Benchmark scope
- Scope: expandable suite
- Number of games / tasks: 57+ in the initial release; Table 1 lists 74 environments at publication

### 3.4 Modality
- Primary modality: text
- Perception burden retained: dialogue, negotiation, state tracking, hidden information, and strategic interaction
- Perception burden removed: no raw visual perception or embodied control burden

## 4. What this benchmark measures
- Primary capability target: agentic competence across competitive text games
- Secondary capability target(s): negotiation, theory of mind, deception, planning, and cross-game robustness
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? yes
- Does it test social reasoning / deception / cooperation? yes
- Does it test visual grounding / spatial-temporal reasoning? no
- Does it test long-horizon autonomy / task completion? partially
- Does it test real-time efficiency? no
- Does it test cross-game transfer / open-ended generalization? yes
- Why is a game environment especially suitable here? Text games can stress dynamic social and strategic behavior while staying cheap to run and easy to expand.

## 5. Interaction paradigm
- Observation channel: text game state, dialogue history, and game-specific context
- Action channel: textual moves, responses, or strategy choices
- Interface type: natural language
- Agent scaffold allowed: none in the benchmark core
- Is there privileged API access? yes; offline interaction is mediated through a Gym-like text-game API, even though online play is also exposed to humans
- How close is the setup to human play? medium-high for text-mediated play; humans and models use the same text-game loop, but the underlying framework is standardized for programmatic access
- Main ecological-validity trade-off: TextArena gains scale and public comparability, but text-only interaction removes visual and motor burdens that matter in richer games

## 6. Evaluation protocol
- Main score: TrueSkill leaderboard rating
- Auxiliary score(s): per-game outcomes, human-versus-model comparisons, and soft-skill breakdowns
- Evaluation style: tournament / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: online play against humans and other submitted models
- Automatic verifiability: mixed-high
- Calibration method: real-time TrueSkill updates with participants initialized at `mu = 25` and `sigma = 25/3`, plus repeated cross-opponent play within the online system
- Anti-contamination argument: the benchmark emphasizes dynamic play and extensibility rather than a fixed static test set
- Reliability or comparability concerns: leaderboard scores depend on the active model pool, selected games, and submission protocol

## 7. Main contributions
- Contribution 1: Builds a broad text-game suite with 57+ initial environments and 74 listed environments at publication under one framework.
- Contribution 2: Connects the suite to a live online-play and leaderboard system with TrueSkill ratings.
- Contribution 3: Frames negotiation, theory of mind, and deception as benchmarkable soft skills rather than side effects.

## 8. Main findings and failure modes
- Core empirical takeaway: the paper presents TextArena as a living relative-evaluation system where model differences remain visible through dynamic competitive play rather than through a saturating fixed test set.
- Notable model failure mode 1: uneven performance across social and competitive game types
- Notable model failure mode 2: difficulty with negotiation, deception, and partner or opponent modeling
- Notable model failure mode 3: some reasoning models fail in game-specific formatting or secrecy constraints, for example by revealing private cards or roles during gameplay
- Does this paper reveal a benchmark-design limitation as well? yes; it shows that public leaderboard design and model-pool drift become part of benchmark validity

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Strong contemporary example of games testing dynamic interaction beyond static QA.
- Best use in Section 1 (taxonomy and evolutionary levels): Useful late-stage step from fixed suites to living benchmark platforms. Good anchor for broad curated text-game suites.
- Best use in Section 2 (core capabilities evaluated by games): Supports social reasoning, deception, and competitive planning claims.
- Best use in Section 3 (interaction and evaluation paradigm): Helps anchor natural-language-only game interaction. Important for leaderboard, TrueSkill, and human-vs-model evaluation discussion.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Supports the need for extensible, continuously updated benchmark ecosystems.

## 10. Relation to nearby papers
- Closest predecessor(s): clembench, game-specific social benchmarks, earlier text-game suites
- Closest follow-up(s): larger public benchmark platforms and online evaluation ecosystems
- Best comparison targets inside our corpus: LMGameBench, AIGameStore, GVGAILLM, Orak
- What this paper uniquely adds relative to neighbors: It turns text-game evaluation into a public, persistent arena rather than a closed offline paper benchmark.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- TextArena is described as an open-source collection of 57+ unique text-based environments, and the paper notes that the collection had grown to 74 games by publication.
- The framework supports single-player, two-player, and multi-player settings and connects them to online play against humans and submitted models.
- The paper uses real-time TrueSkill ratings and explicitly highlights negotiation, theory of mind, and deception as key benchmark targets.
- Table 1 breaks the current environment inventory down as 16 single-player, 47 two-player, and 11 multi-player environments.

### 11.2 Our synthesis / interpretation
- TextArena is one of the strongest missing pieces for the survey's paradigm section because it combines suite breadth with live leaderboard infrastructure.
- It is also a useful bridge between narrow social-deduction benchmarks and broader agent-platform work.

### 11.3 Uncertain or needs re-check
- Re-check the exact environment taxonomy and whether the final version of the paper reports the full leaderboard roster or only a subset.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? Full paper read completed for this audit; revisit only if we later need the exact online submission flow or the full environment appendix.
- Which section to read next if needed: Section 4 / Appendix A / Appendix B
- Follow-up question(s): How stable are TextArena rankings under changes in opponent pool and game mix?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P1
- Reading depth: deep
- Batch ID: B06
- Outline sections: 1,2,3,4
- Survey role: representative
- Paper card path: `paper_cards/B06/TextArena.md`
- Check status: unchecked
- Last updated: 2026-04-10
