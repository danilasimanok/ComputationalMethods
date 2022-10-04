from ...linear import hilbert_left_side
import numpy as np

delta = -1/15

m1 = [
	[1, -1, -1, -1, -1],
	[delta, 1, -1, -1, -1],
	[delta, 0, 1, -1, -1],
	[delta, 0, 0, 1, -1],
	[delta, 0, 0, 0, 1]
]

m2 = [
	[-400.6, 199.8],
	[1198.8, -600.4]
]

m3 = [
	[1, 0.99],
	[0.99, 0.98]
]

examples = map(np.asarray, [m1, m2, m3, hilbert_left_side(4), hilbert_left_side(6)])
