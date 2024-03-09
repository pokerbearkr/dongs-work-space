from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
if n==1:
    print('1')
    sys.exit()
queue = deque(range(1, n + 1))

while len(queue)!=1:
    queue.popleft()
    if len(queue)==1:
        print(queue[0])
        break
    queue.rotate(-1)
