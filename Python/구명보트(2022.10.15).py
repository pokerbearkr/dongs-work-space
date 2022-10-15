def solution(people, limit):
    people.sort(reverse=True)
    t=0
    m=len(people)-1
    x=0
    while True:
        if t>=len(people):
            break
        if people[x]+people[m]<=limit:
            t+=2
            m-=1
        else:
            t+=1
        x+=1
        
    return x

#Test Case # print(solution([70,50,80,50],100))