import numpy as np
from numpy.linalg import inv, norm, det, solve
from functools import reduce as fold
from operator import mul
import sys

def cond_s(matrix):
	inverted = inv(matrix)
	return norm(matrix) * norm(inverted)

def cond_v(matrix):
	numerator = fold(lambda acc, vec: acc * norm(vec), matrix, 1)
	denominator = abs(det(matrix))
	return numerator / denominator

def cond_a(matrix):
	inverted = inv(matrix).transpose()
	matrix_norms = map(norm, matrix)
	inverted_norms = map(norm, inverted)
	return max(map(mul, matrix_norms, inverted_norms))

if __name__ == '__main__':
	# define program parameters
	left_side_filename = sys.argv[1]
	right_side_filename = 'rside_' + left_side_filename
	precision_left = int(sys.argv[2])
	precision_right = int(sys.argv[3])
	
	# read system to solve
	left_side = np.loadtxt(left_side_filename)
	right_side = np.loadtxt(right_side_filename)
	
	# vary system
	left_side_varied = left_side.round(precision_left)
	rigth_side_varied = right_side.round(precision_right)
	
	# print system and conds
	print('Solve system Ax = b')
	print('A =', left_side)
	print('b =', right_side)
	print('cond_s =', cond_s(left_side))
	print('cond_v =', cond_v(left_side))
	print('cond_a =', cond_a(left_side))
	
	# solve original and varied systems
	solution = solve(left_side, right_side)
	left_varied_solution = solve(left_side_varied, right_side)
	right_varied_solution = solve(left_side, rigth_side_varied)
	print('x =', solution)
	print("(lft) x' =", left_varied_solution, "\t|x - x'| =", norm(solution - left_varied_solution))
	print("(rght) x'' =", right_varied_solution, "\t|x - x''| =", norm(solution - right_varied_solution))
