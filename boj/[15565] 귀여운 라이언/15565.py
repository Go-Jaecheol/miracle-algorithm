import sys
from collections import defaultdict

N, K = map(int, sys.stdin.readline().split())
dolls = [int(x) for x in sys.stdin.readline().split()]

start, end = 0, 0
count = defaultdict(int)
count[dolls[end]] += 1
answer = 1000001
while end < N:
    if count[1] == K:
        answer = min(answer, end - start + 1)
        count[dolls[start]] -= 1
        start += 1
    else:
        end += 1
        if end >= N: break
        count[dolls[end]] += 1
if answer == 1000001: answer = -1
print(answer)
