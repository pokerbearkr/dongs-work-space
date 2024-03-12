a=int(input())
b=list(map(int,input().split()))
c=int(input())
count=0
for x in b:
    if x==c:
        count+=1
print(count)
