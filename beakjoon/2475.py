import sys

input = sys.stdin.readline

n = list(map(int, input().split()))
ans = 0
for x in range(len(n)):
    ans += n[x] ** 2
print(ans % 10)
