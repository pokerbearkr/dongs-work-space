import heapq

"""def solution(scoville, K):   # heapify가 문제인가 해봤는데 아니다.
    heap=[]
    for x in scoville:
        heapq.heappush(heap,x)
    count=0
    while min(heap)<=K:
        try:
            heapq.heappush(heap,heapq.heappop(heap)+heapq.heappop(heap)*2)
        except:
            return -1
        count+=1
    
    return count"""

def solution(scoville, K):    # 답은 맞는데 효율성테스트는 다 실패한다
    heapq.heapify(scoville)
    count=0
    while scoville[0]<=K:  #여기 min함수쓰면 시간복잡도가n이라서 안됨
        try:
            heapq.heappush(scoville,heapq.heappop(scoville)\
                +heapq.heappop(scoville)*2)
        except IndexError:
            return -1
        count+=1
    
    return count

"""def solution(scoville, K):    
    heapq.heapify(scoville)
    count=0
    while min(scoville)<K and len(scoville)!=1:
        heapq.heappush(scoville,heapq.heappop(scoville)+heapq.heappop(scoville)*2)
        count+=1
    
    return -1 if scoville[0] < K else count"""

print(solution([1,2,3,9,10,12],7))