import threading
import matplotlib.pyplot as plt
import numpy as np
import random
import time

Flag = 0
result_prob = [] # 改成list result_prob = []

def draw(i):
    plt.clf()  # 清除刷新前的图表，防止数据量过大消耗内存
    # 标签
    labels = np.array(['happy', 'angry', 'sad', 'fear', 'bored', 'neutral'])
    # 数据个数
    dataLenth = 6
    # 数据
    data = i
    # print(data)
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
    ax.set_rlim(0, 10)
    ax.grid(True)
    # plt.clf()  # 清除刷新前的图表，防止数据量过大消耗内存
    # plt.show()
    plt.pause(0.1) #暂停时间

class radar(threading.Thread):
    def run(self):
        global Flag
        global result_prob
        while(True):
            if(Flag ==1):
                v = np.array(result_prob)
                # print(result_prob)
                plt.ion()  # 开启interactive mode
                draw(v)# 调雷达图
                # plt.show()
                Flag = 0


def random_int_list(start, stop, length):
    start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
    length = int(abs(length)) if length else 0
    random_list = []
    for i in range(length):
        random_list.append(random.randint(start, stop))
    return random_list

def haha():
    thread_radar = radar()
    thread_radar.start()

    while(True):
        global Flag
        global result_prob
        result_prob = eval(input()) # 情感识别返回的概率（list）
        # result_prob = np.array(random_int_list(1,10,6))
        Flag = 1


haha()
plt.ioff()  # 关闭画图的窗口
plt.show()