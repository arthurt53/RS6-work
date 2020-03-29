## Thinking  
**1、排序模型按照样本生成方法和损失函数的不同，可以划分成Pointwise、Pairwise、Listwise三类方法，这三类排序方法有何区别？**  
答：（1）Pointwise是针对单个文档进行训练，它将每个文档转化成独立的特征向量，并计算其与输入query的相关性。输入为各个文档的特征向量以及输入query；输出为各个文档与输入的相关性或分类标签；损失函数有RMSE、logloss、entropy cross。  
（2）Pairwise是针对两个文档进行配对训练，计算两个文档的先后顺序关系。输入为文档对以及输入query；输出为文档的偏向得分；损失函数为Pairwise分类Loss。  
（3）Listwise是针对一个文档列表进行训练，根据输入query计算最优评分函数，并据此将文档列表进行排序；输入为文档列表以及输入query；输出为所有文档的打分或排序；损失函数为NDCG、MAP、MRR等评价指标。  
**2、排序模型按照结构划分，可以分为线性排序模型、树模型、深度学习模型，这些模型都有哪些典型的代表？**  
答：（1）线性排序模型：LR；  
（2）树模型：GBDT、GBDT+LR；  
（3）深度学习模型：Wide&Deep、DeepFM、NFM等。  
**3、NDCG如何计算？**  
答：（1）对所有返回结果的增益进行求和累加得到累计增益；  
（2）由于排名越靠前的结果价值越大，故对各个返回结果的增益除以log2（n+1）后进行累加得到折损累计增益；  
（3）计算理想正确排序搜索情况下的折损累计增益，并与之前计算的实际折损累计增益进行相处，最终得到NDCG。  
**4、搜索排序和推荐系统的相同和不同之处有哪些？**  
答：（1）相同之处：I、都是采用排序学习策略；II、都是以满足客户需求为最终目的；  
（2）不同之处：I、推荐系统通常采用pointwise排序学习策略，而搜索排序通常采用pairwise、listwise排序学习策略；II、推荐系统通常是满足客户的泛性需求，即在客户没有特定目标时根据历史行为为客户推荐商品，对商品排序没有特定的要求，而搜索排序则是满足客户的特性需求，即在客户有特定目标时为客户返回匹配度高的商品，对商品排序有较高的要求；III、基于前述应用场景的差异，推荐系统通常具有主动性，而搜索排序则具有被动型。  
**5、Listwise排序模型能否应用到推荐系统中？**  
答：Listwise可以应用到推荐系统中，但没有太大必要。由于推荐系统的应用场景是满足客户的非特定需求推荐，故对于返回结果间的排序没有特定的要求，因为此时客户对于自身的需求本身就是模糊的，一方面Listwise返回的排序对于满足客户需求并没有实质性的提升，另一方面Listwise相较Pointwise需要占用更多的资源；同时，推荐系统对于泛化推荐的需求比精确排序的需求更高。