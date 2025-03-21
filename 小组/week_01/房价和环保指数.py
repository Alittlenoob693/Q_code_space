import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
#更改字体使图形中可以显示中文名称
matplotlib.rc('font',family='YouYuan')
#接受csv文件中的数据
df = pd.DataFrame(pd.read_csv('house_data.csv'))
x = df['NOX']
y = df['MEDV']
plt.figure(figsize = (12,13),dpi=100,clear=True,tight_layout=True)
plt.scatter(x,y,s=None,c='b',marker='o',label='Industrial',alpha=0.5)
plt.legend()
#尝试用一次和二次函数拟合，一次函数用红色，二次函数用绿色
z = np.polyfit(x,y,1)
h = np.polyfit(x,y,2)
p = np.poly1d(z)
f = np.poly1d(h)
plt.plot(x,p(x),'r')
plt.plot(x,f(x),'g--')
plt.title('房价和环保指数的关系')
plt.xlabel('环保指数')
plt.ylabel('房价（用房价中位数代表）')
plt.xlim(0,1)
plt.show()
#通过散点图的分布我们可以看到虽然大多数点有按照拟合函数的趋势来进行变化，但在房价的方向上所呈现的范围太广，因此环保指数和房价无关