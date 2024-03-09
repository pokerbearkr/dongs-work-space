n = int(input())
arr = [0] + list(map(int, input().split()))
dp = [0] * (n + 1)
dp[n] = 1
for x in range(n - 1, 0, -1):
    temp = 1
    for y in range(x + 1, n + 1):
        if arr[x] < arr[y]:
            if dp[y] + 1 > temp:
                temp = dp[y] + 1
    dp[x] = temp

print(max(dp))
