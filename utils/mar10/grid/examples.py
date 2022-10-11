from math import exp, sin, log

examples = [
	(
		lambda x: (3 - x) * (x + 2) / 2,
		lambda x: (x - 3) * exp(x / 2),
		lambda x: (3 - x) * (2 - x)
	),
	(
		lambda x: x * (x + 2) / (x - 2),
		lambda x: (sin(x) - 1) * (x + 2) / (x - 2),
		lambda x: x ** 2 * (x + 2) / (x - 2)
	),
	(
		lambda x: (x - 1) * (2 * x - 5) / (2 * (x - 4)),
		lambda x: log(3 + x) * (2 * x - 5) / (2 * (x - 4)),
		lambda x: (x + 3) * (2 * x - 5) / (3 * (4 - x))
	),
	(
		lambda x: log(10 * (x + 2)) * (3 - x) / 2,
		lambda x: (3 - x) * exp(x / 2),
		lambda x: (x - 2) * sin(x - 3)
	)
]
