import sys

input = sys.stdin.readline

n = int(input())


answer = 0

for k in range(2, int(n ** 0.5) + 1):

    answer += (k * ((n // k) - k + 1) + (k + 1 + n // k) * (n // k - k) // 2)

print(answer % 1000000)
