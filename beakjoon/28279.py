from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
queue = deque()
for x in range(n):
    order = list(input().split())
    match (order[0]):
        case '1':
            queue.appendleft(order[1])
        case '2':
            queue.append(order[1])
        case '3':
            if len(queue) == 0:
                print('-1')
            else:
                print(queue.popleft())
        case '4':
            if len(queue) == 0:
                print('-1')
            else:
                print(queue.pop())
        case '5':
            print(len(queue))
        case '6':
            if len(queue) == 0:
                print('1')
            else:
                print('0')
        case '7':
            if len(queue) == 0:
                print('-1')
            else:
                print(queue[0])
        case '8':
            if len(queue) == 0:
                print('-1')
            else:
                print(queue[-1])
