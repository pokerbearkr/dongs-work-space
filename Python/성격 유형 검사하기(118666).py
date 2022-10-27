"""def solution(survey, choices):
    sum=[0]*4
    answer=''
    for i in range(survey):
        survey[i].sort()
    for x in range(len(survey)):
        if choices[x]==4:
            1
        else:
            if survey[i][0]=="R":
                sum[0]+=choices[i]
            elif survey[i][0]=="C":
                sum[1]+=choices[i]
            elif survey[i][0]=="J":
                sum[2]+=choices[i]
            elif survey[i][0]=="A":
                sum[3]+=choices[i]
    if sum[0]>=4:
        answer='R'
    else:
        answer='T'
    if sum[1]>=4:
        answer='C'
    else:
        answer='F'
    if sum[0]>=4:
        answer='J'
    else:
        answer='M'
    if sum[0]>=4:
        answer='A'
    else:
        answer='N'
    
            
    
    return answer
"""
def solution(survey, choices):
    answer = ''
    dic= {"R" : 0,"T" : 0,"C" : 0,"F" : 0,"J" : 0,"M" : 0,"A" : 0,"N" : 0 }
    
    for s,c in zip(survey,choices):
        if c>4:     dic[s[1]] += c-4
        elif c<4:   dic[s[0]] += 4-c
    
    li = list(dic.items())
    
    for i in range(0,8,2):
        if li[i][1] < li[i+1][1]: answer += li[i+1][0]
        else:   answer += li[i][0]
        
    return answer
print(solution(["AN", "CF", "MJ", "RT", "NA"],[5, 3, 2, 7, 5]))