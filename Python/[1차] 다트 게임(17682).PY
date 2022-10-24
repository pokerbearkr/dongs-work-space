"""def solution(dartResult):
    b=list(dartResult)
    answer=0
    for x in range(len(b)):
        if b[x]=='S':
            try:
                if b[x+1]=='*'or b[x+3]=='*'or b[x+4]=='*':
                    answer+=int(b[x-1])*2
                elif b[x+1]=='#'or b[x+3]=='#'or b[x+4]=='#':
                    answer-=int(b[x-1])
                else:
                    answer+=int(b[x-1])
            except:
                answer+=int(b[x-1])
        elif b[x]=='D':
            try:
                if b[x+1]=='*'or b[x+3]=='*'or b[x+4]=='*':
                    answer+=int(b[x-1])**2*2
                elif b[x+1]=='#'or b[x+3]=='#'or b[x+4]=='#':
                    answer-=int(b[x-1])**2
                else:
                    answer+=int(b[x-1])
            except:
                answer+=int(b[x-1])**2
        elif b[x]=='T':
            try:
                if b[x+1]=='*'or b[x+3]=='*'or b[x+4]=='*':
                    answer+=int(b[x-1])**3*2
                elif b[x+1]=='#'or b[x+3]=='#'or b[x+4]=='#':
                    answer-=int(b[x-1])**3
                else:
                    answer+=int(b[x-1])
            except:
                answer+=int(b[x-1])**3

    return answer
"""
def solution(dartResult):
    n = ''
    score = []
    for i in dartResult:
        if i.isnumeric():
            n += i
        elif i == 'S':
            n = int(n)**1
            score.append(n)
            n = ''
        elif i == 'D':
            n = int(n)**2
            score.append(n)
            n = ''
        elif i == 'T':
            n = int(n)**3
            score.append(n)
            n = ''
        elif i == '*':
            if len(score) > 1:
                score[-2] = score[-2] * 2
                score[-1] = score[-1] * 2
            else:
                score[-1] = score[-1] * 2
        elif i == '#':
            score[-1] = score[-1] * -1
        
    return sum(score)
    
#print(solution("1S2D*3T"))
print(solution("1T2D3D#"))
print(solution("1D2S#10S"))
