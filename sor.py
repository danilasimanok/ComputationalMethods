import numpy as np
from random import randint
from utils.feb24.simple_iteration.examples import diagonally_dominant

def max_within_indexes(arr, indexes):
	result, result_index = None, None
	for index in indexes:
		if (result is None) or (abs(result) < abs(arr[index])):
			result = arr[index]
			result_index = index
	return (result, result_index)

def sor_step(x0, left_side, right_side, precision):
	x0 = np.copy(x0)
	indexes = set(range(x0.shape[0]))
	x0_position = 0
	
	while indexes:
		sigma = left_side @ x0 - right_side
		sigma_i, i = max_within_indexes(sigma, indexes)
		x11 = (right_side[i] - left_side[i][1:] @ x0[1:]) / left_side[i][1] # what if x0_position > 1?
		indexes.remove(i)
		x0[x0_position] = x11
		x0_position += 1

m1_lft = np.asarray([[1, 1, 2], [1, 1, 3], [1, 1, 4]])

m1_rght = np.asarray([5, 6, 7])

cmd = "a"
print(m1_lft)
print(m1_rght)
x_prev = np.copy(m1_rght)
while cmd != "e":
	indexes = set(range(m1_rght.shape[0]))
	k = 0
	
	while indexes:
		delta = m1_lft @ x_prev - m1_rght
		print('x_prev = {}'.format(x_prev))
		print('indexes = {}'.format(indexes))
		print('k = {}'.format(k))
		print('delta = {}'.format(delta))
		delta_i, i = max_within_indexes(delta, indexes)
		print('delta_i = {}, i = {}'.format(delta_i, i))
		a_i = m1_lft[i]
		a_ik = m1_lft[i][k]
		
		a1_i = list(np.copy(a_i))
		del a1_i[k]
		x = list(np.copy(x_prev))
		del x[k]
		a1_i = np.copy(a1_i)
		x = np.copy(x)
		
		print('a1_i = {}'.format(a1_i))
		print('x = {}'.format(x))
		
		x_k = (m1_rght[i] - a1_i @ x) / a_ik if a_ik != 0 else 0
		print(x_k)
		x_prev[k] = x_k
		
		k += 1
		indexes.remove(i)
	
	cmd = input()
