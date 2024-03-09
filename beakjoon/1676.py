import sys

input = sys.stdin.readline

n = int(input())
ans = 0
if n <= 4:
    print('0')
    sys.exit(0)
else:
    for x in range(4):
        if n % 5 != 0:
            n -= 1
    ans += n // 5
    ans += n // 25
    ans += n // 125
    print(ans)
