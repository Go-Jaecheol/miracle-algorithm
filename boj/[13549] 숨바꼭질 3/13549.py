import sys, heapq

N, K = map(int, sys.stdin.readline().split())
distance = [float('inf') for _ in range(100001)]
dx = [-1, 1]

def dijkstra():
    h = []
    distance[N] = 0
    heapq.heappush(h, (N, distance[N]))
    while h:
        x, cost = heapq.heappop(h)
        if distance[x] < cost: continue
        for i in range(3):
            if i == 2:
                next_x = 2 * x
                next_cost = cost
            else:
                next_x = x + dx[i]
                next_cost = cost + 1
            if 0 <= next_x <= 100000 and next_cost < distance[next_x]:
                distance[next_x] = next_cost
                heapq.heappush(h, (next_x, next_cost))
dijkstra()
print(distance[K])