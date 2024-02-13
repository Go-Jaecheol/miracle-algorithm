import sys
from collections import deque

N = int(sys.stdin.readline())
heights = [int(sys.stdin.readline()) for _ in range(N)]

stack = deque()
stack.append((0, heights[0]))
result = 0
for i in range(1, N):
    temp = i
    while stack and stack[-1][1] > heights[i]:
        x, y = stack.pop()
        result = max(result, (i - x) * y)
        temp = x
    stack.append((temp, heights[i]))
while stack:
    x, y = stack.pop()
    result = max(result, (N - x) * y)
print(result)
