# Orak Orak: A Foundational Benchmark for Training and Evaluating LLM Agents on Diverse Video Games

## 0. Metadata
- Date: 2025/06
- Venue: ICLR 2026
- Authors: Dongmin Park, Minkyu Kim, Beongjun Choi, Junhyuck Kim, Keon Lee, Jonghyun Lee, Inkyu Park, Byeong-Uk Lee, Jaeyoung Hwang, Jaewoo Ahn, Ameya S. Mahabaleshwarkar, Bilal Kartal, Pritam Biswas, Yoshi Suhara, Kangwook Lee, Jaewoong Cho
- Paper link: https://arxiv.org/pdf/2506.03610v2
- Code link: https://github.com/krafton-ai/Orak
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: high
- Review gate label: strong

## 1. One-paragraph benchmark summary
- Orak is a cross-genre benchmark and training platform for LLM game agents operating across 12 real video games. It uses Model Context Protocol as a plug-and-play layer between backbone models, game environments, and agentic modules such as reflection, planning, memory, or skill management, and it also releases expert gameplay trajectories for supervised fine-tuning. For this survey, Orak is one of the strongest anchor papers for the modern "benchmark plus agentic scaffold plus alignment dataset" pattern.

## 2. Position in our survey
- Why-games relevance: Diverse real video games make it possible to evaluate whether an LLM agent can remain useful across very different cognitive demands instead of only one narrow ruleset.
- Historical stage: ecological agent benchmark
- Narrative level(s): L4 visual agency / L5 cross-game generalization
- Most relevant outline section(s): 1,2,3,4
- Role in corpus: anchor

## 3. Design-space coding
### 3.1 Environment structure
- Information structure: mixed
- Transition structure: mixed
- Agent structure: mixed
- Social structure: mixed
- Time structure: mixed

### 3.2 World structure
- World type(s): mixed video games
- Real game / simulated game / designed task-game hybrid: real video games benchmarked through a common interface
- Benchmark unit: game episode

### 3.3 Benchmark scope
- Scope: genre-diverse suite
- Number of games / tasks: 12 games
- Benchmark intent: train+eval foundation

### 3.4 Modality
- Primary modality: mixed
- Perception burden retained: rule following, memory, planning, error handling, and some visual grounding when image input is enabled
- Perception burden removed: Orak preprocesses game states into structured text and hides information deemed irrelevant to gameplay

## 4. What this benchmark measures
- Primary capability target: versatile game-agent competence across major video-game genres
- Secondary capability target(s): value of agentic modules, effect of visual input, transfer from gameplay fine-tuning
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? yes
- Does it test social reasoning / deception / cooperation? no; some games involve adversarial or multi-step interaction, but the suite is not a social-language benchmark
- Does it test visual grounding / spatial-temporal reasoning? yes
- Does it test long-horizon autonomy / task completion? yes
- Does it test real-time efficiency? partially
- Does it test cross-game transfer / open-ended generalization? yes
- Why is a game environment especially suitable here? Cross-genre video games demand different mixes of perception, reasoning, memory, and planning while keeping outcomes concretely measurable.

## 5. Interaction paradigm
- Observation channel: MCP-mediated structured game states, with optional visual inputs in separate experiments
- Action channel: discrete game actions emitted through MCP wrappers, optionally mediated by reflection, planning, or skill modules
- Interface type: API / structured action space / hybrid
- Agent scaffold allowed: memory / reflection / planner
- Is there privileged API access? yes
- How close is the setup to human play? low-to-medium; the games are real, but Orak intentionally preprocesses states into structured text favorable to LLM reasoning
- Main ecological-validity trade-off: Orak offers broad real-game coverage, but MCP-mediated state abstraction and scaffolded interaction reduce raw human-like play.

## 6. Evaluation protocol
- Main score: per-game benchmark score and leaderboard performance
- Auxiliary score(s): LLM battle arenas, ablations over agentic modules, visual-input studies, and fine-tuning transfer analyses
- Evaluation style: hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: LLM leaderboards plus battle arenas across games
- Automatic verifiability: mixed
- Calibration method: shared MCP interface, standardized evaluation pipeline, and controlled module ablations
- Anti-contamination argument: not central
- Reliability or comparability concerns: results depend materially on scaffold choice, input modality, and the benchmark's favorable state preprocessing for LLM reasoning

## 7. Main contributions
- Contribution 1: Builds a 12-game, all-major-genre benchmark for LLM and VLM game agents.
- Contribution 2: Uses MCP as a plug-and-play interface between games and agentic modules.
- Contribution 3: Releases a cross-genre gameplay trajectory dataset for fine-tuning smaller models into more effective game agents.

## 8. Main findings and failure modes
- Core empirical takeaway: proprietary models outperform open-source models broadly, but scaffolding and fine-tuning meaningfully reshape the gap
- Notable model failure mode 1: open-source models gain much less from extended agentic workflows than proprietary models
- Notable model failure mode 2: visual inputs often hurt performance rather than help
- Notable model failure mode 3: fine-tuning mainly improves valid action generation and some intra-game transfer, but does not remove weak spatial reasoning or OOD-game failures
- Does this paper reveal a benchmark-design limitation as well? yes; a common interface is valuable, but heavy scaffolding makes it harder to separate raw backbone ability from workflow engineering

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Shows how genre diversity creates a broader capability test than single-game benchmarks.
- Best use in Section 1 (taxonomy and evolutionary levels): Strong example of the benchmark-plus-platform turn in recent work. Important cross-genre anchor.
- Best use in Section 2 (core capabilities evaluated by games): Covers rule following, planning, memory, spatial reasoning, and error handling in one suite.
- Best use in Section 3 (interaction and evaluation paradigm): One of the best cases for MCP-like scaffolded game interaction. Useful for discussing module ablations and benchmark leaderboards.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Supports the claim that future benchmark work should discuss scaffolding explicitly, not just backbone models.

## 10. Relation to nearby papers
- Closest predecessor(s): BALROG, Cradle, V-MAGE, LMGame-Bench, earlier multi-game suites
- Closest follow-up(s): broader benchmark-plus-training ecosystems
- Best comparison targets inside our corpus: AI GameStore, BALROG, MCU, GVGAI-LLM
- What this paper uniquely adds relative to neighbors: It joins real-game breadth, scaffold ablations, and fine-tuning transfer inside one benchmark package.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- Orak covers 12 real video games spanning six major genres and connects game environments plus agentic modules through MCP.
- The benchmark studies gameplay leaderboards, LLM battle arenas, the effect of visual input, and the effect of fine-tuning on smaller models.
- The paper reports that proprietary models lead overall, visual input often hurts gameplay, and fine-tuning yields mixed but real gains in valid action generation and transfer.

### 11.2 Our synthesis / interpretation
- Orak is one of the most useful survey anchors for the "generic gaming agent" framing.
- It is especially valuable because it makes scaffolding an explicit experimental variable instead of hiding it inside the implementation.

### 11.3 Uncertain or needs re-check
- The suite intentionally hides information deemed unnecessary for gameplay, so ecological claims should always be paired with the state-preprocessing caveat.
- Recheck Sections 5.4 to 5.6 if we later need the exact per-module gains or the strongest fine-tuning transfer examples.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? A targeted reread is likely worthwhile later because Orak will probably anchor multiple outline sections.
- Which section to read next if needed: 3.1 / 5.4 / 5.6
- Follow-up question(s): Should Orak or AI GameStore anchor the survey's "future of benchmark platforms" subsection?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P0
- Reading depth: deep
- Batch ID: B05
- Outline sections: 1,2,3,4
- Survey role: anchor
- Paper card path: `paper_cards/B05/Orak.md`
- Check status: unchecked
- Next action: draft-section
- Last updated: 2026-04-09
