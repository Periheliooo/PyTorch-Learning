"""练习 1：数据加载。先完成此文件，再开始网络。"""
from pathlib import Path

import torch
from torch.utils.data import DataLoader, random_split
from torchvision.datasets import FashionMNIST
from torchvision.transforms import ToTensor

DATA_DIR = Path(__file__).resolve().parent / "data"


def make_loaders(batch_size=64, seed=42):
    # TODO 1: 构造 FashionMNIST，使用 root=DATA_DIR、train=True、
    # download=True、transform=ToTensor()。Dataset 负责获取单个样本。
    # TODO 2: 使用 random_split 分成 54000 / 6000 个训练/验证样本。
    # 传入 generator=torch.Generator().manual_seed(seed)，固定划分。
    # TODO 3: 构造两个 DataLoader。训练 shuffle=True，验证 shuffle=False，
    # 均使用 batch_size=batch_size、num_workers=0。
    # 返回 train_loader, val_loader。
    training_data = datasets.FashionMNIST(
        root="data",
        train=True,
        download=True,
        transform=v2.Compose([v2.ToImage(), v2.ToDtype(torch.float32, scale=True)]),
    )

    test_data = datasets.FashionMNIST(
        root="data",
        train=False,
        download=True,
        transform=v2.Compose([v2.ToImage(), v2.ToDtype(torch.float32, scale=True)]),
    )

    
    raise NotImplementedError("请先完成数据集、划分与 DataLoader")


if __name__ == "__main__":
    train_loader, val_loader = make_loaders()
    images, labels = next(iter(train_loader))
    print("数据量:", len(train_loader.dataset), len(val_loader.dataset))
    print("images:", images.shape, images.dtype)
    print("labels:", labels.shape, labels.dtype)
    print("像素范围:", images.min().item(), images.max().item())
    print("前 10 个标签:", labels[:10])
    assert images.shape == (64, 1, 28, 28)
    assert labels.shape == (64,) and labels.dtype == torch.int64
    assert 0 <= images.min() <= images.max() <= 1
