import sys

input = sys.stdin.readline

count = 0
n = int(input())
t = []
for x in range(n):
    t.append(list(map(int, input().split())))
ans = 0
print(t)
for x in range(1, 10):
    for y in range(10):
        for z in range(10):

            if x == y or y == z or z == x:
                continue
            for arr in t:
                number = str(arr[0])
                ball = arr[1]
                strike = arr[2]
                if x or y or z in (number[0],number[1],number[2]):
                    if x==number[0] 
