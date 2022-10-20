"""from itertools import permutations
t=[]
def solution(numbers):
    answer=list(permutations(numbers,len(numbers)))
    for x in range(len(answer)):
        t.append(list(answer[x]))
    for x in range(len(t)):
        t[x]=("".join(map(str,t[x])))
    return str(max(t))

print(solution([6, 10, 2]))
""" #시간초과

def solution(numbers):
    max=0
    for x in range(len(numbers)):
        if max<int(numbers[x][0]):
            max=int(numbers[x][0])

    return 1

print(solution([6,10,2]))