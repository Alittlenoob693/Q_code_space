import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
#更改字体使图形中可以显示中文名称
matplotlib.rc('font',family='YouYuan')
#提取csv文件中的数据
df = pd.DataFrame(pd.read_csv('house_data.csv'))
x = df['RAD']
y = df['MEDV']
#散点图观察大致分布
plt.figure(figsize = (12,12),dpi=100,clear=True,edgecolor='black',tight_layout=True)
plt.scatter(x,y,s=None,c='b',marker='o',label='Industrial',alpha=0.8)
plt.legend()
#尝试用一次和二次函数拟合，一次函数用红色，二次函数用绿色
z = np.polyfit(x,y,1)
h = np.polyfit(x,y,2)
p = np.poly1d(z)
f = np.poly1d(h)
plt.plot(x,p(x),'r')
plt.plot(x,f(x),'g--')
plt.title('房价和距离高速公路的便利指数的关系',fontsize=15)
plt.xlabel('便利指数',fontsize=10)
plt.ylabel('房价（用房价中位数代表）',fontsize=10)
plt.show()
#通过图像看出房价和距离高速公路便利指数几乎无关