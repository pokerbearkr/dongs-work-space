import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
count = 0
min = 0
for x in range(n, m + 1):
    for i in range(2, x + 1):
        if x % i == 0:
            if x == i:
                count += x
                if min > x:
                    min = x
            break

if min == 0:
    print('-1')
else:
    print(count)
    print(min)
