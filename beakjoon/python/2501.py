import sys

input = sys.stdin.readline
num, k = map(int, input().split())
arr=[]
for x in range(1,num+1):
    if num%x==0:
        arr.append(x)
try:
    print(arr[k-1])
except:
    print('0')