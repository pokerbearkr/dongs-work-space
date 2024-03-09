import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr = list(map(int, input().split()))

for _ in range(m):
    a, b, c = map(int, input().split())
    if a == 1:
        arr[b - 1] = c
    elif a == 2:
        for x in range(b - 1, c):
            if arr[x] == 0:
                arr[x] = 1
            else:
                arr[x] = 0
    elif a == 3:
        for x in range(b - 1, c):
            arr[x] = 0
    elif a == 4:
        for x in range(b - 1, c):
            arr[x] = 1
print(*arr)
