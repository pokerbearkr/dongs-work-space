import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
for i in range(n):
    order = input().strip()
    n = int(input())
    flag = 1
    arr = input().strip()
    queue = deque(arr[1:-1].split(','))
    if n == 0:
        queue = deque()
    R = 0
    for i in range(len(order)):
        if order[i] == 'R':
            R += 1
        elif order[i] == 'D':
            if len(queue) == 0:
                print('error')
                flag = 0
                break
            else:
                if R % 2 == 0:
                    queue.popleft()
                else:
                    queue.pop()

    if flag == 0:
        continue
    else:
        if R % 2 == 0:
            print('[' + ",".join(queue) + ']')
        else:
            queue.reverse()
            print('[' + ",".join(queue) + ']')
