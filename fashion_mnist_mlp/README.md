# Fashion-MNIST：从零完成 MLP 训练闭环

本项目是练习骨架，TODO 和 NotImplementedError 是刻意保留的练习点。
核心实现由学习者完成，导师先提供提示、形状检查与错误定位方法。

参考：https://docs.pytorch.org/tutorials/beginner/basics/quickstart_tutorial.html

## 环境

复用上一级 PyTorch/.venv。进入本目录后使用 `../.venv/bin/python`，
避免误用系统 Python。重建环境时可通过 requirements.txt 安装依赖。

## 第一阶段顺序

1. data.py：Dataset → 固定训练/验证划分 → DataLoader；运行数据检查。
2. model.py：最小 MLP；用一个 batch 检查输出形状。
3. engine.py：先完成单 batch 的参数更新，再实现整轮训练和评估。
4. experiments.md：训练前写基线假设。
5. train.py：连接模块，运行 5 epochs，记录并解释指标。

先运行 `../.venv/bin/python data.py`。首次运行需要联网下载数据。
ToTensor 将灰度图像转换为 [1, 28, 28] 的 float32 张量，像素缩放至 [0, 1]。
DataLoader 将样本组合成 [B, 1, 28, 28]；标签为 [B] 的 int64 类别索引。
Flatten 保留 batch 维度，网络形状为 [B, 784] → [B, 128] → [B, 10]。
CrossEntropyLoss 直接接收 logits 和类别索引，输出一个标量损失。

验收：能解释形状变化；确认一个 batch 更新了参数；完成整轮训练和
无梯度评估；损失与准确率按样本数统计；记录实际结果并解释。
准确率没有硬性门槛；训练未改善时，先检查梯度、参数更新和数据标签。

## 后续模块（本阶段不实现）

实验可视化将在闭环通过后加入：先训练曲线，再 TensorBoard 的
train/validation loss、accuracy、梯度范数和激活分布。
之后逐项研究网络结构、学习率、BatchNorm，最后整理对照结果与分析报告。
CNN 将建立独立项目目录。
