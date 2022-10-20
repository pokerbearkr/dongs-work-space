def solution(prices):
    answer=[]
    for x in range(len(prices)):
        count=0
        for y in range(x,len(prices)):
            if prices[x]<=prices[y]:
                count+=1
                if y==len(prices)-1:
                    answer.append(count-1)
            else:
                answer.append(count)
                break
    return answer


print(solution([1,2,3,2,3]))