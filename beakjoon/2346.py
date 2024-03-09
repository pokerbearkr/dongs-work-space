import sys

input = sys.stdin.readline

from collections import deque

n = int(input())
arr = list(map(int, input().split()))
dic = {}
for x in range(1, n + 1):
    dic[x] = arr[x - 1]
queue = deque(range(1, n + 1))
for x in range(n):
    t = queue.popleft()
    print(t, end=' ')
    if dic[t]>0:
        queue.rotate(-(int(dic[t]-1)))
    else:
        queue.rotate(-int(dic[t]))
