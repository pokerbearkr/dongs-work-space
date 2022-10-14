def solution(d, budget):
    d.sort()
    sum=0
    count=0
    for x in range(len(d)):
        sum+=d[x]
        count+=1
        if sum>budget:
            return count-1
    return counta

# Test Case # print(solution([1,3,2,5,4],9))