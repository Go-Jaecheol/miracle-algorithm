import sys
from bisect import bisect_left

N, H = map(int, sys.stdin.readline().split())
obstacles = [int(sys.stdin.readline().strip()) for _ in range(N)]
upwards, downwards = [], []
for i, value in enumerate(obstacles):
    if i % 2 == 0:
        upwards.append(value)
    else:
        downwards.append(value)
upwards.sort()
downwards.sort()
result, count = float('inf'), 0
for i in range(1, H + 1):
    temp = len(upwards) - bisect_left(upwards, i)
    temp += len(downwards) - bisect_left(downwards, H + 1 - i)
    if temp < result:
        result = temp
        count = 1
    elif temp == result:
        count += 1
print(result, count)
