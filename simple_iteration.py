import numpy as np
from numpy.linalg import norm
from utils.linear import hilbert_left_side
from utils.feb24.simple_iteration.examples import examples

def simple_iterational_method(left_side, right_side, precision, iterations):
	size = left_side.shape[0]
	
	# define coeff for iteration
	alpha = np.zeros((size, size))
	beta = np.zeros(size)
	for i in range(size):
		for j in range(size):
			if i != j:
				alpha[i][j] = -left_side[i][j] / left_side[i][i]
	for i in range(size):
		beta[i] = right_side[i] / left_side[i][i]
	
	# check the system can be solved
	if norm(alpha) >= 1:
		return None
	else:
		x0 = beta
		x1 = beta + alpha @ x0
		while (iterations > 0) and (norm(x0 - x1) >= precision):
			iterations -= 1
			x0 = x1
			x1 = beta + alpha @ x0
		return x1

if __name__ == '__main__':
	print('Simple iteration')
	for system in examples:
		solution = simple_iterational_method(system.left_side, system.right_side, 0.001, 1000)
		if solution is None:
			print('Method sucks')
		else:
			print(solution)
