import sys
from collections import deque


def bfs(x, y):
    q = deque()
    q.append((x, y, 0))
    visited = [[False for _ in range(c)] for _ in range(r)]
    visited[y][x] = True
    max_cost = 0
    while q:
        cx, cy, cost = q.popleft()
        max_cost = max(max_cost, cost)
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < c and 0 <= ny < r and maps[ny][nx] == 'L':
                if visited[ny][nx]: continue
                q.append((nx, ny, cost + 1))
                visited[ny][nx] = True
    return max_cost


r, c = map(int, sys.stdin.readline().split())
maps = [[x for x in sys.stdin.readline().strip()] for _ in range(r)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
answer = 0

for i in range(r):
    for j in range(c):
        if maps[i][j] == 'W': continue
        answer = max(answer, bfs(j, i))

print(answer)
