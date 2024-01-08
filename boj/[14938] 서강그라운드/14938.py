import sys
import heapq
from collections import defaultdict


def input_graph():
    for _ in range(r):
        a, b, l = map(int, sys.stdin.readline().split())
        graph[a - 1].append([b - 1, l])
        graph[b - 1].append([a - 1, l])


def dijkstra(start):
    h = []
    distance[start] = 0
    heapq.heappush(h, [distance[start], start])
    while h:
        cost, vertex = heapq.heappop(h)
        if distance[vertex] < cost:
            continue
        for next_vertex, next_cost in graph[vertex]:
            new_dist = cost + next_cost
            if new_dist < distance[next_vertex]:
                distance[next_vertex] = new_dist
                heapq.heappush(h, [distance[next_vertex], next_vertex])


n, m, r = map(int, sys.stdin.readline().split())
item = [int(x) for x in sys.stdin.readline().split()]
graph = defaultdict(list)
result = 0

input_graph()
for i in range(n):
    count = 0
    distance = [float('inf') for _ in range(n)]
    dijkstra(i)
    for e, d in enumerate(distance):
        if d <= m:
            count += item[e]
    result = max(result, count)
print(result)