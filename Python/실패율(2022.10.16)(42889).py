"""def solution(N, stages):
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
"""
def solution(N, stages):
    People = len(stages)
    faillist = {}
    for i in range(1, N + 1):
        if People != 0:
            faillist[i] = stages.count(i) / People
            People -= stages.count(i)
        else:
            faillist[i] = 0

    return sorted(faillist, key=lambda i: faillist[i], reverse=True)

print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))