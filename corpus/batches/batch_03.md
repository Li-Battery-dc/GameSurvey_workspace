# Batch B03: social-intelligence-and-coordination

## Why This Batch Exists
- Group deception, cooperation, negotiation, and partner-modeling benchmarks into one social-intelligence evidence block.
- Support Level 3 taxonomy plus Section 2.3 and the multi-agent contrasts in Sections 3 and 4.

## Suggested Drafting Order

| Order | paper_id | Title | Survey role | Outline anchors | Why this paper is in the batch |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | AvalonBench | AvalonBench: Evaluating LLMs Playing the Game of Avalon | representative | 1,2,3,4 | Early prompt-mediated social-deduction benchmark with naive-bot baselines; strongest as a historical contrast rather than an ecological anchor. |
| 2 | WerewolfArena | Werewolf Arena | anchor | 1,2,3,4 | Anchor for social deduction and deceptive multi-agent evaluation with partial observability. |
| 3 | Wolf | WOLF: Werewolf-based Observations for LLM Deception and Falsehoods | representative | 2,3,4 | Direct follow-on benchmark separating deception generation from deception detection in Werewolf. |
| 4 | BeyondSurvival | Beyond Survival: Evaluating LLMs in Social Deduction Games with Human-Aligned Strategies | representative | 2,3,4 | Human-grounded social deduction benchmark built from Panda Kill; strongest as an offline reference-alignment contrast rather than a live-agent benchmark. |
| 5 | CKArena | Is Your LLM Really Mastering the Concept? A Multi-Agent Benchmark | contrast | 2,3,4 | Contrast case for concept use through Undercover-style multi-agent play; strongest as a Section 2/3 contrast rather than a core social benchmark anchor. |
| 6 | MulticulturalSpyfall | Multicultural Spyfall: Assessing LLMs through Dynamic Multilingual Social Deduction Game | representative | 2,3,4 | Multilingual Spyfall benchmark for non-English and cultural-stress effects in social deduction, especially beyond English-only evaluation. |
| 7 | LLMHanabi | LLM-Hanabi: Evaluating Multi-Agent Gameplays with Theory-of-Mind and Rationale Inference in Imperfect Information Collaboration Game | representative | 1,2,3,4 | Cooperative imperfect-information benchmark for theory-of-mind and rationale inference. |
| 8 | StrategicHanabi | Sparks of Cooperative Reasoning: LLMs as Strategic Hanabi Agents | representative | 2,3,4 | Representative cooperative Hanabi benchmark for scaffold sensitivity, self-play versus cross-play, and benchmark-plus-training-resource design. |
| 9 | CollabOvercooked | Collab-Overcooked: Benchmarking and Evaluating Large Language Models as Collaborative Agents | representative | 1,2,3,4 | Forced-collaboration Overcooked benchmark with text-state interaction and PC/IC/RC-style process metrics; strong for cooperation analysis rather than ecological play. |
| 10 | HumanLevelDiplomacy | Human-level play in the game of Diplomacy by combining language models with strategic reasoning | anchor | 0,1,2,3 | Anchor milestone for negotiation-heavy play and ecological human evaluation; use for language-plus-planning and comparability trade-offs rather than as a standardized benchmark protocol. |
| 11 | LLMCoordination | LLM-Coordination: Evaluating and Analyzing Multi-agent Coordination Abilities in Large Language Models | representative | 1,2,3,4 | Pure-coordination benchmark with text-state, scaffolded agentic play plus CoordQA; strongest for the split between environment reasoning, partner modeling, and unseen-partner robustness. |
| 12 | TeamCraft | TeamCraft: A Benchmark for Multi-Modal Multi-Agent Systems in Minecraft | representative | 2,3,4 | Minecraft multimodal multi-agent benchmark with MineFlayer-backed high-level skills and Goal/Scene/Agents generalization splits; strong for visual collaboration, not cross-game transfer. |

## Expected Survey Payoff
- Keep deduction, negotiation, and cooperation comparisons in one place.
- Show how social evaluation changes when the setting moves from hidden-role games to richer collaborative worlds.

## Questions To Resolve While Drafting
- Which papers are the best anchors for deception, which for cooperation, and which only as historical bridges?
- How much social-intelligence evidence survives once we discount privileged prompting or fixed partner protocols?

## Batch Use Note
- Use this batch to draft Level 3 and the cooperation/deception/negotiation subsections in Sections 2 and 4.
