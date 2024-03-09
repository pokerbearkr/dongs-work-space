import sys

input = sys.stdin.readline

n = int(input())
t = 2
while n != 1:
    if n % t == 0:
        print(t)
        n = n / t
    else:
        t+=1
