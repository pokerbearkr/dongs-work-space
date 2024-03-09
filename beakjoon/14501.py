import sys

input = sys.stdin.readline

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]
ans = 0


def recu(idx, price):
    global ans
    if idx>n:
        return
    if idx == n:
        ans = max(ans, price)
        return
    recu(idx + arr[idx][0], price + arr[idx][1])

    recu(idx + 1, price)


recu(0, 0)
print(ans)