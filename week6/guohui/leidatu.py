
import numpy as np
import matplotlib.pyplot as plt

#定义各个参数的值
happy = 0.1
angry = 0.2
sad = 0.3
fear = 0.4
bored = 0.5
neutral = 0.6

#标签
labels = np.array(['happy','angry','sad','fear','bored','neutral'])
#数据个数
dataLenth = 6
#数据
data = np.array([happy,angry,sad,fear,bored,neutral])


angles = np.linspace(0, 2*np.pi, dataLenth, endpoint=False)
data = np.concatenate((data, [data[0]])) # 闭合
angles = np.concatenate((angles, [angles[0]])) # 闭合

fig = plt.figure()

# polar参数
ax = fig.add_subplot(111, polar=True)
ax.plot(angles, data, 'bo-', linewidth=2)
ax.fill(angles, data, facecolor='r', alpha=0.25)
ax.set_thetagrids(angles * 180/np.pi, labels, fontproperties="SimHei")
ax.set_title("Emotion Recognition", va='bottom', fontproperties="SimHei")

#在这里设置雷达图的数据最大值
ax.set_rlim(0,1)


ax.grid(True)
plt.show()
