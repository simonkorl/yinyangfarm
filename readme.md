# 阴阳农场原型

游戏设计原则：

1. 游戏有两个状态，一个叫阳，一个叫阴
2. 在阳状态，要让玩家感受到“这些东西越来越多，我好爽啊。”；在阴状态，要让玩家感受到“这些东西越来越少，我好爽啊。”
3. 玩家的角色死亡后，会转变为敌人；敌人死亡后，会转变为我方角色和（或）资源
4. 阴和阳的状态中，游戏中的设计最好是相反的，除非无法避免

## 原型设计 1

整体上类似于少前，可以抽角色，角色有技能，有基建宿舍，可以探索地图什么的。

额外规则：
1. 在阳状态下，游戏内的数值不允许下降（玩家看到的那些）；在阴状态下，游戏内的数值不允许上升。【假如说需要建筑建筑物，那么必须先在晚上消耗资源，然后第二天才能建出来。又比如说角色只有在白天才能回血，且白天不能掉血；角色在晚上不能回血。】