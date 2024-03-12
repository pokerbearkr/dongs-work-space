a,b=map(int,input().split())
i,j=[],[]
for _ in range(a):
    t=list(map(int,input().split()))
    i.append(t)
for _ in range(a):
    t=list(map(int,input().split()))
    j.append(t)
for x in range(a):
    for y in range(b):
        sum=i[x][y]+j[x][y]
        print(sum,end=' ')
    print()

