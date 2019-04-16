import matplotlib.pyplot as plt
import numpy as np
import random
import time


def random_int_list(start, stop, length):
    start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
    length = int(abs(length)) if length else 0
    random_list = []
    for i in range(length):
        random_list.append(random.randint(start, stop))
    return random_list

def drawradar(c):
    labels = np.array(['aa','bb','cc','dd','ee','ff'])
    # data = np.array([1, 4, 3, 6, 4, 8])
    data = c
    angles = np.linspace(0, 2*np.pi, data.shape[0], endpoint=False)
    # 闭合
    data = np.hstack([data, data[0]])
    angles = np.hstack([angles, angles[0]])
    plt.polar(angles, data, 'ro-', linewidth=2)
    # 标签
    plt.thetagrids(angles * 180 / np.pi, labels)
    # 填充
    plt.fill(angles, data, facecolor='b', alpha=0.25)
    plt.title('radar')
    plt.ylim(0, 10)
    plt.grid(True)
    plt.show()

def draw(i):
    plt.clf()  # 清除刷新前的图表，防止数据量过大消耗内存
    # 标签
    labels = np.array(['happy', 'angry', 'sad', 'fear', 'bored', 'neutral'])
    # 数据个数
    dataLenth = 6
    # 数据
    data = i
    angles = np.linspace(0, 2 * np.pi, dataLenth, endpoint=False)
    data = np.concatenate((data, [data[0]]))  # 闭合
    angles = np.concatenate((angles, [angles[0]]))  # 闭合
    #fig = plt.figure()
    fig = plt.figure(1)

    # polar参数
    ax = fig.add_subplot(111, polar=True)
    ax.plot(angles, data, 'bo-', linewidth=2)
    ax.fill(angles, data, facecolor='r', alpha=0.25)
    ax.set_thetagrids(angles * 180 / np.pi, labels, fontproperties="SimHei")
    ax.set_title("Emotion Recognition", va='bottom', fontproperties="SimHei")
    # 在这里设置雷达图的数据最大值
    ax.set_rlim(0, 1)
    ax.grid(True)
    # plt.clf()  # 清除刷新前的图表，防止数据量过大消耗内存
    # plt.show()
    plt.pause(0.1) #暂停时间


plt.ion()  # 开启interactive mode
num = random.randint(4, 9)
for i in range(num):
    sltime = random.randint(1, 3)
    b = random_int_list(1, 10, 6)
    # print(b)
    c = np.array(b)
    # print(c)
    d = 0.1 * c
    draw(d)
    time.sleep(sltime)

plt.ioff()                 # 关闭画图的窗口
plt.show()
# plt.ioff()