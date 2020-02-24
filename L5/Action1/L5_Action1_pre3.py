import re
import pandas as pd

#在文件中获取ID
file_1 = pd.read_csv('combined_data_1_test2.csv')
temp = file_1['ID'].tolist()
temp_1 = set(temp)
temp_2 = list(temp_1)
temp_3 = [temp[-1]]
temp_4 = set(temp_3)
ID_1 = list(temp_1-temp_4)
print(ID_1)

file_2 = pd.read_csv('combined_data_2_test2.csv')
temp = file_2['ID'].tolist()
temp_1 = set(temp)
temp_2 = list(temp_1)
temp_3 = [temp[-1]]
temp_4 = set(temp_3)
ID_2 = list(temp_1-temp_4)
print(ID_2)

file_3 = pd.read_csv('combined_data_3_test2.csv')
temp = file_3['ID'].tolist()
temp_1 = set(temp)
temp_2 = list(temp_1)
temp_3 = [temp[-1]]
temp_4 = set(temp_3)
ID_3 = list(temp_1-temp_4)
print(ID_3)


file_4 = pd.read_csv('combined_data_4_test2.csv')
temp = file_4['ID'].tolist()
temp_1 = set(temp)
temp_2 = list(temp_1)
temp_3 = [temp[-1]]
temp_4 = set(temp_3)
ID_4 = list(temp_1-temp_4)
print(ID_4)

ID = ID_1 + ID_2 + ID_3 +ID_4
#print(ID)

#将probe数据集中存在的与之前提取的ID相一致的所有数据提取出来，作为新的probe集
file_5 = open('probe.txt','r')
text = file_5.read()
file_5.close()
temp_4 = pd.DataFrame()
probe = pd.DataFrame()

for i in ID:
    UID = str(i)
    if UID == '1' :
        temp = re.compile(r'(.*?)('+UID+'):(.*?):',re.S)
    else:
        temp = re.compile(r'(.*\n)('+UID+'):(.*?):',re.S)
    temp_1 = temp.match(text)
    if temp_1 is None:
        continue
    else:
        temp_2 = temp_1.group(3)
        temp_3 = temp_2.split('\n')
        MovieID = temp_3[1:len(temp_3)-1]
        temp_4 = pd.DataFrame({'ID':UID,'MovieID':MovieID})
        probe = probe.append(temp_4,ignore_index=True)

probe.to_csv('probe_test2.csv',index = 0)
print('Done')
#print(probe)
