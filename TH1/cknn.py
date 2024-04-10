import sys

# thuật toán Prim
def prim(n, graph):
    min_cost = 0    # Biến lưu tổng trọng số của cây khung nhỏ nhất
    visited = [False] * n  
    min_weights = [float('inf')] * n  # Danh sách trọng số nhỏ nhất đến từng đỉnh

    # Bắt đầu từ đỉnh 0
    min_weights[0] = 0

    for _ in range(n):
        u = -1  # Đỉnh chưa thăm có trọng số nhỏ nhất
        for v in range(n):
            if not visited[v] and (u == -1 or min_weights[v] < min_weights[u]):
                u = v
        
        visited[u] = True
        min_cost += min_weights[u]

        # Cập nhật trọng số nhỏ nhất đến các đỉnh kề của u
        for v in range(n):
            if not visited[v] and graph[u][v] < min_weights[v]:
                min_weights[v] = graph[u][v]

    return min_cost

if __name__ == "__main__":
    filename = "data.txt"
    graph = []

    with open(filename, "r") as file:
        n = int(file.readline())
        for line in file:
            row = line.split()
            for j in range(n):
                if row[j] == '0':
                    row[j] = float('inf')
                else:
                    row[j] = int(row[j])
            graph.append(row)

    min_cost = prim(n, graph)  # Tìm cây khung nhỏ nhất
    print("Tổng trọng số của cây khung nhỏ nhất:", min_cost)  # In kết quả lên màn hình
