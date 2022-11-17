def solution(priorities, location):
    rank=0
    arr=[(v,i) for i,v in enumerate(priorities)]  # 번호와 순번을 묶어줌
    while True:
        if arr[0][0]==max(arr)[0]: # 우선순위가 제일 높으면
            rank+=1
            if arr[0][1]==location: 
                return rank
            arr.remove(arr[0]) # 출력한다
        else:
            arr.append(arr[0])
            arr.remove(arr[0])





print(solution([2,1,3,2],2))
#print(solution([1,1,9,1,1,1],0))