def solution(k, score):
    arr=[]
    answer = []
    for x in range(k):
        if x>=len(score):
            return answer
        arr.append(score[x])
        answer.append(min(arr))
    for y in range(k,len(score)):
        if min(arr)<score[y]:
            arr.pop(arr.index(min(arr)))
            arr.append(score[y])
        answer.append(min(arr))
    return answer


print(solution(11, [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]))
# print(solution(3,[10, 100, 20, 150, 1, 100, 200]))