import numpy as np
import random

def generate_initial_solution(num_cities):
    # Tạo một giải pháp ngẫu nhiên
    return random.sample(range(num_cities), num_cities)

def calculate_total_distance(tour, distance_matrix):
    # Tính tổng khoảng cách của tour
    total_distance = np.sum([distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1)])
    total_distance += distance_matrix[tour[-1]][tour[0]]  # Quay lại thành phố xuất phát
    return total_distance

def read_graph(filename):
    with open(filename, "r") as file:
        num_vertices = int(file.readline())
        graph = [list(map(int, file.readline().split())) for _ in range(num_vertices)]
        return np.array(graph)

def generate_neighbors(current_tour):
    # Tạo một số giải pháp hàng xóm ngẫu nhiên
    neighbors = []
    num_cities = len(current_tour)
    num_neighbors = min(5000, num_cities*(num_cities-1)//2)  # Giả sử chỉ tạo 5 giải pháp hàng xóm
    for _ in range(num_neighbors):
        i, j = random.sample(range(num_cities), 2)
        neighbor = current_tour.copy()
        neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
        neighbors.append(neighbor)
    return neighbors

def hill_climbing_tsp(num_cities, distance_matrix, max_iterations):
    current_tour = generate_initial_solution(num_cities)

    for _ in range(max_iterations):
        neighbors_of_current = generate_neighbors(current_tour)
        best_neighbor = min(neighbors_of_current, key=lambda tour: calculate_total_distance(tour, distance_matrix))

        if calculate_total_distance(best_neighbor, distance_matrix) >= calculate_total_distance(current_tour, distance_matrix):
            break  # Nếu không còn cải thiện được nữa, thoát khỏi vòng lặp
        else:
            current_tour = best_neighbor

    return current_tour

# Ví dụ sử dụng
num_cities = 250
distance_matrix = read_graph("TH4\\tsp1.txt")

max_iterations = 1000
# final_tour = hill_climbing_tsp(num_cities, distance_matrix, max_iterations)

# print("Final Tour:", final_tour)
# print("Total Distance:", calculate_total_distance(final_tour, distance_matrix))

final_tour = []
for i in range(1):
    print(i)
    final_tour.append(hill_climbing_tsp(num_cities, distance_matrix, max_iterations))

# print("Final Tour:", final_tour)
cost = float('inf')
for i in range(1):
    temp = calculate_total_distance(final_tour[i], distance_matrix)
    if cost > temp:
        cost = temp
print("Total Distance:", cost)
