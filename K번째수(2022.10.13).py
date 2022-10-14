def solution(array, commands):
    result=[]
    arr=[]
    for x in range(len(commands)):
        t=commands[x]
        arr=array[t[0]-1:t[1]]
        arr.sort()
        result.append(arr[t[2]-1])

    return result



# Test Case # print(solution([1,5,2,6,3,7,4],[[2,5,3],[4,4,1],[1,7,3]]))