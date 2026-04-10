# TextAtari TextAtari: 100K Frames Game Playing with Language Agents

## 0. Metadata
- Date: 2025/06
- Venue: arXiv
- Authors: Wenhao Li, Wenwu Li, Chuyun Shen, Junjie Sheng, Zixiao Huang, Di Wu, Yun Hua, Wei Yin, Xiangfeng Wang, Hongyuan Zha, Bo Jin
- Paper link: https://arxiv.org/pdf/2506.04098v2.pdf
- Code link: https://github.com/Lww007/Text-Atari-Agents
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: high
- Review gate label: usable

## 1. One-paragraph benchmark summary
- TextAtari is a long-horizon benchmark that converts Atari environments into text using AtariARI and evaluates language agents on tasks that conceptually extend toward 100,000 steps. In practice, the paper studies 23 Atari games under four prompt conditions, yielding nearly 100 benchmark settings while reporting 1000-step rollouts for cost reasons. The core contribution is less about beating Atari and more about establishing a text-only testbed for extremely long sequential decision-making with controlled knowledge injections and reasoning prompts. For this survey, the paper is a useful contrast to raw-vision Atari benchmarks because it isolates language-side planning and state tracking while stripping away pixel perception.

## 2. Position in our survey
- Why-games relevance: Text-translated games let the benchmark stress long-horizon planning while controlling how much perceptual prior knowledge is exposed.
- Historical stage: diagnostic capability probe
- Narrative level(s): L2 strategic reasoning / L5 cross-game generalization
- Most relevant outline section(s): 2,3,4
- Role in corpus: contrast

## 3. Design-space coding
### 3.1 Environment structure
- Information structure: mixed
- Transition structure: mixed
- Agent structure: single-agent
- Social structure: N/A
- Time structure: turn-based / throttled real-time abstraction

### 3.2 World structure
- World type(s): arcade / puzzle / adventure / other
- Real game / simulated game / designed task-game hybrid: Atari suite rendered into textual state descriptions
- Benchmark unit: episode

### 3.3 Benchmark scope
- Scope: curated suite
- Number of games / tasks: 23 Atari games and nearly 100 game-condition settings
- Benchmark intent: diagnostic evaluation

### 3.4 Modality
- Primary modality: text
- Perception burden retained: symbolic state tracking, sequential planning, and instruction use over long contexts
- Perception burden removed: raw visual perception is replaced by AtariARI-derived text descriptions

## 4. What this benchmark measures
- Primary capability target: very long-horizon sequential reasoning with text-only game state
- Secondary capability target(s): effect of prior knowledge, reflection, lexical priors, and reference trajectories
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? yes
- Does it test social reasoning / deception / cooperation? no
- Does it test visual grounding / spatial-temporal reasoning? no in the core setting
- Does it test long-horizon autonomy / task completion? yes
- Does it test real-time efficiency? partially
- Does it test cross-game transfer / open-ended generalization? yes
- Why is a game environment especially suitable here? Atari offers standardized long control sequences while still supporting controlled interventions on the agent’s available knowledge.

## 5. Interaction paradigm
- Observation channel: natural-language descriptions derived from RAM variables through AtariARI translators
- Action channel: text-selected Atari actions
- Interface type: natural language / structured action space / hybrid
- Agent scaffold allowed: other; depending on condition the prompt may include manual excerpts, PPO trajectory demonstrations, fixed CoT exemplars, optional memory buffers, and episodic reflections
- Is there privileged API access? yes; state is exposed through symbolic text rather than raw pixels
- How close is the setup to human play? low; the environment is intentionally textualized to isolate reasoning from vision
- Main ecological-validity trade-off: TextAtari gives up visual realism and uses prompt-side assistance in order to study long-horizon reasoning and prior-knowledge interventions cleanly

## 6. Evaluation protocol
- Main score: normalized per-game performance over 1000-step runs
- Auxiliary score(s): comparisons across Basic, Obscured, Manual Augmentation, and Reference-based settings, plus prompting-framework ablations
- Evaluation style: native score / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: three open-source LLMs are compared under shared scenarios and prompting frameworks, with human-level PPO demonstrations used only for the Reference-based condition
- Automatic verifiability: high
- Calibration method: common 23-game suite, fixed horizon, five random seeds, and shared sliding-window context handling
- Anti-contamination argument: not a central claim; the paper's novelty is interface control and horizon length rather than hidden or freshly curated content
- Reliability or comparability concerns: the reported experiments use 1000-step rollouts rather than the full 100K horizon because of cost, and the text interface plus prompt scaffolds make direct comparison to raw-vision Atari work unsafe

## 7. Main contributions
- Contribution 1: Builds a 23-game text Atari benchmark aimed at ultra-long sequential reasoning.
- Contribution 2: Introduces four controlled knowledge conditions that vary lexical prior, manuals, and demonstrations.
- Contribution 3: Compares zero-shot, CoT, and reflection-style agents under the same benchmark.

## 8. Main findings and failure modes
- Core empirical takeaway: current language agents remain far from competent on long-horizon Atari-style control even after manuals and demonstrations are added.
- Notable model failure mode 1: weak long-range state tracking and strategic consistency
- Notable model failure mode 2: over-reliance on lexical priors that collapse in the Obscured setting
- Notable model failure mode 3: reflection and prompting changes help only modestly relative to the benchmark difficulty
- Does this paper reveal a benchmark-design limitation as well? yes; it shows that long-horizon evaluation is expensive enough that many studies shorten horizons and may therefore understate failure severity

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Shows how game environments can scale decision horizons far beyond most static benchmarks.
- Best use in Section 1 (taxonomy and evolutionary levels): Useful in the lineage from Atari RL toward language-agent control benchmarks. Clarifies the difference between text-rendered and raw-visual game environments without over-claiming ecological realism.
- Best use in Section 2 (core capabilities evaluated by games): Supports analysis of memory, planning, and instruction grounding over long trajectories.
- Best use in Section 3 (interaction and evaluation paradigm): A good contrast case for text-translated state interfaces. Useful for condition-based prompt intervention studies.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Supports the need for benchmarks that can test both long horizons and stronger ecological validity.

## 10. Relation to nearby papers
- Closest predecessor(s): AtariARI-style symbolic verbalization work and Atari benchmarks such as AtariGPT
- Closest follow-up(s): later studies that compare symbolic or text-rendered control against more ecological visual-agent settings
- Best comparison targets inside our corpus: TextQuests, Mars, InteractiveFictionGames, NetHackLearningEnvironment
- What this paper uniquely adds relative to neighbors: It studies very long-horizon play while systematically varying lexical priors, manuals, expert demonstrations, and reasoning prompts inside a text-only Atari interface.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- TextAtari covers 23 Atari 2600 games and uses AtariARI to translate RAM-derived state into text.
- It defines four settings: Basic, Obscured, Manual Augmentation, and Reference-based, yielding nearly 100 game-condition benchmark settings.
- The main baseline experiments use 1000-step rollouts, five seeds, and compare Basic, CoT, and Reflection-style prompting agents with sliding-window context management.

### 11.2 Our synthesis / interpretation
- TextAtari is more useful for survey comparison than for ecological claims: its strength lies in controlled interventions on horizon and prior knowledge.
- It pairs especially well with TextQuests and raw-vision Atari papers.
- The paper's headline 100K framing should be read as a benchmark ambition, not as the horizon fully exercised in the reported experiments.

### 11.3 Uncertain or needs re-check
- Re-check the strongest condition/model combination if we later need exact numbers in a summary table.
- Re-check whether any specific Atari categories benefit more from manuals than from reference trajectories.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? Audit completed from the full paper; reread only if we later need exact per-game scenario outcomes or appendix comparisons to other 100K-step benchmarks.
- Which section to read next if needed: Section 2.2, Section 3.1 to 3.3, and Appendix D for prompt scaffolds
- Follow-up question(s): How much of the observed gain comes from domain knowledge versus prompt-format changes, and which games are most sensitive to lexical masking?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P1
- Reading depth: deep
- Batch ID: B05
- Outline sections: 2,3,4
- Survey role: contrast
- Paper card path: `paper_cards/B05/TextAtari.md`
- Check status: unchecked
- Next action: draft-section
- Last updated: 2026-04-10
