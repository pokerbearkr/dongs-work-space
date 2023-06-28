
def solution(t, p):
    answer = 0
    for x in range(len(t)-len(p)+1):
        if(t[x:x+len(p)])<=p:
            answer+=1
    
    return answer

# print(solution("3141592","271"))