def solution(n):
    count=1
    while n>1:
        if n%2==0:
            n=n/2
        else:
            count+=1
            n=(n-1)/2
    

    return count