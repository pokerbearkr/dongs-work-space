import math
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
print(round(math.factorial(n)/(math.factorial(k)*math.factorial(n-k))))