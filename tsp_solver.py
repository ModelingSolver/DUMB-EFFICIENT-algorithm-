import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.metrics.pairwise import euclidean_distances
from scipy.spatial import distance

print("Welcome to the Dumb-Efficient TSP Solver!")
print("This program uses a simple algorithm to find a solution to the Traveling Salesman Problem.")

def get_user_input():
    while True:
        try:
            num_cities = int(input("Enter the number of cities: "))
            if num_cities <= 0:
                print("Please enter a positive integer.")
            else:
                break
        except ValueError:
            print("Please enter a valid integer.")

    while True:
        try:
            eps = float(input("Enter the epsilon value (eps): "))
            if eps <= 0:
                print("Please enter a positive value.")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")

    while True:
        try:
            min_samples = int(input("Enter the minimum number of samples (min_samples): "))
            if min_samples <= 0:
                print("Please enter a positive integer.")
            else:
                break
        except ValueError:
            print("Please enter a valid integer.")

    while True:
        try:
            max_cluster_size = int(input("Enter the maximum cluster size (max_cluster_size): "))
            if max_cluster_size <= 0:
                print("Please enter a positive integer.")
            else:
                break
        except ValueError:
            print("Please enter a valid integer.")

    return num_cities, eps, min_samples, max_cluster_size

def cluster(cities, eps, min_samples, max_cluster_size):
    db = DBSCAN(eps=eps, min_samples=min_samples).fit(cities)
    labels = db.labels_
    clusters = []
    for label in np.unique(labels):
        if label != -1:
            cluster_cities = cities[labels == label]
            if len(cluster_cities) > max_cluster_size:
                sub_clusters = cluster(cluster_cities, eps / 2, min_samples, max_cluster_size)
                clusters.extend(sub_clusters)
            else:
                clusters.append(cluster_cities)
    return clusters

def calculate_medoids(clusters):
    medoids = []
    for cluster_cities in clusters:
        medoid = np.argmin(np.sum(euclidean_distances(cluster_cities, cluster_cities), axis=0))
        medoids.append(cluster_cities[medoid])
    return medoids

def calculate_distance(road):
    total_distance = sum(distance.euclidean(road[i], road[i + 1]) for i in range(len(road) - 1))
    return total_distance

def dumb_efficient(cities, eps, min_samples, max_cluster_size):
    clusters = cluster(cities, eps, min_samples, max_cluster_size)
    medoids = calculate_medoids(clusters)
    road = []
    current_city = medoids[0]
    road.append(current_city)
    medoids.remove(current_city)
    while medoids:
        next_city = min(medoids, key=lambda city: distance.euclidean(current_city, city))
        road.append(next_city)
        medoids.remove(next_city)
        current_city = next_city
    total_distance = calculate_distance(road)
    return road, total_distance

if __name__ == "__main__":
    num_cities, eps, min_samples, max_cluster_size = get_user_input()
    cities = np.random.rand(num_cities, 2)  
    road, total_distance = dumb_efficient(cities, eps, min_samples, max_cluster_size)
    print("Road:", road)
    print("Total distance:", total_distance)
```
