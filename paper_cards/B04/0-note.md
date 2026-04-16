# note记录

读论文想到的一些点

## V-MAGE

游戏环境pygame， 自己认为设计level不是很好。

ELO和human baseline的对比逐渐体现出来。

## ARE LARGE VISION LANGUAGE MODELS GOOD GAME PLAYERS?

从rule based 游戏到更加开放的游戏环境实际上评测这件事变难了

Game selection部分质疑了复杂游戏中实际上也是limited to simplified scenarios， 所以用来棋类游戏

task分解多级，对早期模型来说rule-following都已经算是难的了

## STARBench

scaffold是yolo + ocr式的文本提取

related works对于游戏的讨论也不错，提到了游戏环境复杂接近真实世界，接口类人，然后指出现有的高层API，模拟器实现，辅助工具hacking的问题。工具最大的问题是将perceprion control混在一起。

跟GameVerse的逻辑好像非常像啊，唯一的不同可能是查攻略的方式是构建RAG环境而不是视觉

result依旧直接控制全部报0，结论是knowing-excution gap， 然后OCR帮助非常大，说明文本还是影响关键，semantic action玩的很好。

## AtariGPT

把VA这种模式类比RL policy，所以用Atari。

主要说明模型的底层控制能力差的离谱，有意思的是在游戏pong中表现比random还差。主要问题是空间推理和