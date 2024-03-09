import sys

input = sys.stdin.readline

n = int(input())
arr = sorted(list(map(int, input().split())))
ans = 0
for x in range(n):
    ans+=arr[x]*(n-x)

print(ans)
