import numpy as np
from utils.feb24.qr.examples import examples
from lu_decomposition import print_conds

def qr_decomposition(matrix):
	size = matrix.shape[0]
	q = np.eye(size)
	r = np.copy(matrix)
	for i in range(size):
		for j in range(i + 1, size):
			cos = r[i][i] / (r[i][i] ** 2 + r[j][i] ** 2) ** 0.5
			sin = r[j][i] / (r[i][i] ** 2 + r[j][i] ** 2) ** 0.5
			r_copy = np.copy(r)
			q_copy = np.copy(q)
			for k in range(size):
				r[i][k] = cos * r_copy[i][k] + sin * r_copy[j][k]
				r[j][k] = -sin * r_copy[i][k] + cos * r_copy[j][k]
				q[k][i] = cos * q_copy[k][i] + sin * q_copy[k][j]
				q[k][j] = -sin * q_copy[k][i] + cos * q_copy[k][j]
	return (q, r)

def decompose_one(matrix):
	print('==== QR DECOMPOSITION ====')
	print('Original matrix (A)')
	print(matrix)
	print_conds('A', matrix)
	(q, r) = qr_decomposition(matrix)
	print('Q = {}'.format(q))
	print_conds('Q', q)
	print('R = {}'.format(r))
	print_conds('R', r)
	print()

if __name__ == '__main__':
	#examples = map(lambda system: system.left_side, examples)
	list(map(decompose_one, examples))
