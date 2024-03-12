import sys

input = sys.stdin.readline
n=int(input())
while n !=-1:
    arr=[]
    for x in range(1,n):
        if n%x==0:
            arr.append(x)
    if sum(arr)==n:
        print(n,'=',' + '.join(map(str,arr)))
    else:
        print(n,'is NOT perfect.')
    n = int(input())