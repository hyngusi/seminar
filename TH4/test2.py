import random

def read_graph(filename):
    with open(filename, "r") as file:

        num_vertices = int(file.readline())
        graph = []
        # graph.append(0)

        for _ in range(num_vertices):
            row = list(map(int, file.readline().split()))
            # row.insert(0, 0)
            graph.append(row)
        return num_vertices, graph;

def write_file(filename):
    with open(filename, 'w') as file:
    # Ghi dữ liệu vào file
        file.write('1.\n')
        file.write('2.\n')
        file.write('3.\n')

def khoiTao(n):
    tour = list(range(1, n+1))
    random.shuffle(tour)
    return tour

def tinhChiPhi(tour):
    cost = 0
    for i in range(num_vertices-1):
        cost += graph[tour[i]-1][tour[i+1]-1]
    cost += graph[tour[-1]-1][tour[0]-1]
    return cost

def c(tour, i, j):
    cost = graph[tour[i]-1][tour[j]-1]
    return cost

def traoDoi(tour, i, j):
    tour[i], tour[j] = tour[j], tour[i]
    return tour

def local_search():
    tour = khoiTao(num_vertices)
    print(tour)

    flag = 0
    improved = True
    while improved:
        if flag == 1000:
            flag = 0
        best = tinhChiPhi(tour) # start with an initial tour
        print(best)
        size = len(tour)
        improved = False

        for i in range(1, size-2):
            for j in range(i+1, size-1):
                gain = c(tour, i-1, i) + c(tour, j, j+1) - c(tour, i-1, j) - c(tour, i, j+1) 

                if gain > 0:                                              
                    flag += 1
                    best -= gain
                    tour = traoDoi(tour, i, j)
                    improved = True
                    break

    return best

num_vertices, graph = read_graph("TH4\\tsp1.txt")
print(local_search())