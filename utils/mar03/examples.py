import numpy as np
from ..linear import hilbert_left_side

m1 = np.asarray([
	[-5.509882, 1.870086, 0.422908],
	[0.287865, -11.811654, 5.7119],
	[0.049099, 4.308033, -12.970687]
])

examples = [m1, *[hilbert_left_side(n) for n in range(3,6)], hilbert_left_side(20)]
