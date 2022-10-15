from math import pi, sin as g

dens1 = lambda _: 2 / pi
sup1 = 2 / pi
p_ksi1 = 'p_ksi(x) = 2 / pi'
dens2 = lambda x: 8 * x / pi ** 2
sup2 = 4 / pi
p_ksi2 = 'p_ksi(x) = 8x / pi^2'

denss = [(dens1, sup1, p_ksi1), (dens2, sup2, p_ksi2)]

ns = [100, 1000, 10000]

true_integral = 1.0
a, b = 0, pi / 2

sup = 1.0
