from py2opt.routefinder import RouteFinder

def read_graph(filename):
    with open(filename, "r") as file:

        num_vertices = int(file.readline())
        graph = []
        # graph.append(0)

        for _ in range(num_vertices):
            row = list(map(int, file.readline().split()))
            # row.insert(0, 0)
            graph.append(row)
        return num_vertices, graph;
    
num_vertices, graph = read_graph("TH4\\tsp1.txt")
tour = [i for i in range(1,num_vertices+1)]

# cities_names = ['A', 'B', 'C', 'D']
# dist_mat = [[0, 29, 45, 35], [29, 0, 57, 42], [15, 57, 0, 61], [35, 42, 61, 0]]
route_finder = RouteFinder(graph, tour, iterations=5)
best_distance, best_route = route_finder.solve()

print(best_distance)
# 114
print(best_route)
# ['A', 'C', 'B', 'D']