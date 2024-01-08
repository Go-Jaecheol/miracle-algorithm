import sys

n = int(sys.stdin.readline())
wine = [int(sys.stdin.readline().strip()) for _ in range(n)]
dp = [[0 for _ in range(3)] for _ in range(n)]

dp[0][0], dp[0][1], dp[0][2] = wine[0], wine[0], wine[0]
for i in range(1, n):
    dp[i][0] = wine[i] + max(dp[i - 2])
    dp[i][1] = wine[i] + dp[i - 1][0]
    dp[i][2] = max(dp[i - 1])
print(max(map(max, dp)))