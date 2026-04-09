# PokeChamp PokéChamp: an Expert-level Minimax Language Agent

## 0. Metadata
- Date: 2025/03
- Venue: ICML 2025
- Authors: Seth Karten, Andy Luu Nguyen, Chi Jin
- Paper link: https://arxiv.org/pdf/2503.04094v1.pdf
- Code link: https://github.com/sethkarten/pokechamp
- Reading depth: deep
- Card status: card-reviewed
- Confidence in this card: high
- Review gate label: strong

## 1. One-paragraph benchmark summary
- PokéChamp is primarily a specialist agent paper, but it includes a substantial evaluation ecosystem for competitive Pokémon battling that makes it valuable for this survey. The agent integrates LLMs into minimax search for action sampling, opponent modeling, and value estimation, and it is evaluated through offline battle datasets, 1,000 puzzle scenarios, arena play against heuristic and LLM baselines, and live Pokémon Showdown ladder games. The results show that a language-model-guided planning system can reach expert-level competitive performance without Pokémon-specific pretraining of the base LLM itself. For this survey, PokeChamp is best used as a strong specialist upper bound and a case study in LLM-plus-search design.

## 2. Position in our survey
- Why-games relevance: Pokémon battles stress hidden information, long horizons, combinatorial action spaces, and opponent modeling in a popular competitive game.
- Historical stage: ecological agent benchmark / specialist comparison
- Narrative level(s): L2 strategic reasoning / L3 social intelligence
- Most relevant outline section(s): 1,2,4
- Role in corpus: contrast

## 3. Design-space coding
### 3.1 Environment structure
- Information structure: imperfect
- Transition structure: stochastic
- Agent structure: multi-agent
- Social structure: competitive
- Time structure: turn-based with clock pressure

### 3.2 World structure
- World type(s): other
- Real game / simulated game / designed task-game hybrid: real competitive Pokémon battle simulator plus curated puzzles
- Benchmark unit: battle / puzzle

### 3.3 Benchmark scope
- Scope: single game with multiple evaluation modes
- Number of games / tasks: 3M replay dataset, 1,000 puzzle scenarios, arena evaluations, and live ladder games
- Benchmark intent: specialist evaluation

### 3.4 Modality
- Primary modality: text / symbolic state
- Perception burden retained: partial observability, move history, and game-state reasoning
- Perception burden removed: no raw visual battle interface

## 4. What this benchmark measures
- Primary capability target: strategic decision making in partially observable competitive battles
- Secondary capability target(s): opponent modeling, search under uncertainty, and use of special mechanics such as Terastallization and Dynamax
- Does it test rule grounding / legal action generation? yes
- Does it test strategic planning under uncertainty? yes
- Does it test social reasoning / deception / cooperation? partially through opponent modeling
- Does it test visual grounding / spatial-temporal reasoning? no
- Does it test long-horizon autonomy / task completion? yes
- Does it test real-time efficiency? yes
- Does it test cross-game transfer / open-ended generalization? no
- Why is a game environment especially suitable here? Competitive Pokémon combines hidden state, rich domain knowledge, and clocked decision making in a fully formalized environment.

## 5. Interaction paradigm
- Observation channel: symbolic battle state, move history, and learned/statistical world-model information
- Action channel: move or switch decisions selected through minimax plus LLM modules
- Interface type: API / hybrid
- Agent scaffold allowed: planner / retrieval / opponent model / value model
- Is there privileged API access? yes
- How close is the setup to human play? medium-low; the battle is authentic, but the agent uses symbolic state and internal planning modules rather than a native UI
- Main ecological-validity trade-off: the system preserves real competitive mechanics and live ladder play, but with substantial structured search and world-model support

## 6. Evaluation protocol
- Main score: win rate and Elo in arena play and online ladder play
- Auxiliary score(s): puzzle win rate, average turns, and specialized mechanic-use analyses
- Evaluation style: win rate / Elo / hybrid
- Human baseline / AI anchor / self-play / model-vs-model setup: PokeChamp is compared against heuristic bots, prior LLM agents, and human ladder opponents
- Automatic verifiability: high
- Calibration method: large replay dataset, at least 25 matches per pairwise arena experiment, and live ladder evaluation
- Anti-contamination argument: live simulator battles and online ladder games reduce the relevance of memorized answer patterns
- Reliability or comparability concerns: performance is sensitive to metagame shifts, timeouts, and the quality of the world model and opponent model

## 7. Main contributions
- Contribution 1: Builds a language-model-guided minimax agent for competitive Pokémon.
- Contribution 2: Provides a large replay dataset and puzzle-style evaluation scenarios.
- Contribution 3: Demonstrates expert-level online performance and strong wins over heuristic and prior LLM baselines.

## 8. Main findings and failure modes
- Core empirical takeaway: coupling LLM priors with search and opponent modeling yields much stronger Pokémon play than pure heuristic or prior LLM agents.
- Notable model failure mode 1: weakness against stall and excessive switching strategies
- Notable model failure mode 2: timeout losses under strict clock constraints
- Notable model failure mode 3: dependence on static opponent modeling that can be exploited adversarially
- Does this paper reveal a benchmark-design limitation as well? yes; it shows that specialist game strength often depends as much on search/world-model integration as on raw LLM reasoning

## 9. Why this paper matters for our survey
- Best use in Section 0 (lead-in and benchmark motivation): Limited; mostly a specialist exemplar.
- Best use in Section 1 (taxonomy and evolutionary levels): Useful in the line from heuristic game bots to LLM-augmented planners. Helps contrast benchmark papers with specialist systems plus rich evaluation harnesses.
- Best use in Section 2 (core capabilities evaluated by games): Strong source on uncertainty, opponent modeling, and search-guided planning.
- Best use in Section 3 (interaction and evaluation paradigm): An example of LLM modules embedded inside a search agent. Useful for discussing offline puzzles plus live ladder evaluation together.
- Best use in Section 4 (synthesis, bottlenecks, and future design): Supports hybrid approaches combining learned priors with planning.

## 10. Relation to nearby papers
- Closest predecessor(s): PokéLLMon
- Closest follow-up(s): future hybrid planning agents
- Best comparison targets inside our corpus: PokerBench, LLMPlayStarCraftII, VLMPlayStarCraftII
- What this paper uniquely adds relative to neighbors: It shows a particularly strong hybrid design where the LLM is not the whole policy but a component inside minimax planning.

## 11. Evidence notes
### 11.1 Direct paper-supported facts
- The paper uses a replay dataset of over 3 million Pokémon Showdown games and a benchmark of 1,000 1v1 puzzle scenarios.
- PokéChamp with GPT-4o reports 84% win rate against the Abyssal bot in Gen 9 OU and estimated online Elo around 1300-1500.
- The paper reports that the smaller Llama 3.1 8B version still beats the prior strongest LLM-based Pokémon bot.

### 11.2 Our synthesis / interpretation
- PokeChamp is one of the strongest specialist upper-bound systems in the corpus, but it should not be mistaken for a general benchmark platform.
- It is especially useful for showing how much structured planning can amplify an LLM in competitive games.

### 11.3 Uncertain or needs re-check
- Re-check the exact ladder win-rate computation excluding timeout losses if later drafting uses it.
- Re-check how much the one-step world model versus the LLM modules each contribute in ablations.

## 12. Follow-up reading plan
- Should we read beyond abstract + intro? why? Only if we later need a specialist-system case study.
- Which section to read next if needed: evaluation on full games / puzzle benchmarks / limitation analysis
- Follow-up question(s): How robust is PokéChamp to metagame drift without refreshing its historical statistics?

## 13. Registry sync
- Registry row synced: yes
- Registry status: card-reviewed
- Priority: P2
- Reading depth: deep
- Batch ID: B13
- Outline sections: 1,2,4
- Survey role: contrast
- Paper card path: `paper_cards/B13/PokeChamp.md`
- Next action: draft-section
- Last updated: 2026-04-05
