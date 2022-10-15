from random import uniform
from utils.apr07.examples import denss, ns, true_integral, a, b, sup, g

def random_value(density, sup, a, b):
	while True:
		eta1 = a + (b - a) * uniform(0, 1)
		eta2 = sup * uniform(0, 1)
		if eta2 <= density(eta1):
			return eta1

def integrate_mk(rnd_density, d_sup, n, g, a, b):
	ksis = [random_value(rnd_density, d_sup, a, b) for _ in range(n)]
	addendum = lambda ksi: g(ksi) / rnd_density(ksi)
	return sum(map(addendum, ksis)) / n

def classical_monte_karlo(sup, n, g, a, b):
	points = [(uniform(a, b), uniform(0, sup)) for _ in range(n)]
	is_under_graph = lambda point: point[1] <= g(point[0])
	points_under_graph = list(filter(is_under_graph, points))
	rect_area = (b - a) * sup
	return len(points_under_graph) * rect_area / n

def print_integration_results(denss, ns, a, b, g, sup, true_integral):
	print('Integrate sin(x)dx from 0 to pi / 2')
	
	for dens, dsup, p_ksi in denss:
		print(p_ksi)
		for n in ns:
			i_mk = integrate_mk(dens, dsup, n, g, a, b)
			i_cl = classical_monte_karlo(sup, n, g, a, b)
			print('n = {}\t|I_mk - I| = {}\t|I_cl - I| = {}'.format(n, abs(true_integral - i_mk), abs(true_integral - i_cl)))

if __name__ == '__main__':
	print_integration_results(denss, ns, a, b, g, sup, true_integral)
