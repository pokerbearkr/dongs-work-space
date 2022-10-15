def solution(arr1, arr2):
    i=len(arr1)
    j=len(arr1[0])
    answer = [[0],[0]]
    for x in range(i):
        for y in range(j):
            answer[x][y]=arr1[x][y]*arr2[x][y]
    return answer



print(solution([[1, 4], [3, 2], [4, 1]],[[3, 3], [3, 3]]))