import sys

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(fees, parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if (fees[a - 1] < fees[b - 1]):
        parent[b] = a
    else:
        parent[a] = b

N, M, k = map(int, sys.stdin.readline().split())
fees = [int(x) for x in sys.stdin.readline().split()]
parent = [int(x) for x in range(N + 1)]
for _ in range(M):
    v, w = map(int, sys.stdin.readline().split())
    union_parent(fees, parent, v, w)
for i in range(1, N + 1):
    find_parent(parent, i)

result = set(parent[1:])
cost = 0
for r in result:
    cost += fees[r - 1]

if k < cost:
    print("Oh no")
else:
    print(cost)
