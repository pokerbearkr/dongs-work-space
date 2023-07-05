"""def solution(k, m, score):
    answer = 0
    score.sort()
    while m <=len(score):
        tem=[]
        for x in range(m):
            tem.append((score[-1]))
            score.remove(score[-1])
        answer+=min(tem)*m

    return answer """
# 위 코드는 시간초과

def solution(k, m, score):
    answer = 0
    score.sort()
    while m <=len(score):
        answer+=score[-m]*m
        del score[-m:]
    return answer 

print(solution(4,3,[4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]))