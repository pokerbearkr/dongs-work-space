import sys

input = sys.stdin.readline

n, k = map(int, input().split())

arr = list(map(int, input().split()))



# for x in range(n - k + 1):
#     t=sum(arr[x:x + k])
#     if  t> max:
#         max = t
# print(max)
start=sum(arr[:k])
max = start
for x in range(n-k):
    start=start-arr[x]+arr[x+k]
    if max<start:
        max=start

print(max)