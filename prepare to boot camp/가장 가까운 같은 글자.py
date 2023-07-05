def solution(s):
    tem=[]   
    answer = []
    for x in range(len(s)):
        if s[x] in tem:
            answer.append(x-tem.index(s[x]))
            tem[tem.index(s[x])]="@"
            tem.append(s[x])
        else:
            tem.append(s[x])
            answer.append(-1)
            
    return answer

print(solution("banana"))