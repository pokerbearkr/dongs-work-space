import sys

input = sys.stdin.readline
n = input().rstrip()

arr = set()
for x in range(1, len(n) + 1):
    for y in range(len(n) - x + 1):
        if n[y:y + x] not in arr:
            arr.add(n[y:y + x])
print(len(arr))
