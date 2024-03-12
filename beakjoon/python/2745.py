n, b = input().split()
ans = 0
for x in range(len(n)):
    if ord(n[len(n) - x - 1]) < 65:
        ans = ans + (int(n[len(n) - x - 1])) * (int(b) ** x)
    else:
        ans = ans + (ord(n[len(n) - x - 1]) - 55) * (int(b) ** x)
print(ans)
