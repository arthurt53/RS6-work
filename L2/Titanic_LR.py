import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import cross_val_score
from sklearn import metrics
from sklearn.feature_extraction import DictVectorizer

# 数据加载
train_data = pd.read_csv('./train.csv')
test_data = pd.read_csv('./test.csv')
# 数据探索
# 查看train_data信息
#pd.set_option('display.max_columns', None) #显示所有列
print('查看数据信息：列名、非空个数、类型等')
print(train_data.info())
print('-'*30)
print('查看数据摘要')
print(train_data.describe())
print('-'*30)
print('查看离散数据分布')
print(train_data.describe(include=['O']))
print('-'*30)
print('查看前5条数据')
print(train_data.head())
print('-'*30)
print('查看后5条数据')
print(train_data.tail())

# 使用平均年龄来填充年龄中的nan值
train_data['Age'].fillna(train_data['Age'].mean(), inplace=True)
test_data['Age'].fillna(test_data['Age'].mean(),inplace=True)
# 使用票价的均值填充票价中的nan值
train_data['Fare'].fillna(train_data['Fare'].mean(), inplace=True)
test_data['Fare'].fillna(test_data['Fare'].mean(),inplace=True)

print(train_data['Embarked'].value_counts())
# 使用登录最多的港口来填充登录港口的nan值
train_data['Embarked'].fillna('S', inplace=True)
test_data['Embarked'].fillna('S',inplace=True)
# 特征选择
features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
train_features = train_data[features]
train_labels = train_data['Survived']
test_features = test_data[features]
print('特征值')
print(train_features)

dvec=DictVectorizer(sparse=False)
train_features=dvec.fit_transform(train_features.to_dict(orient='record'))
test_features=dvec.transform(test_features.to_dict(orient='record'))
print(dvec.feature_names_)

# 采用Z-Score规范化
ss = preprocessing.StandardScaler()
train_ss_features = ss.fit_transform(train_features)
test_ss_features = ss.transform(test_features)

# 创建LR分类器
lr = LogisticRegression()
lr.fit(train_ss_features, train_labels)

# LR预测
pred_labels = lr.predict(test_ss_features)

# 得到LR准确率(基于训练集)
acc_decision_lr = round(lr.score(train_ss_features, train_labels), 6)
print(u'score准确率为 %.4lf' % acc_decision_lr)

# 使用K折交叉验证 统计LR准确率
print(u'cross_val_score准确率为 %.4lf' % np.mean(cross_val_score(lr, train_ss_features, train_labels, cv=10)))
