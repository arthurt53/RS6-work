**（1）生成baseline NDCG数据**  
java -jar RankLib-patched.jar -test Fold1/test.txt -metric2T NDCG@10 -idv output/baseline.ndcg.txt  
  
**（2）分别训练三个模型（RankNet, ListNet, LambdaMart）**  
**RankNet**：java -jar RankLib-patched.jar -train Fold1/train.txt -test Fold1/test.txt -validate Fold1/vali.txt -ranker 1 -metric2t NDCG@10 -metric2T NDCG@10 -save model_ranknet.txt  
**ListNet**：java -jar RankLib-patched.jar -train Fold1/train.txt -test Fold1/test.txt -validate Fold1/vali.txt -ranker 7 -metric2t NDCG@10 -metric2T NDCG@10 -save model_listnet.txt  
**LambdaMart**：java -jar RankLib-patched.jar -train Fold1/train.txt -test Fold1/test.txt -validate Fold1/vali.txt -ranker 6 -metric2t NDCG@10 -metric2T NDCG@10 -save model_LambdaMART.txt  
  
**（3）得出三个模型的NDCG结果（RankNet, ListNet, LambdaMart）**  
**RankNet**：java -jar RankLib-patched.jar -load model_ranknet.txt -test Fold1/test.txt -metric2T NDCG@10 -idv output/ranknet.ndcg.txt  
**ListNet**：java -jar RankLib-patched.jar -load model_listnet.txt -test Fold1/test.txt -metric2T NDCG@10 -idv output/listnet.ndcg.txt  
**LambdaMart**：java -jar RankLib-patched.jar -load model_LambdaMART.txt -test Fold1/test.txt -metric2T NDCG@10 -idv output/LambdaMART.ndcg.txt  
  
**（4）多个模型对比（RankNet, ListNet, LambdaMart）**  
java -cp RankLib-patched.jar ciir.umass.edu.eval.Analyzer -all output/ -base baseline.ndcg.txt > analysis.txt  
