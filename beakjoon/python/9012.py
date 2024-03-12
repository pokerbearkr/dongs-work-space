import sys

input = sys.stdin.readline

n = int(input())
for x in range(n):
    arr = list(input().rstrip())
    tem = []
    for y in range(len(arr)):
        if arr[y] == '(':
            tem.append(arr[y])
        else:
            if len(arr) == 0:
                print('NO')
                break
            else:
                try:
                    tem.pop()
                except:
                    print('NO')
                    break
    else:
        if len(tem) == 0:
            print('YES')
        else:
            print('NO')
