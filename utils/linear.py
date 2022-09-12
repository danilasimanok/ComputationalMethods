import numpy as np

class LinearSystem:
	def __init__(self, left_side, right_side):
		self.left_side = left_side
		self.right_side = right_side

def hilbert_left_side(n):
	x = np.arange(1, n + 1) + np.arange(0, n)[:, np.newaxis]
	return 1.0 / x
