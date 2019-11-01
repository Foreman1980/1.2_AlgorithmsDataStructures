#    Задание № 2 урока № 8:
#    Доработать алгоритм Дейкстры (рассматривался на уроке), чтобы он дополнительно возвращал список вершин, которые
# необходимо обойти.

g = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 5, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0]
]

def dijkstra(graph, start):
    length = len(graph)
    isVisited = [False] * length
    cost = [float('inf')] * length
    parent = [-1] * length

    cost[start] = 0
    minCost = 0

    while minCost < float('inf'):
        isVisited[start] = True

        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not isVisited[i]:

                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
                    parent[i] = start

        minCost = float('inf')
        for i in range(length):
            if minCost > cost[i] and not isVisited[i]:
                minCost = cost[i]
                start = i

    return cost

s = int(input('От какой вершины идти: '))
print(dijkstra(g, s))

# Вывод вида -  Введите количество встретившихся друзей: 5
#               [0, 1, 1, 1, 1]
#               [0, 0, 1, 1, 1]
#               [0, 0, 0, 1, 1]
#               [0, 0, 0, 0, 1]
#               [0, 0, 0, 0, 0]
#
#               Всего рукопожатий = 10
#
#               Process finished with exit code 0
