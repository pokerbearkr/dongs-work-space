n = int(input())

arr = list(map(int, input().split()))

ans = [0 for _ in range(n + 1)]

for x in range(n):
    ans[x + 1] = max(ans[x] + arr[x], arr[x])

print(max(ans[1:]))
