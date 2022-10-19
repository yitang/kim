import sys
sys.path.append('../python')
import kim as ndl
import kim.nn as nn
import numpy as np
import time
import os

np.random.seed(0)

def ResidualBlock(dim, hidden_dim, norm=nn.BatchNorm1d, drop_prob=0.1):
    return nn.Sequential(
        nn.Linear(dim, hidden_dim),
        nn.ReLU(),
        nn.Linear(hidden_dim, dim),
        nn.Dropout(drop_prob),
        norm(dim),
    )


def MLPResNet(dim, hidden_dim=100, num_blocks=3, num_classes=10, norm=nn.BatchNorm1d, drop_prob=0.1):
    f = nn.Linear(dim, hidden_dim)
    # for i in range(num_blocks):



def epoch(dataloader, model, opt=None):
    np.random.seed(4)
    ### BEGIN YOUR SOLUTION
    raise NotImplementedError()
    ### END YOUR SOLUTION



def train_mnist(batch_size=100, epochs=10, optimizer=ndl.optim.Adam,
                lr=0.001, weight_decay=0.001, hidden_dim=100, data_dir="data"):
    np.random.seed(4)
    ### BEGIN YOUR SOLUTION
    raise NotImplementedError()
    ### END YOUR SOLUTION



if __name__ == "__main__":
    train_mnist(data_dir="../data")
