
"""def is_prime_num(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True 
def solution(n, k):
    arr=[]
    result=0
    while n>1:
        arr.append(n%k)
        n=n//k
    arr.reverse()
    n=""
    for x in arr:
        if x!=0:
            n=str(n)+str(x)
        else:
            if n!='1':
                if is_prime_num(int(n)):
                    result+=1
            n=""
    if n!="":
        if is_prime_num(int(n)):
                    result+=1
    return arr,result

#print(solution(437674,3))
print(solution(110011,10))
"""
def to_k_number(n, k):  # n을 k진수로 반환
    ret = ""
    while n > 0:
        ret += str(n % k)
        n = n //  k
    return ''.join(reversed(ret))
 
 
def is_prime_num(k):
    if k == 2 or k == 3: return True  # 
    if k % 2 == 0 or k < 2: return False  
    for i in range(3, int(k ** 0.5) + 1, 2):
        if k % i == 0:
            return False
    return True
 
 
def solution(n, k):
    answer = 0
    k_num = to_k_number(n, k)  # k진수로 반환
    # k_num을 0을 기준으로 분할하여 n을 가져옴
    for n in k_num.split('0'):
        if n == "": continue
        if is_prime_num(int(n)):  # n이 소수인 경우 answer+=1
            answer += 1
    return answer
