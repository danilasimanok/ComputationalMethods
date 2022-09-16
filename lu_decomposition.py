import numpy as np
from functools import reduce as fold
from conds import cond_s, cond_v, cond_a
from utils.feb24.lu.examples import examples

def create_multiplier(matrix, n):
	matrix_size = matrix.shape[0]
	multiplier = np.eye(matrix_size)
	
	for i in range(n + 1, matrix_size):
		multiplier[i][n] = - matrix[i][n] / matrix[n][n]
	
	return multiplier

def inv_multiplier(multiplier, n):
	result = np.copy(multiplier)
	for i in range(n + 1, multiplier.shape[0]):
		result[i][n] = - result[i][n]
	return result

def lu_decomposition_with_rside(left_side, right_side):
	u = np.copy(left_side)
	size = u.shape[0]
	multipliers = []
	invs = []
	for n in range(size):
		multiplier = create_multiplier(u, n)
		invs.append(inv_multiplier(multiplier, n))
		u = np.matmul(multiplier, u)
	l = fold(lambda acc, m: acc + m, invs, np.zeros((size, size))) - (size - 1) * np.eye(size)
	
	b = fold(lambda x, y: np.matmul(y, x), multipliers, np.reshape(right_side, (size, 1)))
	return l, u, np.reshape(b, (1, size))[0]

def solve_diagonal(left_side, right_side):
	size = len(right_side)
	
	solution = np.copy(right_side)
	for i in range(size - 1, -1, -1):
		subtrahend = 0.0
		for j in range(i + 1, size):
			subtrahend += left_side[i][j] * solution[j]
		solution[i] = (solution[i] - subtrahend) / left_side[i][i]
	return solution

def print_conds(matrix_name, matrix):
	print('cond_s({}) = {}'.format(matrix_name, cond_s(matrix)))
	print('cond_v({}) = {}'.format(matrix_name, cond_v(matrix)))
	print('cond_a({}) = {}'.format(matrix_name, cond_a(matrix)))

def solve_one(lin_sys):
	print('======')
	left_side = lin_sys.left_side
	right_side = lin_sys.right_side
	
	print('Solve Ax = b using LU-decomposition')
	print('A =', left_side)
	print('b =', right_side)
	print_conds('A', left_side)
	
	l, u, b = lu_decomposition_with_rside(left_side, right_side)
	print('Decomposition:')
	print('L =', l)
	print_conds('L', l)
	print('U =', u)
	print_conds('U', u)
	
	print('Solution:')
	print('x = {}'.format(solve_diagonal(u, b)))

if __name__ == '__main__':
	list(map(solve_one, examples))
