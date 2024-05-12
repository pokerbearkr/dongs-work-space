import sys

input = sys.stdin.readline

move = int(input())

arr=list(input().rstrip())
n=int(input())
for x in range(n):
    temarr=arr
    left,right=map(int,input().split())
    left,right=left-1,right-1
    while True:
        if left>=1 and right>=1:
            if 'X' in temarr:
                left,right=left-1,right-1
                temarr.remove('X')
            else:
                break
        else:
            break
    while True:
        if left>=1:
            if ''

print(arr)