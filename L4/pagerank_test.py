import numpy as np
a = np.array([[0,0,0,1/3,0,0],
            [1/4,0,0,0,1/2,0],
            [0,1,0,1/3,1/2,0],
            [1/4,0,0,0,0,1],
            [1/4,0,1,1/3,0,0],
            [1/4,0,0,0,0,0]])

b = np.array([0,0,0,0,0,1])
w = b

def work(a, w):
    re_1 = np.array([0,0,0,0,0,0])
    for i in range(100):
        w = np.dot(a, w)
        print(w)
        if i == 99:
            re_1 = w
    return re_1

def random_work(a, w, n):
    d = 0.85
    re_2 = np.array([0,0,0,0,0,0])
    for i in range(100):
        w = (1-d)/n + d*np.dot(a, w)
        print(w)
        if i == 99:
            re_2 = w
    return re_2

print('简化模型计算：')
result_work = work(a, w)
print('简化模型计算结果：',result_work)
print('-'*100)
print('随机模型计算：')
result_random_work = random_work(a, w, 6)
print('随机模型计算结果：',result_random_work)
