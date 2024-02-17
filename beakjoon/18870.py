import sys

input = sys.stdin.readline
n = int(input())
numbers = list(map(int, input().split()))
rank = sorted(list(set(numbers.copy())))
cache = dict()
for i in range(len(rank)):
    cache[rank[i]] = i
for x in range(n):
    print(cache.get(numbers[x]), end=" ")
