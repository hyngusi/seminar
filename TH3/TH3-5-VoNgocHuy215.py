import heapq

# Lớp Node đại diện cho một nút trong đồ thị
class Node:
    def __init__(self, id):
        self.id = id
        self.neighbors = []  # Danh sách các nút kề
        self.parent = None
        self.g = float('inf')  # Chi phí từ nút xuất phát đến nút hiện tại
        self.h = 0  # Heuristic

    def add_neighbor(self, neighbor, weight):
        self.neighbors.append((neighbor, weight))

# Hàm A* để tìm đường đi
def astar(graph, start, goal):
    open_list = []
    closed_set = set()

    start_node = graph[start]
    start_node.g = 0
    start_node.h = graph[start].h
    heapq.heappush(open_list, (start_node.g + start_node.h, start_node))

    while open_list:
        current_cost, current_node = heapq.heappop(open_list)

        if current_node.id == goal:
            path = []
            while current_node:
                path.append(current_node.id)
                current_node = current_node.parent
            return path[::-1]

        closed_set.add(current_node.id)

        for neighbor_id, weight in current_node.neighbors:
            neighbor = graph[neighbor_id]

            if neighbor_id not in closed_set:
                g = current_node.g + weight
                h = neighbor.h

                if g + h < neighbor.g + neighbor.h:
                    neighbor.parent = current_node
                    neighbor.g = g
                    heapq.heappush(open_list, (g + h, neighbor))

    return None  # Không tìm thấy đường đi

# Đọc dữ liệu từ tệp đầu vào
with open("TH3\graph1.txt", "r") as file:
    n, m, s, t = map(int, file.readline().split())
    graph = [Node]*(n+1)
    for i in range(n):
        graph[i] = Node(i)
    
    # Đọc thông tin về cạnh và trọng số của mỗi cạnh
    for _ in range(m):
        u, v, w = map(int, file.readline().split())
        graph[u].add_neighbor(v, w)
    
    # Đọc giá trị h của các đỉnh cuối
    h_values = list(map(int, file.readline().split()))
    
    # Gán giá trị h cho mỗi đỉnh cuối
    for i in range(n):
        graph[i].h = h_values[i]


path = astar(graph, s, t)
if path:
    print("Đường đi từ", s, "đến", t, "là:", path)
else:
    print("Không có đường đi từ", s, "đến", t)
