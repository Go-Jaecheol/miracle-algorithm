import sys
from math import ceil, log


def segment(idx, start, end):
    if start == end:
        tree[idx] = nums[start]
        return tree[idx]

    mid = (start + end) // 2
    left_child = segment(idx * 2, start, mid)
    right_child = segment(idx * 2 + 1, mid + 1, end)

    tree[idx] = min(left_child, right_child)
    return tree[idx]


def search(idx, start, end, search_range1, search_range2):
    if search_range1 > end or search_range2 < start:
        return float('inf')
    if search_range1 <= start and end <= search_range2:
        return tree[idx]
    mid = (start + end) // 2
    left_child = search(idx * 2, start, mid, search_range1, search_range2)
    right_child = search(idx * 2 + 1, mid + 1, end, search_range1, search_range2)
    return min(left_child, right_child)


N, M = map(int, sys.stdin.readline().split())
nums = [int(sys.stdin.readline().strip()) for _ in range(N)]
pairs = [[int(x) for x in sys.stdin.readline().split()] for _ in range(M)]

h = ceil(log(N, 2) + 1)
tree = [0 for _ in range(pow(2, h))]
segment(1, 0, N - 1)

for a, b in pairs:
    answer = search(1, 0, N - 1, a - 1, b - 1)
    print(answer)
