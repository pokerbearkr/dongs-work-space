import heapq #heapq 사용해서 시간단축
def solution(n,works):
    answer=0
    if n>sum(works):
        return 0
    heap=[-i for i in works]
    heapq.heapify(heap) #이거없으면 2번쨰 케이스때 앤앞에있는 -1꺼내옴
    while n>0:
        tem=heapq.heappop(heap)
        tem+=1
        heapq.heappush(heap,tem)
        n-=1
    for x in range(len(works)):
        answer+=heap[x]**2


    return answer


print(solution(4,[4,3,3]))
print(solution(99,[2,15,22,55,55]))



"""def solution(n, works): #답은 맞는데 효율성 테스트 실패함(시간초과)
    answer=0
    count=n
    for x in range(n):
        for y in range(len(works)):
            if max(works)==0:
                return 0
            if works[y]==max(works):
                works[y]-=1
                count-=1
            if count==0:
                break
        if count==0:
            break
    for z in range(len(works)):
        answer+=works[z]**2


    return answer"""

