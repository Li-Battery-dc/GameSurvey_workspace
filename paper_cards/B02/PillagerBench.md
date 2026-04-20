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
- PillagerBench extends Minecraft benchmarking from cooperative setups to competitive team-vs-team play. It provides a modular benchmark with built-in opponents, repeated multi-episode testing, persistent system state across episodes, and two short real-time scenarios, Mushroom War and Dash & Dine, that stress task allocation, opponent adaptation, and resource-constrained strategy inside bounded Minecraft arenas. For this survey, its main value is not as a core formal reasoning benchmark, but as an ecological Level 2 contrast: strategic adaptation under richer world dynamics and team interaction, while still relying on privileged symbolic interfaces rather than human-like perception or control.

## 2. Position in our survey
- Why-games relevance: Competitive Minecraft lets the benchmark combine teammate coordination, adversarial pressure, spatial/resource dependencies, and real-time execution in one automatically scorable setting.
- Historical stage: ecological agent benchmark
- Benchmark level(s): L2 strategic reasoning / L3 social intelligence
- Most relevant outline section(s): 1,2,3,4
- Role in corpus: contrast

## 3. Design-space coding
### 3.1 Game structure
- Information structure: imperfect
- Transition structure: stochastic
- Agent structure: multi-agent
- Social structure: mixed
- Time structure: real-time

### 3.2 World structure
- World type(s): sandbox
- Real game / simulated game / designed task-game hybrid: designed competitive scenarios inside Minecraft rather than open-ended survival play
- Benchmark unit: timed episode

### 3.3 Benchmark scope
- Scope: single game
- Number of games / tasks: 2 competitive scenarios

### 3.4 Modality
- Observation modality: text or symbolic
- Action modality: semantic
- Perception burden retained: spatial reasoning, inventory management, teammate coordination, opponent adaptation, temporal pressure
- Perception burden removed: raw pixel perception and native human UI control

## 4. What this benchmark measures
- Primary capability target: competitive multi-agent adaptation and task allocation in structured Minecraft scenarios
- Secondary capability target(s): opponent modeling, causal recipe planning, time-sensitive coordination, and cross-episode adaptation
- Does it test rule grounding / legal action generation? partially; mainly through action-execution correctness and control-primitive use rather than formal legality checks
- Does it test strategic planning under uncertainty? yes
- Does it test social reasoning / deception / cooperation? yes; mainly cooperation and opponent-aware adaptation rather than deception or negotiation
- Does it test visual grounding / spatial-temporal reasoning? partially
- Does it test long-horizon autonomy / task completion? no; episodes are short, and persistence across episodes serves adaptation rather than long-horizon completion
- Does it test real-time efficiency? yes
- Does it test cross-game transfer / open-ended generalization? no
- Why is a game environment especially suitable here? Minecraft combines team coordination, adversarial interference, spatial/resource dependencies, and real-time execution inside scenarios that remain automatically scorable.

## 5. Interaction paradigm
- Observation channel: scenario metadata plus chat and observe events with nearby blocks, mobs, inventories, self-status, and environment feedback during play
- Action channel: executable JavaScript action code using control primitives and Mineflayer API calls
- Interface type: hybrid
- Agent scaffold allowed: persistent cross-episode state / memory / planner / tool use
- Is there privileged API access? yes
- How close is the setup to human play? low to medium; agents operate in real-time Minecraft scenarios, but they act through privileged structured APIs and code generation rather than raw perception and native control
- Main ecological-validity trade-off: PillagerBench keeps real-time multi-agent competition and Minecraft resource dynamics, but heavily abstracts perception and control into Mineflayer events and JavaScript actions.

## 6. Evaluation protocol
- Main score: points, sabotage, point difference, and win rate over repeated timed episodes
- Auxiliary score(s): scenario-specific opponent heatmaps, consecutive-episode adaptation curves, and module/backbone ablations
- Evaluation style: tournament / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: built-in scripted opponents plus repeated multi-episode evaluation of TactiCrafter and baseline systems
- Automatic verifiability: high
- Calibration method: fixed 2-minute episodes, scenario-specific built-in opponents, five consecutive episodes per matchup, and repeated benchmark runs
- Anti-contamination argument: not central
- Reliability or comparability concerns: only two scenarios are included, Dash & Dine has documented arena asymmetries, built-in opponents are scenario-specific, and the paper’s evidence is still tightly coupled to TactiCrafter versus only random and simple CoT baselines

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
- Best use in Section 1 (taxonomy and evolutionary levels): Ecological Level 2 contrast for competitive multi-agent benchmarking once the survey moves beyond formal small-game suites, while still making the interface-privilege caveat explicit.
- Best use in Section 2 (core capabilities evaluated by games): Direct evidence for time-sensitive task allocation, opponent-aware adaptation, and causal dependency management in competitive multi-agent settings.
- Best use in Section 3 (interaction and evaluation paradigm): Strong comparison point for persistent multi-agent systems, Mineflayer-mediated symbolic interfaces, built-in opponent ladders, and latency-sensitive repeated evaluation.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Supports the claim that ecological strategic benchmarks remain narrow in scenario coverage, partially asymmetric, and method-coupled.

## 10. Relation to nearby papers
- Closest predecessor(s): VillagerBench-style cooperative Minecraft systems, Voyager-style Mineflayer agents, and team-vs-team RL benchmarks such as SMAC and Lux AI
- Closest follow-up(s): later multimodal or competitive Minecraft benchmarks that broaden scenario coverage or reduce method coupling
- Best comparison targets inside our corpus: DSGBench, BeyondScaling, TeamCraft, CivRealm
- What this paper uniquely adds relative to neighbors: It isolates short-horizon competitive Minecraft play with built-in opponent suites and persistent cross-episode adaptation in a structured symbolic interface.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- PillagerBench provides two competitive Minecraft scenarios, Mushroom War and Dash & Dine, with built-in opponents, a common API, and two-minute timed episodes.
- The benchmark exposes pre-game, game, and post-game phases; the multi-agent system object persists across episodes to enable continuous learning.
- The observation stream includes scenario metadata plus chat and observe events, while actions are executable JavaScript using Mineflayer API calls and control primitives.
- A typical benchmark run has the evaluated system play each built-in opponent of each scenario for five consecutive episodes, repeated three times.
- Table IV shows that TactiCrafter outperforms the random and CoT baselines, but still reaches only 0.46 overall win rate and -1.16 average point difference against the built-in opponents.

### 11.2 Our synthesis / interpretation
- PillagerBench is more valuable for the survey's strategic and interaction sections than for broad benchmark-coverage claims because its scenario set is still small.
- The safest placement is to keep it in B02 as an ecological Level 2 contrast, not to treat it as a core reasoning anchor and not to move it toward long-horizon or visual-agent batches.
- It is a useful bridge between abstract strategic arenas and richer multi-agent Minecraft benchmarks, but it should not be cited as evidence of human-like visual play or open-ended autonomy.

### 11.3 Uncertain or needs re-check
- Recheck Equation 9 to Equation 11 if we later need to compare sabotage or point-difference metrics across papers.
- Recheck Section V-B or V-D if later drafting needs the exact Dash & Dine asymmetry caveat or the full opponent-adaptation analysis.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? No immediate reread; the benchmark structure and survey role are already clear.
- Which section to read next if needed: III-A / V-B / V-D
- Follow-up question(s): If we compare PillagerBench to DSGBench or TeamCraft in the draft, which contrast matters more: opponent adaptation, interface privilege, or scenario breadth?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P2
- Reading depth: deep
- Batch ID: B02
- Outline sections: 1,2,3,4
- Survey role: contrast
- Paper card path: `paper_cards/B02/PillagerBench.md`
- Next action: draft-section
- Check status: unchecked
- Last updated: 2026-04-19
