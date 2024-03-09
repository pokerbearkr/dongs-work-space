import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    non=[[0 for _ in range(n)] for _ in range(m)]
    for _ in range(k):
        x,y=map(int,input().split())
        non[y-1][x-1]=1
    print(non)
