def solution(n):
    array=['1','2','4']
    answer=""
        
    while n > 0 :
        answer=array[n%3-1]+answer
        n=n//3


    return answer 
    # 역순인 진수를 뒤집어 줘야 원래 변환 하고자하는 base가 출력
    
print(solution(1))
print(solution(2))
print(solution(3))
print(solution(4))
print(solution(5))
print(solution(6))
print(solution(7))
print(solution(8))
print(solution(9))
print(solution(10))