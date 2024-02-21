import sys

input = sys.stdin.readline

n = int(input())
num = set(map(int, input().split()))
m = int(input())
num2 = list(map(int, input().split()))
ans = []
for x in num2:
    if x in num:
        ans.append('1')
    else:
        ans.append('0')
print(' '.join(ans))
