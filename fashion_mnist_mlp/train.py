"""练习 5：将已检查的模块连接起来。第一阶段固定使用 CPU。"""
import torch
from torch import nn

from data import make_loaders
from engine import evaluate, train_one_epoch
from model import MLP

SEED = 42
BATCH_SIZE = 64
LEARNING_RATE = 0.01
EPOCHS = 5


def main():
    torch.manual_seed(SEED)
    # TODO: 创建 loaders、MLP、nn.CrossEntropyLoss 和 torch.optim.SGD。
    # 优化器需要 model.parameters() 和 lr=LEARNING_RATE。
    # 每个 epoch 调用 train_one_epoch 和 evaluate，打印两组指标。
    # 完成前请先在 experiments.md 写下基线假设。
    raise NotImplementedError("请在前四个练习通过后连接训练闭环")


if __name__ == "__main__":
    main()
