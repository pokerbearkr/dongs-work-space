def solution(numbers):
    result=[]
    for x in range(len(numbers)):
        for y in range(x+1,len(numbers)):
            result.append(numbers[x]+numbers[y])
    t=set(result)
    answer=list(t)
    answer.sort()
    return answer

# test case # print(solution([2,1,3,4,1]))