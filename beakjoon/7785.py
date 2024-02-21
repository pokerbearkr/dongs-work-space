import sys

input = sys.stdin.readline

n = int(input())
arr = set()
for x in range(n):
    t = input().split()[0]
    if t in arr:
        arr.remove(t)
    else:
        arr.add(t)
arr2 = sorted(list(arr), reverse=True)
print('\n'.join(arr2))
