import sys

input = sys.stdin.readline

k = int(input())
arr = []
for x in range(k):
    t = int(input())
    if t == 0:
        arr.pop()
    else:
        arr.append(t)
print((sum(arr)))
