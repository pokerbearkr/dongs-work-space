import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr=[]
def dfs(t):
    if t==m:
        print(*arr)
    for x in range(t):
        arr.append(x)
        dfs(t+1)
        arr.pop()

dfs(n)