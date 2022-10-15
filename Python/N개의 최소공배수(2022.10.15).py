def solution(arr):
    answer = 0
    n = 1                           
    
    while True:
        answer = max(arr) * n       
        result = True               
        for num in arr:
            if answer % num != 0:   
                result = False      
                break
        if result:                  
            break                   
        n += 1
        
    return answer

# print(solution([2,6,8,14]))

"""from fractions import gcd (gcb는 최대공약수 구하는함수)


def nlcm(num):      
    answer = num[0]
    for n in num:
        answer = n * answer / gcd(n, answer)

    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(nlcm([2,6,8,14]));"""