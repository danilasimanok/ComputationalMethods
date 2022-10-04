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
sol1 = [1, 2, 3, 4, 5]
m1_rght = m1_lft @ sol1

m2_lft = [
	[-400.46, 200.18],
	[1200.08, -600.64]
]
sol2 = [11.45, 6.23]
m2_rght = np.matmul(m2_lft, sol2)

m3_lft = [
	[1, 0.99],
	[0.99, 0.98]
]
sol3 = [3.1, 2.3]
m3_rght = np.matmul(m3_lft, sol3)

m4_lft = hilbert_left_side(10)
sol4 = [random() for _ in range(10)]
m4_rght = np.matmul(m4_lft, sol4)

m5_lft = diagonally_dominant(300)
sol5 = [randint(1, 5) for _ in range(300)]
m5_rght = m5_lft @ sol5

systems = [
	LinearSystem(m1_lft, m1_rght),
	LinearSystem(m2_lft, m2_rght),
	LinearSystem(m3_lft, m3_rght),
	LinearSystem(m4_lft, m4_rght),
	LinearSystem(m5_lft, m5_rght),
]

solutions = [sol1, sol2, sol3, sol4, sol5]

examples = zip(systems, solutions)
