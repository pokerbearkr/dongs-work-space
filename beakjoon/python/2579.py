import sys

input = sys.stdin.readline

n = int(input())
stair = [0] + [int(input()) for _ in range(n)]
dp = [0] * (n + 1)
if n <= 2:
    print(sum(stair))
    exit(0)
dp[1] = stair[1]
dp[2] = stair[1] + stair[2]
for x in range(3, n + 1):
    dp[x] = max(dp[x - 3] + stair[x - 1] + stair[x], dp[x - 2] + stair[x])

print(dp[n])
