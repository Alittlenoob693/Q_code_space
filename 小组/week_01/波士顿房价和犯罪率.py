import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#更改字体使图形中可以显示中文名称
matplotlib.rc('font',family='YouYuan')
#提取csv文件中的数据
df = pd.DataFrame(pd.read_csv('house_data.csv'))
#人均城市犯罪率和房价的关系，这里用房屋房价中位数代表房价
x = df['CRIM']
y = df['MEDV']
plt.figure(num=None,figsize=(20,15),dpi=100,clear=True,tight_layout=True)
plt.scatter(x,y,s=None,color='blue',marker='s',alpha=1)
#用最小二乘法拟合，用一次函数，找出线性关系
z = np.polyfit(x,y,1)
p = np.poly1d(z)
plt.plot(x,p(x),'r--',linewidth=2)
plt.title('房价和犯罪率的关系')
plt.xlabel('犯罪率(0-10)区间')
plt.ylabel('房价(用中位数代替)(万美元)')
plt.xlim(0,10)           #犯罪率超过10的不多则舍去
plt.show()
#大部分的点集中在图像的左侧，并且这些点大都还在拟合函数周围，但是远离拟合函数的点也多，只能猜测犯罪率可能与房价呈负相关，