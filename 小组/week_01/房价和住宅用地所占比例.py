import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
#更改字体使图形中可以显示中文名称
matplotlib.rc('font',family='YouYuan')
#提取csv文件中的数据
df = pd.DataFrame(pd.read_csv('house_data.csv'))
x = df['ZN']
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
plt.title('房价和住宅用地所占比例的关系',fontsize=15)
plt.xlabel('住宅用地所占比例',fontsize=10)
plt.ylabel('房价（用房价中位数代表）',fontsize=10)
plt.show()
#从散点图来看，住宅用地所占比例绝大多数为0而且房价在这个占比下范围也较大，其他的数据并不多不具备代表性，因此二者没有特征关系