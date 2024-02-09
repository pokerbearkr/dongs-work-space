# 바구니 뒤집기
n, m = map(int, input().split())
list = [i + 1 for i in range(n)]
for x in range(m):
    a, b = map(int, input().split())
    for y in range((b - a) // 2 +1):
        list[a + y - 1], list[b - y - 1] = list[b - y - 1], list[a + y - 1]
for x in range(n):
    print(list[x], end=' ')
