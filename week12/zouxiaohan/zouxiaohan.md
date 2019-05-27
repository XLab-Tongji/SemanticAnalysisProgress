# Report of week 12 (2019-05-15~2019-05-21)

整理[代码](https://github.com/Renovamen/Speech-Emotion-Recognition/tree/Major-Update)：

- 解决了上次预测情感时出现的的问题；
- 整合了 SVM、MLP、LSTM，因为 CNN 效果较差训练速度较慢所以没有加进去；
- 尝试了[苏昭帆代码中的特征提取方式（librosa）](https://github.com/Zhaofan-Su/SpeechEmotionRecognition-papers-codes/blob/master/codes/PCA-SVM-KNN/features.py)，准确率略升，而且不需要安装 Opensmile（…）。