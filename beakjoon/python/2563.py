import sys

input = sys.stdin.readline
n = int(input())
arr = [[0] * 100 for _ in range(100)]
for i in range(n):
    x, y = map(int, input().split())
    for j in range(x,x+10):
        for k in range(y,y+10):
            arr[j][k] = 1
count = 0
for x in range(100):
    for y in range(100):
        if arr[x][y] == 1:
            count += 1
print(count)
