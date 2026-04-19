# note 

## LLMChess

主要做了instruction following
比较平庸，但是启发我可以用agent接口调用来说rule following 这件事

## BotzoneBench

评测方式很有意思，作为主要卖点了，related works也是说别人的评测方式。

对于board game 里面的评测方式就很有意思

这篇论文又说rule——following完全不是问题了

## BoardGame Arena

整合框架的工作，同类board game整合到一起

## GridBasedGameCompetitions

对非法落子做了讨论，适合作为rule-following

prompt设计了多种形式，observation形式从list到Image， 影响结果

obeservation影响非法落子的频率。

## GTbench

对博弈论环境讨论多，把这些游戏环境做成规则清晰的，动作空间明确的评测环境

最后反而发现模型在完全信息下弱，LLM适合启发式搜索，不适合确定性搜索

## RuleOracles

桌游规则书理解，最符合rule-following

把失败分成局面理解和规则理解两部分了

## SmartPlay