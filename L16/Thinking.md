## Thinking  
**1、机器学习中的监督学习、非监督学习、强化学习有何区别**  
答：监督学习是通过对样本的已知分类标签进行学习对分类器进行优化的过程；无监督学习是学习无分类标签的样本，通过分类器将样本进行聚类的过程；强化学习是通过不断实践以获取正负反馈从而优化机器行为的过程。与监督学习相比，强化学习没有事先定义好的分类标签，其反馈是每一个行为结束后给出的；而与非监督学习相比，强化学习在每一轮学习后存在反馈给予原模型以一个激励。此外，监督学习与无监督学习的样本间相互独立，而强化学习的样本间存在前后的依赖关系。  
**2、什么是策略网络，价值网络，有何区别**  
答：策略网络是在给定环境下，各个动作行为对应的状态集合；价值网络则是在给定环境下，各个不同动作对应最终目标的价值集合；两者区别在于策略网络的输出是不同行为实行的概率，；而价值网络的输出是实行不同行为后所能达成最终目标的概率。  
**3、请简述MCTS（蒙特卡洛树搜索）的原理，4个步骤Select, Expansion，Simluation，Backpropagation是如何操作的**  
答：蒙特卡洛树搜索是通过不断进行选择、扩展、模拟和回传的循环，从而达到给决策树剪枝，快速获得最有决策的方法。  
（1）选择：从根节点开始，根据既定策略选择最有价值的子节点，并最终到达未拓展的叶子节点，即在该节点上存在可行动选择；  
（2）拓展：将该叶子节点进行拓展，添加新的子节点；  
（3）模拟：用随机模拟的方式完成该子节点后的所有行为，并得到最终的结果反馈；  
（4）回传：将最终的结果反馈加到该子节点的所有父节点上，并开始下一轮的循环。  
**4、假设你是抖音的技术负责人，强化学习在信息流推荐中会有怎样的作用，如果要进行使用强化学习，都有哪些要素需要考虑**  
答：强化学习在信息流推荐中可以帮助建立序列化的内容组合，从而非基于单个内容与用户匹配度进行推荐。以短视频推荐为例，用户的兴趣迁移往往具有一定的趋势性，利用强化学习可以提升向用户进行推荐内容间的关联性，优化用户的观看体验。 
如果要进行使用强化学习，需要考虑episode、reward、state和action的定义问题，此处先做一个简单的定义。Episode可以是从用户点开一个抖音视频开始，到用户点击推荐视频或退出抖音app为止，Reward则收集用户对于推荐的反馈，即用户是否点击推荐视频或退出抖音视频；Action则是用户对于不同视频的点击行为；State则是用户的不同状态；根据用户的不同状态向其推荐特定的视频，提高视频与用户之间的匹配效率。  
**5、在自动驾驶中，如何使用强化学习进行训练，请说明简要的思路**  
答：自动驾驶过程中，Episode是车辆起步开始、车辆到达目的地/发生碰撞/违反交通规则等一系列行为为止，Reward收集车辆的反馈，是到达目的地还是发生碰撞抑或是违反交通规则；Action是车辆对于路况的反应行为，包括左打方向盘、右打方向盘、油门、刹车、鸣笛等；State是车辆的现实状态，包括目前的路况、车况、车辆健康状态等。通过在模拟行驶过程中的不断迭代进行训练，从而达到在一定路段上的自动驾驶。  
