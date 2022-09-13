import numpy as np
from ...linear import LinearSystem, hilbert_left_side

alpha = -1/15

m1_lft = [
	[1, -1, -1, -1, -1],
	[alpha, 1, -1, -1, -1],
	[alpha, 0, 1, -1, -1],
	[alpha, 0, 0, 1, -1],
	[alpha, 0, 0, 0, 1]
]

m1_rght = [0, 0, 0, 0, 0]

examples = [LinearSystem(m1_lft, m1_rght)]
