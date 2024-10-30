class KNN:
	def __init__(self, k, data):
		self.k = k
		self.data = data

	def dist(self, a, b):
		return abs(a[0] - b[0]) + abs(a[1] - b[1])


	# Returns k nearest data points and their distance to the given point
	# Example: [((2.5, 4.3, -1), 3.251), ((-1.4, 2.8, 1), 4.134)]
	# Here k=2, so there are two tupels returned
	# The first tupel within a tupel is the data point, where the first two elements are to coordinates
	# and the last element is the label. The other number is the distance to the given point.
	def k_nearest(self, point):
		point_dist_tupels = []

		for data_point in self.data:
			point_dist_tupels.append((data_point, self.dist(data_point, point)))

		sorted_point_dist_tupels = sorted(point_dist_tupels, key=lambda x: x[1])
		return sorted_point_dist_tupels[:self.k]


	def guess(self, point):
		nearest_point_dist_tupels = self.k_nearest(point)
		nearest_labels = list(map(lambda x: x[0][2], nearest_point_dist_tupels))
		votes = {}

		for label in nearest_labels:
			if label in votes:
				votes[label] += 1
			else:
				votes[label] = 1

		return max(votes, key=votes.get)

if __name__ == "__main__":
	data = [(1, 1, -1), (1, 7, 1), (3, 3, 1), (5, 4, -1), (2, 5, -1)]
	model = KNN(3, data)
	print(model.k_nearest((3, 6)))
	print(model.guess((3, 6)))