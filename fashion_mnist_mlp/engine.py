"""练习 3、4：训练与评估。先实现一个 batch，再扩展到一个 epoch。"""
import torch


def train_one_epoch(model, loader, loss_fn, optimizer):
    # TODO: model.train()；逐 batch 前向传播、计算 loss、清空梯度、
    # 反向传播、更新参数。注意 PyTorch 默认会累积梯度。
    # 返回 {"loss": 平均损失, "accuracy": 准确率}，均为 Python 数值。
    # loss_fn 默认给出 batch 均值；累计时乘以本 batch 样本数，
    # 最后除以总样本数。accuracy = 总预测正确数 / 总样本数。
    raise NotImplementedError("请实现训练循环")


@torch.no_grad()
def evaluate(model, loader, loss_fn):
    # TODO: model.eval()；统计 loss 与 accuracy；不更新参数。
    # 返回与 train_one_epoch 相同的字典。
    # 思考：eval() 和 no_grad() 各负责什么？
    raise NotImplementedError("请实现评估循环")
