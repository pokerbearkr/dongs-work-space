def solution(answers):
    one=[1,2,3,4,5]*2000
    oc=0
    tc=0
    thc=0
    two=[2,1,2,3,2,4,2,5]*1250
    three=[3,3,1,1,2,2,4,4,5,5]*1000
    for x in range(len(answers)):
        if answers[x]==one[x]:
            oc+=1
        if answers[x]==two[x]:
            tc+=1
        if answers[x]==three[x]:
            thc+=1
    if oc==tc and tc==thc: 
        return [1,2,3]
    if oc==max(oc,tc,thc) and oc==tc: 
        return [1,2]
    if oc==max(oc,tc,thc) and oc==thc: 
        return [1,3]
    if tc==max(oc,tc,thc) and tc==thc: 
        return [2,3]
    if oc==max(oc,tc,thc): 
        return [1]
    if tc==max(oc,tc,thc): 
        return [2]
    if thc==max(oc,tc,thc): 
        return [3]
    return [oc,tc,thc]

# Test Case # print(solution([1,2,3,4,5]))