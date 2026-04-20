# GVGAILLM GVGAI-LLM: Evaluating Large Language Model Agents with Infinite Games

## 0. Metadata
- Date: 2025/08
- Venue: arXiv
- Authors: Yuchen Li, Cong Lin, Muhammad Umair Nasir, Philip Bontrager, Jialin Liu, Julian Togelius
- Paper link: https://arxiv.org/pdf/2508.08501v2
- Code link:
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: medium
- Review gate label: strong

## 1. One-paragraph benchmark summary
- GVGAI-LLM adapts the General Video Game AI framework into a benchmark for language-only agents operating over symbolic game states. It translates VGDL rules and ASCII game scenes into textual prompts, evaluates models on more than 100 2D arcade-style games, and reports interpretable metrics such as meaningful step ratio, step efficiency, win rate, reward, and an overall score. For this survey, it is a strong representative of symbolic general-video-game benchmarking with explicit anti-saturation properties.

## 2. Position in our survey
- Why-games relevance: Procedurally extensible game families let us probe reasoning, planning, and symbolic grounding beyond fixed benchmark sets.
- Historical stage: diagnostic capability probe
- Narrative level(s): L1 rule following / L2 strategic reasoning / L5 cross-game generalization
- Most relevant outline section(s): 1,2,3,4
- Role in corpus: representative

## 3. Design-space coding
### 3.1 Environment structure
- Information structure: mixed
- Transition structure: mixed
- Agent structure: single-agent
- Social structure: none
- Time structure: step-based

### 3.2 World structure
- World type(s): other (2D arcade-style GVGAI games)
- Real game / simulated game / designed task-game hybrid: simulated game family built on GVGAI
- Benchmark unit: full level

### 3.3 Benchmark scope
- Scope: game family
- Number of games / tasks: 118 games with up to 5 levels each

### 3.4 Modality
- Primary modality: symbolic state
- Perception burden retained: rule interpretation, spatial reasoning, reactive planning, action selection under evolving state
- Perception burden removed: raw pixel perception

## 4. What this benchmark measures
- Primary capability target: symbolic spatial reasoning and reactive problem solving across many game rulesets
- Secondary capability target(s): per-step rule grounding, prompt robustness, cross-game generalization
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? partially
- Does it test social reasoning / deception / cooperation? no
- Does it test visual grounding / spatial-temporal reasoning? partially, in symbolic form
- Does it test long-horizon autonomy / task completion? yes
- Does it test real-time efficiency? no
- Does it test cross-game transfer / open-ended generalization? yes
- Why is a game environment especially suitable here? GVGAI supplies a large, extensible set of rule-based environments where performance remains far from saturated and easy to verify.

## 5. Interaction paradigm
- Observation channel: ASCII maps, translated game rules, action mappings, and avatar position at the current step only
- Action channel: natural-language choice of a discrete action
- Interface type: natural language / structured action space
- Agent scaffold allowed: none
- Is there privileged API access? yes
- How close is the setup to human play? low; the benchmark strips away raw perception and exposes exact symbolic state
- Main ecological-validity trade-off: GVGAI-LLM cleanly isolates symbolic reasoning, but it removes perception, memory, and forward interaction pressures that shape real game play.

## 6. Evaluation protocol
- Main score: overall score averaging normalized meaningful step ratio, inverse steps, reward, and win rate
- Auxiliary score(s): meaningful step ratio, step efficiency, win rate, and normalized reward
- Evaluation style: hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: LLMs compared with classical planning and RL baselines; no human baseline is used
- Automatic verifiability: high
- Calibration method: per-game normalization and a shared benchmark pipeline across many games
- Anti-contamination argument: yes; VGDL-based game generation and level extensibility are presented as protection against saturation
- Reliability or comparability concerns: the default zero-shot, no-memory design intentionally narrows what "playing a game" means

## 7. Main contributions
- Contribution 1: Reworks GVGAI into a text-facing benchmark for language-only agents across 100+ games.
- Contribution 2: Defines interpretable behavior metrics such as meaningful step ratio and step efficiency.
- Contribution 3: Analyzes failure modes including spatial grounding errors and symbolic identity confusion.

## 8. Main findings and failure modes
- Core empirical takeaway: current LLMs remain far from solving GVGAI-style symbolic games, with GPT-4o-mini winning only 10.27% of evaluated levels and failing on 477 of 540 levels
- Notable model failure mode 1: models make persistent spatial grounding and logical consistency errors
- Notable model failure mode 2: coordinate tagging and verbose grounding help somewhat but do not resolve deeper planning and identity-tracking failures
- Notable model failure mode 3: LLM agents are orders of magnitude slower per move than symbolic search methods
- Does this paper reveal a benchmark-design limitation as well? yes; the zero-shot symbolic interface is useful diagnostically but not ecologically realistic

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Shows why procedurally extensible game families resist saturation better than fixed task sets.
- Best use in Section 1 (taxonomy and evolutionary levels): Strong example of the GVGAI lineage entering LLM benchmarking. Important symbolic-game family comparison point.
- Best use in Section 2 (core capabilities evaluated by games): Direct evidence for spatial reasoning and rule-grounding limits.
- Best use in Section 3 (interaction and evaluation paradigm): Useful as a privileged symbolic-state foil to visual and GUI benchmarks. Strong metric-design example.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Supports the claim that symbolic access can clarify failure modes but weakens ecological claims.

## 10. Relation to nearby papers
- Closest predecessor(s): original GVGAI, SmartPlay, symbolic planning benchmarks
- Closest follow-up(s): broader general video-game and multimodal suites
- Best comparison targets inside our corpus: Orak, AIGameStore, GameVerse, LMGameBench
- What this paper uniquely adds relative to neighbors: It combines broad game coverage with a deliberately symbolic, language-only interface and explicit process metrics.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- GVGAI-LLM is built on the original GVGAI framework and exposes game rules plus ASCII scene descriptions to LLMs.
- The benchmark evaluates 118 games with up to five levels each and reports meaningful step ratio, step efficiency, win rate, reward, and an aggregated overall score.
- The paper finds persistent spatial and logical errors, limited gains from coordinate tagging, and large latency gaps relative to MCTS.

### 11.2 Our synthesis / interpretation
- This is one of the clearest cards for discussing anti-saturation through procedural breadth without requiring raw visual perception.
- It is especially valuable when contrasting symbolic access against ecological realism.

### 11.3 Uncertain or needs re-check
- The benchmark intentionally removes memory and trajectory history, so it should not be used as direct evidence about long-horizon agent coherence without that caveat.
- Recheck the experiments section if we later need exact per-model rankings across the six highlighted evaluation games.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? No immediate reread; the benchmark design and metrics are already clear enough.
- Which section to read next if needed: Benchmark Design / Evaluation Metrics / Discussion
- Follow-up question(s): Which metric should anchor our discussion of meaningful interaction versus raw task success?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P1
- Reading depth: deep
- Batch ID: B06
- Outline sections: 1,2,3,4
- Survey role: representative
- Paper card path: `paper_cards/B06/GVGAILLM.md`
- Check status: unchecked
- Next action: draft-section
- Last updated: 2026-04-10
