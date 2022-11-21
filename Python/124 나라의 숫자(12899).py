def solution(n):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, 3)
        rev_base += str(mod)
    
    tem=rev_base[::-1]
    return tem 
    # 역순인 진수를 뒤집어 줘야 원래 변환 하고자하는 base가 출력
    
print(solution(1))
print(solution(2))
print(solution(3))
print(solution(4))
print(solution(5))
print(solution(6))
print(solution(7))