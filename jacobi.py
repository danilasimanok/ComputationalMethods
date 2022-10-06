import numpy as np
from utils.math import sign
from utils.mar03.examples import examples
from numpy.linalg import eig, norm

def max_element(matrix):
	size = matrix.shape[0]
	res_i, res_j = 0, 1
	for i in range(size):
		for j in range(i + 1, size):
			if abs(matrix[i][j]) > abs(matrix[res_i][res_j]):
				res_i, res_j = i, j
	return res_i, res_j

def circle(i, j, size):
	if (j < size - 1 and j + 1 != i):
		return i, j + 1
	elif j == size - 1:
		return i + 1, 0
	else:
		return i, j + 2

def jacobi_method(matrix, precision, find_element):
	matrix = np.copy(matrix)
	size = matrix.shape[0]
	iters = 0
	i, j = find_element(0, 0, matrix)
	
	while (i != size or j != size) and matrix[i][j] > precision:
		h = np.eye(size)
		
		x = - matrix[i][j]
		y = matrix[i][i] - matrix[j][j]
		cos, sin = 1 / 2 ** 0.5, 1 / 2 ** 0.5
		if y != 0:
			cos = (1 / 2 * (1 + abs(y) / (x ** 2 + y ** 2) ** 0.5)) ** 0.5
			sin = sign(x * y) * abs(x) / (2 * cos * (x ** 2 + y ** 2) ** 0.5)
		
		h[i, i], h[j, j] = cos, cos
		h[i, j], h[j, i] = -sin, sin
		matrix = np.transpose(h) @ matrix @ h
		
		iters += 1
		i, j = find_element(i, j, matrix)
	
	return np.diag(matrix), iters

def abs_method(matrix, precision):
	find_element = lambda _1, _2, matrix: max_element(matrix)
	return jacobi_method(matrix, precision, find_element)

def circle_method(matrix, precision):
	find_element = lambda i, j, matrix: circle(i, j, matrix.shape[0])
	return jacobi_method(matrix, precision, find_element)

def gershgorin_circles(matrix):
	return [(matrix[i, i], sum(abs(matrix[i])) - abs(matrix[i,i])) for i in range(matrix.shape[0])]

def is_in_circles(num, circles):
	any([abs(center - num) <= radius for center, radius in circles])

if __name__ == '__main__':
	percisions = [10 ** -i for i in range(2, 6)]
	
	for matrix in examples:
		true_lambdas = np.sort(eig(matrix)[0])
		print('----====----')
		print(matrix)
		
		for precision in percisions:
			print('epsilon = {}'.format(precision))
			lambda_ans, ans_iters = abs_method(matrix, precision)
			lambda_cir, cir_iters = circle_method(matrix, precision)
			print('ans lambda error: {}\tans iters: {}'.format(lambda_ans, ans_iters))
			print('circle lambda error: {}\tcircle iters: {}'.format(lambda_cir, cir_iters))
			
			circles = gershgorin_circles(matrix)
			ans_in_circles = all([is_in_circles(x, circles) for x in lambda_ans])
			circle_in_circles = all([is_in_circles(x, circles) for x in lambda_cir])
			print('ans lambdas are in circles: {}\tcircle lambdas are in circles: {}'.format(ans_in_circles, circle_in_circles))