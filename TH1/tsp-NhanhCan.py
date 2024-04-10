import time
start_time = time.time()

with open('tsp.txt') as file:
    cities = int(file.readline())
    graph = []
    for i in range(cities):
        graph.append(list(map(int, file.readline().split())))

# for a in graph:
#     print(a)
total=0
def tsp(graph, start):
    # chứa kết quả thăm các thành phố
    result = []       #x
    # kiểm tra 1 thành phố đã thăm chưa
    flag = []       #d
    for i in range(0,cities):
        flag.append(False)
        
    result.append(start)
    flag[start] = True

    def output():
        if graph[result[cities-1]][start] > 0:   #ton tai duong di quay lai thanh pho ban dau
            for i in range(0,cities):
                print(result[i], ' -> ', end='')
            print(start, '- Total: ', total)

    def travel(idx, total):
        for i in range(0,cities):
            if flag[i] == False and graph[result[idx-1]][i] > 0:
                result.append(i)
                flag[i] = True
                total += graph[result[idx-1]][i]

                if idx == cities-1: #đã thăm n thành phố
                    output()
                else:
                    travel(idx+1, total)

                result.remove(i)
                flag[i] = False
                total -= graph[result[idx-1]][i]

    
    travel(start,total)

# for i in range(0, cities):
tsp(graph, 2)
print('----------')
print("--- %s seconds ---" % (round(time.time() - start_time, 2)))