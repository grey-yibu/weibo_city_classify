import numpy as np

#%matplotlib inline
import matplotlib.pyplot as plt
import matplotlib
plt.rcParams['axes.labelsize'] = 14
plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12
# plt.rcParams['font.sans-serif'] = ['SimHei']


def logit(x):
    return 1/(1+np.exp(-x))

z = np.linspace(-5,5,200)
plt.plot([-5,5],[0,0],'k-')
plt.plot([-5,5],[1,1],'k--')
plt.plot([0,0],[-2,1.2],'k-')
plt.plot([-5,5],[-3/4, 7/4], 'g--')
plt.plot(z, logit(z), 'b-', linewidth=2)
props = dict(facecolor='black', shrink=0.1)
plt.annotate('Saturating', xytext=(3.5, 0.7), xy=(5,1), arrowprops=props, fontsize=14, ha='center')
plt.annotate('Linear', xytext=(2, 0.2), xy=(0,0.5), arrowprops=props, fontsize=14, ha='center')
plt.annotate('Saturating', xytext=(-3.5, 0.7), xy=(-5,0), arrowprops=props, fontsize=14, ha='center')
plt.grid(True)
plt.title(u'我就是我') # 注意以u开头
plt.axis([-5, 5, -0.2, 1.2])

plt.show()