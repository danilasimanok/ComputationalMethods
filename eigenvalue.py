import numpy as np
from utils.mar03.eig.examples import examples
from numpy.linalg import eig

def pow_method(matrix, x0, precision, max_iters):
	x0 = np.copy(x0)
	x1 = matrix @ x0
	
	lambda0, lambda1 = x1[0] / x0[0], None
	num_of_iters = 1
	
	while (lambda1 is None) or (abs(lambda1 - lambda0) > precision and num_of_iters < max_iters):
		x0, x1 = x1, matrix @ x1
		lambda1, lambda0 = lambda0, x1[0] / x0[0]
		num_of_iters += 1
	
	return abs(lambda0), num_of_iters

def scal_method(matrix, x0, precision, max_iters):
	x0 = np.copy(x0)
	x1 = matrix @ x0
	
	y0 = np.copy(x0)
	transposed = np.transpose(matrix)
	y1 = transposed @ x0
	
	lambda0, lambda1 = np.dot(x1, y1) / np.dot(x0, y0), None
	num_of_iters = 1
	
	while (lambda1 is None) or (abs(lambda1 - lambda0) > precision and num_of_iters < max_iters):
		x0, x1 = x1, matrix @ x1
		y0, y1 = y1, transposed @ y1
		lambda1, lambda0 = lambda0, np.dot(x1, y1) / np.dot(x0, y1)
		num_of_iters += 1
	
	return abs(lambda0), num_of_iters

if __name__ == '__main__':
	for matrix in examples:
		x0 = np.ones(matrix.shape[1])
		lambda_true = max(abs(eig(matrix)[0]))
		print('----====----')
		print(matrix)
		for k in range(-2, -6, -1):
			precision = 10 ** k
			print('epsilon = {}'.format(precision))
			lambda_pow, iters_pow = pow_method(matrix, x0, precision, 1000)
			print('|lambda_pow - lambda| = {}, iters {}'.format(abs(lambda_true - lambda_pow), iters_pow))
			lambda_scl, iters_scl = scal_method(matrix, x0, precision, 1000)
			print('|lambda_scl - lambda| = {}, iters {}'.format(abs(lambda_true - lambda_scl), iters_scl))
