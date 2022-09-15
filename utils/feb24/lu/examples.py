from ...linear import LinearSystem, hilbert_left_side
from random import uniform as random

delta = -1/15

m1_lft = [
	[1, -1, -1, -1, -1],
	[delta, 1, -1, -1, -1],
	[delta, 0, 1, -1, -1],
	[delta, 0, 0, 1, -1],
	[delta, 0, 0, 0, 1]
]

m1_rght = [0, 0, 0, 0, 0]

m2_lft = [
	[1, 2, 4],
	[3, 8, 14],
	[2, 6, 13]
]

m2_rght = [1, 1, 1]

m3_lft = [
	[-400.6, 199.8],
	[1198.8, -600.4]
]

m3_rght = [200, -600]

m4_lft = [
	[1, 0.99],
	[0.99, 0.98]
]

m4_rght = [-0.393, -0.398]

hilbert_rght = [ random(0, 1) for _ in range(5) ]

examples = [
	LinearSystem(m1_lft, m1_rght),
	LinearSystem(m2_lft, m2_rght),
	LinearSystem(m3_lft, m3_rght),
	LinearSystem(m4_lft, m4_rght),
	LinearSystem(hilbert_left_side(5), hilbert_rght),
]
