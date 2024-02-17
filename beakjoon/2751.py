import sys

n = int(input())
a = []
for _ in range(n):
    a.append(int(sys.stdin.readline()))
a.sort()
for x in range(n):
    print(a[x])
