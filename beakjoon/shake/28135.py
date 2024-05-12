import sys

input = sys.stdin.readline

n = int(input())
cnt = 0
for x in range(1, n + 1):
    cnt += 1
    if x == n:
        print(cnt)
        exit()
    if str(x).find('50') > -1:
        cnt += 1
print(cnt)
