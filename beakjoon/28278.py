import sys

input = sys.stdin.readline

n = int(input())
arr = []
for x in range(n):
    t = input().rstrip()
    match (t[0]):
        case '1':
            arr.append(int(t[2:]))
        case '2':
            if len(arr) >= 1:
                print(arr.pop())
            else:
                print('-1')
        case '3':
            print(len(arr))
        case '4':
            if len(arr) == 0:
                print('1')
            else:
                print('0')
        case '5':
            if len(arr) >= 1:
                print(arr[-1])
            else:
                print('-1')
