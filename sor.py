import numpy as np

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
