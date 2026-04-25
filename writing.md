# Writing

This file is the active drafting workspace for the survey on game benchmarks for LLMs and VLM agents. `outline.md` is the canonical section map. `paper_cards/` and `corpus/registry/benchmark_registry.csv` remain the evidence layer. 

This file inlcude the detailed idea and high-level story I want to write in the survey. For different section, always draft the script along with this file. 

## Collaboration Rule

- Do not modify `writing.md` directly during drafting assistance.
- Always provide proposed `writing.md` revisions and candidate survey prose in the dialogue as reference material for human review.
- Treat any wording, structure, or paragraph plan shown in the chat as a suggestion until I manually decide whether to apply it.

## Narrative Spine

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

1. Level 1: 

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
