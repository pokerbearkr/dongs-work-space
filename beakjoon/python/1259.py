import sys

input = sys.stdin.readline
n = str(input().rstrip())
while n != '0':
    if n[::1] == n[::-1]:
        print('yes')
    else:
        print('no')
    n = str(input().rstrip())
