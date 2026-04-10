# Batch B02: strategic-uncertainty-and-adaptation

## Why This Batch Exists
- Gather the main Level 2 papers on planning under uncertainty, adversarial adaptation, and mixed social-competitive structure.
- Support Section 2.2 and time-sensitive decision-making without scattering strategic evidence across specialist or social batches.

## Suggested Drafting Order

| Order | paper_id | Title | Survey role | Outline anchors | Why this paper is in the batch |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | BeyondScaling | Beyond Scaling: Assessing Strategic Reasoning and Rapid Decision-Making Capability of LLMs in Zero-sum Environments | contrast | 1,2,3,4 | Useful contrast on zero-sum strategy, protocol-mediated play, and real-time pressure in a narrow arena design. |
| 2 | GameBench | GameBench: Evaluating Strategic Reasoning Abilities of LLM Agents | representative | 1,2,3,4 | Cross-domain strategy benchmark spanning multiple games and prompting setups. |
| 3 | GAMABench | How Far Are We on the Decision-Making of LLMs? Evaluating LLMs' Gaming Ability in Multi-Agent Environments | representative | 1,2,3,4 | Multi-agent decision benchmark grounded in game-theoretic settings and prompting variants. |
| 4 | TMGBench | TMGBench: A Systematic Game Benchmark for Evaluating Strategic Reasoning Abilities of LLMs | contrast | 1,2,3,4 | Broad strategic benchmark useful for taxonomy coverage though overlap with earlier suites is high. |
| 5 | OpenGuanDan | OpenGuanDan: A Large-Scale Imperfect Information Game Benchmark | representative | 1,2,3,4 | Specialized imperfect-information card benchmark with built-in GuanDan agents, pairwise AI-vs-AI evaluation, and limited human-AI calibration. |
| 6 | DSGBench | DSGBench: A Diverse Strategic Game Benchmark for Evaluating LLM-based Agents in Complex Decision-Making Environments | representative | 1,2,3,4 | Genre-diverse strategic suite with unified text interfaces, fine-grained capability metrics, and trajectory logging; broad diagnostic platform rather than a full generalization benchmark. |
| 7 | PillagerBench | PillagerBench: Benchmarking LLM-Based Agents in Competitive Minecraft Team Environments | representative | 1,2,3,4 | Competitive Minecraft benchmark with built-in opponents and persistent cross-episode learning; ecological contrast despite structured API access. |
| 8 | CivRealm | CivRealm: A Learning and Reasoning Odyssey in Civilization for Decision-Making Agents | representative | 1,2,4 | Civilization environment bridging strategic planning long horizons and generalization across settings. |

## Expected Survey Payoff
- Tighten the Level 2 narrative from formal probes to richer strategic environments.
- Provide a shared comparison set for uncertainty, real-time pressure, and agent-vs-agent evaluation.

## Questions To Resolve While Drafting
- Where is the clearest line between strategic depth, benchmark coverage, and evaluation engineering?
- Which papers best expose uncertainty and time pressure rather than just prompt tuning or environment coupling?

## Batch Use Note
- Use this batch to draft Level 2, Section 2.2, and the strategy-versus-execution discussion in the synthesis.
