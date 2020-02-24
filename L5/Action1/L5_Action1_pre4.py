import pandas as pd

data = pd.read_csv('combined_data_all_test2.csv')
data_new = data
probe = pd.read_csv('probe_test2.csv')
probe_new = pd.DataFrame()
print(len(probe))

#形成训练集与测试集
for i in range(len(probe)):
    UID = probe.iloc[i,0]
    MovieID = probe.iloc[i,1]
    test = data[(data['ID'] == UID) & (data['MovieID'] == MovieID)]
    test_1 = data[(data['ID'] == UID) & (data['MovieID'] == MovieID)].index
    data_new = data_new.drop(test_1)
    probe_new = probe_new.append(test)

print(data_new)
print(probe_new)


data_new.to_csv('data_new.csv',index = 0)
probe_new.to_csv('probe_new_1.csv',index = 0)

#print('done')
