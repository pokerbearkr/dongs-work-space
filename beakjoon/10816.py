import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
dic = {}
tem = list(map(int, input().split()))
for x in range(m):
    dic[tem[x]] = 0
for x in range(n):
    try:
        dic[arr[x]] += 1
    except:
        continue
for x in tem:
    print(dic[x], end=' ')
