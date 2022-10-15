def solution(citations):
    answer=0
    citations.sort()
    for x in range(max(citations)):
        count=0
        for y in range(len(citations)):
            if citations[y]>=x:
                count+=1
        if count>=x:
            answer=x
    return answer

# Test Case # print(solution([3,0,6,1,5]))