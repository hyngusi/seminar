class FordFulkerson:
    def __init__(self, graph, source, sink):
        self.graph = graph
        self.source = source
        self.sink = sink
        self.visited = set()

    def find_augmenting_path(self, node, min_capacity):
        if node == self.sink:
            return min_capacity

        self.visited.add(node)

        for neighbor, capacity in self.graph[node]:
            if neighbor not in self.visited and capacity > 0:
                new_min_capacity = min(min_capacity, capacity)
                flow = self.find_augmenting_path(neighbor, new_min_capacity)
                if flow > 0:
                    return flow

        return 0

    def ford_fulkerson(self):
        max_flow = 0

        while True:
            self.visited = set()
            augmenting_path = self.find_augmenting_path(self.source, float("inf"))

            if augmenting_path == 0:
                break

            max_flow += augmenting_path

        return max_flow


def main():
    num_vertices, num_edges, source, sink = map(int, input().split())
    graph = {i: [] for i in range(1, num_vertices + 1)}

    for _ in range(num_edges):
        u, v, capacity = map(int, input().split())
        graph[u].append((v, capacity))
        graph[v].append((u, 0))  # Add reverse edge with capacity 0 for residual graph

    ff = FordFulkerson(graph, source, sink)
    max_flow = ff.ford_fulkerson()
    print("Giá trị luồng cực đại là:", max_flow)


if __name__ == "__main__":
    main()
