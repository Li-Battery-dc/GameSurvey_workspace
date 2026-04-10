# TextQuests TextQuests: How Good are LLMs at Text-Based Video Games?

## 0. Metadata
- Date: 2025/07
- Venue: arXiv
- Authors: Long Phan, Mantas Mazeika, Andy Zou, Dan Hendrycks
- Paper link: https://arxiv.org/pdf/2507.23701v3.pdf
- Code link: https://github.com/centerforaisafety/textquests
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: high
- Review gate label: strong

## 1. One-paragraph benchmark summary
- TextQuests is a long-horizon text-game benchmark built from 25 Infocom games running through Jericho/Frotz. It is explicitly designed to test whether language agents can sustain coherent planning over hundreds of steps without external tools, and it evaluates both progress and harm in morally charged action spaces. The benchmark always provides the games' required `feelies`, optionally adds official `InvisiClues`, keeps the full turn history, and exposes an autosave or restore command that lets agents backtrack within the same run. For this survey, TextQuests is a strong anchor for long-horizon textual game autonomy, but its assistance mechanisms need to be stated explicitly when we compare it with less scaffolded settings.

## 2. Position in our survey
- Why-games relevance: Text adventures expose memory, planning, exploration, and instruction-following over very long action horizons in an automatically scored environment.
- Historical stage: ecological agent benchmark
- Narrative level(s): L2 strategic reasoning / L5 cross-game generalization
- Most relevant outline section(s): 2,3,4
- Role in corpus: representative

## 3. Design-space coding
### 3.1 Environment structure
- Information structure: imperfect
- Transition structure: mixed
- Agent structure: single-agent
- Social structure: N/A
- Time structure: turn-based

### 3.2 World structure
- World type(s): adventure
- Real game / simulated game / designed task-game hybrid: suite of classic commercial text adventures
- Benchmark unit: full game run

### 3.3 Benchmark scope
- Scope: curated suite
- Number of games / tasks: 25 Infocom games
- Benchmark intent: ecological evaluation

### 3.4 Modality
- Primary modality: text
- Perception burden retained: language grounding, long-context state tracking, and command interpretation
- Perception burden removed: no visual grounding is required

## 4. What this benchmark measures
- Primary capability target: long-horizon task completion in text environments
- Secondary capability target(s): memory, exploration, map-building, safety-relevant action choice, and robustness to sparse reward
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? yes
- Does it test social reasoning / deception / cooperation? no
- Does it test visual grounding / spatial-temporal reasoning? no
- Does it test long-horizon autonomy / task completion? yes
- Does it test real-time efficiency? no
- Does it test cross-game transfer / open-ended generalization? yes
- Why is a game environment especially suitable here? Text adventures create long, branching task arcs with sparse feedback and natural-language actions while remaining machine-verifiable.

## 5. Interaction paradigm
- Observation channel: textual room descriptions, inventory changes, and game feedback
- Action channel: free-form text commands
- Interface type: natural language
- Agent scaffold allowed: other; built-in autosave and restore are available within the environment, but no external planning tools are allowed
- Is there privileged API access? limited; play remains parser-based, but the benchmark exposes a restore command and injects clue documents into context in the clue-assisted setting
- How close is the setup to human play? high; it uses the standard text-adventure command loop
- Main ecological-validity trade-off: the parser loop is human-like, but the always-available feelies, optional official clues, and restore support make the benchmark easier to study than completely blind play

## 6. Evaluation protocol
- Main score: checkpoint-based game progress
- Auxiliary score(s): average harm, clue-versus-no-clue performance, and save/restore effects
- Evaluation style: milestone / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: multiple frontier LLMs are evaluated on the same 25 games with and without clues, with an optimal human walkthrough used as a progress reference in plots
- Automatic verifiability: high
- Calibration method: 500-step cap, preserved full history, standardized clue regimes, and explicit checkpoint labels for each game
- Anti-contamination argument: not a central claim; the benchmark's difficulty comes from long interactive trajectories rather than from fresh source material
- Reliability or comparability concerns: checkpoint scoring may undercount partial strategic competence, and results depend meaningfully on whether restore and clue access are available

## 7. Main contributions
- Contribution 1: Introduces a 25-game long-horizon text-adventure benchmark with standardized evaluation.
- Contribution 2: Adds a harm metric so that reckless progress can be separated from safer play.
- Contribution 3: Shows that memory and self-consistency failures dominate current language-agent performance.

## 8. Main findings and failure modes
- Core empirical takeaway: current LLM agents perform poorly on long-horizon text adventures, with large context windows alone not solving the problem.
- Notable model failure mode 1: hallucinating prior interactions or inventory state
- Notable model failure mode 2: repetitive navigation loops caused by weak mental maps
- Notable model failure mode 3: failure to sustain coherent strategy as context grows past very long horizons
- Does this paper reveal a benchmark-design limitation as well? yes; it shows that many agent benchmarks remain far shorter and easier than the horizons required for genuine autonomous play

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Strong evidence that games can operationalize hours-long, hundreds-step decision horizons in a compact benchmark.
- Best use in Section 1 (taxonomy and evolutionary levels): Extends the text-game lineage from short interactive tasks to genuinely long quests. Helps define long-horizon adventure suites as a distinct region of the design space.
- Best use in Section 2 (core capabilities evaluated by games): Supports discussion of memory, exploration, and planning failures.
- Best use in Section 3 (interaction and evaluation paradigm): An anchor for free-form natural-language command interfaces. Useful for checkpoint scoring plus harm-aware evaluation.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Supports the claim that long-horizon robustness remains a major open problem.

## 10. Relation to nearby papers
- Closest predecessor(s): InteractiveFictionGames and the Jiminy Cricket moral-evaluation setup it builds upon
- Closest follow-up(s): later long-horizon text-game agent evaluations rather than broad multimodal open-world benchmarks
- Best comparison targets inside our corpus: InteractiveFictionGames, MineNPCTask, TextAtari, Mars
- What this paper uniquely adds relative to neighbors: It combines long parser-based game trajectories with checkpoint progress, harm scoring, clue/no-clue conditions, and built-in restore support.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- The benchmark contains 25 Infocom games and caps runs at 500 steps.
- It always provides required game `feelies`, evaluates `With Clues` and `No Clues` settings, and keeps the full interaction history.
- It includes an autosave mechanism that lets agents issue `restore {step_id}` to backtrack within a run.
- It reports both checkpoint-based `Game Progress` and `Average Harm`.

### 11.2 Our synthesis / interpretation
- TextQuests is one of the most useful corpus papers for arguing that many current agent benchmarks still understate real long-horizon difficulty.
- The harm metric also makes it a useful bridge from raw progress scoring to more nuanced evaluation.
- It should not be used as a strong anti-contamination example, because the paper's contribution is interaction design and long-context pressure, not benchmark freshness.

### 11.3 Uncertain or needs re-check
- Re-check the appendix if we later need exact game lists or the strongest model numbers by condition.
- Re-check how save/restore changes performance if we use it in a discussion of scaffolding.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? Audit completed from the full paper; reread only if we later need exact per-game checkpoint or harm details.
- Which section to read next if needed: Appendix A and Appendix D for environment assistance details
- Follow-up question(s): Which specific games best expose memory collapse versus exploration failure, and how much of the gain comes from restore versus clues?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P1
- Reading depth: deep
- Batch ID: B05
- Outline sections: 2,3,4
- Survey role: representative
- Paper card path: `paper_cards/B05/TextQuests.md`
- Check status: unchecked
- Next action: draft-section
- Last updated: 2026-04-10
