def solution(left, right):
    answer=0
    for x in range(left,right+1):
        t=0
        for y in range(1,x+1):
            if x%y==0:
                t+=1
        if t%2==0:
            answer+=x
        else:
            answer-=x
    return answer

#Test Case # print(solution(13,24))