from collections import deque
def solution(numbers, target):
    n=len(numbers)
    queue=deque()
    answer = 0
    queue.append([numbers[0],0]) # 시작점
    queue.append([-1*numbers[0],0])
    while queue:
        x,y=queue.popleft()
        y+=1
        if y<n:
            queue.append([x+numbers[y],y])
            queue.append([x-numbers[y],y])
        else: #만약 N번째로 탐색했다면
            if x==target: # 탐색결과가 Target이라면 +1
                answer+=1
    return answer


print(solution([1,1,1,1,1],3))