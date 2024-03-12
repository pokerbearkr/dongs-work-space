num = int(input())
a = []
for _ in range(num):
    a.append(int(input()))
a.sort()
for x in range(num):
    print(a[x])
