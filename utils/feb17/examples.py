import numpy as np
from ..linear import LinearSystem, hilbert_left_side

m1_lft = [
	[-400.46, 200.18],
	[1200.08, -600.64]
]

m1_rght = [199, -601]

m2_lft = np.eye(5) * 1000.48

m2_rght = [2000.96, 2000.96, 2000.96, 2000.96, 2000.96]

m3_lft = [
	[401.52, 200.16],
	[1200.96, -601.68]
]

m3_rght = m1_rght

m4_lft = [
	[2, -1, 0, 0, 0, 0, 0, 0, 0],
	[-1, 2, -1, 0, 0, 0, 0, 0, 0],
	[0, -1, 2, -1, 0, 0, 0, 0, 0],
	[0, 0, -1, 2, -1, 0, 0, 0, 0],
	[0, 0, 0, -1, 2, -1, 0, 0, 0],
	[0, 0, 0, 0, -1, 2, -1, 0, 0],
	[0, 0, 0, 0, 0, -1, 2, -1, 0],
	[0, 0, 0, 0, 0, 0, -1, 2, -1],
	[0, 0, 0, 0, 0, 0, 0, -1, 2],
]

m4_rght = [4.0001, 4.0001, 4.0001, 4.0001, 4.0001, 4.0001, 4.0001, 4.0001, 4.0001]

hilbert_rght = [201, 399, 112, 487, 749]

examples = [
	LinearSystem(m1_lft, m1_rght),
	LinearSystem(m2_lft, m2_rght),
	LinearSystem(m3_lft, m3_rght),
	LinearSystem(m4_lft, m4_rght),
	LinearSystem(hilbert_left_side(5), hilbert_rght)
]
