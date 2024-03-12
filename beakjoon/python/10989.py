import sys

n = int(input())
a = [0] * 10001
for x in range(n):
    m = int(sys.stdin.readline())
    a[m] += 1
for x in range(10001):
    for y in range(a[x]):
        print(x)
