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
    a = [True] * (n + 1)
    m = int(n**0.5)

    for i in range(2, m + 1):
        if a[i] == True:
            for j in range(i + i, n + 1, i):
                a[j] = False
    return len([i for i in range(2, n + 1) if a[i] == True])
# 에라토스테네스의 체 100개 깔고 2의배수지우고 3의배수지우고...