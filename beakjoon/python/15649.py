import sys,itertools

input = sys.stdin.readline

n, m = map(int, input().split())
nums = [i for i in range(1, n+1)]

array = itertools.permutations(nums, m)

for i in array:
    for j in i:
        print(j, end = ' ')
    print()