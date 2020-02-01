import pandas as pd
import time

# 数据加载
data = pd.read_csv('./Market_Basket_Optimisation.csv',header = None,keep_default_na='')

# 采用efficient_apriori工具包
def rule1():
    from efficient_apriori import apriori
    start = time.time()

    # 格式转换
    transactions = []
    orders_series = set()
    orders_series  = data.values.tolist()
    for i in orders_series:
        while  '' in i:
            i.remove('')
        transactions.append(i)

    # 挖掘频繁项集和频繁规则
    itemsets, rules = apriori(transactions, min_support=0.01,  min_confidence=0.5)
    print('频繁项集：', itemsets)
    print('关联规则：', rules)
    end = time.time()
    print("用时：", end-start)

def encode_units(x):
    if x <= 0:
        return 0
    if x >= 1:
        return 1
# 采用mlxtend.frequent_patterns工具包
def rule2():
    from mlxtend.frequent_patterns import apriori
    from mlxtend.frequent_patterns import association_rules
    pd.options.display.max_columns=100
    start = time.time()
    # 格式转换
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
    hot_encoded_data = data_test['items'].str.get_dummies('|')
    hot_encoded_data = hot_encoded_data.applymap(encode_units)

    # 挖掘频繁项集和频繁规则
    frequent_itemsets = apriori(hot_encoded_data, min_support=0.01, use_colnames=True)
    rules = association_rules(frequent_itemsets, metric="lift", min_threshold=0.5)
    print("频繁项集：", frequent_itemsets)
    print("关联规则：", rules[ (rules['lift'] >= 1) & (rules['confidence'] >= 0.5) ])
    #print(rules['confidence'])
    end = time.time()
    print("用时：", end-start)

rule1()
print('-'*100)
rule2()
