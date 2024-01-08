import sys
import heapq
from collections import defaultdict


def input_graph():
    for _ in range(M):
        A, B, C = map(int, sys.stdin.readline().split())
        graph[A].append([B, C])
        graph[B].append([A, C])


def dijkstra():
    h = []
    distance[1] = 0
    heapq.heappush(h, [distance[1], 1])
    while h:
        cost, vertex = heapq.heappop(h)
        if distance[vertex] < cost:
            continue
        for next_vertex, next_cost in graph[vertex]:
            new_dist = cost + next_cost
            if new_dist < distance[next_vertex]:
                distance[next_vertex] = new_dist
                heapq.heappush(h, [distance[next_vertex], next_vertex])


N, M = map(int, sys.stdin.readline().split())
graph = defaultdict(list)
distance = [float('inf') for _ in range(N + 1)]

input_graph()
dijkstra()
print(distance[N])
