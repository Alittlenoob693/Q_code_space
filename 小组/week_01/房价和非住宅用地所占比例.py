import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
#更改字体使图形中可以显示中文名称
matplotlib.rc('font',family='YouYuan')
#提取csv文件中的数据
df = pd.DataFrame(pd.read_csv('house_data.csv'))
x = df['INDUS']
y = df['MEDV']
#用散点图找大致分布
plt.figure(figsize = (10,10),dpi=100,clear=True,facecolor='yellow',edgecolor='black',tight_layout=True)
plt.scatter(x,y,s=None,color='b',marker='o',label='Industrial',alpha=0.5)
plt.legend()
#最小二乘法拟合，找线性关系
z = np.polyfit(x,y,1)
p = np.poly1d(z)
plt.plot(x,p(x),'r--')
plt.title('房价和非住宅用地所占比例的关系')
plt.xlabel('非住宅用地所占比例')
plt.ylabel('房价（用房价中位数代表）')
plt.show()#虽然竖直分布较开，但大致为线性负相关