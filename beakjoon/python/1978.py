import sys

input = sys.stdin.readline

n = int(input())
arr = []
count = 0
arr = list(map(int, input().split()))

for x in arr:
    for i in range(2, x + 1):
        if x % i == 0:
            if x == i:
                count += 1

            break
print(count)
