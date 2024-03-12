import sys

input = sys.stdin.readline

n, k = map(int, input().split())
token = []
for _ in range(n):
    token.append(int(input()))
count=0
while k!=0:
    if k==0:
        break
    for x in token[::-1]:
        if k//x>=1:
            count += k//x
            k=k%x

print(count)