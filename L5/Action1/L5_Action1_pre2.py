import pandas as pd
file_1 = pd.read_csv('./combined_data_1_test2.csv')
file_2 = pd.read_csv('./combined_data_2_test2.csv')
file_3 = pd.read_csv('./combined_data_3_test2.csv')
file_4 = pd.read_csv('./combined_data_4_test2.csv')
#文件合并
file_all = pd.DataFrame()
file_all = file_all.append(file_1)
file_all = file_all.append(file_2)
file_all = file_all.append(file_3)
file_all = file_all.append(file_4)

file_all.to_csv('combined_data_all_test2.csv',index = False)
print('Done')
