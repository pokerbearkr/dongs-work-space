##공넣기
n,m=map(int,input().split())
list = [0 for i in range(n)]
for x in range(m):
    a,b,c=map(int,input().split())
    for y in range(b-a+1):
        list[a-1+y]=c
for x in range(n):
    print(list[x],end=' ')
