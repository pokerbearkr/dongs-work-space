from collections import deque
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
queue = deque(range(1, n + 1))
ans = []
while len(queue) != 0:
    queue.rotate(-k + 1)
    ans.append(str(queue.popleft()))

print('<',end='')
print(', '.join(ans),end='')
print('>')