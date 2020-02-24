#from surprise import SVD
from surprise import Dataset
from surprise import Reader
from surprise import BaselineOnly, KNNBasic, NormalPredictor, SlopeOne
from surprise import accuracy
from surprise.model_selection import KFold
#import pandas as pd

# 数据读取
reader = Reader(line_format='user item rating', sep=',', skip_lines=1)
data = Dataset.load_from_file('./data_new.csv', reader=reader)
train_set = data.build_full_trainset()
test = Dataset.load_from_file('./probe_new_1.csv', reader=reader)
test_set = test.build_full_trainset()
test_set_1 = test_set.build_testset()

# ALS优化
bsl_options_als = {'method': 'als','n_epochs': 5,'reg_u': 12,'reg_i': 5}
# SGD优化
bsl_options_sgd = {'method': 'sgd','n_epochs': 5}
#KNN算法
sim_options = {'name': 'pearson_baseline'}

#模型建立
algo_1 = KNNBasic(bsl_options=bsl_options_als, sim_options=sim_options)
algo_2 = KNNBasic(bsl_options=bsl_options_sgd, sim_options=sim_options)
algo_3 = BaselineOnly(bsl_options=bsl_options_als)
algo_4 = BaselineOnly(bsl_options=bsl_options_sgd)
algo_5 = NormalPredictor()
algo_list = [algo_1,algo_2,algo_3,algo_4,algo_5]
algo_list_name = ['KNNBasic_als','KNNBasic_sgd','BaselineOnly_als','BaselineOnly_sgd','NormalPredictor']
n = 0

#选取模型
for i in algo_list:
    i.fit(train_set)
    predictions = i.test(test_set_1)
    print('正在使用', algo_list_name[n], ':')
    accuracy.rmse(predictions, verbose=True)
    n += 1
