def read_graph(filename):
    with open(filename, "r") as file:
        first_line = file.readline().strip()
        # Loại bỏ ký tự không mong muốn từ dòng đầu tiên
        first_line = first_line.replace("ï»¿", "")

        num_vertices, vertexs = map(int, first_line.split())
        list_vertices = list(map(int, file.readline().split()))
        graph = []

        for _ in range(num_vertices):
            row = list(map(int, file.readline().split()))
            graph.append(row)
        return num_vertices,vertexs, list_vertices, graph;

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

def greedy_tsp2(num_vertices,vertexs, list_vertices, graph):
    best_cost = float('inf')
    best_tour = None

    # temp_cost = temp_tour = None
    for i in range(vertexs):
        temp_tour, temp_cost = greedy_tsp1(num_vertices, list_vertices[i], graph)
        if temp_cost < best_cost:
            best_cost = temp_cost
            best_tour = temp_tour

    for i in range(num_vertices):
        print(f"{best_tour[i]}->", end='')
    print(f"{best_tour[num_vertices]}")
    print("Chi phí đường đi ngắn nhất: " + str(best_cost))
    return

num_vertices,vertexs, list_vertices, graph = read_graph("TH3\GTS2c.txt")
greedy_tsp2(num_vertices,vertexs, list_vertices, graph)