n, b = map(int, input().split())
a = 0
while n // (b ** a) != 0:
    a += 1

for x in reversed(range(a)):
    if n // b ** x >= 10:
        print(chr(n // (b ** x) + 55), end='')
    else:
        print(n // (b ** x), end='')
    n = n - (n // b ** x) * (b ** x)
