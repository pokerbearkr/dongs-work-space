import sys

input = sys.stdin.readline

n = int(input())
dp = [0] * 13
dp[1] = 1
dp[2] = 2
dp[3] = 4
for x in range(4, 12):
    dp[x] = dp[x - 1] + dp[x - 2] + dp[x - 3]
for _ in range(n):
    print(dp[int(input())])
