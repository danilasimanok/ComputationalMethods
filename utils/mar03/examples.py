from ..linear import hilbert_left_side
import numpy as np

m1 = [
	[-5.509882, 1.870086, 0.422908],
	[0.287865, -11.811654, 5.7119],
	[0.049099, 4.308033, -12.970687]
]

m2 = [
	[4.2, -3.4, 0.3],
	[4.7, -3.9, 0.3],
	[-5.6, 5.2, 0.1]
]

examples = map(np.asarray, [m1, m2, hilbert_left_side(3), hilbert_left_side(4)])
