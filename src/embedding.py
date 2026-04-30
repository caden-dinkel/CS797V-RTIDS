import torch
from torch import nn


class Embedding:
    def __init__(self, dimension, sequence_length):
        self.W = nn.Parameter(torch.randn(sequence_length, dimension))
        self.b = nn.Parameter(torch.zeros(sequence_length, dimension))

    def forward(self, x):
        return x.unsqueeze(-1) * self.W + self.b
