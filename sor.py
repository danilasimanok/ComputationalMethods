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
		delta = left_side @ x0 - right_side
		delta_i, i = max_within_indexes(delta, indexes)
		x11 = (right_side[i] - left_side[i][1:] @ x0[1:]) / left_side[i][1] # what if x0_position > 1?
		indexes.remove(i)
		x0[x0_position] = x11
		x0_position += 1

m1_lft = np.asarray([[10, 1, 2], [1, 10, 3], [1, 1, 10]])

m1_rght = np.asarray([5, 6, 7])

cmd = "a"
print(m1_lft)
print(m1_rght)
x_prev = np.copy(m1_rght)
while cmd != "e":
	indexes = set(range(m1_rght.shape[0]))
	
	while indexes:
		print('x_prev = {}'.format(x_prev))
		print('indexes = {}'.format(indexes))
		
		delta = m1_lft @ x_prev - m1_rght
		print('delta = {}'.format(delta))
		
		delta_i, i = max_within_indexes(delta, indexes)
		print('delta_i = {}, i = {}'.format(delta_i, i))
		
		a_i = m1_lft[i]
		
		a1_tilda = list(a_i)
		del a1_tilda[i]
		x = list(x_prev)
		del x[i]
		a1_tilda = np.asarray(a1_tilda)
		x = np.asarray(x)
		
		print('a1_tilda = {}'.format(a1_tilda))
		print('x = {}'.format(x))
		
		x_i = (m1_rght[i] - a1_tilda @ x) / a_i[i] if a_i[i] != 0 else 0
		print(x_i)
		x_prev[i] = x_i
		
		indexes.remove(i)
	
	cmd = input()
