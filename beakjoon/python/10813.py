##공 바꾸기
n,m=map(int,input().split())
list=[i+1 for i in range(n)]
for _ in range(m):
    a,b=map(int,input().split())
    c=list[b-1]
    list[b-1]=list[a-1]
    list[a-1]=c
for x in range(n):
    print(list[x],end=' ')
        
