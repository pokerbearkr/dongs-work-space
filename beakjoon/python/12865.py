import sys

input = sys.stdin.readline
N, K = map(int, input().split())
stuff = [[0, 0]]
knapsack = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for _ in range(N):
    stuff.append(list(map(int, input().split())))

for i in range(1, N + 1):
    for j in range(1, K + 1):
        weight = stuff[i][0]
        value = stuff[i][1]

        if j < weight:
            knapsack[i][j] = knapsack[i - 1][j]
        else:
            knapsack[i][j] = max(value + knapsack[i - 1][j - weight], knapsack[i - 1][j])

print(knapsack[N][K])

# 시간 초과(재귀함수 완전탐색)
# import sys
#
# input = sys.stdin.readline
#
# n, k = map(int, input().split())
#
# arr = [list(map(int, input().split())) for _ in range(n)]
# ans = 0
#
#
# def resu(idx, weigh, price):
#     global ans
#     if weigh>k:
#         return
#     if idx == n:
#         if weigh <= k:
#             ans = max(ans, price)
#             return
#         else:
#             return
#     resu(idx + 1, weigh + arr[idx][0], price + arr[idx][1])
#
#     resu(idx + 1, weigh, price)
#
#
# resu(0, 0, 0)
#
# print(ans)
