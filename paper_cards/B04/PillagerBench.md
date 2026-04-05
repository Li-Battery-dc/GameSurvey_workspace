# PillagerBench PillagerBench: Benchmarking LLM-Based Agents in Competitive Minecraft Team Environments

## 0. Metadata
- Date: 2025/09
- Venue: CoG 2025
- Authors: Olivier Schipper, Yudi Zhang, Yali Du, Mykola Pechenizkiy, Meng Fang
- Paper link: https://arxiv.org/pdf/2509.06235v1
- Code link: https://github.com/aialt/PillagerBench
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: medium
- Review gate label: usable

## 1. One-paragraph benchmark summary
- PillagerBench extends Minecraft benchmarking from cooperative sandboxes to competitive team-vs-team play. It provides a modular benchmark with built-in opponents, multi-round testing, persistent learning across episodes, and two real-time scenarios, Mushroom War and Dash & Dine, that stress coordination, task allocation, opponent adaptation, and resource-constrained strategy. For this survey, the benchmark matters because it brings adversarial multi-agent evaluation into a richer open-world setting than most symbolic arenas.

## 2. Position in our survey
- Why-games relevance: Competitive Minecraft combines open-ended embodied environments with teammate coordination and adversarial adaptation in one benchmark.
- Historical stage: diagnostic capability probe
- Narrative level(s): L2 strategic reasoning / L3 social intelligence / L4 embodied interaction
- Most relevant outline section(s): 2,3,4,5,6
- Role in corpus: representative

## 3. Design-space coding
### 3.1 Environment structure
- Information structure: imperfect
- Transition structure: stochastic
- Agent structure: multi-agent
- Social structure: mixed
- Time structure: real-time

### 3.2 World structure
- World type(s): open world / crafting / embodied
- Real game / simulated game / designed task-game hybrid: real Minecraft benchmark with competitive scenario design
- Benchmark unit: timed episode

### 3.3 Benchmark scope
- Scope: scenario suite
- Number of games / tasks: 2 scenarios
- Benchmark intent: diagnostic evaluation

### 3.4 Modality
- Primary modality: symbolic event stream
- Perception burden retained: spatial reasoning, inventory management, teammate coordination, opponent adaptation, temporal pressure
- Perception burden removed: raw pixel perception and native human UI control

## 4. What this benchmark measures
- Primary capability target: competitive multi-agent adaptation in an open-ended Minecraft environment
- Secondary capability target(s): task allocation, causal reasoning, opponent modeling, self-play adaptation
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? yes
- Does it test social reasoning / deception / cooperation? yes
- Does it test visual grounding / spatial-temporal reasoning? partially
- Does it test long-horizon autonomy / task completion? yes
- Does it test real-time efficiency? yes
- Does it test cross-game transfer / open-ended generalization? no
- Why is a game environment especially suitable here? Minecraft lets the benchmark combine rich world interaction with adversarial team play instead of isolating only one of those dimensions.

## 5. Interaction paradigm
- Observation channel: scenario metadata plus Mineflayer observations and event logs during play
- Action channel: Mineflayer-compatible game actions executed through a common API
- Interface type: API / hybrid
- Agent scaffold allowed: tool use
- Is there privileged API access? yes
- How close is the setup to human play? medium; the 3D strategic structure is preserved, but agents operate through a machine-oriented interface
- Main ecological-validity trade-off: PillagerBench is more ecological than symbolic board arenas, but less human-like than raw-vision Minecraft play.

## 6. Evaluation protocol
- Main score: point differential or points earned over repeated timed episodes
- Auxiliary score(s): ablations, self-play learning curves, and scenario-specific comparisons against built-in opponents
- Evaluation style: tournament / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: built-in scripted opponents plus repeated self-play
- Automatic verifiability: high
- Calibration method: fixed 2-minute episodes, scenario-specific built-in opponents, and shared benchmark infrastructure
- Anti-contamination argument: not central
- Reliability or comparability concerns: only two scenarios are included, and the paper's strongest results are intertwined with the TactiCrafter method

## 7. Main contributions
- Contribution 1: Introduces a competitive Minecraft benchmark with built-in opponents and persistent multi-episode learning.
- Contribution 2: Provides two scenario families that target different forms of coordination and adversarial adaptation.
- Contribution 3: Analyzes a reference LLM multi-agent system, TactiCrafter, with tactics, causal modeling, and opponent modeling modules.

## 8. Main findings and failure modes
- Core empirical takeaway: TactiCrafter beats random and simpler LLM baselines, and repeated self-play changes team strategies over time
- Notable model failure mode 1: agents can overfit to their own self-play strategies and lose adaptability against different opponents
- Notable model failure mode 2: execution errors still break otherwise reasonable tactics, such as harvesting or signaling routines
- Notable model failure mode 3: the learned causal model captures inventory dependencies well but misses broader world-state and spatial-temporal dynamics
- Does this paper reveal a benchmark-design limitation as well? yes; the benchmark is promising but still narrow in scenario count and closely tied to one reference method

## 9. Why this paper matters for our survey
- Best use in Section 0 (why games): Shows how games expose adaptation, coordination, and failure modes in a controlled but rich world.
- Best use in Section 1 (historical evolution): Later-stage example of embodied competitive multi-agent benchmarking.
- Best use in Section 2 (design space): Strong case of an open-world competitive scenario suite.
- Best use in Section 3 (capability targets): Direct evidence for planning under uncertainty, cooperation, and opponent modeling.
- Best use in Section 4 (interaction paradigm): Useful comparison point between symbolic wrappers and raw ecological play.
- Best use in Section 5 (evaluation protocol): Helpful for repeated-episode testing and built-in-opponent evaluation.
- Best use in Section 6/7 (limitations and future): Supports the claim that multi-agent open-world competition remains under-benchmarked.

## 10. Relation to nearby papers
- Closest predecessor(s): Minecraft cooperative benchmarks and team-vs-team RL challenges such as SMAC
- Closest follow-up(s): broader open-world competitive benchmarks
- Best comparison targets inside our corpus: MCU, BALROG, TeamCraft, StarBench
- What this paper uniquely adds relative to neighbors: It isolates competitive, team-based adaptation in Minecraft instead of only solo or cooperative play.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- PillagerBench provides two competitive Minecraft scenarios, Mushroom War and Dash & Dine, with built-in opponents and a shared API.
- The benchmark supports pre-game, in-game, and post-game phases, and the multi-agent system persists across episodes to enable learning.
- The paper shows that TactiCrafter outperforms baseline approaches and that self-play changes strategy quality over repeated episodes.

### 11.2 Our synthesis / interpretation
- PillagerBench is more valuable for the survey's strategic and interaction sections than for broad benchmark-coverage claims because its scenario set is still small.
- It is a useful bridge between abstract strategic arenas and more ecological open-world benchmarks.

### 11.3 Uncertain or needs re-check
- Recheck Section V-B or V-C if we later need the exact benchmark scoring formula or the full built-in-opponent roster.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? No immediate reread; the benchmark structure and survey role are already clear.
- Which section to read next if needed: III-A / V-B / V-D
- Follow-up question(s): How much weight should we give scenario diversity versus ecological richness when comparing PillagerBench to broader suites?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P1
- Reading depth: deep
- Batch ID: B04
- Outline sections: 2,3,4,5,6
- Survey role: representative
- Paper card path: `paper_cards/B04/PillagerBench.md`
- Next action: draft-section
- Last updated: 2026-04-05
