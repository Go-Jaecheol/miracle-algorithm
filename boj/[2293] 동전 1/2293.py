import sys

n, k = map(int, sys.stdin.readline().split())
coin = [int(sys.stdin.readline().strip()) for _ in range(n)]
dp = [0 for _ in range(10001)]
for c in coin:
    if c > 10000:
        continue
    dp[c] += 1
    for i in range(c + 1, k + 1):
        dp[i] += dp[i - c]
print(dp[k])
