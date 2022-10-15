import numpy as np
import matplotlib.pyplot as plt
import sympy as sym
from utils.mar24.examples import *

def grid(a, T, N, M):
	h, tau = a / N , T / M
	x_p = np.array([i * h for i in range(N + 1)])
	t_p = np.array([i * tau for i in range(N + 1)])
	return x_p, t_p

def equation_by_solution(u, a, x, t, kappa):
	f = sym.diff(u, t, 1) - kappa * sym.diff(u, x, 2)
	mu = u.subs(t, 0)
	mu_1 = u.subs(x, 0)
	mu_2 = u.subs(x, a)
	return f, mu, mu_1, mu_2

def explicit_scheme(a, T, kappa, N, M, x, t, f, mu, mu_1, mu_2):
	x_p, t_p = grid(a, T, N, M)
	u_p = np.zeros([N + 1, M + 1], dtype = float)
	h, tau = a / N, T / M
	for k in range(1, M + 1):
		for i in range(0, N + 1):
			u_p[i, 0] = mu.subs(x, x_p[i])
		for i in range(1, N):
			u_p[i, k] = tau * kappa * (u_p[i + 1 , k - 1] - 2 * u_p[i, k - 1] + u_p[i - 1, k - 1]) / (h ** 2) + tau * f.subs([(x, x_p[i]), (t, t_p[k - 1])]) + u_p[i, k - 1]
		u_p[0, k] = mu_1.subs(t, t_p[k])
		u_p[N, k] = mu_2.subs(t, t_p[k])
	X, T = np.meshgrid(x_p, t_p, indexing = 'ij')
	return X, T, u_p

def implicit_scheme(a, T, kappa, N, M, x, t, f, mu, mu_1, mu_2):
	x_p, t_p = grid(a, T, N, M)
	u_p = np.zeros((N + 1, M + 1), dtype = float)
	A, C = [np.zeros(N + 1, dtype = float) for _ in range(2)]
	B = np.ones(N + 1,dtype = float)
	D = np.zeros(N + 1, dtype = sym.Symbol)
	h, tau = a / N, T / M
	for k in range(1, M + 1):
		D[0] = mu_1.subs(t, t_p[k])
		D[N] = mu_2.subs(t, t_p[k])
		for i in range(0, N + 1):
			u_p[i, 0] = mu.subs(x, x_p[i])
		for i in range(1, N):
			A[i] = kappa / h ** 2
			B[i] = -2 * kappa / h ** 2 - 1 / tau
			C[i] = kappa / h**2
			D[i] = -u_p[i, k - 1] / tau - f.subs([(x, x_p[i]), (t, t_p[k])])
		s = np.zeros(N + 1, dtype = float)
		t1 = np.zeros(N + 1, dtype = float)
		s[0] = -C[0] / B[0]
		t1[0] = D[0] / B[0]
		for i in range(1, N + 1):
			s[i] = -C[i] / (A[i] * s[i - 1] + B[i])
			t1[i] = (D[i] - A[i] * t1[i - 1]) / (A[i] * s[i - 1] + B[i])
		u_p[N, k] = t1[N]
		for i in range(N - 1, -1, -1):
			u_p[i, k] = s[i] * u_p[i + 1, k] + t1[i]
	X, T = np.meshgrid(x_p, t_p, indexing = 'ij')
	return X, T, u_p

def process_one(fun, a, T, N, M, x, t):
	fig = plt.figure()
	fig.set_size_inches(20, 10)
	
	ax1 = fig.add_subplot(131, projection = '3d')
	title1 = 'Explicit scheme, kappa = 0.001, '
	
	ax2 = fig.add_subplot(132, projection = '3d')
	title2 = 'Implicit scheme, kappa = 0.001'
	
	ax3 = fig.add_subplot(133, projection = '3d')
	title3 = 'Explicit scheme, kappa = 0.1, '

	kappa = 0.001
	f, mu, mu_1, mu_2 = equation_by_solution(fun, a, x, t, kappa)
	h, tau = a / N, T / M
	stability = 'stable' if 2 * kappa * tau <= h ** 2 else 'unstable'

	x_coord, t_coord, res = explicit_scheme(a, T, kappa, N, M, x, t, f, mu, mu_1, mu_2)
	ax1.set_title(title1 + stability)
	ax1.plot_wireframe(x_coord, t_coord, res)

	x_coord, t_coord, res = implicit_scheme(a, T, kappa, N, M, x, t, f, mu, mu_1, mu_2)
	ax2.set_title(title2)
	ax2.plot_wireframe(x_coord, t_coord, res)

	kappa = 0.1
	h, tau = a / N, T / M
	stability = 'stable' if 2 * kappa * tau <= h ** 2 else 'unstable'
	
	x_coord, t_coord, res = explicit_scheme(a, T, kappa, N, M, x, t, f, mu, mu_1, mu_2)
	ax3.set_title(title3 + stability)
	ax3.plot_wireframe(x_coord, t_coord, res)

	plt.show()

process_fun = lambda fun: process_one(fun, a, T, N, M, x, t)

if __name__ == '__main__':
	list(map(process_fun, solutions))
