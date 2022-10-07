import numpy as np
import math
from numpy.linalg import norm, eig
from utils.linear import hilbert_left_side
from utils.mar03.examples import examples

def max_abs(matrix):
	res_i, res_j = 0, 1
	size = matrix.shape[0]
	for i in range(size):
		for j in range(i + 1, size):
			if abs(matrix[res_i, res_j]) < abs(matrix[i, j]):
				res_i, res_j = i, j
	return res_i, res_j

def cyclic_choice(i, j, matrix_size):
	if (j < (matrix_size - 1) and j + 1 != i):
		return i, j + 1
	elif j == matrix_size - 1:
		return i + 1, 0
	else:
		return i, j + 2

def jacobi_method(matrix, precision, choosing_strategy):
	size = matrix.shape[0]
	i, j = choosing_strategy(0, 0, matrix)
	iters = 0
	
	while (i != size - 1 or j != size) and abs(matrix[i, j]) > precision:
		h = np.eye(size)
		phi = 0.5 * (math.atan((2 * matrix[i, j]) / (matrix[i, i] - matrix[j, j])))
		cos, sin = math.cos(phi), math.sin(phi)
		h[i, i], h[j, j] = cos, cos
		h[i, j], h[j, i] = -sin, sin
		
		matrix = np.transpose(h) @ matrix @ h
		
		i, j = choosing_strategy(i, j, matrix)
		iters += 1
	
	return np.diag(matrix), iters 

def gershgorin_circles(matrix):
	return [(matrix[i, i], sum(abs(matrix[i])) - abs(matrix[i, i])) for i in range(matrix.shape[0])]

def are_in_gershgorin_circles(xs, circles):
	is_at_least_in_one_circle = lambda x: any([abs(center - x) <= radius for center, radius in circles])
	xs_in_at_least_one = map(is_at_least_in_one_circle, xs)
	return all(xs_in_at_least_one)

max_abs_strat = lambda _1, _2, matrix: max_abs(matrix)
max_abs_jacobi = lambda matrix, precision: jacobi_method(matrix, precision, max_abs_strat)

cyclic_strat = lambda i, j, matrix: cyclic_choice(i, j, matrix.shape[0])
cyclic_jacobi = lambda matrix, precision: jacobi_method(matrix, precision, cyclic_strat)

if __name__ == '__main__':
	precisions = [10 ** (-i) for i in range(2, 6)]
	
	for matrix in examples:
		print('|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
		print(matrix)
		lambda_true = np.sort(eig(matrix)[0])
		
		for precision in precisions:
			lambda_abs, abs_iters = max_abs_jacobi(matrix, precision)
			lambda_circle, circle_iters = cyclic_jacobi(matrix, precision)
			
			print('precision = {}'.format(precision))
			print('abs error: {}\tabs iters: {}'.format(norm(np.sort(lambda_abs) - lambda_true), abs_iters))
			print('cir error: {}\tcir iters: {}'.format(norm(np.sort(lambda_circle) - lambda_true), circle_iters))
			
			circles = gershgorin_circles(matrix)
			print('abs in circles: {}'.format(are_in_gershgorin_circles(lambda_abs, circles)))
			print('cir in circles: {}'.format(are_in_gershgorin_circles(lambda_circle, circles)))
			print('----------==========----------')
