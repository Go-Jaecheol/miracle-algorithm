from collections import deque

def solution(maps):
    def bfs(x, y):
        q = deque()
        q.append((x, y))
        visited[y][x] = True
        cost = int(maps[y][x])
        while q:
            cx, cy = q.popleft()
            for i in range(4):
                nx, ny = cx + dx[i], cy + dy[i]
                if 0 <= nx < m and 0 <= ny < n and maps[ny][nx] != "X":
                    if visited[ny][nx]: continue
                    q.append((nx, ny))
                    visited[ny][nx] = True
                    cost += int(maps[ny][nx])
        return cost
    answer = []
    maps = [list(m) for m in maps]
    n, m = len(maps), len(maps[0])
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    visited = [[False for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if maps[i][j] != "X" and not visited[i][j]:
                answer.append(bfs(j, i))
    answer.sort()
    if len(answer) == 0: answer.append(-1)
    return answer