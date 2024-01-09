import sys
from collections import defaultdict

N, K = map(int, sys.stdin.readline().split())
data = [int(x) for x in sys.stdin.readline().split()]

start, end = 0, 0
dic = defaultdict(int)
answer = 0
for start in range(N):
    while end < N:
        if dic[data[end]] >= K:
            break
        dic[data[end]] += 1
        end += 1
    answer = max(answer, end - start)
    dic[data[start]] -= 1
print(answer)
