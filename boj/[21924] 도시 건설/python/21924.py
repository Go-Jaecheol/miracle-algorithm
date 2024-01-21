import sys, heapq

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if (a < b):
        parent[b] = a
    else:
        parent[a] = b

def kruskal():
    result = 0
    while h:
        c, a, b = heapq.heappop(h)
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result += c
    return result

N, M = map(int, sys.stdin.readline().split())
roads = [[int(x) for x in sys.stdin.readline().split()] for _ in range(M)]
parent = [int(x) for x in range(N + 1)]
cost_sum, h = 0, []
for a, b, c in roads:
    cost_sum += c
    heapq.heappush(h, (c, a, b))
result = kruskal()

for i in range(1, N + 1):
    find_parent(parent, i)
if len(set(parent[1:])) != 1:
    print(-1)
else:
    print(cost_sum - result)
