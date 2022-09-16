import numpy as np
from conds import cond_s, cond_v, cond_a
from utils.feb24.regularisation.examples import hilbert_lft, ones, rght_ones, random_solution, random_rght
from utils.linear import LinearSystem
from numpy.linalg import solve, norm

format_str = "'a = {}\ncond_s(H + 'aE) = {}\ncond_v(H + 'aE) = {}\ncond_a(H + 'aE) = {}\n|x' - x_0| = {}\n|x'' - x_1| = {}\n///"

if __name__ == '__main__':
	alphas = [ 10 ** x for x in range(-12, -1) ]
	identity_matrix = np.eye(20)
	
	print('Regularisation of Hx = b')
	print('cond_s(H) = {}, cond_v(H) = {}, cond_a(H) = {}'.format(cond_s(hilbert_lft), cond_v(hilbert_lft), cond_a(hilbert_lft)))
	print('======')
	
	print('x_0 = {}'.format(ones))
	print('x_1 = {}'.format(random_solution))
	print('======')
	
	print("(H - 'aE)x = b_0 and (H - 'aE)x = b_1 investigation")
	results = []
	for alpha in alphas:
		corrected_left = np.add(hilbert_lft, alpha * identity_matrix)
		
		solution1 = solve(corrected_left, rght_ones)
		error1 = norm(solution1 - ones)
		
		solution2 = solve(corrected_left, random_rght)
		error2 = norm(solution2 - random_solution)
		
		results.append((alpha, error1, error2))
		
		print(format_str.format(alpha, cond_s(corrected_left), cond_v(corrected_left), cond_a(corrected_left), error1, error2))
	
	print('======')
	
	best_alpha1 = min(results, key = lambda triple: triple[1])[0]
	print('Best alpha for first system: {}'.format(best_alpha1))
	
	best_alpha2 = min(results, key = lambda triple: triple[2])[0]
	print('Best alpha for second system: {}'.format(best_alpha2))
