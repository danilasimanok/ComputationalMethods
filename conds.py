import numpy as np
from numpy.linalg import inv, norm, det, solve
from functools import reduce as fold
from operator import mul
from utils.feb17.examples import examples

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

def solve_one(lin_sys):
	print('======')
	left_side = lin_sys.left_side
	right_side = lin_sys.right_side
	
	# print system and conds
	print('Solve system Ax = b')
	print('A =', left_side)
	print('b =', right_side)
	print('cond_s =', cond_s(left_side))
	print('cond_v =', cond_v(left_side))
	print('cond_a =', cond_a(left_side))
	
	# solve original system
	solution = solve(left_side, right_side)
	solution_norm = norm(solution)
	print('x =', solution)
	
	cmd = 'n'
	while cmd != 'y':
		precision_left = int(input('Input precision for left side: '))
		precision_right = int(input('Input precision for right side: '))
		
		# vary system and solve it
		left_side_varied = left_side.round(precision_left)
		rigth_side_varied = right_side.round(precision_right)
		left_varied_solution = solve(left_side_varied, right_side)
		right_varied_solution = solve(left_side, rigth_side_varied)
		
		# print results
		left_abs = norm(solution - left_varied_solution)
		left_delta = left_abs / solution_norm
		right_abs = norm(solution - right_varied_solution)
		right_delta = right_abs / solution_norm
		print("(lft) x' =", left_varied_solution, "\t|x - x'| =", left_abs, "\t|x - x'| / |x| =", left_delta)
		print("(rght) x'' =", right_varied_solution, "\t|x - x''| =", right_abs, "\t|x - x'| / |x| =", right_delta)
		print()
		
		cmd = input('Proceed? (y/n) ')
		print()

if __name__ == '__main__':
	list(map(solve_one, examples))
