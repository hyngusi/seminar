def read_graph(filename):
    with open(filename, "r") as file:
        first_line = file.readline().strip()
        # Loại bỏ ký tự không mong muốn từ dòng đầu tiên
        first_line = first_line.replace("ï»¿", "")

        num_vertices= int(first_line)
        graph = []

        for _ in range(num_vertices):
            row = list(map(int, file.readline().split()))
            graph.append(row)
        return num_vertices, graph;

def greedy_tsp1(num_vertices, start_vertex, graph):
    start_vertex -= 1
    totalCost = 0
    tour = []
    visited = [False]*num_vertices
    visited[start_vertex] = True
    
    next_vertex = start_vertex
    tour.append(next_vertex+1)
    for j in range(0, num_vertices-1):
        cost = float('inf')
        temp = None
        for i in range(0, num_vertices): #duyệt từ 0->249
            if not visited[i] and graph[next_vertex][i] != 0 and graph[next_vertex][i] < cost:
                cost = graph[next_vertex][i]
                temp = i
        totalCost += cost
        next_vertex = temp
        tour.append(next_vertex+1)
        visited[next_vertex] = True

    totalCost += graph[next_vertex][start_vertex] #trở về đỉnh bắt đầu
    tour.append(start_vertex+1)
    return tour, totalCost;

num_vertices, graph = read_graph("TH4\\tsp2.txt")
tour, totalCost = greedy_tsp1(num_vertices, 366, graph)

for i in range(num_vertices):
    print(f"{tour[i]}->", end='')
print(f"{tour[num_vertices]}")
print("cost: " + str(totalCost))