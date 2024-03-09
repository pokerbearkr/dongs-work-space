import sys

input = sys.stdin.readline

n, m = map(int, input().split())

t = min(n, m)
while t != 1:
    if n % t == 0 and m % t == 0:
        print(t)
        break
    else:
        t -= 1
if t==1:
    print('1')

print(round(n*m/t))
