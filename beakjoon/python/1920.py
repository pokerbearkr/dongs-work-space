import sys

input = sys.stdin.readline

n = int(input())
arr = set(map(int, input().split()))
m = int(input())
ans = list(map(int, input().split()))
for x in range(m):
    if ans[x] in arr:
        print('1')
    else:
        print('0')
