import sys

input = sys.stdin.readline
sys.setrecursionlimit(99999999)

def sol(idx, dan, zzan,use):
    global ans
    if idx == n:
        if use==0:
            return
        result = abs(dan - zzan)
        ans = min(result, ans)
        return

    sol(idx + 1, dan * arr[idx][0], zzan + arr[idx][1],use+1)
    sol(idx + 1, dan, zzan,use)


n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

ans = 999999999999999

sol(0,1,0,0)
print(ans)