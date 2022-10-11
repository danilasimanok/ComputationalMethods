import numpy as np
import math
from numpy.linalg import norm, eig
from utils.linear import hilbert_left_side
from utils.mar03.jacobi.examples import examples

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

def jacobi_max_abs(matrix, precision):
	size = matrix.shape[0]
	i, j = max_abs(matrix)
	iters = 0
	
	while abs(matrix[i, j]) > precision:
		h = np.eye(size)
		phi = 0.5 * (math.atan((2 * matrix[i, j]) / (matrix[i, i] - matrix[j, j])))
		cos, sin = math.cos(phi), math.sin(phi)
		h[i, i], h[j, j] = cos, cos
		h[i, j], h[j, i] = -sin, sin
		
		matrix = np.transpose(h) @ matrix @ h
		
		i, j = max_abs(matrix)
		iters += 1
	
	return np.diag(matrix), iters

def jacobi_cyclic(matrix, precision):
	size = matrix.shape[0]
	iters = 0
	
	max_i, max_j = max_abs(matrix)
	while abs(matrix[max_i, max_j]) > precision:
		
		i, j = cyclic_choice(0, 0, size)	
		
		while i != size - 1 or j != size:
			h = np.eye(size)
			phi = 0.5 * (math.atan((2 * matrix[i, j]) / (matrix[i, i] - matrix[j, j])))
			cos, sin = math.cos(phi), math.sin(phi)
			h[i, i], h[j, j] = cos, cos
			h[i, j], h[j, i] = -sin, sin
			
			matrix = np.transpose(h) @ matrix @ h
			
			i, j = cyclic_choice(i, j, size)
			iters += 1
		
		max_i, max_j = max_abs(matrix)
	
	return np.diag(matrix), iters

def gershgorin_circles(matrix):
	return [(matrix[i, i], sum(abs(matrix[i])) - abs(matrix[i, i])) for i in range(matrix.shape[0])]

def are_in_gershgorin_circles(xs, circles):
	is_at_least_in_one_circle = lambda x: any([abs(center - x) <= radius for center, radius in circles])
	xs_in_at_least_one = map(is_at_least_in_one_circle, xs)
	return all(xs_in_at_least_one)

if __name__ == '__main__':
	precisions = [10 ** (-i) for i in range(2, 15)]
	
	for matrix in examples:
		print('|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
		print(matrix)
		lambda_true = np.sort(eig(matrix)[0])
		
		for precision in precisions:
			lambda_abs, abs_iters = jacobi_max_abs(matrix, precision)
			lambda_circle, circle_iters = jacobi_cyclic(matrix, precision)
			
			print('precision = {}'.format(precision))
			print('abs error: {}\tabs iters: {}'.format(norm(np.sort(lambda_abs) - lambda_true), abs_iters))
			print('cir error: {}\tcir iters: {}'.format(norm(np.sort(lambda_circle) - lambda_true), circle_iters))
			
			circles = gershgorin_circles(matrix)
			print('abs in circles: {}'.format(are_in_gershgorin_circles(lambda_abs, circles)))
			print('cir in circles: {}'.format(are_in_gershgorin_circles(lambda_circle, circles)))
			print('----------==========----------')
