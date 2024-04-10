import heapq

def read_graph(filename):
    with open(filename, 'r') as file:
        num_vertices, start_vertex, end_vertex = map(int, file.readline().split())
        graph = []
        for _ in range(num_vertices):
            row = list(map(int, file.readline().split()))
            graph.append(row)
        return num_vertices, start_vertex, end_vertex, graph

def dijkstra(graph, start, end):
    n = len(graph)
    distances = [float('inf')] * n
    distances[start] = 0
    visited = [False] * n
    min_heap = [(0, start)]

    while min_heap:
        dist, node = heapq.heappop(min_heap)

        if visited[node]:
            continue

        visited[node] = True

        for neighbor, weight in enumerate(graph[node]):
            if not visited[neighbor] and weight > 0:
                new_dist = dist + weight
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    heapq.heappush(min_heap, (new_dist, neighbor))

    return distances[end]


num_vertices, start_vertex, end_vertex, graph = read_graph('TH2\graph2.txt')

# Tìm đường ngắn nhất từ đỉnh bắt đầu đến đỉnh kết thúc
shortest_distance = dijkstra(graph, start_vertex, end_vertex)
if shortest_distance == float('inf'):
    print(f"Không có đường đi từ đỉnh {start_vertex} đến đỉnh {end_vertex}.")
else:
    print(f"Đường ngắn nhất từ đỉnh {start_vertex} đến đỉnh {end_vertex} có độ dài là {shortest_distance}.")
