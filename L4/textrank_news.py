#-*- encoding:utf-8 -*-
from textrank4zh import TextRank4Keyword, TextRank4Sentence
import jieba
from snownlp import SnowNLP
import jieba.analyse

file = open('./news.txt')
text = file.read()

#用jieba
keywords = jieba.analyse.textrank(text, topK=20, withWeight=True, allowPOS=('n', 'ns'))
for item in keywords:
    print(item[0],item[1])

#用textrank4zh
# 输出关键词，设置文本小写，窗口为2
tr4w = TextRank4Keyword()
tr4w.analyze(text=text, lower=True, window=2)
print('关键词：')
for item in tr4w.get_keywords(20, word_min_len=2):
    print(item.word, item.weight)
# 输出重要的句子
tr4s = TextRank4Sentence()
tr4s.analyze(text=text, lower=True, source = 'all_filters')
print('摘要：')
# 重要性较高的三个句子
for item in tr4s.get_key_sentences(num=3):
    # index是语句在文本中位置，weight表示权重
    print(item.index, item.weight, item.sentence)

#用snownlp
snow = SnowNLP(text)
# 打印关键词
print(snow.keywords(20))
# TextRank算法
print(snow.summary(10))
