import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = set()
count = 0
for x in range(n):
    arr.add(input().rstrip())
for x in range(m):
    if input().rstrip() in arr:
        count += 1
print(count)
