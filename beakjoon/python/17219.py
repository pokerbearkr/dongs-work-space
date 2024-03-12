import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = {}
for _ in range(n):
    t = list(input().split())
    arr[t[0]] = t[1]

for _ in range(m):
    tem=input().rstrip()
    print(arr[tem])
