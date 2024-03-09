import sys

input = sys.stdin.readline

n = int(input())
dp=[1,1,2,3]+[0]*999997
for x in range(3,n+1):
    dp[x]=(dp[x-1]+dp[x-2])%15746
print(dp[n])