def solution(n, m):
    arr1=[]
    arr2=[]
    for x in range(1,n+1):
        if n%x==0 and m%x==0:
            arr1.append(x)
    for x in range(n,n*m+1):
        if x%n==0 and x%m==0:
            arr2.append(x)
    return [max(arr1),min(arr2)]

#Test Case # print(solution(2,5))