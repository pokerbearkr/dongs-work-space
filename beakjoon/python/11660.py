import sys

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

nu = [[0] * (n + 1) for _ in range(n + 1)]

for x in range(n):
    for y in range(n):
        nu[x + 1][y + 1] = nu[x + 1][y] + nu[x][y + 1] - nu[x][y] + graph[x][y]
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    ans = nu[x2][y2] - nu[x2][y1 - 1] - nu[x1 - 1][y2] + nu[x1 - 1][y1 - 1]
    print(ans)
