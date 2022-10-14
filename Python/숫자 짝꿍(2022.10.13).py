def solution(X, Y):
    answer = []
    for i in (set(X)&set(Y)) :
        for j in range(min(X.count(i), Y.count(i))) :
            answer.append(i)
    answer.sort(reverse=True)
    if len(answer) == 0:
        return "-1"
    if answer[0] == "0":
        return "0"
    answer = "".join(answer)
    return answer





# 시간초과코드
"""def solution(X, Y):
    test=list(Y)
    answer=[]
    for x in X:
        if x in test:
            answer.append(x)
            test.remove(x)
    answer.sort(reverse=True)
    
    if len(answer)==0:
        answer.append(str(-1))
    if len(answer[0])==0:
        return "0"
    return str(int("".join(answer)))


print(solution("12321","42531"))
print(solution("100","203045"))
"""