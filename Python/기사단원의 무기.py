def solution(number, limit, power):
    count=1
    for x in range(1,number):
        tem=0
        for y in range(1,x):
            if x%y==0:
                tem+=1
        if tem>limit:
            count+=power
        else:
            count+=tem
    return count

print(solution(5,3,2))