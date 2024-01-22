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

N = int(sys.stdin.readline())
cost_sum, h = 0, []
parent = [int(x) for x in range(N)]
for i in range(N):
    temp = sys.stdin.readline().strip()
    for j, t in enumerate(temp):
        if t == '0': continue
        elif t.isupper():
            cost = ord(t) - 38
        else:
            cost = ord(t) - 96
        cost_sum += cost
        heapq.heappush(h, (cost, i, j))
result = kruskal()

for i in range(N):
    find_parent(parent, i)
if len(set(parent)) != 1:
    print(-1)
else:
    print(cost_sum - result)
