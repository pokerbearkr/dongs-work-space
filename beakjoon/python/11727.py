import sys

input = sys.stdin.readline

n = int(input())

dp = [0] * 1002
dp[1] = 1
dp[2] = 3
if n >= 3:
    for x in range(3, n + 1):
        dp[x] = dp[x - 1] + dp[x - 2]*2

print(dp[n] % 10007)
