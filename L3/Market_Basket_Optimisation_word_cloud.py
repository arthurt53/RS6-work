# -*- coding:utf-8 -*-
# 词云展示
from wordcloud import WordCloud
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from lxml import etree
from nltk.tokenize import word_tokenize

# 生成词云
def create_word_cloud(f):
    print('根据词频，开始生成词云!')
    cut_text = word_tokenize(f)
    #print(cut_text)
    cut_text = " ".join(cut_text)
    wc = WordCloud(
        max_words=10,
        width=2000,
        height=1200,
    )
    wordcloud = wc.generate(cut_text)
    # 写词云图片
    wordcloud.to_file("wordcloud.jpg")
    # 显示词云文件
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()

# 数据加载
data = pd.read_csv('./Market_Basket_Optimisation.csv',header = None,keep_default_na='')
# 数据预处理
data_test = pd.DataFrame({'items':[]})

for i in range(len(data)):
    test =str()
    test_dict=dict()
    for t in range(len(data.iloc[i])):
        if t == 0 :
            test = data.iloc[i][t]
        else:
            if data.iloc[i][t] == '':
                continue
            else:
                test = test + '|' + data.iloc[i][t]
    test_dict['items'] = test
    data_test = data_test.append(test_dict,ignore_index=True)

all_word = " ".join(data_test['items'])

# 生成词云
create_word_cloud(all_word)
