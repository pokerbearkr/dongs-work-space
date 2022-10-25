def solution(n, s):
    if n>s:
        return [-1]
    answer=[]
    for _ in range(n-s%n):
        answer.append(s//n)
    for _ in range(s%n):
        answer.append((s//n)+1)
    return answer

print(solution(2,9))
print(solution(2,1))
print(solution(2,8))