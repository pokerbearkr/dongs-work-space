"""def solution(n):
    count=0
    for x in range(2,n+1):
        div=0
        for y in range(2,x+1):
            if x%y==0:
                div+=1
        if div==1:
            count+=1
    return count
""" # 시간초과 -> 에라토스테네스의 체 사용


def solution(n):

    tem=[True for i in range(n)]
    print(tem)
    for x in range(1,int(n**0.5)+1):
        
    return 1

print(solution(10))
