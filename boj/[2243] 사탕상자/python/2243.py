import sys
from math import ceil, log
from collections import defaultdict


def segment(idx, start, end, num, count):
    if num < start or end < num:
        return tree[idx]
    if start == end:
        tree[idx] += count
        num_dict[idx] = num
        return tree[idx]
    mid = (start + end) // 2
    tree[idx] = segment(idx * 2, start, mid, num, count) + segment(idx * 2 + 1, mid + 1, end, num, count)
    return tree[idx]


def search(idx, start, end, num):
    if start == end:
        tree[idx] -= 1
        print(num_dict[idx])
        return tree[idx]
    mid = (start + end) // 2
    if tree[idx * 2] >= num:
        search(idx * 2, start, mid, num)
    else:
        search(idx * 2 + 1, mid + 1, end, num - tree[idx * 2])
    tree[idx] = tree[idx * 2] + tree[idx * 2 + 1]
    return tree[idx]


n = int(sys.stdin.readline())
h = ceil(log(1000000, 2) + 1)
tree = [0 for _ in range(pow(2, h))]
num_dict = defaultdict(int)

for _ in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    if temp[0] == 1:
        search(1, 1, 1000000, temp[1])
    else:
        segment(1, 1, 1000000, temp[1], temp[2])
