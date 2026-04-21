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

引入： While conventional game genres categorize titles by player experience, benchmark taxonomies must prioritize the functional demands imposed on an agent.  所以需要从多个角度对benchmark中的游戏环境进行更深层次的拆分和分析。

基本符合outline中的table content code描述。对每个维度的table code的具体含义和体现进行描述。描述时主要回答这些benchmark的结构类型，先不深入这些类型如何让benchmark发生系统性变化。
每个维度的story具体是:
1. benchmark level: 讲解全文的5层级发展分类：
- Level 1: Rule understanding — Can it make legal moves? (SmartPlay, GTBench)
- Level 2: Strategic Reasoning — Can it think effectively? (PokerBench, DSGBench. BeyondScaling)
- Level 3: Social Intelligence — Can it cooperate and deceive? (Werewolf Arena, WOLF)
- Level 4: Visual Agency — Can it play like a human? (BALROG, StarBench)
- Level 5: Cross-Game Generalization — Can it play anything? (GameVerse, AI GAMESTORE)

过渡，high——level的演化背后需要对游戏的设计结构进行进一步的探讨：
1. Game Structure: 只放形式机制：信息结构、随机性、agent 数量、合作/对抗、时间结构。
2. Environment Structure: 只放环境类型：tabletop / abstract puzzle / social interaction arena / combat-strategy world / adventure-quest world / sandbox-open-world。
2和3的正文进行叙述：游戏本身带有的属性和游戏环境的结构使其成为研究者选择其作为评测环境的原因，带给agent不同的挑战。从博弈论游戏到board games再到 复杂的商业游戏，研究者可设计和调整的范围更大了，通过不同structure的组合可以得到多样化的评测环境.
3. Benchmark Scope：
   - 早期single game大多强调推理深度，expert 能力,特点是metrics简单有效，方便做很深的case study。
   - game family 则在同类游戏结构下拓展，避免对单一游戏过拟合，同时保持相对统一的接口、规则分布和评测逻辑(FlashAdventure)。
   - curated suite基于作者对benchmark的设计有目的地覆盖多个 capability slice, 有意识地覆盖多种能力压力。通过差异化游戏结构评测模型的general 能力。 
   - expandable suite通过生成化方式引出无限的可拓展种类(AI GameStore)。 让 generalization 的重点从“是否见过这几个 benchmark games”转向“是否能应对新实例、新规则、新 level”。
   - open-ended tasks偏向大规模组合式、长尾、持续扩展的任务空间，强调 benchmark 如何在单一环境中不断生成新任务实例，而不等同于环境本身是否是 open-world。
4. Modality: (注意不要预先展开这些content code对于benchmark的影响)
   - obs: 
     - text or symbolic: 游戏状态用自然语言描述，符合LLM的language-centric,核心目标是diagnotic clarity. 
     - visual image: 使用screenshot, (其他方式)将游戏状态直接
     - mixed： 受限于当前模型能力，提供一些scaffold, 同时提供多种modality, 比较raw和assited. (STARBench)
   - action:
     - semantic: 高层次语义动作
     - native control: huamn-like的交互方式, gui, 键鼠交互，模拟器交互，
  
### Purpose

1. Level 1: 

### Paragim

#### Interface

#### Evaluation
