## Thinking
**1、在CTR点击率预估中，使用GBDT+LR的原理是什么？**  
答：GBDT+LR的总体思想就是在特征工程的过程中，利用GBDT模型代替人工的手段对现有特征进行特征组合，然后将GBDT构造的新特征传入LR模型进行分类计算，最后通过Sigmod函数将结果映射到（0,1）上以得到分类结果。  
具体而言，算法实现步骤如下：  
（1）将特征传入GBDT模型，GBDT由多个决策树构成，每个决策树的训练对象是前一个决策树训练结果的残差，并记录下每棵树计算结果所属的叶子节点位置，最终将每棵树所记录的特征向量进行拼合输出构造的特征向量；  
（2）将GBDT模型输出的新特征向量传入LR模型进行训练，并通过Sigmod函数将结果映射至（0,1）上得到最终的分类结果。  
**2、Wide & Deep的模型结构是怎样的，为什么能通过具备记忆和泛化能力（memorization and generalization）**  
答：Wide & Deep模型通过同时对特征进行Wide模型训练以及Deep模型训练，并将结果累加得到最终数据；模型的整体结构是Wide模型与Deep模型的并行，并在Deep模型中采用塔型结构进行模型的训练。  
Wide模型可以通过利用交叉特征高效的实现记忆能力，达到准确推荐的目的；Deep模型则可以通过学习到的低纬度稠密向量实现模型的泛化能力；于是结合了两种模型的Wide & Deep模型同时具备了记忆与泛化能力。  
**3、在CTR预估中，使用FM与DNN结合的方式，有哪些结合的方式，代表模型有哪些？**  
答：FM与DNN的结合方式有两种，串行与并行，串行就是将FM模型的训练结果作为DNN模型的输入进行训练，串行结构的代表模型有NFM、AFM模型；而并行则是将FM模型与DNN模型同时进行训练，并行结构的代表模型有DeepFM、Wide & Deep模型。  
**4、Surprise工具中的baseline算法原理是怎样的？BaselineOnly和KNNBaseline有什么区别？**  
答：Baseline算法预测的结果基于全局平均、用户偏置项和物品偏置项三个参数，具体计算公式为b_ui=μ+b_u+b_i；并加入正则化项防止过拟合，最终通过求解lose的最小值来完成模型的训练。  
KNNBaseline模型之于BaselineOnly模型的区别在于BaselineOnly只用了Baseline算法，而KNNBaseline则是在KNNWithMeans的基础上，用baseline的值代替了原来的均值。  
**5、GBDT和随机森林都是基于树的算法，它们有什么区别？**  
答：GBDT使用的是Boosting的方法，即通过集成串行的多个决策树进行计算来提升模型的精度，GBDT中的分类器为弱分类器；而随机森林则是使用Bagging的方法，通过自助采样的方式生成多个并行分类器，通过投票的方式完成模型训练，随机森林中的分类器为强分类器。  
**6、基于邻域的协同过滤都有哪些算法，请简述原理。**  
答：基于领域的协同过滤算法主要包括两类，一类是基于用户相似度进行推荐的UserCF算法；另一类则是基于物品相似度进行推荐的ItemCF算法。  
（1）UserCF算法的原理是根据所有用户对商品的偏好，发现与当前用户偏好相近的K个用户，并形成一个用户群，同时基于这 K 个用户的历史偏好信息，为当前用户进行推荐。  
（2）ItemCF算法的原理是基于所有用户对商品的偏好，发现商品与商品之间的相似度，然后根据用户的历史偏好信息，将类似的商品推荐给当前用户。  