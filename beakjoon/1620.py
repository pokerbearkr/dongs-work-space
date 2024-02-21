import sys

input = sys.stdin.readline

n, m = map(int, input().split())
dic = {}
dic2 = {}
for x in range(1, n + 1):
    t = input().rstrip()
    dic[x] = t
    dic2[t] = x
for x in range(m):
    t = input().rstrip()
    try:
        print(dic[int(t)])
    except:
        print(dic2[t])
