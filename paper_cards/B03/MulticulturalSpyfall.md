# MulticulturalSpyfall Multicultural Spyfall: Assessing LLMs through Dynamic Multilingual Social Deduction Game

## 0. Metadata
- Date: 2026/01
- Venue: arXiv
- Authors: Haryo Akbarianto Wibowo, Alaa Elsetohy, Qinrong Cui, Alham Fikri Aji
- Paper link: https://arxiv.org/pdf/2601.09017v1.pdf
- Code link:
- Reading depth: deep
- Card status: finalized
- Confidence in this card: medium
- Review gate label: usable

## 1. One-paragraph benchmark summary
- Multicultural Spyfall adapts Spyfall into a multilingual, multicultural social-deduction benchmark for LLMs. Models play a turn-based version of the game under hidden roles while reasoning over culturally specific locations or foods, so multilingual competence and local world knowledge both affect social play. The paper emphasizes dynamic gameplay as a more saturation-resistant alternative to static multilingual QA, but its most survey-relevant result is that non-English and local-knowledge settings change model rankings and failure modes in ways English-only evaluation hides. It is best used as an extension of the social-evaluation line rather than as a pure language benchmark.

## 2. Position in our survey
- Why-games relevance: Social deduction creates a repeatable setting where deception, belief tracking, and strategic dialogue can be tested jointly rather than as isolated QA skills.
- Historical stage: diagnostic capability probe
- Benchmark level(s): L3 social intelligence
- Most relevant outline section(s): 2,3,4
- Role in corpus: representative

## 3. Design-space coding
### 3.1 Structure
- Form: Dialogue
- Construction: Adapted
- Construction note: real game adapted into an LLM benchmark
- Benchmark unit: full game

### 3.2 Mechanics profile
- State visibility: partial
- Transition uncertainty: mixed
- Actor configuration: multi-agent
- Incentive structure: mixed
- Temporal regime: turn-based

### 3.3 Benchmark scope
- Scope: single game
- Number of games / tasks: 5-player Spyfall matches across four language settings and three entity regimes (generic locations, local locations, local foods)

### 3.4 Modality
- Observation modality: text or symbolic
- Action modality: semantic
- Perception burden retained: hidden-role reasoning, multilingual dialogue, cultural grounding, and accusation strategy
- Perception burden removed: no visual table interaction or embodied play burden

## 4. What this benchmark measures
- Primary capability target: multilingual social reasoning under hidden roles
- Secondary capability target(s): cultural grounding, rule following, strategic dialogue, and deception robustness
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? yes
- Does it test social reasoning / deception / cooperation? yes
- Does it test visual grounding / spatial-temporal reasoning? no
- Does it test long-horizon autonomy / task completion? no
- Does it test real-time efficiency? no
- Does it test cross-game transfer / open-ended generalization? no
- Why is a game environment especially suitable here? Spyfall forces models to reveal or conceal identity through dialogue, so multilingual weakness becomes visible in actual interaction instead of static translation-style scoring.

## 5. Interaction paradigm
- Observation channel: role instructions, dialogue history, 30 candidate entities, and game-state metadata
- Action channel: JSON-formatted questions, answers, spy guesses, and votes
- Interface type: natural language / structured output
- Agent scaffold allowed: none
- Is there privileged API access? no
- How close is the setup to human play? medium; the dialogue loop is preserved, but the game is turn-based, exposes a fixed entity list, and requires strict JSON outputs
- Main ecological-validity trade-off: the setup retains hidden-role dialogue and accusation, but it simplifies real-time play into a turn-based protocol with benchmark-curated entity pools

## 6. Evaluation protocol
- Main score: overall multilingual game ranking from repeated model-vs-model play
- Auxiliary score(s): role success rate, entity-guess accuracy, vote entropy, language-specific breakdowns, and ranking agreement with Chatbot Arena
- Evaluation style: ranking / win rate / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: model-vs-model play across multilingual settings, compared post hoc to Chatbot Arena rankings
- Automatic verifiability: medium to high
- Calibration method: repeated play across languages and culturally localized entity sets
- Anti-contamination argument: the paper explicitly frames dynamic gameplay as more leakage-resistant than static multilingual benchmarks
- Reliability or comparability concerns: it can be hard to separate cultural-knowledge deficits from prompt-language weakness, and using four identical non-spy instances may introduce behavioral coupling

## 7. Main contributions
- Contribution 1: Introduces a dynamic multilingual social-deduction benchmark based on Spyfall.
- Contribution 2: Adds culturally localized entities such as locations and foods to stress multicultural grounding.
- Contribution 3: Shows that social-game rankings can align with broad model rankings while still exposing major non-English weaknesses.

## 8. Main findings and failure modes
- Core empirical takeaway: benchmark rankings broadly align with Chatbot Arena, but performance drops sharply in non-English and culturally specific settings, especially for local foods and weaker models.
- Notable model failure mode 1: weak handling of locally specific entities in non-English contexts
- Notable model failure mode 2: rule-following and strategic-integrity failures during multilingual play
- Notable model failure mode 3: brittle deception or detection behavior once cultural grounding pressure is added
- Does this paper reveal a benchmark-design limitation as well? yes; it shows that English-only social benchmarks can overestimate social competence

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Supports the claim that dynamic games can reduce static multilingual benchmark leakage while exposing failures that only appear during role-governed interaction.
- Best use in Section 1 (taxonomy and evolutionary levels): Use as a Level 3 extension, not a level anchor: Spyfall is adapted into a text-symbolic Dialogue benchmark where cultural entity pools become part of the social-deduction pressure.
- Best use in Section 2 (core capabilities evaluated by games): Strong Purpose evidence that social intelligence is language- and culture-conditioned; successful play requires hidden-role reasoning plus locally grounded entity knowledge.
- Best use in Section 3 (interaction and evaluation paradigm): Useful Paradigm case for strict JSON actions, fixed candidate entity pools, role permutations, leakage-rate analysis, and multilingual model-vs-model ranking.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Supports the design claim that English-only social benchmarks overestimate robustness; non-English local foods and locations expose rule-following, leakage, and strategic-integrity failures.

## 10. Relation to nearby papers
- Closest predecessor(s): Werewolf Arena, WOLF, CK-Arena, other social-deduction evaluations
- Closest follow-up(s): multilingual or culturally grounded social benchmarks
- Best comparison targets inside our corpus: BeyondSurvival, WerewolfArena, CKArena, Wolf
- What this paper uniquely adds relative to neighbors: It makes multilingual and multicultural stress a first-class variable in a deception benchmark rather than a side condition.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- The paper proposes a turn-based Spyfall benchmark for multilingual and multicultural evaluation.
- Experiments use five-player games with four non-spies and one spy, a 10-turn limit, and repeated role permutations across models.
- The benchmark covers generic locations, local locations, and local foods across English, Indonesian, Chinese, and Egyptian Arabic settings.
- The authors report that game-based rankings align closely with Chatbot Arena, but non-English performance is weaker and models often struggle with rule-following or strategic integrity.
- The reported ranking aggregates play across languages and scenarios over 9,000 matches, and the paper separately analyzes entity-guess accuracy and leakage when non-spies reveal the target entity.

### 11.2 Our synthesis / interpretation
- This is one of the clearest papers for arguing that social-intelligence benchmarks should not be treated as language-neutral.
- It is especially useful as a bridge from deception benchmarks to contamination-robust multilingual evaluation.

### 11.3 Uncertain or needs re-check
- Re-check the exact language roster, match counts, and per-role scoring details if we later compare multilingual social benchmarks numerically.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? Completed in this audit; the game protocol, multilingual setup, results, and limitations are now checked against the full paper.
- Which section to read next if needed: setup / evaluation / discussion
- Follow-up question(s): How much of the reported non-English gap comes from cultural grounding versus weaker dialogue strategy?

## 13. Registry sync
- Registry row synced: yes
- Registry status: finalized
- Priority: P1
- Reading depth: deep
- Batch ID: B03
- Outline sections: 2,3,4
- Survey role: representative
- Paper card path: `paper_cards/B03/MulticulturalSpyfall.md`
- Check status: unchecked
- Next action: draft-section
- Last updated: 2026-04-27
