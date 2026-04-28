# Writing

This file is the active drafting workspace for the survey on game benchmarks for LLMs and VLM agents. `outline.md` is the canonical section map. `paper_cards/` and `corpus/registry/benchmark_registry.csv` remain the evidence layer. 

This file inlcude the detailed idea and high-level story I want to write in the survey. For different section, always draft the script along with this file. 

## Collaboration Rule

- Do not modify `writing.md` directly during drafting assistance.
- Always provide proposed `writing.md` revisions and candidate survey prose in the dialogue as reference material for human review.
- Treat any wording, structure, or paragraph plan shown in the chat as a suggestion until I manually decide whether to apply it.

## Narrative Spine

Taxonomy 已经回答 “game benchmark 长成什么样”；Purpose 应该回答 “这些结构为什么能测某种能力”；Paradigm 再回答 “接口和指标如何改变这些证据的含义”。

high-level narrative stages, all sections follow or recall:
- Level 1: Rule understanding — Can it make legal moves? (SmartPlay, GTBench)
- Level 2: Strategic Reasoning — Can it think effectively? (PokerBench, DSGBench. BeyondScaling)
- Level 3: Social Intelligence — Can it cooperate and deceive? (Werewolf Arena, WOLF)
- Level 4: Visual Agency — Can it play like a human? (BALROG, StarBench)
- Level 5: Cross-Game Generalization — Can it play anything? (GameVerse, AI GAMESTORE，ARC-AGI-3)

## Section Tracker

### Lead-in

从static benchmark mismatch开始，引入game benchmark的核心点不是“games are harder tasks”，而是“games preserve the dynamic, interactive, human-oriented structure that static benchmarks abstract away”.用三个问题引出全文三个主体部分：benchmark structure, capability target, and evaluation paradigm.

段落计划：

1. Problem framing:
   - 从基础问题切入：如果模型越来越被讨论为 agent，应该如何评估它们
   - static QA 和 one-shot tests 主要提供 bounded knowledge / reasoning / one-shot multimodal understanding 的证据
   - agent intelligence 需要在持续 interaction 中体现：状态跟踪、长期规划、根据反馈调整、出错后恢复
   - 因此 evaluation gap 不在于题目是否更难，而在于是否保留 closed-loop interaction

2. Why games:
   - games 是为人类设计的动态任务系统，不只是娱乐类别
   - 它们天然包含规则、目标、反馈、阶段推进、胜负或进度结构
   - 正因为这些结构本来就是为人类玩家组织 challenge，games 才能成为 human-relevant capability probes
   - 可用代表例子覆盖 formal / social / agency 三类，但不要展开成 benchmark catalogue

3. Diversity as coverage:
   - 游戏多样性不是 genre taxonomy 的装饰，而是Multiverse of games 带来的 capability coverage. 
   - 不同 game structures 对 intelligence 提出不同压力：规则理解、规划、不完全信息、社会推理、长期任务推进
   - extensibility 在这里作为 benchmark space 的性质出现：人类游戏库和生成化 benchmark 让评测不容易被固定题集耗尽

4. Roadmap by three questions:
   - What kinds of game environments have benchmark designers built?
   - What capabilities do these game structures actually probe?
   - How do benchmark protocols turn gameplay into evidence, and what do benchmark scores really mean?

### Taxonomy

引入，为什么 genre taxonomy 不够： While conventional game genres categorize titles by player experience, benchmark taxonomies must prioritize the functional demands imposed on an agent.  所以需要从多个角度对benchmark中的游戏环境进行更深层次的拆分和分析。

段落结构如下：

引入benchmark level evolutionary spine， 明确发展历史主线，taxonomy 这里只做历史定位和组织，不讲每一级的 capability 细节，只讲 benchmark ambition 和 environment form 的历史推进。并且这种推进实际上和模型的能力和发展方向是近乎统一的。
- Level 1: Rule understanding — Can it make legal moves? (SmartPlay, GTBench)： Level 1 corresponds to early benchmarks built around formal rule-grounded interaction.
- Level 2: Strategic Reasoning — Can it think effectively? (PokerBench, DSGBench. BeyondScaling): Level 2 reflects a shift toward broader strategic decision making in evolving environments.
- Level 3: Social Intelligence — Can it cooperate and deceive? (Werewolf Arena, WOLF): multi-agent social reasoning.
- Level 4: Visual Agency — Can it play like a human? (BALROG, StarBench): preserves more of the visual and interface burden of human play.
- Level 5: Cross-Game Generalization — Can it play anything? (GameVerse, AI GAMESTORE): extends evaluation from competence in one game to adaptability across multiverse of games.

过渡，high——level的演化背后需要对 benchmark 作为 “game turned into evaluation object” 的方式做进一步解释：The five levels provide the survey's historical backbone, but they do not by themselves specify how a benchmark turns gameplay into an evaluable object. We therefore add secondary coding axes to describe structure, scope, and modality within and across these stages.

1. Structure: taxonomy 这里不再问 “这个游戏天然会施加什么 capability pressure”，那部分会在 Part 2 展开；这里问的是两个更 benchmark-centric 的问题：
   - `Form`: 这个 benchmark 实际让模型完成的 playable/evaluable unit 是什么。这个字段要让读者一眼看出 “progress 是如何被组织起来的”，以及 “什么算一次完整评测单元”。 `Form` 决定 benchmark 如何定义 episode、progress、completion、failure，也决定同样一个 “game” 在 benchmark 中是被当成 battle、story、world 还是 question 来评。
   - 词表：
     - `Match`: bounded 对局，终局和胜负清晰，适合 formal board/card/strategy benchmarks。
     - `Puzzle`: 单个约束求解实例或 question-like interactive problem，重点是局部解题或状态求解，而不是完整长期 play session。
     - `Dialogue`: 语言互动本身就是主要行动媒介，episode 靠协商、辩论、说服、身份判断推进。
     - `Encounter`: bounded tactical segment，例如一场战斗、一个关卡片段、一个短时任务场景。
     - `Arc`: 完整 story / quest progression，强调从开头到结尾的长依赖链。
     - `World`: 持续世界中的探索、生存、资源、achievement graph 或 open-ended task progression。
     - `Mixed`: 仅用于确实横跨多种 playable units 的 suites/platforms，不作为默认兜底项。
   - `Construction`: 这个 benchmark 是如何把 game 变成 benchmark artifact 的。这个字段直接回答 benchmark 与原始游戏 substrate 的关系。 `Construction` 决定 benchmark 和原始游戏的距离，直接影响 ecological validity、可仪器化程度、可重复性、contamination 风险与扩展方式。
   - 词表：
     - `Embedded`: benchmark 尽量保留原生 client/runtime/play surface，在原生游戏中直接评测。
     - `Wrapped`: benchmark 复用现有游戏或环境，但通过统一 harness / API / wrapper 重新暴露给模型。
     - `Adapted`: benchmark 取材于现有游戏，但把它切成特定 tasks / scenarios / questions / spots / logs 等评测对象。
     - `Authored`: 研究者为了评测专门设计 game-like environment 或 benchmark task-game。
     - `Generated`: benchmark 的核心对象由程序化、算法化或模型化生成，增长新任务/新规则/新游戏本身就是 benchmark 设计的一部分。  
    
2. Benchmark Scope：
   - 早期single game大多强调推理深度，expert 能力,特点是metrics简单有效，方便做很深的case study。
   - game family 则在同类游戏结构下拓展，避免对单一游戏过拟合，同时保持相对统一的接口、规则分布和评测逻辑(FlashAdventure)。
   - curated suite基于作者对benchmark的设计有目的地覆盖多个 capability slice, 有意识地覆盖多种能力压力。通过差异化游戏结构评测模型的general 能力。 
   - expandable suite通过生成化方式引出无限的可拓展种类(AI GameStore)。 让 generalization 的重点从“是否见过这几个 benchmark games”转向“是否能应对新实例、新规则、新 level”。
   - open-ended tasks偏向大规模组合式、长尾、持续扩展的任务空间，强调 benchmark 如何在单一环境中不断生成新任务实例，而不等同于环境本身是否是 open-world。
3. Modality: (注意不要预先展开这些 content codes 对 benchmark 结果的影响，留到 paradigm 中说)
   - obs: 
     - text or symbolic: 游戏状态用自然语言描述或结构化符号暴露，符合 LLM 的 language-centric interface，核心目标是 diagnostic clarity.
     - visual image: 使用 screenshot 或其他图像化观测直接暴露游戏状态，尽量保留原生感知负担。
     - mixed： 同时提供多种 observation modality，或者在 raw visual 之上加入有限 scaffold，便于比较 raw 与 assisted setting 的差异。`StarBench` 是典型例子。
   - action:
     - semantic: 高层次语义动作，例如 move / skill / target 级别的动作输出。
     - native control: human-like 的交互方式，例如 GUI、键鼠、模拟器输入。
     - mixed: 同一 benchmark 同时提供 semantic 和 native-control 两类 action channel，或让 agent 在两者之间切换。
  
### Purpose

引入：
从 taxonomy 的环境结构转向 benchmark 的能力目标，解释不同structure如何成为capability probes。五级结构在这里应被写成 capability ladder. 
提出后面的写法是：每一级level回答测什么能力，为什么这些游戏是适合的介质，值得关注的measuremnet mechanisms 如何让游戏成为能力探针。

本节沿用五级 evolutionary spine，但每一级都按同一逻辑展开为三个段落式：
1. Measurement target：这一层主要测什么能力。
2. Game affordance and Boundary：为什么这类游戏结构适合让该能力显形, 引出pros and cons, 明确这类游戏测试的boundary, 防止过度解读。
3. Measurement mechanisms：哪些 benchmark 设计将对应的能力很好的探测出来。强调设计服务于能力probe。这里只归纳整合机制，将一簇论文或者重要论文作为引用论据。不过度展开具体论文实现细节。

#### 2.1 Level 1: Rule Understanding — Games as rule-grounded formal containers

Core claim:
Level 1 的目标不是证明模型“聪明”，而是检验模型能否稳定进入一个规则化行动系统。它测的是 rule interpretation, state maintenance, legal-action generation, output conformity, tool/action formatting。只有这些基本环节稳定，后续 strategic reasoning 或 social reasoning 的分数才可解释。

Game affordance and boundary:
博弈论任务、棋盘游戏、网格游戏和 tabletop rule tasks 的共同价值在于 formal containment：规则封闭、状态转移明确、合法动作可检查、结果可自动评分。因此它们能提供比普通文字题更干净的 rule-grounding 证据。边界也来自这种干净性：许多 Level 1 benchmark 通过 text/API interface 暴露规则、状态、历史或 legal moves，移除了视觉感知、界面发现和低层动作控制；RuleOracles 还说明 rulebook access 和 situated rule application 也会分离。因此 Level 1 更适合作为 later gameplay evidence 的 entry condition，而不是 human-like play 的证明。

Measurement mechanisms:
- Rule-state-action formalization：把规则、状态、历史和动作空间转成可解析接口，使 legal participation 和 state tracking 可重复评估 `(SmartPlay; GTBench; BoardGameArena; BotzoneBench)`。
- Legality/interface diagnostics：把非法动作、格式错误、工具调用失败、timeout 与策略质量分开，避免把执行失败误读为战略失败 `(LLMChess; GridBasedGameCompetitions)`。
- Representation and rule-context stress tests：通过 list/illustration/image prompts、rulebook modality、board/grid 表示变化，检查规则理解是否稳定迁移到当前状态 `(GridBasedGameCompetitions; RuleOracles)`。

#### 2.2 Level 2: Reasoning — Games as interactive decision environments

Core claim:
Level 2 测的不是静态“会不会推理”，而是 interactive decision quality：模型是否能在状态变化、延迟后果、不完全信息、对手适应、空间约束和时间压力下持续做出有效行动。关键不是回答一道推理题，而是让 reasoning 在 action-consequence loop 中接受检验。

Game affordance and boundary:
游戏把 reasoning 外化为轨迹：每个动作改变后续状态，错误会积累，对手或环境会反馈，计划必须随新信息更新。这让 game benchmarks 可以测 stateful reasoning, adaptive planning, opponent-aware decision making, spatial planning 和 long-horizon strategy。边界是，多数 Level 2 benchmark 仍高度 textified/API-mediated；多游戏覆盖也不等于 transfer evidence；DSGBench/GameBench 这类维度分解主要是 benchmark designer 的测量框架，不应被写成已经验证的自然认知因子。

Measurement mechanisms:
- Formal strategic anchors：用 payoff、hidden information、equilibrium/regret、solver 或 graded AI anchors 给策略质量建立参照 `(GTBench; GAMABench; TMGBench; BotzoneBench)`。
- Coverage-oriented strategic suites：用多游戏/多场景覆盖 hidden information、uncertainty、cooperation、real-time pressure、adaptation 等不同 reasoning pressures，但避免把固定 suite 误读为 generalization `(GameBench; DSGBench; CivRealm)`。
- Spatial and temporal execution probes：用 maze/map traversal、dynamic spatial tasks、turn-based vs real-time matched settings 检验计划是否能转化为可执行轨迹 `(MazeEval; GameTraversalBenchmark; BeyondScaling)`。

#### 2.3 Level 3: Social Intelligence — Games as social interdependence engines

Core claim:
Level 3 测的不是一般 social QA，而是 social interdependence：一个 agent 的成功取决于它如何建模、影响、协调或抵抗其他 agents。这里的能力包括 hidden-role inference, deception, persuasion, trust calibration, theory of mind, joint planning, collaboration initiation and response。

Game affordance and boundary:
Hidden-role、negotiation、cooperative 和 coordination games 的优势在于把语言、信念、身份、承诺和协作变成胜负相关的环境变量。语言不只是解释任务，而是改变后续行动和他人信念。边界是，这些证据通常仍来自 text-only dialogue、structured roles、rules-based moderators、prompted ToM reports、LLM judge/self-label 或 scaffolded state；因此它们证明的是 instrumented social gameplay，而不是完整人类社交能力。

Measurement mechanisms:
- Hidden/private-information social inference：通过隐藏身份、私有信息、辩论、投票、怀疑轨迹和 deception labels 测身份推断、欺骗检测、信任和意图建模 `(AvalonBench; WerewolfArena; Wolf; Cicero)`。
- Cooperative interdependence probes：通过共享目标、非对称信息、hint interpretation、cross-play、initiating/responding metrics 测协作是否真正转化为联合行动 `(LLMHanabi; StrategicHanabi; CollabOvercooked; LLMCoordination)`。
- Process-level social diagnostics：用 suspicion trajectories、ToM scores、IC/RC、CoordQA、role-conditioned win rates 等指标解释 social success 的来源，而不是只看最终胜率 `(Wolf; LLMCoordination; CollabOvercooked)`。

#### 2.4 Level 4: Visual Agency — From knowing what to do to doing it in the game world

Core claim:
Level 4 的核心是 knowing-doing gap：模型是否能把视觉或半视觉状态可靠转成动作，并在长轨迹中保持目标、纠错和推进任务。这里测的不只是 perception，而是 perception + UI grounding + action localization + timing + recovery + memory。

Game affordance and boundary:
视觉游戏保留了人类玩家面对的 screen-to-action loop。模型不能只说出正确目标，还必须定位 UI、点击、移动、等待、避障、战斗、导航、使用物品，并从错误中恢复。这样静态视觉理解无法暴露的问题会变成可观察失败。边界是，越接近 human-like play，分数解释越困难：低分可能来自视觉误读、UI grounding、计划错误、latency、动作格式、记忆崩溃或恢复失败。因此 Level 4 的关键不是宣称“更真实所以更好”，而是明确 interface privilege 如何改变证据含义。

Measurement mechanisms:
- Perception-before-control diagnostics：先检验 gameplay video 或 dense visual state understanding，说明视觉状态理解本身就是瓶颈，但不把 QA 误读为 active play `(GameplayQA)`。
- Matched interface comparisons：在同一任务中比较 raw/direct control、semantic/tool-assisted control、paused vs real-time、text/image tracks，以拆分 reasoning、grounding 和 execution `(StarBench; GameWorld; LMGameBench; Balrog)`。
- Progress and recovery evaluation：用 milestones、quest progress、state-verifiable scoring、deadlock/recovery taxonomy 和 full-arc completion 评估长期推进与错误恢复 `(FlashAdventure; PokeGym; GameWorld; VideoGameBench)`。

#### 2.5 Level 5: Cross-Game Generalization and Open-Ended Task Generalization

Core claim:
Level 5 不应简单等于 “many games”。它测的是模型能否超越固定任务：面对新游戏、新规则、新关卡、新任务组合、新机制或 first-contact environment 时，仍能保持可迁移的游戏能力。

Game affordance and boundary:
人类游戏空间天然可扩展：同一机制可组合出新关卡，同一世界可生成长尾任务，不同游戏家庭可提供异质挑战，生成式或 living benchmark 可以持续增加新规则和新环境。这让 games 比固定题集更适合讨论 anti-saturation 和 generalist agency。边界必须明确区分三种证据：fixed curated breadth 主要说明 capability coverage；single-world open-ended tasks 说明 intra-world generalization；generated/living/first-contact settings 才更接近 novelty 和 anti-saturation。不要把 MCU/StarDojo、Orak/GameVerse、AIGameStore/ARCAGI3 写成同一种 generalization evidence。

Measurement mechanisms:
- Broad curated suite evidence：用固定多游戏集合测试模型或 scaffold 是否能跨不同游戏结构保持有效，但不声称 held-out transfer `(Orak; GameVerse; LMGameBench; TextQuests; TextAtari)`。
- Single-world open-ended task universes：在持续世界中扩展任务组合，评估 intra-world open-ended task generalization、长期任务推进和自动评估 `(MCU; StarDojo; TeamCraft; MineNPCTask)`。
- Generated/living/first-contact environments：通过程序化规则、human-game multiverse、private/OOD splits 或 hidden mechanics 测试 novelty、anti-saturation 和 first-contact adaptation `(GVGAILLM; AIGameStore; PuzzleJAX; ARCAGI3; Mars)`。



### Paragim

引入：游戏本身并不为了模型而设计，不会自动成为一个benchmark，需要interaction contract 和 evaluation contract才能利用上游戏的好处。The front end decides what part of the human play loop is preserved, while the back end decides what kinds of evidence can be extracted from play.游戏 benchmark 的关键难点，不是找到更难的游戏，而是把 gameplay 转换成可解释、可比较、可持续的 measurement pipeline。

前端 interaction 决定模型到底面对了什么难题。
后端 evaluation 决定研究者到底从行为里读出了什么证据。

段落结构：

paradigm 重要性和pipeline lens重要性。举例论证同一个游戏由于接口和评分方式不同，不同的paradigm可以变成完全不同的benchmark. 

#### Interface: privilege的层级

这部分先从observation和action角度对范式的优缺点进行简单论述。然后进行previlege的层级探讨。
重点参考Starbench， orak, GameVerse对于action和obs这些的探讨。

- Observation：
  从text进行游戏状态的抽象表示走向raw visual stream是通向通用视觉agent和human-like的范式转变。
  - 原始的text的表示服务于language-centric的LLMs并主要被用于推理评测。在很多基于文字和对话推理的游戏上好，但是对于一般的视觉商业游戏，这种转化需要依赖游戏API对于信息的获取，并且减弱了可拓展性。
  - 转向纯视觉输入是更加human-like的评测方式，顺应对模型能力要求提升。但是目前的纯视觉评测效果不好，因为视觉输入引入的状态噪声对于当前的模型来说比较难处理，模型得分非常低(VideoGameBench)， 中间可以有一些桥接的思路，比如STARbench用的OCR, Orak的text和image对比。

- Action: action形式决定模型如何和游戏状态互动。semantic action tuple 到 native mouse-keyboard control
  - semantic action通过规则化模型输出形式，并由工具解析后执行。这种方式让模型更多地关注到推理和决策本身，符合早期模型的关注点。
  - native control: 直接使用游戏原生的，为人类设计的动作接口，达到非常agentic的评测。这些接口通常很好被纳入一个统一的框架下(game pad, mouse-keyboard), 这种统一带来了benchmark的原生可拓展性，可以直接拓展到商业游戏。

- 接口不同的previlege层级讨论：
   -  Previlege讨论：SmartPlay、GTBench、DSGBench、GameBench 这种 textified / API-mediated benchmark，将perception burden、UI grounding burden 从任务中剥离出来，让 benchmark 更接近一个“strategic reasoning instrument”。自动评测稳定，适合单独分析高层能力。被整理好的状态表示和动作空间上做决策的能力。但是弱化了模型从环境中理解状态的能力。也适当讨论一下latency部分。问题一些论文做了多种设定的对比(VideoGameBench, orak, StarBench)，基本说明现在模型的弱点就是在于这些被previleged benchmark剥离的能力。
  - 现在的模型发展趋势是要做到end-to-end的agent loop, 博阿留了视觉 grounding、界面理解、动作执行、时序协调这些挑战，是现在的模型最缺乏，而human-like play 最需要的能力。但是现在的模型还不能在这些benchmark上做的好，导致这些benchmark内失败原因混杂，需要做更深入的case-study和comparison。

#### Evaluation

- 一些现有的evaluation metrics范式：
  -  Result-based metrics：游戏天然提供可用的结果信号，保留原生指标。从RL范式继承下来，符合native 的 end-to-end的agent 游玩目标，它最忠于游戏自身的目标语义，最容易自动化，也最适合大规模 benchmark。但是在模型失败的时候缺乏可解释性，太过于粗粒度。而且跨游戏的 score semantics 很弱，往往不同得分没有跨游戏统一含义。并且对于现在的模型而言，在native的游戏分数上取得较好的结果还是比较困难(Video Gamebench全部报0)，这种时候这些metrics失去评测意义。
  -  Adversarial evaluation:benchmark 是否通过对手、竞争环境或 live interaction 来制造动态评测压力，更不容易像静态题集那样快速饱和；能测试对手建模、欺骗、协作、策略调整这些只有互动中才出现的能力； leaderboard, 天然适合对抗社交multi-agent任务，在 social deduction 中尤其自然。得到模型的相对表现。得到排名但是不知道强在哪里，不知道模型为什么强，高度依赖对手池，参与模型，和protocol。adversarial evaluation 通过动态对抗提升 benchmark freshness，但也让分数更容易受到生态系统本身的影响。
  -  Process-level/里程碑型：添加更多metrics和提供环境更稠密的milestone类型。可解释性更强，更适合做failure analysis，更加细粒度，更能揭示模型能力缺陷和能力范围。对于长程任务尤其重要，因为长程任务的success太稀疏。但是对于process—level的分解和定义依赖特定的游戏，是benchmark构建者的预假设，天然不可以跨benchmark比较，并且设计较为复杂，设计有效性也很难说。

- Calibration and robustness: 如何保持metric的语义，如何保证evaluation准
  - Calibration: calibration 的作用，是让不同 evaluation 范式产生的分数拥有更丰富的语义，并且在合理范围内可比。给分数补充解释框架。提供解释分数意义的anchor, 评测解释性很强，让分数获得外部语义，保持分数有效性。ARC-AGI-3对于human first-contact baseline比较的强调等。
  - Robustness：  既包括结果是否稳定可复现，也包括 benchmark 是否没有被 shortcut、contamination 或 benchmark-specific optimization 主导。LMGAME-BENCH显式做了对比contamination案例。...其他案例。
