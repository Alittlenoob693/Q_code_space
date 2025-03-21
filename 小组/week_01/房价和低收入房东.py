import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
#更改字体使图形中可以显示中文名称
matplotlib.rc('font',family='YouYuan')
#提取csv文件中数据
df = pd.DataFrame(pd.read_csv('house_data.csv'))
x = df['LSTAT']
y = df['MEDV']
# 如果输出长度不一致，说明数据过滤有问题
#使用散点图
plt.figure(figsize = (10,10), dpi = 100,clear=True,tight_layout=True)
plt.scatter(x,y,s=None,color='b',marker='o',alpha=0.7)
#用最小二乘法拟合，找出线性关系
z = np.polyfit(x,y,1)
p = np.poly1d(z)
plt.plot(x,p(x),'r--')

plt.title("房价和低收入房东个数关系",fontsize=20)
plt.xlabel("低收入房东个数",fontsize=15)
plt.ylabel("房价（用房价中位数代表）",fontsize=15)
plt.show()#大致为线性负相关