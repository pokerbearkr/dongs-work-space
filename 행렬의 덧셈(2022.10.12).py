def solution(arr1, arr2):
    sum=[]
    answer=[]
    for x in range(len(arr1)):
        sum=[]
        for y in range(len(arr1[0])):
            sum.append(arr1[x][y]+arr2[x][y])
        answer.append(sum)
    return answer


# Test Case # print(solution([[1,2],[2,3]],[[3,4],[5,6]]))