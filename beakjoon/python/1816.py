import sys

input = sys.stdin.readline

n = int(input())
for _ in range(n):
    num = int(input())
    for x in range(2, 1000000):
        if num % x == 0:
            print('NO')
            break
        else:
            continue
    else:
        print('YES')