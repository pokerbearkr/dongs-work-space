def solution(lottos, win_nums):
    count=0
    zerocount=0
    for x in lottos:
        if x==0:
            zerocount+=1
        if x in win_nums:
            count+=1
    if 7-count-zerocount=7:
        return [6,6]
    return [7-count-zerocount,min(7-count,6)]

print(solution([44, 1, 0, 0, 31, 25],[31, 10, 45, 1, 6, 19]))