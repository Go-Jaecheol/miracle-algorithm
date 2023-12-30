import sys
from collections import deque

N = int(sys.stdin.readline())
maps = [[int(x) for x in sys.stdin.readline().strip()] for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
result = []

def bfs(x, y):
    q = deque()
    cost = 1
    q.append((x, y))
    visited[y][x] = True
    while q:
        cur_x, cur_y = q.popleft()
        for i in range(4):
            next_x, next_y = cur_x + dx[i], cur_y + dy[i]
            if 0 <= next_x < N and 0 <= next_y < N and maps[next_y][next_x] == 1:
                if visited[next_y][next_x]: continue
                cost += 1
                q.append((next_x, next_y))
                visited[next_y][next_x] = True
    return cost

for i in range(N):
    for j in range(N):
        if maps[i][j] == 1 and not visited[i][j]:
            result.append(bfs(j, i))
result.sort()
print(len(result))
for value in result:
    print(value)
