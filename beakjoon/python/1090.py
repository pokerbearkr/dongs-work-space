import sys

input = sys.stdin.readline

n = int(input())
arr = []
min = 999999999999
for _ in range(n):
    arr.append(input().split())
for x in range(n):
    base = arr[x]
    tmp = arr.copy()
    tmp.remove(arr[x])
    print(tmp)
    sum=0
    for y in range(n-1):
        sum+=abs(int(base[0])-int(tmp[y][0]))+abs(int(base[1])-int(tmp[y][1]))
    if sum<min:
        print(sum)
        min=sum
print((arr))
