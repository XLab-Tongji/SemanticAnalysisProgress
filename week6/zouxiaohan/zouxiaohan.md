# Report of week 6 (2019-04-03~2019-04-09)

用LSTM, CNN 和 MLP识别语音情感。



## Code

代码：https://github.com/Renovamen/Speech-Emotion-Recognition

- LSTM, CNN, MLP模型实现
- 保存和加载模型
- 置信概率和雷达图
- 尽可能实现了高内聚低耦合

MLP模型的保存和加载了[苏昭帆和郭辉的工作](https://github.com/Zhaofan-Su/SpeechEmotionRecognition)。



## Experiment

数据集：CASIA，1200条数据，按8:2分成960条训练集和240条测试集。

1. LSTM准确率最高能上60%；
2. MLP准确率50%-55%；
3. 由于上周只用CNN对5种情感进行了分类，所以准确率偏高。这周分类6种情感，准确率降到了50%以下。进行了一些调参，并没有什么效果（实际上把准确率还调低了：）



## Unfinished

- 试图把[苏昭帆写的SVM](https://github.com/Zhaofan-Su/SpeechEmotionRecognition)整合进来。