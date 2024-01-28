import sys

N, C = map(int, sys.stdin.readline().split())
houses = [int(sys.stdin.readline().strip()) for _ in range(N)]
houses.sort()
start, end = 1, houses[-1] - houses[0]
while start <= end:
    mid = (start + end) // 2
    left, right, count = 0, 0, 1
    while right < N:
        if houses[right] - houses[left] < mid:
            right += 1
        else:
            left = right
            count += 1
    if count < C:
        end = mid - 1
    else:
        start = mid + 1
print(end)
