import numpy as np
import matplotlib.pyplot as plt
from scipy.special import eval_jacobi
from scipy.misc import derivative
from scipy.integrate import quad
from numpy.linalg import solve
from utils.mar10.galerkin.examples import funs, segment, N_h_pairs

def jacobi(n):
	return lambda t: (1 - t ** 2) * eval_jacobi(n, 1, 1, t)

def jacobi_der1(n): # jacobi'
	return lambda t: derivative(jacobi(n), t)

def jacobi_der2(n): # jacobi''
	return lambda t: derivative(jacobi_der1(n), t)

def A_i(funs, phi, dphi, ddphi, i):
	k, p, q, f = funs
	return lambda x: k(x) * ddphi[i](x) + p(x) * dphi[i](x) + q(x) * phi[i](x)

def galerkin_method(segment, funs, N):
	a, b = segment
	k, p, q, f = funs
	phi = [jacobi(i) for i in range(N)]
	dphi = [jacobi_der1(i) for i in range(N)]
	ddphi = [jacobi_der2(i) for i in range(N)]
	A = np.array([A_i(funs, phi, dphi, ddphi, i) for i in range(N)])
	C = np.array([quad(lambda t: f(t) * phi[i](t), a, b)[0] for i in range(N)])
	B = np.zeros([N, N])
	for i in range(N):
		for j in range(N):
			B[i, j] = quad(lambda t: phi[i](t) * A[j](t), a, b)[0]
	alpha = solve(B, C)
	return lambda t: sum([alpha[i] * phi[i](t) for i in range(N)])

if __name__ == '__main__':
	_, axes = plt.subplots(3, 2, figsize = (20, 15))
	for i in range(3):
		for j in range(2):
			N, h = N_h_pairs[j]
			u = galerkin_method(segment, funs[i], N)
			a, b = segment
			n = round((b - a) / h)
			x = np.zeros(n + 1)
			y = np.zeros(n + 1)
			for t in range(n + 1):
				x[t] = a + t * h
				y[t] = u(x[t])
			axes[i,j].plot(x, y, marker = '.', color = 'red', mec = 'black', ms = 10)
			axes[i,j].set_title("N = {}".format(N - 1))
	plt.show()
