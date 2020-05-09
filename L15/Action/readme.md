## Avazu CTR数据集项目  
1、特征选择方面，我剔除了'id、hour、site_domain、app_domain、device_ip'这四个特征，并将剩余特征全进行了保留；  
2、训练集方面，我分别采样了2M和10M两个训练集分别进行了训练，并对全量预测集进行预测，分别得到submission_2M.csv和submission_10M.csv两个预测集、将两个预测集上传至kaggle后，基于2M数据集在Public和Private的评分分别为0.53016和0.52762；而基于10M数据集的评分分别为0.53500和0.53279；  
3、模型选择方面，我先用XdeepFM和XGboost分别对训练集进行训练并得出预测结果，并将两者的结果进行平均从而得到最终的预测结果。
