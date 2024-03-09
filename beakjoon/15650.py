import sys, itertools

input = sys.stdin.readline

n, m = map(int, input().split())
if m == 1:
    for x in range(n):
        print(x + 1)
    exit(0)
arr = [x for x in range(1, n + 1)]

for x in itertools.combinations(arr, m):
    print(*x)
