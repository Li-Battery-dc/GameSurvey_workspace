# AtariGPT Atari-GPT: Benchmarking Multimodal Large Language Models as Low-Level Policies in Atari Games

## 0. Metadata
- Date: 2024/08
- Venue: arXiv
- Authors: Nicholas R. Waytowich, Devin White, MD Sunbeam, Vinicius G. Goecks
- Paper link: https://arxiv.org/pdf/2408.15950v2.pdf
- Code link: https://github.com/nwayt001/atari-gpt
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: high
- Review gate label: usable

## 1. One-paragraph benchmark summary
- Atari-GPT benchmarks multimodal LLMs as zero-shot low-level visual-action policies on seven Atari games from the Arcade Learning Environment rather than as high-level planners. Its evaluation is explicitly two-track: a gameplay track that measures cumulative reward over 1,000-timestep rollouts against human, random, and DQN references, and a companion diagnostic track that scores visual understanding, spatial reasoning, acceptable strategy, and environment identification on eight static images. For this survey, Atari-GPT is best used as an early Level 4 contrast case because it keeps pixel-conditioned action selection but also tries to explain failure rather than only report reward. The paper's strongest evidence is the gap between recognizing what is on the screen and converting that scene into spatially grounded action; latency matters, but mostly as a secondary systems constraint rather than the central survey takeaway.

## 2. Position in our survey
- Why-games relevance: Atari provides a compact way to test whether multimodal models can turn raw-screen understanding into concrete low-level actions, while the paper's paired diagnostics help decompose why those actions fail.
- Historical stage: diagnostic capability probe
- Narrative level(s): L4 visual agency
- Most relevant outline section(s): 2,3,4
- Role in corpus: contrast

## 3. Design-space coding
### 3.1 Environment structure
- Information structure: mixed
- Transition structure: mixed
- Agent structure: single-agent
- Social structure: N/A
- Time structure: real-time

### 3.2 World structure
- World type(s): arcade / other
- Real game / simulated game / designed task-game hybrid: standardized arcade game suite in ALE
- Benchmark unit: fixed-horizon rollout / static frame probe

### 3.3 Benchmark scope
- Scope: curated suite
- Number of games / tasks: 7 gameplay games plus an 8-environment companion understanding probe
- Benchmark intent: diagnostic evaluation

### 3.4 Modality
- Primary modality: image
- Perception burden retained: raw frames, object identification, relative spatial layout, and scene-to-action grounding under a short visual history
- Perception burden removed: the control loop is simplified to prompted discrete actions with resized frames, fixed frame skipping, output repair, and a short rollout horizon rather than full human controller dexterity

## 4. What this benchmark measures
- Primary capability target: low-level visual-action policy quality from raw frames
- Secondary capability target(s): visual understanding, spatial reasoning, scene-to-action translation, and environment identification
- Does it test rule grounding / legal action generation? partially
- Does it test strategic planning under uncertainty? partially
- Does it test social reasoning / deception / cooperation? no
- Does it test visual grounding / spatial-temporal reasoning? yes
- Does it test long-horizon autonomy / task completion? no
- Does it test real-time efficiency? partially
- Does it test cross-game transfer / open-ended generalization? partially
- Why is a game environment especially suitable here? Atari gives a controlled low-level action loop with native reward, while the paper's companion frame-based probes let the authors separate reward failure from visual and spatial reasoning failure.

## 5. Interaction paradigm
- Observation channel: gameplay uses the current ALE frame plus a short buffer of the two previous frames and responses; the diagnostic track uses single resized screenshots
- Action channel: gameplay requires JSON output with free-form reasoning plus a numeric Atari action; the diagnostic track uses short free-form text answers
- Interface type: structured action space / hybrid
- Agent scaffold allowed: short frame-and-response history, chain-of-thought prompting, environment-specific action documentation, and invalid-action repair
- Is there privileged API access? no
- How close is the setup to human play? low-medium; the models see raw frames, but control is mediated through prompted discrete actions, resized inputs, short history, and aggressive frame skipping
- Main ecological-validity trade-off: the benchmark preserves pixel-conditioned action selection, but the prompt-scaffolded control loop and fixed-horizon protocol make it a diagnostic visual-action benchmark rather than a close replica of native human play

## 6. Evaluation protocol
- Main score: no single unified headline score; the gameplay track reports cumulative reward over four 1,000-step rollouts, summarized in both raw form and human-normalized form
- Auxiliary score(s): per-game raw rewards, plus rubric-scored percent performance on visual understanding, spatial reasoning, acceptable strategy, and game identification
- Evaluation style: hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: gameplay compares four multimodal LLMs with human, random, and DQN references, while the companion diagnostic track scores a broader frontier-model set with a human-authored rubric
- Automatic verifiability: mixed; gameplay is automatically scored, but the understanding track relies on rubric-based human judgment and broad "acceptable strategy" criteria
- Calibration method: fixed gameplay protocol with 8-frame skipping, two-frame history, and reward carried across resets, plus a fixed prompt set and Appendix rubric averaged over four diagnostic trials
- Anti-contamination argument: not a central paper claim; the paper’s main contribution is low-level interactive evaluation rather than a formal leakage defense
- Reliability or comparability concerns: the paper mixes two evaluation tracks with different model sets and interfaces, strategy scoring is intentionally coarse, and latency, rate limits, and output-format instability affect feasibility more clearly than they support a clean benchmark claim

## 7. Main contributions
- Contribution 1: Frames Atari as a low-level multimodal control benchmark for LLMs.
- Contribution 2: Pairs gameplay reward with a companion diagnostic benchmark that separately scores visual understanding, spatial reasoning, acceptable strategy, and environment identification.
- Contribution 3: Shows that current frontier multimodal LLMs can outperform random play in several Atari settings but remain far below humans and RL agents, with spatial grounding emerging as the clearest explanation of failure.

## 8. Main findings and failure modes
- Core empirical takeaway: multimodal LLMs beat random play on average in most environments but remain far below both humans and classical RL baselines.
- Notable model failure mode 1: models often recognize visual elements but degrade sharply on relative spatial reasoning
- Notable model failure mode 2: scene understanding does not reliably convert into safe next-action selection, so errors compound over the 1,000-step rollout
- Notable model failure mode 3: policy quality is unstable across games, with especially poor results on fast-response settings such as Pong
- Does this paper reveal a benchmark-design limitation as well? yes; its paired diagnostic track is useful, but the paper also mixes automatically scored gameplay with rubric-based human diagnosis and only treats latency as a discussion-level system constraint

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Narrow contrast case showing that interactive visual control reveals failure modes that static screenshot QA does not surface.
- Best use in Section 1 (taxonomy and evolutionary levels): Early Level 4 contrast for raw-screen low-level action in ALE, but still much more diagnostic than ecological.
- Best use in Section 2 (core capabilities evaluated by games): Stronger for Section 2.4 visual grounding and scene-to-action translation than for Section 2.6 latency; use it to show that spatial grounding is a bottleneck inside visual action.
- Best use in Section 3 (interaction and evaluation paradigm): Strong evidence for evaluation decomposition, because it pairs reward-based gameplay with a separate visual / spatial / strategy / identification probe instead of treating reward as the only signal.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Supports the claim that frontier MLLMs often know what is on the screen better than they can spatially ground the next action, while also showing how low-level-controller benchmarks inherit systems-level feasibility constraints.

## 10. Relation to nearby papers
- Closest predecessor(s): Atari RL baselines in ALE and early LLM-as-game-agent work such as LLMPlayStarCraftII
- Closest follow-up(s): TextAtari, VMage, VideoGameBench
- Best comparison targets inside our corpus: TextAtari, VMage, VideoGameBench, StarBench
- What this paper uniquely adds relative to neighbors: It is an early multimodal benchmark that combines direct low-level Atari control with a separate diagnostic probe for visual understanding, spatial reasoning, acceptable strategy, and environment identification.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- The gameplay benchmark evaluates seven Atari games from ALE: Space Invaders, Breakout, Seaquest, Pong, Alien, Ms. Pacman, and Frogger.
- The gameplay rollout uses 1,000 timesteps, 8-frame skipping, a context buffer of the two previous frames and responses, and error handling that asks the model to correct invalid actions.
- The companion diagnostic benchmark uses eight environments, adds Basic Math to the seven gameplay games, and evaluates four prompt types: visual understanding, spatial reasoning, strategy, and environment identification.
- Reported average normalized performance is 23.2% for GPT-4o, 18.36% for GPT-4V Turbo, 12.36% for Claude 3 Haiku, and 8.5% for Gemini 1.5 Flash.
- The paper states that GPT-4o performs strongest across the diagnostic tasks, but that spatial reasoning accuracy declines noticeably across all tested models.

### 11.2 Our synthesis / interpretation
- Atari-GPT is not the strongest benchmark-design paper in the corpus, but it is useful as a clean contrast showing that popular RL domains are still challenging for multimodal LLMs.
- It is especially helpful when discussing how much "general" multimodal intelligence still lags specialized control systems once perception has to be converted into concrete actions.
- Its strongest survey role is in Section 2.4 and Section 3.2 as a visual-action contrast paper with decomposed evaluation, not as a primary latency benchmark or a broad ecological benchmark.

### 11.3 Uncertain or needs re-check
- Re-open Figure 5 or Figure 7 if the draft later needs exact per-task percentages rather than the paper's qualitative statement about spatial-reasoning drop-offs.
- The discussion mentions temperature tuning as a possible mitigation for output inconsistency, but there is no systematic ablation; avoid stronger claims unless we inspect supplementary material or code.
- Keep cross-track comparisons qualified because gameplay uses API-based rollouts while the diagnostic task uses web-interface prompting for a broader model set.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? Already done for this audit; rereading is only needed if the draft later needs exact Figure 5 or Figure 7 percentages.
- Which section to read next if needed: Visual And Spatial Reasoning, Figure 5, and Appendix Table 2
- Follow-up question(s): If we cite Atari-GPT in Section 2.6 at all, should it appear only as a secondary system-latency caveat rather than a primary anchor?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P2
- Reading depth: deep
- Batch ID: B04
- Outline sections: 2,3,4
- Survey role: contrast
- Paper card path: `paper_cards/B04/AtariGPT.md`
- Check status: unchecked
- Last updated: 2026-04-16
