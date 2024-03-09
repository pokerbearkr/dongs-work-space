
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
tree = list(map(int, input().split()))
start = 1
end = max(tree)

while start <= end:
    mid = (start + end) // 2

    wood = 0
    for x in tree:
        if x >= mid:
            wood += x - mid
    if wood >= m:
        start = mid + 1
    else:
        end = mid - 1
print(end)

# 시간초과
# import sys
# input = sys.stdin.readline
#
# n,m=map(int,input().split())
# tree=list(map(int,input().split()))
# t=max(tree)
# while 1:
#     sum=0
#     for x in range(n):
#         if tree[x]>t:
#             sum+= tree[x]-t
#     if sum==m:
#         print(t)
#         exit(0)
#     else:
#         t-=1
