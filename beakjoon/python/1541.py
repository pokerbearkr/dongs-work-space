import re
import sys

input = sys.stdin.readline

expression = input().rstrip()

numbers = []
operators = []

tokens = re.findall(r'(\d+|[\+\-])', expression)

for token in tokens:
    if token.isdigit():
        numbers.append(int(token))
    else:
        operators.append(token)

for x in range(len(operators)):
    if operators[x] == '-':
        stop = 0
        stop = int(x)
        break
try:
    print(sum(numbers[:stop + 1]) - sum(numbers[stop + 1:]))
except:
    print(sum(numbers))
