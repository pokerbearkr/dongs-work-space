import sys

input = sys.stdin.readline
n, m = map(int, input().split())
line = [int(input()) for _ in range(n)]
start = 1
end = max(line)+1

while end - start != 1:
    mid = (start + end) // 2

    count = 0
    for x in line:
        count += x // mid
    if count >= m:
        start = mid
    else:
        end = mid
print(start)
