"""练习 2：最小 MLP，784 → 128 → 10。"""
from torch import nn


class MLP(nn.Module):
    def __init__(self):
        super().__init__()
        # TODO: 注册 Flatten、Linear、ReLU、Linear；可用 nn.Sequential。
        # 先在纸上写出每一层的输入/输出形状。
        raise NotImplementedError("请定义网络层")

    def forward(self, x):
        # TODO: 返回 [B, 10] 的原始分数 logits，不加 softmax。
        raise NotImplementedError("请实现前向传播")
