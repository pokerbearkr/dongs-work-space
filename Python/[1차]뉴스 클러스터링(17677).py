from collections import Counter
def solution(str1, str2):
    str11=str1.upper()
    str22=str2.upper()
    sum1=[]
    sum2=[]
    for x in range(len(str11)-1):
        if str11[x].isalpha() and str11[x+1].isalpha():
            sum1.append(str11[x:x+2])
    for x in range(len(str22)-1):
        if str22[x].isalpha() and str22[x+1].isalpha():
            sum2.append(str22[x:x+2])
    Counter1 = Counter(sum1)
    Counter2 = Counter(sum2)
    
    inter = list((Counter1 & Counter2).elements())
    union = list((Counter1 | Counter2).elements())
    
    if len(union) == 0 and len(inter) == 0:
        return 65536
    else:
        return int(len(inter) / len(union) * 65536)


print(solution("FRANCE","french"))