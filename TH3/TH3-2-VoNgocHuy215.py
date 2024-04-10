def read_graph(filename):
    with open (filename, "r") as file:
        num_vertices = int(file.readline())
        graph = []

        for _ in range(num_vertices):
            row = list(map(int , file.readline().split()))
            graph.append(row)
    return num_vertices, graph

def Welsh_Powell(num_vertices, graph):
    # danh sách các đỉnh kề
    list_neighbors = []
    for i in range(num_vertices):
        col = []
        for j in range(num_vertices):
            if graph[i][j] != 0:
                col.append(j)
        list_neighbors.append(col)
    
    # for i in range(num_vertices):
    #     print(f"Danh sách đỉnh kề đỉnh {i}: {list_neighbors[i]}")
    # print("")

    # sắp xếp theo bậc
    for i in range(num_vertices):
        list_neighbors[i].append(i)
    sorted_list_neighbors = sorted(list_neighbors, key=len, reverse=True)

    painted = [-1]*num_vertices
    color_map = [[] for _ in range(num_vertices)]
    count = 0
    for i in range(num_vertices):
        if count == num_vertices: # tất cả đỉnh đã tô
            return painted, max(painted)
        
        max_degree = sorted_list_neighbors[i][-1]
        sorted_list_neighbors[i].pop(-1)
        for j in range(1,num_vertices+1):
            if painted[max_degree] == -1 and j not in color_map[max_degree]: # màu j
                painted[max_degree] = j
                count += 1
                for neighbor in sorted_list_neighbors[i]:
                    color_map[neighbor].append(j)
                break

    return painted, max(painted)

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


num_vertices, graph = read_graph("TH3\color2.txt")
list_color1, color1 = Welsh_Powell(num_vertices, graph)
print(f"Welsh Powell: \n {list_color1}")
print(f"Số màu: {color1} \n")

list_color2, color2 = DSatur(num_vertices, graph)
print(f"DSatur: \n {list_color2}")
print(f"Số màu: {color2}")