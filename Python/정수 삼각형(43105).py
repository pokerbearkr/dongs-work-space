def solution(triangle):
    triangle=[[0]+t+[0] for t in triangle]
    for x in range(1,len(triangle)):
        for y in range(1,x+2):
            triangle[x][y]+=max(triangle[x-1][y-1],triangle[x-1][y])



    return max(triangle[-1])

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))