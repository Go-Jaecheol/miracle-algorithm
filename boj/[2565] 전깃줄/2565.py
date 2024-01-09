import sys
from collections import defaultdict

n = int(sys.stdin.readline())
line = defaultdict(int)
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    line[a] = b
dp = [0 for _ in range(501)]

for i in sorted(line.keys()):
    dp[i] = 1
    for j in range(1, i):
        if line[j] < line[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print(n - max(dp))