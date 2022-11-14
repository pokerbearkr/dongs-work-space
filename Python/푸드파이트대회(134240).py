def solution(food):
    result=[]
    result1=[]
    for x in range(1,len(food)):
        for y in range(int(food[x]/2)):
            result.append(x)
    answer=result

    result.reverse()
    result1=['0']+result
    result1.reverse()
    answer=result1+answer


    return ''.join(map(str, answer))  #int형들을 합쳐줄때는 str로 mapping 한다음 합쳐야한다.



#print(solution([1,3,4,6]))
#print(solution([1,7,1,2]))