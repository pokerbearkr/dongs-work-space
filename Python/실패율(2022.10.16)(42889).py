def solution(N, stages):
    count=[0]*(N+1)
    rank=[0]*(N+1)
    for x in range(0,N+1):
        count[x]=(stages.count(x+1))
        print(count)
    for x in range(0,N):
        try:
            rank[x]=count[x]/sum(count[x:])
        except:
            1

    print(rank)
    for i in rank:
        temp.append(sorted(rank).index(i)+1)

    return 1


print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4,[4,4,4,4,4]))