import torch
import torch.nn as nn


class EevixModel(nn.Module):
    def __init__(self, input_dim=20, hidden_dim1=128, hidden_dim2=64, output_dim=10):
        super(EevixModel, self).__init__()
        self.fc1 = nn.Linear(input_dim, hidden_dim1)
        self.fc2 = nn.Linear(hidden_dim1, hidden_dim2)
        self.fc3 = nn.Linear(hidden_dim2, output_dim)
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        x = self.relu(x)
        x = self.fc3(x)
        return x


def create_eevix_model():
    return EevixModel()