def solution(N, stages):
    count=[0]*N
    rank=[0]*N
    for x in range(0,N):
        count[x]=(stages.count(x+1))
        print(count)
    for x in range(0,N):
        rank[x]=count[x]/sum(count[x:])

    print(rank)

    return 1


print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4,[4,4,4,4,4]))