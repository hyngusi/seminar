from collections import defaultdict

class FordFulkerson:
    def __init__(self, graph):
        self.graph = graph # Đồ thị dưới dạng danh sách kề
        self.V = len(graph)  # Số đỉnh trong đồ thị

    def bfs(self, s, t, parent):
        visited = [False] * self.V
        queue = []
        queue.append(s)
        visited[s] = True
  # Duyệt qua các đỉnh bằng thuật toán BFS để tìm đường bổ sung
        while queue:
            u = queue.pop(0)
            for v, capacity, _ in self.graph[u]:
                # Kiểm tra đỉnh v chưa được thăm và cạnh còn có khả năng dư
                if not visited[v] and capacity > 0:
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u
# Trả về True nếu có đường bổ sung từ s đến t, ngược lại False
        return visited[t]

    def ford_fulkerson(self, source, sink):
        parent = [-1] * self.V
        max_flow = 0
# Thực hiện thuật toán Ford-Fulkerson để tìm cặp ghép cực đại
        while self.bfs(source, sink, parent):
            path_flow = float("inf")
            s = sink
            while s != source:
                for u, capacity, _ in self.graph[parent[s]]:
                    if u == s:
                        path_flow = min(path_flow, capacity)
                s = parent[s]
# Cập nhật luồng và khả năng còn lại trên mạng
            max_flow += path_flow

            v = sink  # Bắt đầu từ đỉnh nguồn
            while v != source:
                u = parent[v]# Lấy đỉnh cha của đỉnh hiện tại
                for i in range(len(self.graph[u])):
                    if self.graph[u][i][0] == v:
                        # Cập nhật khả năng trên cạnh từ u đến v bằng cách trừ đi luồng tăng cường
                        self.graph[u][i] = (v, self.graph[u][i][1] - path_flow, 0)
                        break
                found = False
                for i in range(len(self.graph[v])):
                    if self.graph[v][i][0] == u:
                        # Cập nhật khả năng trên cạnh từ v đến u bằng cách cộng thêm luồng tăng cường
                        self.graph[v][i] = (u, self.graph[v][i][1] + path_flow, 0)
                        found = True
                        break
                if not found:
                    # Nếu không tìm thấy cạnh từ v đến u, thêm cạnh mới với luồng tăng cường vào danh sách
                    self.graph[v].append((u, path_flow, 0))
                v = parent[v]
 # Trả về luồng cực đại trong mạng
        return max_flow

# Đọc dữ liệu đồ thị từ tệp tin
def read_graph_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        V, E = map(int, lines[0].split())
        graph = [[] for _ in range(V)]

        for i in range(1, E + 1):
            u, v = map(int, lines[i].split())
            graph[u - 1].append((v - 1, 1, 0))  # Thêm cạnh với khả năng 1 (đồ thị nhị phân)

    return V, graph

if __name__ == "__main__":
    filename = "graph4a.txt"  # Tên tệp tin chứa dữ liệu đồ thị
    V, graph = read_graph_from_file(filename)

    g = FordFulkerson(graph)

    # Chọn một nguồn và một nguồn trút trong mạng
    source = 0
    sink = V - 1

    max_flow = g.ford_fulkerson(source, sink)
    print("Số cặp ghép cực đại là:", max_flow)
