import sys

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

N, M = map(int, sys.stdin.readline().split())
parent = [int(x) for x in range(N + 1)]
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    union_parent(parent, a, b)
times = [int(x) for x in sys.stdin.readline().split()]
last = find_parent(parent, times[0])
count = 0
for time in times[1:]:
    current = find_parent(parent, time)
    if current != last:
        count += 1
        last = current
print(count)
