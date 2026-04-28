# TMGBench TMGBench: A Systematic Game Benchmark for Evaluating Strategic Reasoning Abilities of LLMs

## 0. Metadata
- Date: 2024/10
- Venue: arXiv
- Authors: Haochuan Wang, Xiachong Feng, Lei Li, Yu Guo, Zhanyue Qin, Dianbo Sui, Lingpeng Kong
- Paper link: https://arxiv.org/pdf/2410.10479v2
- Code link: https://github.com/PinkEx/TMGBench
- Reading depth: deep
- Card status: finalized
- Confidence in this card: high
- Review gate label: strong

## 1. One-paragraph benchmark summary
- TMGBench is a formal game-theoretic benchmark built around all 144 equivalence classes in the Robinson-Goforth topology of strictly ordinal 2x2 games. It pairs each classic payoff-matrix game with five GPT-4o-generated, human-reviewed story-based counterparts, then reorganizes these atomic games into sequential, parallel, and nested compositions. The benchmark's distinctive contribution is not broad ecological game coverage, but topology-level coverage, leakage-aware contextual reframing, and exact diagnosis through perfect accuracy, inconsistency degree, and bias degree against Nash-equilibrium targets. For this survey, TMGBench is best used as a narrow formal contrast on coverage design and contamination mitigation, not as a main representative of broad strategic game benchmarking.

## 2. Position in our survey
- Why-games relevance: The 2x2 topology gives benchmark designers a closed formal space in which strategic structure can be varied systematically while responses remain exactly scoreable against equilibrium-based targets.
- Historical stage: diagnostic capability probe
- Benchmark level(s): L2 strategic reasoning
- Most relevant outline section(s): 1,3,4
- Role in corpus: contrast

## 3. Design-space coding
### 3.1 Structure
- Form: Match
- Construction: Adapted
- Construction note: designed task-game hybrid based on 2x2 matrix-game topology
- Benchmark unit: atomic game / composed task

### 3.2 Mechanics profile
- State visibility: full
- Transition uncertainty: deterministic
- Actor configuration: multi-agent
- Incentive structure: mixed
- Temporal regime: hybrid

### 3.3 Benchmark scope
- Scope: curated suite
- Number of games / tasks: 144 atomic game types, plus multiple story-based variants and composed forms

### 3.4 Modality
- Observation modality: text or symbolic
- Action modality: semantic
- Perception burden retained: payoff-matrix interpretation, equilibrium reasoning, context transfer to story-framed tasks, and limited compositional reasoning across coupled atomic games
- Perception burden removed: no perceptual grounding, live multi-agent interaction, or embodied action burden

## 4. What this benchmark measures
- Primary capability target: equilibrium-oriented strategic reasoning across the full space of 2x2 ordinal games
- Secondary capability target(s): consistency under symmetric game structures, transfer between classic and story framings, theory-of-mind prompting sensitivity, and compositional difficulty in coupled game forms
- Does it test rule grounding / legal action generation? limited only; answers are chosen from explicit option sets rather than discovered in an open action space
- Does it test strategic planning under uncertainty? limited only; it probes stylized strategic interdependence, not hidden-state or rich sequential uncertainty
- Does it test social reasoning / deception / cooperation? limited only; it uses cooperation and competition framing plus ToM prompting, but no dialogue or emergent social interaction
- Does it test visual grounding / spatial-temporal reasoning? no
- Does it test long-horizon autonomy / task completion? no
- Does it test real-time efficiency? no
- Does it test cross-game transfer / open-ended generalization? limited only; it compares classic and story-based counterparts inside one formal topology rather than cross-game generalization
- Why is a game environment especially suitable here? The full topology of 2x2 games lets the benchmark cover formal strategic structures systematically while keeping exact evaluation possible.

## 5. Interaction paradigm
- Observation channel: text descriptions of payoff matrices or story scenarios with explicit choices, preferences, and payoff structures
- Action channel: textual output of equilibrium choice combinations in a fixed Python-style format; complex forms require multiple linked decisions
- Interface type: hybrid
- Agent scaffold allowed: none by default; DA, CoT, FoToM, and SoToM are evaluation conditions rather than external tools
- Is there privileged API access? no direct API, but yes in the broader sense of strong semantic privilege: the benchmark exposes payoff structures, named options, and a constrained answer format
- How close is the setup to human play? very low; the benchmark is intentionally abstract, prompt-based, and analysis-first
- Main ecological-validity trade-off: TMGBench maximizes formal coverage, leakage-aware contextualization, and exact grading, but strips away perception, negotiation, action discovery, and native play-loop pressure

## 6. Evaluation protocol
- Main score: a metric family consisting of perfect accuracy rate, inconsistency degree, and bias degree
- Auxiliary score(s): sub-metrics by equilibrium class, classic-versus-story comparisons, and results on sequential, parallel, and nested compositions
- Evaluation style: native score / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: 12 mainstream LLMs are evaluated directly against benchmark-standard answers on atomic tasks, and 4 strong reasoning models are stress-tested on complex forms; there is no human baseline or agent-vs-agent competition
- Automatic verifiability: high
- Calibration method: full-topology coverage, five story-based variants per classic game, four repeated tests per atomic data point, temperature at 0 or near 0, and separate complex-form stress tests on selected strong models
- Anti-contamination argument: moderate; Appendix H argues relatively low leakage risk from synthetic template-based data and PPL checks, but the paper explicitly says subtle contamination cannot be fully ruled out and famous-game familiarity may still help
- Reliability or comparability concerns: the benchmark is rigorous inside the 2x2 topology, but its abstraction says little about richer game agents; complex forms are still built from the same atomic formal units, and the metric family is not directly comparable to win-rate-style suites

## 7. Main contributions
- Contribution 1: Covers all 144 Robinson-Goforth 2x2 game equivalence classes instead of a small handpicked subset.
- Contribution 2: Adds five story-based variants per class with topic control and human inspection to reduce leakage and context overfitting.
- Contribution 3: Builds sequential, parallel, and nested compositions plus metric families for inconsistency, bias, and perfect accuracy.

## 8. Main findings and failure modes
- Core empirical takeaway: strong reasoning models such as o3-mini, Qwen3-32B, and deepseek-reasoner exceed 90% perfect accuracy on classic atomic tasks, but robustness drops in story-based framings, GPT-family models show asymmetric inconsistency patterns on some task types, ToM prompting helps selectively rather than uniformly, and even strong models struggle as sequential, parallel, and nested compositions grow harder.
- Notable model failure mode 1: asymmetric inconsistency or bias patterns across topologically symmetric task regions
- Notable model failure mode 2: fragile transfer from classic payoff matrices to story-based framings across narratives
- Notable model failure mode 3: performance drops on complex forms when multiple atomic games must be handled jointly
- Does this paper reveal a benchmark-design limitation as well? yes; it shows how far formal coverage and leakage-aware contextualization can go, but also how little that says about ecological or open-ended game competence

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Very limited use only; it can caution that formal game benchmarks can respond to coverage and leakage concerns without becoming ecological.
- Best use in Section 1 (taxonomy and evolutionary levels): Useful contrast showing a later formal branch that reacts to low-coverage classical-game studies by moving to topology coverage, synthetic reframing, and compositional variants while remaining inside Level 2 formal diagnostics.
- Best use in Section 2 (core capabilities evaluated by games): Limited use only; cite it narrowly for equilibrium reasoning, context-reframing robustness, or ToM prompting inside formal game settings, not for broad strategic-agent capability.
- Best use in Section 3 (interaction and evaluation paradigm): Strongest landing point: semantic privilege, exact-answer grading, symmetry-aware diagnostic metrics, synthetic story reframing, and benchmark-specific anti-leakage logic.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Contrast-only source for the point that better formal coverage and cleaner diagnostics still do not solve ecological validity or cross-benchmark comparability.

## 10. Relation to nearby papers
- Closest predecessor(s): GTBench, GAMABench, and earlier canonical game-theory LLM studies
- Closest follow-up(s): later leakage-aware or coverage-oriented formal strategic benchmarks
- Best comparison targets inside our corpus: GTBench, GAMABench, GameBench
- What this paper uniquely adds relative to neighbors: It is the clearest 2x2-topology benchmark in the corpus: full Robinson-Goforth coverage, story-based counterparts per class, and bias/inconsistency maps tied to symmetry structure.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- TMGBench includes all 144 equivalence classes from the Robinson-Goforth topology of 2x2 games (Section 2.2).
- For each classic game, the paper generates five story-based counterparts using GPT-4o, topic guidance, and iterative human review (Section 2.3; Appendix E).
- The benchmark reorganizes atomic games into sequential, parallel, and nested forms, and reports perfect accuracy rate, inconsistency degree, bias degree, and related sub-metrics (Sections 2.4-2.5).
- Atomic-task evaluation uses four tests per data point across classic and story-based settings, totaling 2,880 tests per model; complex-form evaluation runs 20 trials per configuration on four strong models (Sections 3.1-3.2).
- Appendix H argues the synthetic dataset has relatively low leakage risk, but the paper explicitly says subtle contamination cannot be fully ruled out and famous-game familiarity may still help.
- The limitations section says TMGBench covers only a very specific part of game theory and does not claim a framework suitable for all games.

### 11.2 Our synthesis / interpretation
- TMGBench is more useful as a design-side contrast on topology coverage, synthetic reframing, and leakage-aware formal evaluation than as a main source for broad strategic benchmark evolution.
- In our survey, it should sit beside GTBench and GAMABench as a narrow formal comparison case, while broader Level 2 claims should lean more on GameBench, DSGBench, or BeyondScaling.
- It is a useful Paradigm example because it shows how exact diagnostic metrics can be made very strong inside a closed formal space, while ecological validity and cross-benchmark comparability remain weak.

### 11.3 Uncertain or needs re-check
- If we later need stronger claims about data quality, re-check Appendix E for the human-review loop because it is described procedurally rather than through inter-annotator statistics.
- If we later cite the complex-form results as evidence for long-horizon or compositional reasoning, re-check Section 3.2 and Appendix G.3; the current evidence is still rooted in coupled 2x2 atomic games.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? Already completed in this audit; no further reread is needed unless we later need exact Appendix E/H details or want to quote the complex-form template.
- Which section to read next if needed: Appendix E / Appendix H / Appendix G.3
- Follow-up question(s): Should TMGBench be kept only as a formal contrast on coverage and leakage mitigation, with broader Level 2 claims anchored elsewhere?

## 13. Registry sync
- Registry row synced: yes
- Registry status: finalized
- Priority: P3
- Reading depth: deep
- Batch ID: B02
- Outline sections: 1,3,4
- Survey role: contrast
- Paper card path: `paper_cards/B02/TMGBench.md`
- Check status: unchecked
- Last updated: 2026-04-27
