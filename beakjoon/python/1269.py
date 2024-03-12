import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr1 = set(map(int, input().split()))
arr2 = set(map(int, input().split()))
count = 0
for x in arr1:
    if x in arr2:
        count += 1

print(len(arr1) + len(arr2) - 2 * count)
