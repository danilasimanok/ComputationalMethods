from random import uniform

dist1 = lambda x, y: max(abs(x[0] - y[0]), abs(x[1] - y[1]))
dist2 = lambda x, y: abs(x[0] - y[0]) + (x[1] - y[1]) ** 2
dists = [dist1, dist2]

centers1 = [(0, 0), (10, 0), (0, 10), (10, 10)]
centers2 = [(0, 5), (5, 0), (5, 10), (10, 5)]
centers = [centers1, centers2]

def random_points(count):
	return [(uniform(0, 10), uniform(0, 10)) for _ in range(count)]
