import sys

input = sys.stdin.readline

n = int(input())
count = 1

while count ** 2 <= n:
    count += 1
print(count - 1)
