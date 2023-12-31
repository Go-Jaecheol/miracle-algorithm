import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
visited = [False for _ in range(100001)]
dx = [-1, 1]

def bfs():
    q = deque()
    q.append((N, 0))
    visited[N] = True
    while q:
        x, cost = q.popleft()
        if x == K:
            return cost
            
        for i in range(3):
            if i == 2: next_x = 2 * x
            else: next_x = x + dx[i]
            if 0 <= next_x <= 100000 and not visited[next_x]:
                q.append((next_x, cost + 1))
                visited[next_x] = True
print(bfs())