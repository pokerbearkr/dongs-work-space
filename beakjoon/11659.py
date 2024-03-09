import sys

input = sys.stdin.readline

n, m = map(int, input().split())

line = list(map(int, input().split()))

prefix = [0] * (n + 1)
for x in range(1, n + 1):
    prefix[x] = prefix[x - 1] + line[x - 1]

for _ in range(m):
    a, b = map(int,input().split())
    print(prefix[b] - prefix[a-1])
