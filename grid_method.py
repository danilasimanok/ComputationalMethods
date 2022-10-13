from numpy.linalg import solve
import matplotlib.pyplot  as plt
from utils.mar10.grid.examples import examples

def segments(a, b, h):
	n = int((b - a) / h)
	return [a + h * k for k in range(n)] + [b]

def create_left_side(qs, rs, h):
	size = len(qs)
	line = [0] * size
	line[0] = 1
	result = [line]
	
	for i in range(1, size - 1):
		line = [0] * size
		line[i - 1] = 1 / h ** 2 - qs[i] / (2 * h)
		line[i] = - (2 / h ** 2 + rs[i])
		line[i + 1] = 1 / h ** 2 + qs[i] / (2 * h)
		result.append(line)
	
	line = [0] * size
	line[size - 1] = 1
	result.append(line)
	
	return result

def solve_difequ(q, r, f, h, a, b, alpha, betta):
	grid = segments(a, b, h)
	qs = list(map(q, grid))
	rs = list(map(r, grid))
	fs = list(map(f, grid))
	
	left_side = create_left_side(qs, rs, h)
	right_side = [alpha] + fs[1:-1] + [betta]
	
	return solve(left_side, right_side)

def compute_error(solution0, solution1):
	norm = abs(solution0[-1] - solution1[-1])
	for i in range(len(solution1) - 1):
		if i % 2 == 0:
			norm = max(norm, abs(solution0[i // 2] - solution1[i]))
		else:
			prev = i // 2
			avg = (solution0[prev] + solution0[prev + 1]) / 2
			norm = max(norm, abs(avg - solution1[i]))
	return norm / 3

def solve_with_precision(q, r, f, a, b, alpha, betta):
	h = 0.05
	solution0 = solve_difequ(q, r, f, 0.1, a, b, alpha, betta)
	solution1 = solve_difequ(q, r, f, 0.05, a, b, alpha, betta)
	
	result = [solution0, solution1]
	
	while h > 0.000390625:
		h /= 2
		solution0 = solution1
		solution1 = solve_difequ(q, r, f, h, a, b, alpha, betta)
		result.append(solution1)
	
	return result

def show_one(q, r, f):
	a, b = -1, 1
	alpha, betta = 0, 0
	
	solutions = solve_with_precision(q, r, f, a, b, alpha, betta)
	n_err_s = map(lambda sol_pair: (len(sol_pair[0]), compute_error(sol_pair[0], sol_pair[1])), zip(solutions[:-1], solutions[1:]))
	
	_, axes = plt.subplots(1, 2, figsize=(20, 4))
	
	ns, errors = [], []
	for n, error in n_err_s:
		ns.append(n)
		errors.append(error)
	
	axes[0].plot(ns, errors, marker='.', color='blue', mec='black', ms=8)
	axes[0].set_title("||delta|| (n)")
	
	grid = segments(a, b, 0.000390625)
	axes[1].plot(grid, solutions[-1], marker='.', color='blue', mec='black', ms=8)
	axes[1].set_title("u(x)")
	
	plt.show()

if __name__ == '__main__':
	for q, r, f in examples:
		show_one(q, r, f)
