# Report of week 10 (2019-05-01~2019-05-07)

## Experiment

使用 [Opensmile](https://github.com/naxingyu/opensmile) 提取 [IS10_paraling](https://github.com/naxingyu/opensmile/blob/master/config/IS10_paraling.conf) 特征（2010 年国际语音挑战赛特征集合，包含 1582 个特征），然后 PCA 降维，MLP 的准确率在 80% 以上，SVM 的准确率在 70% 以上（当然如果我的代码有问题就另说了...）。

PCA 降维对准确率的提高不是特别大，所以主要应该是特征的问题。

还没有对 LSTM 和 CNN 进行实验，把特征输入神经网络的部分还没有处理好。

代码整理好后将更新在[这里](https://github.com/Renovamen/Speech-Emotion-Recognition)。



## Survey

整理了一些带代码的论文：[Papers with code](https://github.com/Renovamen/Speech-Emotion-Recognition/tree/Survey)



## Future

- 在 LSTM 和 CNN 上进行实验
- 尝试别的特征集，如 [IS09_emotion](https://github.com/naxingyu/opensmile/blob/master/config/IS09_emotion.conf) 等