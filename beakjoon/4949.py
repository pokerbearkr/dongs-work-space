import sys

input = sys.stdin.readline
while 1:
    arr = input().rstrip()
    big = []
    small = []
    if arr == '.':
        break
    for x in range(len(arr)):
        if arr[x] == '[':
            big.append(arr[x])
        elif arr[x] == '(':
            small.append(arr[x])
        elif arr[x] == ']':
            if len(big) == 0:
                print('no')
                break
            else:
                big.pop()
        elif arr[x] == '(':
            if len(small) == 0:
                print('no')
                break
            else:
                small.pop()
        else:
            continue
else:
    if len(big) == 0 and len(small) == 0:
        print('yes')
    else:
        print('no')
