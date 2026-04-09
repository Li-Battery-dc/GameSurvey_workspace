# MulticulturalSpyfall Multicultural Spyfall: Assessing LLMs through Dynamic Multilingual Social Deduction Game

## 0. Metadata
- Date: 2026/01
- Venue: arXiv
- Authors: Haryo Akbarianto Wibowo, Alaa Elsetohy, Qinrong Cui, Alham Fikri Aji
- Paper link: https://arxiv.org/pdf/2601.09017.pdf
- Code link:
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: medium
- Review gate label: usable

## 1. One-paragraph benchmark summary
- Multicultural Spyfall turns the social-deduction party game Spyfall into a multilingual, multicultural benchmark for LLMs. Models must sustain strategic dialogue under hidden roles while grounding play in culturally specific locations or foods, which makes the benchmark test both social reasoning and localized world knowledge. The paper argues that this game-based setup is more leakage-resistant than static multilingual QA because game instances are generated dynamically and judged through interactive play. For this survey, it is a strong extension of the social-evaluation line because it shows that multilingual and multicultural stress can materially change conclusions drawn from English-only social benchmarks.

## 2. Position in our survey
- Why-games relevance: Social deduction creates a repeatable setting where deception, belief tracking, and strategic dialogue can be tested jointly rather than as isolated QA skills.
- Historical stage: diagnostic capability probe
- Narrative level(s): L3 social intelligence
- Most relevant outline section(s): 1,2,3,4
- Role in corpus: representative

## 3. Design-space coding
### 3.1 Environment structure
- Information structure: imperfect
- Transition structure: mixed
- Agent structure: multi-agent
- Social structure: mixed
- Time structure: turn-based

### 3.2 World structure
- World type(s): social deduction
- Real game / simulated game / designed task-game hybrid: real game adapted into an LLM benchmark
- Benchmark unit: full game

### 3.3 Benchmark scope
- Scope: single game
- Number of games / tasks: Spyfall episodes instantiated across multiple languages and culturally grounded entity sets
- Benchmark intent: diagnostic evaluation

### 3.4 Modality
- Primary modality: text
- Perception burden retained: hidden-role reasoning, multilingual dialogue, cultural grounding, and accusation strategy
- Perception burden removed: no visual table interaction or embodied play burden

## 4. What this benchmark measures
- Primary capability target: multilingual social reasoning under hidden roles
- Secondary capability target(s): cultural grounding, rule following, strategic dialogue, and deception robustness
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? yes
- Does it test social reasoning / deception / cooperation? yes
- Does it test visual grounding / spatial-temporal reasoning? no
- Does it test long-horizon autonomy / task completion? partially
- Does it test real-time efficiency? no
- Does it test cross-game transfer / open-ended generalization? no
- Why is a game environment especially suitable here? Spyfall forces models to reveal or conceal identity through dialogue, so multilingual weakness becomes visible in actual interaction instead of static translation-style scoring.

## 5. Interaction paradigm
- Observation channel: role instructions, dialogue history, culturally specific candidate entities, and game-state metadata
- Action channel: natural-language questions, answers, and accusations
- Interface type: natural language
- Agent scaffold allowed: none
- Is there privileged API access? no
- How close is the setup to human play? high for a text-mediated version of Spyfall
- Main ecological-validity trade-off: the setup preserves the dialogue game loop well, but cultural grounding is still filtered through benchmark-selected entities and prompts

## 6. Evaluation protocol
- Main score: game outcome / role success rate
- Auxiliary score(s): language-specific comparisons, ranking agreement with Chatbot Arena, and rule-integrity analysis
- Evaluation style: win rate / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: model-vs-model play across multilingual settings
- Automatic verifiability: mixed
- Calibration method: repeated play across languages and culturally localized entity sets
- Anti-contamination argument: the paper explicitly frames dynamic gameplay as more leakage-resistant than static multilingual benchmarks
- Reliability or comparability concerns: it can be hard to separate cultural-knowledge deficits from prompt-language weakness and role-play instability

## 7. Main contributions
- Contribution 1: Introduces a dynamic multilingual social-deduction benchmark based on Spyfall.
- Contribution 2: Adds culturally localized entities such as locations and foods to stress multicultural grounding.
- Contribution 3: Shows that social-game rankings can align with broad model rankings while still exposing major non-English weaknesses.

## 8. Main findings and failure modes
- Core empirical takeaway: benchmark rankings broadly align with Chatbot Arena, but model performance drops substantially in non-English and culturally specific settings.
- Notable model failure mode 1: weak handling of locally specific entities in non-English contexts
- Notable model failure mode 2: rule-following and strategic-integrity failures during multilingual play
- Notable model failure mode 3: brittle deception or detection behavior once cultural grounding pressure is added
- Does this paper reveal a benchmark-design limitation as well? yes; it shows that English-only social benchmarks can overestimate social competence

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Shows why dynamic game play can reduce leakage pressure in multilingual evaluation.
- Best use in Section 1 (taxonomy and evolutionary levels): Useful late-stage extension of social-deduction benchmarks toward multilingual and multicultural stress. Good example of a social-deduction benchmark whose key axis is language and culture rather than only game mechanics.
- Best use in Section 2 (core capabilities evaluated by games): Strong evidence for social reasoning plus cultural grounding.
- Best use in Section 3 (interaction and evaluation paradigm): Helpful for natural-language multi-agent play without privileged state abstractions. Supports discussion of dynamic, leakage-resistant multilingual evaluation.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Useful for arguing that future social benchmarks should go beyond English-centric settings.

## 10. Relation to nearby papers
- Closest predecessor(s): Werewolf Arena, WOLF, CK-Arena, other social-deduction evaluations
- Closest follow-up(s): multilingual or culturally grounded social benchmarks
- Best comparison targets inside our corpus: WerewolfArena, Wolf, CKArena, LLMHanabi
- What this paper uniquely adds relative to neighbors: It makes multilingual and multicultural stress a first-class variable in a deception benchmark rather than a side condition.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- The paper proposes a dynamic benchmarking framework based on Spyfall for multilingual and multicultural evaluation.
- Models must reason over culturally relevant locations or foods while trying to identify a secret agent or avoid detection.
- The authors report that game-based rankings align closely with Chatbot Arena, but non-English performance is much weaker and models often struggle with rule-following or strategic integrity.

### 11.2 Our synthesis / interpretation
- This is one of the clearest papers for arguing that social-intelligence benchmarks should not be treated as language-neutral.
- It is especially useful as a bridge from deception benchmarks to contamination-robust multilingual evaluation.

### 11.3 Uncertain or needs re-check
- Re-check the exact language roster, match counts, and per-role scoring details if we later compare multilingual social benchmarks numerically.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? Yes, likely, because the protocol details matter for cross-benchmark claims about multilingual social reasoning.
- Which section to read next if needed: setup / evaluation / discussion
- Follow-up question(s): How much of the reported non-English gap comes from cultural grounding versus weaker dialogue strategy?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P1
- Reading depth: deep
- Batch ID: B02
- Outline sections: 1,2,3,4
- Survey role: representative
- Paper card path: `paper_cards/B02/MulticulturalSpyfall.md`
- Next action: draft-section
- Last updated: 2026-04-08
