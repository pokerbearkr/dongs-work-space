import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

arr = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
count=0

def bfs(arr, start, visited):
    q = deque([start])
    visited[start] = 1

    while len(q) > 0:
        x = q.popleft()
        for i in arr[x]:
            if not visited[i]:
                q.append(i)
                visited[i] = 1
for i in range(1,n+1):
    if not visited[i]:
        bfs(arr,i,visited)
        count+=1

print(count)
