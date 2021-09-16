import torch
import torch.nn as nn
import torch.nn.functional as F


def sigmoid(x):
    return (1 + (-x).exp()).reciprocal()


def binary_cross_entropy(pred, y):
    return -(pred.log() * y + (1 - y) * (1 - pred).log()).mean()


if __name__ == '__main__':
    batch_size, n_classes = 10, 4
    x = torch.randn(batch_size, n_classes)

    target = torch.randint(n_classes, size=(batch_size,), dtype=torch.long)
    y = torch.zeros(batch_size, n_classes)
    y[range(y.shape[0]), target] = 1

    pred = sigmoid(x)
    loss = binary_cross_entropy(pred, y)
    print(loss)

    pred = torch.sigmoid(x)
    loss = F.binary_cross_entropy(pred, y)
    print(loss)

    loss = F.binary_cross_entropy_with_logits(x, y)
    print(loss)

