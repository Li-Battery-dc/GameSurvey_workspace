# Batch B04: visual-agency-and-ecological-control

## Why This Batch Exists
- Collect the core Level 4 evidence on pixels, GUI control, video-conditioned play, and ecological interaction loops.
- Support the visual-agency taxonomy plus the interaction-design discussion in Section 3.

## Suggested Drafting Order

| Order | paper_id | Title | Survey role | Outline anchors | Why this paper is in the batch |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | Balrog | BALROG | anchor | 0,1,2,3,4 | Core visual-agent benchmark bridging ecological play and interface design. |
| 2 | GameplayQA | GameplayQA: A Benchmarking Framework for Decision-Dense POV-Synced Multi-Video Understanding of 3D Virtual Agents | representative | 2,3,4 | Dense first-person multi-video perception benchmark for agentic state tracking and temporal grounding. |
| 3 | StarBench | StarBench: A Turn-Based RPG Benchmark for Agentic Multimodal Decision-Making and Information Seeking | anchor | 0,1,2,3,4 | Anchor for matched raw GUI vs semantic-action control, ask-or-act policy, and family-native combat metrics. |
| 4 | FlashAdventure | FlashAdventure: A Benchmark for GUI Agents Solving Full Story Arcs in Diverse Adventure Games | representative | 2,3,4 | Long-horizon GUI benchmark centered on full story completion and memory-dependent play. |
| 5 | VideoGameBench | VideoGameBench: Can VLM Complete Popular Video Games? | representative | 2,3,4 | Supporting raw-visual comparison case for low VLM scores, checkpoint scoring, and the paused Lite trade-off. |
| 6 | VMage | V-MAGE: A Game Evaluation Framework for Assessing Vision-Centric Capabilities in Multimodal Large Language Models | representative | 1,2,3,4 | Vision-centric diagnostic suite with mixed screenshot+prompt input, level-engineered visual probes, and separate Elo versus human-score evaluation. |
| 7 | LVLMGamePlayers | Are Large Vision-Language Models Good Game Players? | contrast | 2,3,4 | Board-centric visual diagnostic contrast paper useful for ability decomposition, task-target alignment, and component-vs-E2E evaluation gaps. |
| 8 | INGVP | ING-VP: MLLMs cannot Play Easy Vision-based Games Yet | contrast | 2,3,4 | Vision-game benchmark highlighting spatial planning limits under light scaffolding. |
| 9 | AtariGPT | Atari-GPT: Benchmarking Multimodal Large Language Models as Low-Level Policies in Atari Games | contrast | 2,3,4 | Atari low-level visual-action contrast paper pairing reward-based play with visual/spatial/strategy/identification diagnostics; latency is secondary. |
| 10 | TowerMind | TowerMind: A Tower Defence Game Learning Environment and Benchmark for LLM as Agents | representative | 2,3,4 | Tower-defense environment adds real-time multimodal control and hallucination-oriented diagnostics. |
| 11 | PokeGym | PokeGym: A Visually-Driven Long-Horizon Benchmark for Vision-Language Models | representative | 2,3,4 | Pure-pixel 3D RPG benchmark with automated AOB-based evaluation and deadlock-centered embodied diagnosis. |
| 12 | VARP | Can VLMs Play Action Role-Playing Games? Take Black Myth Wukong as a Study Case | contrast | 0,2,3,4 | Early visual ARPG case study useful for API-versus-screen interaction, non-API action composition, and coarse task-success evaluation contrasts. |

## Expected Survey Payoff
- Clarify the difference between perception-only diagnostics, GUI play, and end-to-end ecological control.
- Provide the main evidence block for interface privilege versus human-like interaction.

## Questions To Resolve While Drafting
- Which papers truly preserve the human play loop, and which remain controlled visual diagnostics?
- How should the survey compare raw-visual control, GUI interaction, and video understanding without flattening them?

## Batch Use Note
- Use this batch to draft Level 4 and the observation-channel/action-channel ladder in Section 3.1.
