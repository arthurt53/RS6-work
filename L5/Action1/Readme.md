## Action1提交说明 
**由于全量数据集处理运算速度较慢，故对数据集做了切分，具体如下文所示**  
1、数据集处理：  
&ensp;&ensp;kaggle初始数据集有5个文件与本次作业相关，分别为combined_data_1.txt、combined_data_2.txt、combined_data_3.txt、combined_data_4.txt、probe.txt；    
具体步骤如下：  
&ensp;（1）除了combined_data_1文件是摘取前7.5万行数据外，其他文件均摘取前10万行数据，共37.5万行数据；同时，将这些数据进行格式转换，并将其输出至csv文件，文件**L5_Action1_pre1**为该过程的示例代码，由于是四个文件，故该代码需执行4次，分别输出combined_data_1_test2.csv、combined_data_2_test2.csv、combined_data_3_test2.csv、combined_data_4_test2.csv。  
&ensp;（2）通过文件**L5_Action1_pre2**中的代码将四个文件合并，作为本次作业的基础数据集combined_data_all_test2.csv。  
&ensp;（3）通过文件**L5_Action1_pre3**中的代码提取基础数据集中的ID信息，与probe.txt中的ID信息进行匹配，筛选出相应数据集作为本次作业的probe数据集probe_test2.csv。  
&ensp;（4）通过文件**L5_Action1_pre4**中的代码将基础数据集中存在于probe数据集的数据剔除作为本次作业的训练集data_new.csv，同时将probe数据集对应的实际评分补全作为本次作业的测试集probe_new_1.csv，共4672条数据。  
2、模型训练与RMSE输出：  
&ensp;（1）通过文件**L5_Action1_main**中的代码使用Surprise工具对训练集进行训练，同时对测试集进行预测，输出相应RMSE值。  
&ensp;（4）**最终，训练出RMSE值最小的算法是采用ALS进行优化的Baseline算法，在probe集上的RMSE值为1.1372。**  
