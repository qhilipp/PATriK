import math

class KMeans:
    def __init__(self, points, centers):
        self.points = points
        self.clusters = []

        for center in centers:
            self.clusters.append([points[center]])

    def centers(self):
        new_centers = []

        for cluster in self.clusters:
            new_centers.append(self.center(cluster))

        return new_centers

    def iterate(self):
        new_centers = self.centers()
        new_clusters = []

        for _ in range(len(self.clusters)):
            new_clusters.append([])

        for point in self.points:
            dists = []

            for center in new_centers:
                dists.append(self.dist(point, center))

            min_dist = dists.index(min(dists))
            new_clusters[min_dist].append(point)

        self.clusters = new_clusters

    def center(self, cluster):
        center = (0.0, 0.0)

        for point in cluster:
            center = (center[0] + point[0], center[1] + point[1])

        return (center[0] / len(cluster), center[1] / len(cluster))

    def print(self, show_ids=True):
        for cluster in self.clusters:
            print(list(map(points.index, cluster)) if show_ids else cluster)

    def print_centers(self, show_ids=True):
        print(list(map(points.index, self.centers())) if show_ids else self.centers())

    def dist(self, p1, p2):
        return math.sqrt(sum((a - b) ** 2 for a, b in zip(p1, p2)))

if __name__ == "__main__":
    points = [(2.0, 10.0), (2.0, 5.0), (8.0, 4.0), (5.0, 8.0), (7.0, 5.0), (6.0, 4.0), (1.0, 2.0), (4.0, 9.0)]
    model = KMeans(points, [0, 3, 6])
    for i in range(5):
        print(i)
        model.iterate()
        model.print()