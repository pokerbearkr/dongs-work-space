import sys

input = sys.stdin.readline
n, m = map(int, input().split())
listen = set()
watch = set()
for x in range(n):
    listen.add(input().rstrip())
for x in range(m):
    watch.add(input().rstrip())
ans = sorted(list(listen & watch))

print(len(ans))
print('\n'.join(ans))
