import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
cnt = 1
for x in range(n):
    try:
        if arr[x + 1] > arr[x]:
            pass
        else:
            cnt += 1
    except:
        if arr[0] > arr[x]:
            pass
        else:
            cnt += 1

print(cnt)
