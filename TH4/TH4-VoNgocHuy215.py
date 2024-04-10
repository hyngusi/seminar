import numpy as np
import random2

class RouteFinder:
    def __init__(self, distance_matrix, cities_names, iterations=5):
        self.distance_matrix = distance_matrix
        self.iterations = iterations
        self.cities_names = cities_names

    def solve(self):
        iteration = 0
        best_distance = 0
        best_route = []

        while iteration < self.iterations:
            num_cities = len(self.distance_matrix)
            initial_route = random2.sample(range(0, num_cities), num_cities)
            tsp = Solver(self.distance_matrix, initial_route)
            new_route, new_distance= tsp.two_opt()

            if iteration == 0:
                best_distance = new_distance
                best_route = new_route
            else:
                pass

            if new_distance < best_distance:
                best_distance = new_distance
                best_route = new_route

            iteration += 1

        if self.cities_names:
            best_route = [self.cities_names[i] for i in best_route]
            return best_distance, best_route
        else:
            return best_distance, best_route


class Solver:
    def __init__(self, distance_matrix, initial_route):
        self.distance_matrix = distance_matrix
        self.num_cities = len(self.distance_matrix)
        self.initial_route = initial_route
        self.best_route = []
        self.best_distance = 0

    def update(self, new_route, new_distance):
        self.best_distance = new_distance
        self.best_route = new_route
        return self.best_distance, self.best_route

    def two_opt(self, improvement_threshold=0.01):
        self.best_route = self.initial_route
        self.best_distance = self.calculate_path_dist(self.distance_matrix, self.best_route)
        improvement_factor = 1
        
        while improvement_factor > improvement_threshold:
            previous_best = self.best_distance
            for swap_first in range(1, self.num_cities - 2):
                for swap_last in range(swap_first + 1, self.num_cities - 1):
                    before_start = self.best_route[swap_first - 1]
                    start = self.best_route[swap_first]
                    end = self.best_route[swap_last]
                    after_end = self.best_route[swap_last+1]
                    before = self.distance_matrix[before_start][start] + self.distance_matrix[end][after_end]
                    after = self.distance_matrix[before_start][end] + self.distance_matrix[start][after_end]
                    if after < before:
                        new_route = self.swap(self.best_route, swap_first, swap_last)
                        new_distance = self.calculate_path_dist(self.distance_matrix, new_route)
                        self.update(new_route, new_distance)

            improvement_factor = 1 - self.best_distance/previous_best
        return self.best_route, self.best_distance

    @staticmethod
    def calculate_path_dist(distance_matrix, path):
        path_distance = 0
        for ind in range(len(path) - 1):
            path_distance += distance_matrix[path[ind]][path[ind + 1]]
        path_distance += distance_matrix[path[-1]][path[0]]
        return path_distance

    @staticmethod
    def swap(path, swap_first, swap_last):
        path_updated = np.concatenate((path[0:swap_first],
                                       path[swap_last:-len(path) + swap_first - 1:-1],
                                       path[swap_last + 1:len(path)]))
        return path_updated.tolist()
    
def read_graph(filename):
    with open(filename, "r") as file:

        num_vertices = int(file.readline())
        graph = []

        for _ in range(num_vertices):
            row = list(map(int, file.readline().split()))
            graph.append(row)
        return num_vertices, graph;
    
num_vertices, graph = read_graph("TH4\\tsp4.txt")
route = [i for i in range(1,num_vertices+1)]

route_finder = RouteFinder(graph, route, iterations=5)
best_distance, best_route = route_finder.solve()

print(f"Cost: {best_distance}")
for i in range(num_vertices):
    print(f"{best_route[i]}", end=" ")