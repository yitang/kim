import kim
import kim.nn as nn
import numpy as np

np.random.seed(0)

def ResidualBlock(dim, hidden_dim, norm=nn.BatchNorm1d, drop_prob=0.1):
    f = nn.Sequential(
        nn.Linear(dim, hidden_dim),
        norm(hidden_dim),
        nn.ReLU(),
        nn.Dropout(drop_prob),
        nn.Linear(hidden_dim, dim),
        norm(dim),
    )
    return nn.Sequential(
        nn.Residual(f),
        nn.ReLU(),
    )
# https://raw.githubusercontent.com/dlsyscourse/hw2/32490e61fbae67d2b77eb48187824ca87ed1a95c/figures/residualblock.png

def MLPResNet(dim, hidden_dim=100, num_blocks=3, num_classes=10, norm=nn.BatchNorm1d, drop_prob=0.1):
    f = nn.Sequential(
        nn.Linear(dim, hidden_dim),
        nn.ReLU(),
        *[ ResidualBlock(hidden_dim, hidden_dim//2, norm=norm, drop_prob=drop_prob)
            for i in range(num_blocks) ],
        nn.Linear(hidden_dim, num_classes),
    )
    return f
# https://raw.githubusercontent.com/dlsyscourse/hw2/32490e61fbae67d2b77eb48187824ca87ed1a95c/figures/mlp_resnet.png

def epoch(dataloader, model, optim=None):
    np.random.seed(4)
    loss_func = nn.SoftmaxLoss()
    training = (optim is not None)

    if training: # model forward computation for train and eval will be (slightly) difference
        model.train()
    else:
        model.eval()

    # int metrics
    losses = 0
    errors = 0
    counts = 0

    for step, (inputs, labels) in enumerate(dataloader):
        predicts = model(inputs)
        loss = loss_func(predicts, labels)

        # update metrics
        errors += (predicts.numpy().argmax(axis=1) != labels.numpy()).sum()
        losses += loss.numpy()
        counts += inputs.shape[0]
        
        if training:
            optim.reset_grad()
            loss.backward() # backward for all nodes of computational graph, including model's params
            optim.step()    # update model's params

    # return metrics after consume all data
    return errors / counts, losses / (step + 1)


def train_mnist(batch_size=100, epochs=10, optimizer=kim.optim.Adam,
                lr=0.001, weight_decay=0.001, hidden_dim=100, data_dir="data"):
    np.random.seed(4)
    test_dataset = kim.data.MNISTDataset(\
            data_dir + "/t10k-images-idx3-ubyte.gz",
            data_dir + "/t10k-labels-idx1-ubyte.gz")
    test_dataloader = kim.data.DataLoader(\
             dataset=test_dataset,
             batch_size=batch_size,
             shuffle=False)

    train_dataset = kim.data.MNISTDataset(\
            data_dir + "/train-images-idx3-ubyte.gz",
            data_dir + "/train-labels-idx1-ubyte.gz")
    train_dataloader = kim.data.DataLoader(\
             dataset=train_dataset,
             batch_size=batch_size,
             shuffle=True)

    model = MLPResNet(784, hidden_dim)
    optim = optimizer(model.parameters(), lr=lr, weight_decay=weight_decay)
    for _ in range(epochs):
        train = epoch(train_dataloader, model, optim)
    return train + epoch(test_dataloader, model)


if __name__ == "__main__":
    train_mnist(data_dir="../data")
