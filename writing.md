# Writing

This file is the active drafting workspace for the survey on game benchmarks for LLMs and VLM agents. `outline.md` is the canonical section map. `paper_cards/` and `corpus/registry/benchmark_registry.csv` remain the evidence layer. 

This file inlcude the detailed idea and high-level story I want to write in the survey. For different section, always draft the script along with this file. 

## Narrative Spine

high-level narrative stages, all sections follow or recall:
- Level 1: Rule understanding — Can it make legal moves? (SmartPlay, GTBench)
- Level 2: Strategic Reasoning — Can it think effectively? (PokerBench, DSGBench. BeyondScaling)
- Level 3: Social Intelligence — Can it cooperate and deceive? (Werewolf Arena, WOLF)
- Level 4: Visual Agency — Can it play like a human? (BALROG, StarBench)
- Level 5: Cross-Game Generalization — Can it play anything? (GameVerse, AI GAMESTORE，ARC-AGI-3)

## Section Tracker

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
2. Game Structure: 只放形式机制：信息结构、随机性、agent 数量、合作/对抗、时间结构。
3. World Structure: 只放环境类型：board / card / puzzle / social deduction / RTS / adventure / sandbox / open-world。
2和3的正文进行叙述：游戏本身带有的属性和游戏环境的结构使其成为研究者选择其作为评测环境的原因，带给agent不同的挑战。从博弈论游戏到board games再到 复杂的商业游戏，研究者可设计和调整的范围更大了，通过不同structure的组合可以得到多样化的评测环境.

4. Benchmark Scope：
   - 早期single game大多强调推理深度，expert 能力,特点是metrics简单有效，方便做很深的case study。
   - game family 则在同类游戏结构下拓展，避免对单一游戏过拟合，同时保持相对统一的接口、规则分布和评测逻辑(FlashAdventure)。
   - curated suite基于作者对benchmark的设计有目的地覆盖多个 capability slice, 有意识地覆盖多种能力压力。通过差异化游戏结构评测模型的general 能力。 
   - expandable suite通过生成化方式引出无限的可拓展种类(AI GameStore)。 让 generalization 的重点从“是否见过这几个 benchmark games”转向“是否能应对新实例、新规则、新 level”。
   - open-ended world偏向真实长程交互和agentic 任务，最接近 agent 叙事里的“持续行为”。最能体现真实 autonomy。
5. Modality: (注意不要预先展开这些content code对于benchmark的影响)
   - obs: 
     - text or symbolic: 游戏状态用自然语言描述，符合LLM的language-centric,核心目标是diagnotic clarity. 
     - visual image: 使用screenshot, (其他方式)将游戏状态直接
     - mixed： 受限于当前模型能力，提供一些scaffold, 同时提供多种modality, 比较raw和assited. (STARBench)
   - action:
     - semantic: 高层次语义动作
     - native control: huamn-like的交互方式, gui, 键鼠交互，模拟器交互，
  
### Purpose

### Paragim

#### Interface

#### Evaluation

