import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)


def bfs(node):
    visited[node] = 1
    for next in graph[node]:
        if visited[next] == 1:
            continue
        bfs(next)


bfs(1)
print(sum(visited)-1)
