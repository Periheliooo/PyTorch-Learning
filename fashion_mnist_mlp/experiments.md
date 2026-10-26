# 实验记录

## E00：最小 MLP 基线（运行前填写）

- 假设：待填写（预测训练损失、验证准确率会怎样变化，并说明理由）。
- 配置：784 → 128 → 10，隐藏层 ReLU，SGD，lr=0.01，batch=64，5 epochs，seed=42，CPU。
- 数据：ToTensor；训练/验证 = 54000/6000；固定划分；不使用官方 test 集调参。
- 主要变量：首次基线，无对照改动。
- 运行命令：`../.venv/bin/python train.py`

| epoch | train loss | train accuracy | validation loss | validation accuracy |
|---|---|---|---|---|

- 观察：待填写。
- 假设是否得到支持：待填写。
- 原因解释与不确定性：待填写。

后续实验必须先写假设；每次只修改一个主要变量，并记录对照实验编号。
