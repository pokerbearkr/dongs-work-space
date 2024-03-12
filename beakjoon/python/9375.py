import sys

input = sys.stdin.readline

n = int(input())
for _ in range(n):

    m = int(input())
    mem=[]
    for _ in range(m):
        tem=list(input().split())
        if tem[-1] in mem:
            pass
        else:
            mem.append(tem[-1][tem[0]])
    print(mem)