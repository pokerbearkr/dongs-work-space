import sys

input = sys.stdin.readline

n = int(input())
dp = [0,1, 1, 1, 2, 2, 3, 4, 5, 7, 9] + [0] * 100
for x in range(11,105):
    dp[x]=dp[x-1]+dp[x-5]

for _ in range(n):
    print(dp[int(input())])