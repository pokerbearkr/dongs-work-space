import sys

input = sys.stdin.readline

size = 2
n = int(input())
dp = [[0, 0]] * 41
dp[0] = [1, 0]
dp[1] = [0, 1]
for _ in range(n):
    t = int(input())
    if t >= size:
        for i in range(size, t + 1):
            dp[i] = [dp[i - 1][0] + dp[i - 2][0], dp[i - 1][1] + dp[i - 2][1]]
            size += 1
    print(dp[t][0], dp[t][1])
