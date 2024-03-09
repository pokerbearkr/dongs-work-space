import sys

input = sys.stdin.readline

a, b = map(int, input().split())
a-=1

def ham(n):
    ans = n
    for x in range(1, 99):
        ans += (n // (2 ** x)) * ((2 ** x) - (2 ** (x - 1)))
    return ans

print(ham(b)-ham(a))