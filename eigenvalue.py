import numpy as np
from utils.mar03.examples import examples
from numpy.linalg import eig

def pow_method(matrix, precision, max_iters):
	x0 = np.random.uniform(-1, 1, size = matrix.shape[1])
	x1 = matrix @ x0
	
	lambda0, lambda1 = x1[0] / x0[0], None
	num_of_iters = 1
	
	while (lambda1 is None) or (abs(lambda1 - lambda0) > precision and num_of_iters < max_iters):
		x0, x1 = x1, matrix @ x1
		lambda1, lambda0 = lambda0, x1[0] / x0[0]
		num_of_iters += 1
	
	return abs(lambda0), num_of_iters

def scal_method(matrix, precision, max_iters):
	x0 = np.random.uniform(-1, 1, size = matrix.shape[1])
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

m1 = [
	[-5.509882, 1.870086, 0.422908],
	[0.287865, -11.811654, 5.7119],
	[0.049099, 4.308033, -12.970687]
]

m1 = np.asarray(m1)

print(scal_method(m1, 0.01, 5000))
print(scal_method1(m1, 0.01))
