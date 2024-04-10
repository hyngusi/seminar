import heapq

class Node:
    def __init__(self, state, g=0, h=0, parent=None):
        self.state = state
        self.g = g
        self.h = h
        self.parent = parent

    def f(self):
        return self.g + self.h

def astar(graph, start, goal):
    open_set = []
    closed_set = set()

    start_node = Node(start, 0, graph[start])
    heapq.heappush(open_set, (start_node.f(), start_node))

    while open_set:
        current_node = heapq.heappop(open_set)[1]

        if current_node.state == goal:
            path = []
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
            return list(reversed(path))

        closed_set.add(current_node.state)

        for neighbor, cost in graph[current_node.state]:
            if neighbor in closed_set:
                continue

            g_score = current_node.g + cost
            h_score = graph[neighbor]
            neighbor_node = Node(neighbor, g_score, h_score, current_node)

            for f, open_node in open_set:
                if open_node.state == neighbor and g_score >= open_node.g:
                    break
            else:
                heapq.heappush(open_set, (neighbor_node.f(), neighbor_node))

    return None

def main():
    # Định nghĩa đồ thị
    graph = {
        'A': {'B': 1, 'C': 2},
        'B': {'D': 3},
        'C': {'D': 1},
        'D': {}
    }

    start = 'A'
    goal = 'D'

    path = astar(graph, start, goal)

    if path:
        print("Đường đi:", path)
    else:
        print("Không tìm thấy đường đi từ {} đến {}".format(start, goal))

if __name__ == "__main__":
    main()
