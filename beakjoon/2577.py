import sys

input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())
mul = str(a * b * c)
ans = [0] * 10
for x in range(len(mul)):
    if mul[x] == '0':
        ans[0] += 1
    elif mul[x] == '1':
        ans[1] += 1
    elif mul[x] == '2':
        ans[2] += 1
    elif mul[x] == '3':
        ans[3] += 1
    elif mul[x] == '4':
        ans[4] += 1
    elif mul[x] == '5':
        ans[5] += 1
    elif mul[x] == '6':
        ans[6] += 1
    elif mul[x] == '7':
        ans[7] += 1
    elif mul[x] == '8':
        ans[8] += 1
    elif mul[x] == '9':
        ans[9] += 1
for x in range(10):
    print(ans[x])
