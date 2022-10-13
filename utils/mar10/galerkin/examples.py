from math import exp, sin, log

funs = [
	[
		lambda x: -(4 - x) / (5 - 2 * x),
		lambda x: (1 - x) / 2,
		lambda x: 0.5 * log(x + 3),
		lambda x: 1 + x / 3
	],
	[
		lambda x: (x - 2) / (x + 2),
		lambda x: x,
		lambda x: 1 - sin(x),
		lambda x: x ** 2
	],
	[
		lambda x: -(7 - x) / (8 + 3 * x),
		lambda x: (1 + x / 3),
		lambda x: (1 - exp(x / 2) / 2),
		lambda x: 1 / 2 - x / 3
	]
]

segment = [-1, 1]

N_h_pairs = [(3, 0.05), (11, 0.01)]
