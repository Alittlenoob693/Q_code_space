import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
#更改字体使图形中可以显示中文名称
matplotlib.rc('font',family='YouYuan')
#提取csv文件中的数据
df = pd.DataFrame(pd.read_csv('house_data.csv'))
x = df['B']
y = df['MEDV']
#散点图观察大致分布
plt.figure(figsize = (10,10),dpi=100,clear=True,edgecolor='black',tight_layout=True)
plt.scatter(x,y,s=None,c='b',marker='o',label='Industrial',alpha=1)
plt.legend()
#尝试用一次和二次函数拟合，一次函数用红色，二次函数用绿色
z = np.polyfit(x,y,1)
h = np.polyfit(x,y,2)
p = np.poly1d(z)
f = np.poly1d(h)
plt.plot(x,p(x),'r')
plt.plot(x,f(x),'g--')
plt.title('房价和黑人比例的关系')
plt.xlabel('黑人比例')
plt.ylabel('房价（用房价中位数代表）')
plt.show()
#从拟合的一次函数和二次函数图像来看，黑人比例和房价呈正相关，但是通过散点图我们看出在黑人比例高的地方房价在各个价位都有较高的分布，因此我们大胆猜测房价和黑人比例没有太大关系