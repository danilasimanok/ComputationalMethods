from random import uniform
import matplotlib.pyplot as plt

def clutser_of_point(distances):
	distances = list(distances)
	min_distance = min(distances)
	return distances.index(min_distance)

def compute_distances(point, distance, centers):
	dist = lambda x: distance(x, point)
	return map(dist, centers)

def define_clusters(points, centers, distance):
	clusters = {}
	for point in points:
		distances = compute_distances(point, distance, centers)
		clusters[point] = clutser_of_point(distances)
	return clusters

def clusters_to_lists(clusters, cluster_count):
	result = [[] for _ in range(cluster_count)]
	for point in clusters:
		cluster_n = clusters[point]
		result[cluster_n].append(point)
	return result

def define_center(cluster):
	n = len(cluster)
	x, y = 0, 0
	for x1, y1 in cluster:
		x += x1
		y += y1
	return (x / n, y / n)

def clusterize(points, centers, distance):
	cluster_count = len(centers)
	clusters0 = define_clusters(points, centers, distance)
	
	clusters_list = clusters_to_lists(clusters0, cluster_count)
	centers = list(map(define_center, clusters_list))
	clusters1 = define_clusters(points, centers, distance)
	
	iters = 1
	while clusters1 != clusters0:
		clusters0 = clusters1
		clusters_list = clusters_to_lists(clusters0, cluster_count)
		centers = list(map(define_center, clusters_list))
		clusters1 = define_clusters(points, centers, distance)
		iters += 1
	
	return clusters0, iters, centers

dist1 = lambda x, y: max(abs(x[0] - y[0]), abs(x[1] - y[1]))
dist2 = lambda x, y: abs(x[0] - y[0]) + (x[1] - y[1]) ** 2
dists = [dist1, dist2]

centers1 = [(0, 0), (10, 0), (0, 10), (10, 10)]
centers2 = [(0, 5), (5, 0), (5, 10), (10, 5)]
centers = [centers1, centers2]

def random_points(count):
	return [(uniform(0, 10), uniform(0, 10)) for _ in range(count)]

def draw_points(plt, marker, color, points):
	xs, ys = [], []
	for x, y in points:
		xs.append(x)
		ys.append(y)
	plt.scatter(xs, ys, marker = marker, color = color)

def draw_one(centers, dist, points, plt):
	clusters, iters, centers = clusterize(points, centers, dist)
	red, green, blue, yellow = clusters_to_lists(clusters, 4)
	
	plt.set_title('iters = {}'.format(iters))
	
	draw_points(plt, 'o', 'r', red)
	draw_points(plt, 'o', 'g', green)
	draw_points(plt, 'o', 'b', blue)
	draw_points(plt, 'o', 'y', yellow)
	draw_points(plt, 'D', 'k', centers)

if __name__ == '__main__':
	points = random_points(1000)
	
	_, axes = plt.subplots(2, 2)
	
	for i in range(2):
		for j in range(2):
			draw_one(centers[i], dists[j], points, axes[i][j])
	
	plt.show()
