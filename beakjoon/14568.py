import sys

input = sys.stdin.readline

candy = int(input())
count = 0
for x in range(1, round(candy / 2)):
    remain = candy - 2 * x
    for y in range(1, remain):
        young = y
        nam = remain - y
        if young + 2 <= nam:
            count += 1
print(count)