from sys import maxsize
import itertools
import sys  
import time
start_time = time.time()

with open('tsp.txt') as file:
    n = int(file.readline())
    dist = []
    for i in range(n):
        dist.append(list(map(int, file.readline().split())))

# for a in graph:
#     print(a)

# memoization for top down recursion
memo = [[-1]*(1 << (n+1)) for _ in range(n+1)]



# for i in range(cities):
# print(travellingSalesmanProblem(graph, 0))
# tsp_dynamic_programming(graph, cities)
print("--- %s seconds ---" % (round(time.time() - start_time, 2)))