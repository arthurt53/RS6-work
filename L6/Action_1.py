import numpy as np
from scipy.linalg import svd
from PIL import Image
import matplotlib.pyplot as plt

# 取前k个特征，对图像进行还原
def get_image_feature(s, k):
    # 对于S，只保留前K%个特征值
    k_1 = int(round(num * k / 100,0))
    s_temp = np.zeros(s.shape[0])
    s_temp[0:k_1] = s[0:k_1]
    s = s_temp * np.identity(s.shape[0])
    # 用新的s_temp，以及p,q重构A
    temp = np.dot(p,s)
    temp = np.dot(temp,q)
    print("保留前",k,"%特征值输出的图像：")
    plt.imshow(temp, cmap=plt.cm.gray, interpolation='nearest')
    plt.show()
    #print(A-temp)


# 加载图片
image = Image.open('./action.jpg')
A = np.array(image.convert('L'),'f')

# 显示原图像
plt.imshow(A, cmap=plt.cm.gray, interpolation='nearest')
plt.show()
# 对图像矩阵A进行奇异值分解，得到p,s,q
p,s,q = svd(A, full_matrices=False)
temp_1 = len(p)
temp_2 = len(q[0])
num = min(temp_1,temp_2)

# 取前k个特征，对图像进行还原
get_image_feature(s, 1)
get_image_feature(s, 10)
get_image_feature(s, 50)
