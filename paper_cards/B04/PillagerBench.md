# PillagerBench PillagerBench: Benchmarking LLM-Based Agents in Competitive Minecraft Team Environments

## 0. Metadata
- Date: 2025/09
- Venue: CoG 2025
- Authors: Olivier Schipper, Yudi Zhang, Yali Du, Mykola Pechenizkiy, Meng Fang
- Paper link: https://arxiv.org/pdf/2509.06235v1
- Code link: https://github.com/aialt/PillagerBench
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: high
- Review gate label: usable

## 1. One-paragraph benchmark summary
- PillagerBench extends Minecraft benchmarking from cooperative sandboxes to competitive team-vs-team play. It provides a modular benchmark with built-in opponents, multi-round testing, persistent learning across episodes, and two real-time scenarios, Mushroom War and Dash & Dine, that stress coordination, task allocation, opponent adaptation, and resource-constrained strategy. For this survey, the benchmark matters because it brings adversarial multi-agent evaluation into a richer open-world setting than most symbolic arenas.

## 2. Position in our survey
- Why-games relevance: Competitive Minecraft combines open-ended embodied environments with teammate coordination and adversarial adaptation in one benchmark.
- Historical stage: ecological agent benchmark
- Narrative level(s): L2 strategic reasoning / L3 social intelligence
- Most relevant outline section(s): 1,2,3,4
- Role in corpus: representative

## 3. Design-space coding
### 3.1 Environment structure
- Information structure: imperfect
- Transition structure: stochastic
- Agent structure: multi-agent
- Social structure: mixed
- Time structure: real-time

### 3.2 World structure
- World type(s): sandbox / open-world
- Real game / simulated game / designed task-game hybrid: designed competitive scenarios inside real Minecraft
- Benchmark unit: timed episode

### 3.3 Benchmark scope
- Scope: curated suite
- Number of games / tasks: 2 scenarios
- Benchmark intent: ecological evaluation

### 3.4 Modality
- Primary modality: symbolic state
- Perception burden retained: spatial reasoning, inventory management, teammate coordination, opponent adaptation, temporal pressure
- Perception burden removed: raw pixel perception and native human UI control

## 4. What this benchmark measures
- Primary capability target: competitive multi-agent adaptation in an open-ended Minecraft environment
- Secondary capability target(s): task allocation under time pressure, causal planning, opponent modeling, and cross-episode adaptation
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? yes
- Does it test social reasoning / deception / cooperation? yes
- Does it test visual grounding / spatial-temporal reasoning? partially
- Does it test long-horizon autonomy / task completion? partially
- Does it test real-time efficiency? yes
- Does it test cross-game transfer / open-ended generalization? no
- Why is a game environment especially suitable here? Minecraft lets the benchmark combine rich world interaction with adversarial team play instead of isolating only one of those dimensions.

## 5. Interaction paradigm
- Observation channel: scenario metadata plus chat and observe events with nearby blocks, mobs, inventories, self-status, and environment feedback during play
- Action channel: executable JavaScript action code using control primitives and Mineflayer API calls
- Interface type: hybrid
- Agent scaffold allowed: memory / planner / tool use
- Is there privileged API access? yes
- How close is the setup to human play? low to medium; agents inhabit real Minecraft scenarios, but they act through privileged structured APIs rather than raw perception and manual control
- Main ecological-validity trade-off: PillagerBench keeps real-time open-world interaction and team competition, but removes raw visual perception in favor of Mineflayer-mediated structured observations and code actions.

## 6. Evaluation protocol
- Main score: points, sabotage, point difference, and win rate over repeated timed episodes
- Auxiliary score(s): scenario-specific opponent heatmaps, consecutive-episode adaptation curves, and module/backbone ablations
- Evaluation style: tournament / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: built-in scripted opponents plus repeated multi-episode evaluation of TactiCrafter and baseline systems
- Automatic verifiability: high
- Calibration method: fixed 2-minute episodes, scenario-specific built-in opponents, five consecutive episodes per matchup, and repeated benchmark runs
- Anti-contamination argument: not central
- Reliability or comparability concerns: only two scenarios are included, the Dash & Dine arena has documented asymmetries, and the paper’s strongest results are tightly coupled to the TactiCrafter implementation

## 7. Main contributions
- Contribution 1: Introduces a competitive Minecraft benchmark with built-in opponents and persistent multi-episode learning.
- Contribution 2: Provides two scenario families that target different forms of coordination and adversarial adaptation.
- Contribution 3: Analyzes a reference LLM multi-agent system, TactiCrafter, with tactics, causal modeling, and opponent modeling modules.

## 8. Main findings and failure modes
- Core empirical takeaway: TactiCrafter beats the random and CoT baselines, especially in the more complex Dash & Dine scenario, but it still finishes below parity against the benchmark’s built-in opponents overall.
- Notable model failure mode 1: simple CoT control remains competitive in Mushroom War but falls off in Dash & Dine, showing how current systems struggle more as causal and opponent-dependent planning complexity rises
- Notable model failure mode 2: even the strongest evaluated system still has a sub-50% overall win rate against the built-in opponents, leaving substantial room for improvement
- Notable model failure mode 3: module and backbone ablations reveal unstable trade-offs between scoring, sabotage, and adaptation rather than one uniformly strong competitive policy
- Does this paper reveal a benchmark-design limitation as well? yes; the benchmark is promising but still narrow in scenario count and closely tied to one reference method

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Shows how games expose adaptation, coordination, and failure modes in a controlled but still rich interactive world.
- Best use in Section 1 (taxonomy and evolutionary levels): Useful ecological Minecraft contrast for competitive multi-agent benchmarking, while still making the interface-privilege caveat explicit.
- Best use in Section 2 (core capabilities evaluated by games): Direct evidence for time-sensitive task allocation, cooperation, opponent modeling, and causal planning in a dynamic sandbox.
- Best use in Section 3 (interaction and evaluation paradigm): Strong comparison point for persistent multi-agent systems, Mineflayer-mediated structured interfaces, built-in opponent suites, and multi-metric evaluation.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Supports the claim that competitive embodied multi-agent benchmarking is still thin, narrow in scenario coverage, and method-coupled.

## 10. Relation to nearby papers
- Closest predecessor(s): Minecraft cooperative benchmarks and team-vs-team RL benchmarks such as SMAC
- Closest follow-up(s): future embodied competitive open-world benchmarks with broader scenario coverage and less method coupling
- Best comparison targets inside our corpus: `TeamCraft`, `MCU`, `CollabOvercooked`
- What this paper uniquely adds relative to neighbors: It isolates competitive, team-based Minecraft adaptation with built-in opponent suites and persistent cross-episode learning.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- PillagerBench provides two competitive Minecraft scenarios, Mushroom War and Dash & Dine, with built-in opponents, a common API, and two-minute timed episodes.
- The benchmark supports pre-game, game, and post-game phases, and the multi-agent system object persists across episodes to enable continuous learning.
- The paper shows that TactiCrafter outperforms the random and CoT baselines, but still posts only a 0.46 overall win rate against the built-in opponents.

### 11.2 Our synthesis / interpretation
- PillagerBench is more valuable for the survey's strategic and interaction sections than for broad benchmark-coverage claims because its scenario set is still small.
- It is a useful bridge between abstract strategic arenas and more ecological open-world benchmarks.

### 11.3 Uncertain or needs re-check
- Recheck Section V-B or V-D if we later need the exact opponent-adaptation analysis, scenario asymmetry caveats, or the full built-in-opponent roster.

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
- Outline sections: 1,2,3,4
- Survey role: representative
- Paper card path: `paper_cards/B04/PillagerBench.md`
- Next action: draft-section
- Check status: unchecked
- Last updated: 2026-04-09
