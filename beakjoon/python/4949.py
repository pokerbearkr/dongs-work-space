import sys

input = sys.stdin.readline

while 1:
    arr = input().rstrip()
    big = []
    if arr == '.':
        break
    for x in range(len(arr)):
        if arr[x] == '[':
            big.append('[')
        elif arr[x] == '(':
            big.append('(')
        elif arr[x] == ']':
            if len(big) == 0:
                print('no')
                break
            elif big[-1] == '[':
                big.pop()
            else:
                print('no')
                break
        elif arr[x] == ')':
            if len(big) == 0:
                print('no')
                break
            elif big[-1] == '(':
                big.pop()
            else:
                print('no')
                break
        else:
            continue
    else:
        if len(big) == 0:
            print('yes')
        else:
            print('no')
