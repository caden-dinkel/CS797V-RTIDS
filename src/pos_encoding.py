from math import cos, sin, sqrt

import torch


class PositionalEncoder(torch.nn.Module):
    def __init__(self, dimension, sequence_length):
        super().__init__()
        self.dimension = dimension

        pos_encoding = torch.zeros(sequence_length, dimension)
        for pos in range(sequence_length):
            for i in range(0, dimension, 2):
                # even positions
                pos_encoding[pos, i] = sin(pos / (1000 ** ((i) / dimension)))

                # odd positions
                pos_encoding[pos, i + 1] = cos(pos / (1000 ** (i / dimension)))

        pos_encoding = pos_encoding.unsqueeze(0)
        self.pos_encoding: torch.Tensor
        self.register_buffer("pos_encoding", pos_encoding)

    # x is input embedding
    def forward(self, x):
        x = x * sqrt(self.dimension)
        seq_len = x.size(1)
        x = x + self.pos_encoding[:, :seq_len]
        return x
