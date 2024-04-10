from collections import defaultdict

class FordFulkerson:
    def __init__(self, graph):
        self.graph = graph # Biểu đồ của mạng (danh sách cạnh)
        self.V = len(graph) # Số đỉnh trong mạng

    def bfs(self, s, t, parent):
        # Tìm kiếm theo chiều rộng để tìm đường tăng cường
        visited = [False] * self.V
        queue = []
        queue.append(s)
        visited[s] = True

        while queue:
            u = queue.pop(0) # Lấy đỉnh u từ hàng đợi
            for v, capacity, _ in self.graph[u]:
                # Kiểm tra các đỉnh kề của u
                if visited[v] is False and capacity > 0:
                    queue.append(v)  # Thêm v vào hàng đợi nếu nó chưa được thăm
                    visited[v] = True
                    parent[v] = u

        return visited[t]

    def ford_fulkerson(self, source, sink):
        parent = [-1] * self.V # Đỉnh cha của mỗi đỉnh
        max_flow = 0 # Luồng cực đại ban đầu

        while self.bfs(source, sink, parent):
            # Nếu còn đường tăng cường từ nguồn đến đích
            path_flow = float("inf") # Khởi tạo luồng trên đường tăng cường
            s = sink
            while s != source:
                for u, capacity, _ in self.graph[parent[s]]:
                    if u == s:
                        path_flow = min(path_flow, capacity)
                s = parent[s]

            max_flow += path_flow # Tăng luồng cực đại

            v = sink
            while v != source:
                u = parent[v]
                for i in range(len(self.graph[u])):
                    if self.graph[u][i][0] == v:
                        # Giảm trọng số trên cạnh u->v bởi luồng trên đường tăng cường
                        self.graph[u][i] = (v, self.graph[u][i][1] - path_flow, 0)
                        break
                found = False
                for i in range(len(self.graph[v])):
                    if self.graph[v][i][0] == u:
                        # Tăng trọng số trên cạnh v->u bởi luồng trên đường tăng cường
                        self.graph[v][i] = (u, self.graph[v][i][1] + path_flow, 0)
                        found = True
                        break
                if not found:
                    # Thêm cạnh ngược với trọng số path_flow (nếu chưa tồn tại)
                    self.graph[v].append((u, path_flow, 0))
                v = parent[v]

        return max_flow

# Đọc dữ liệu đồ thị từ tệp tin
def read_graph_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        V, E, source, sink = map(int, lines[0].split())
        graph = [[] for _ in range(V)]

        for i in range(1, E + 1):
            u, v, capacity = map(int, lines[i].split())
            graph[u - 1].append((v - 1, capacity, 0))
            graph[v - 1].append((u - 1, 0, 0))  # Thêm cạnh ngược với công suất 0

    return V, graph, source - 1, sink - 1

if __name__ == "__main__":
    filename = "graph3a.txt"  # Tên tệp tin chứa dữ liệu đồ thị
    V, graph, source, sink = read_graph_from_file(filename)

    g = FordFulkerson(graph)

    max_flow = g.ford_fulkerson(source, sink)
    print("Luồng cực đại trong mạng là:", max_flow)
