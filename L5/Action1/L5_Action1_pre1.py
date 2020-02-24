import pandas as pd
import re
import time
from tqdm import tqdm

file = open('./combined_data_4.txt','r')
text = file.readlines()
file.close()
temp_3 = 0
a = 100000
text_test = text[0:a]
txt_1 =''.join(text_test)
n = txt_1.count(':')
data = pd.DataFrame(columns = ['ID','MovieID','Rating'],index = range(0,len(text_test)-n))
pbar = tqdm(total=100)
count = int(round(len(text_test)/20,0))
#格式整理
for line in text_test:
    temp = re.search(r':',line)
    temp_1 = []
    if temp is None:
        temp_1 = line.split(',')
        temp_3 += 1
    else:
        temp_2 = line.find(':')
        UID = line[:temp_2]
        continue
    data.iloc[temp_3-1,0] = UID
    data.iloc[temp_3-1,1] = temp_1[0]
    data.iloc[temp_3-1,2] = temp_1[1]
    num = (temp_3-1) % count
    if num == 0:
        pbar.update(5)
        time.sleep(0.1)

pbar.close()
data.to_csv('combined_data_4_test2.csv',index = False)
