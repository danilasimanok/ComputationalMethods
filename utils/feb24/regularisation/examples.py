from ...linear import LinearSystem, hilbert_left_side
from random import uniform as random
import numpy as np

def calculate_rght(matrix, solution):
	solution = np.reshape(solution, (20, 1))
	rght = np.matmul(matrix, solution)
	return np.reshape(rght, (1, 20))[0]

hilbert_lft = hilbert_left_side(20)

ones = [1] * 20

rght_ones = calculate_rght(hilbert_lft, ones)

random_solution = [ random(0, 1) for _ in range(20) ]

random_rght = calculate_rght(hilbert_lft, random_solution)
