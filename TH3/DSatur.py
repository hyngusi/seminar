def read_graph(filename):
    with open (filename, "r") as file:
        num_vertices = int(file.readline())
        graph = []

        for _ in range(num_vertices):
            row = list(map(int , file.readline().split()))
            graph.append(row)
    return num_vertices, graph

def DSatur(num_vertices, graph):
    # danh sách các đỉnh kề đỉnh thứ i
    list_neighbors = []
    for i in range(num_vertices):
        col = []
        for j in range(num_vertices):
            if graph[i][j] != 0:
                col.append(j)
        list_neighbors.append(col)

    # bậc của mỗi đỉnh
    degree_each_vertex = [0]*num_vertices
    for i in range(num_vertices):
        degree_each_vertex[i] = len(list_neighbors[i])

    list_can_colored = [0]*num_vertices
    for i in range(num_vertices):
        list_can_colored[i] = [i for i in range(1, num_vertices+1)]
    
    painted = [-1]*num_vertices
    while(max(degree_each_vertex) != 0):
        max_degree = max(degree_each_vertex)
        max_degree_index = degree_each_vertex.index(max_degree)
        degree_each_vertex[max_degree_index] = 0

        #màu nhỏ nhất trong danh sách màu có thể tô
        pain = min(list_can_colored[max_degree_index]) 

        # ngăn cấm tô màu cho các đỉnh kề 
        temp = list_neighbors[max_degree_index]
        for i in temp:
            if pain in list_can_colored[i]:
                list_can_colored[i].remove(pain)

        # tô màu đỉnh i0
        painted[max_degree_index] = pain

        #  bậc đỉnh kề giảm 1 đơn vị
        for i in list_neighbors[max_degree_index]:
            degree_each_vertex[i] -= 1

    for i in range(len(painted)):
        if painted[i] == -1:
            painted[i] = min(list_can_colored[i])

    # print(list_can_colored)
    return painted, max(painted)

num_vertices, graph = read_graph("TH3\color3.txt")
list_color, color = DSatur(num_vertices, graph)
print(list_color)
print(f"Số màu: {color}")