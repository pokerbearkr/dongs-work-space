import sys
n=sorted(list(map(int,sys.stdin.readline().rstrip())), reverse=True)
for x in range(len(n)):
    print(n[x],end='')