import sys

input = sys.stdin.readline

N = int(input())
numbers = [[] * 2] * N
for i in range(N):
    X, Y = map(int, input().split())
    numbers[i] = [X, Y]
numbers = sorted(numbers, key=lambda x: (x[1], x[0]))
for i in range(N):
    print(numbers[i][0], numbers[i][1])
