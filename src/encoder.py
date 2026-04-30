import torch
from torch import nn


class Encoder(nn.Module):
    def __init__(self, dimension, sequence_length):
        super().__init__()
        self.norm1 = nn.LayerNorm(dimension)
        self.norm2 = nn.LayerNorm(dimension)
