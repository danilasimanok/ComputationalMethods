from ...linear import LinearSystem, hilbert_left_side
from random import random, randint
import numpy as np

def diagonally_dominant(size):
	result = np.zeros((size, size))
	sum = 0
	for i in range(size):
		for j in range(i + 1, size):
			if random() < 0.45:
				x = randint(1, 10)
				result[i][j] = x
				result[j][i] = x
				sum += x
	sum += 1
	return result + sum * np.eye(size)

m1_lft = np.eye(5)

m1_rght = [1] * 5

m2_lft = [
	[-400.46, 200.18],
	[1200.08, -600.64]
]

m2_rght = [199, -601]

m3_lft = [
	[1, 0.99],
	[0.99, 0.98]
]

m3_rght = [-0.393, -0.398]

m4_lft = hilbert_left_side(10)

m4_rght = [1] * 10

m5_lft = diagonally_dominant(300)

m5_rght = [1] * 300

examples = [
	LinearSystem(m1_lft, m1_rght),
	LinearSystem(m2_lft, m2_rght),
	LinearSystem(m3_lft, m3_rght),
	LinearSystem(m4_lft, m4_rght),
	LinearSystem(m5_lft, m5_rght),
]
