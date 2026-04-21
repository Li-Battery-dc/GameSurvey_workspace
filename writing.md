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

引入：游戏本身并不为了模型而设计，不会自动成为一个benchmark，需要interaction contract 和 evaluation contract才能利用上游戏的好处。The front end decides what part of the human play loop is preserved, while the back end decides what kinds of evidence can be extracted from play.

段落结构：

1. 举例论证同一个游戏由于接口和评分方式不同，不同的paradigm可以变成完全不同的benchmark. 

#### Interface

- Observation： 

- Action: 

#### Evaluation
