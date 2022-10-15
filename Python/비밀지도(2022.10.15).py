"""def solution(n, arr1, arr2):
    answer1=[]
    answer2=[]
    answer3=[]
    for x in range(len(arr1)):
        answer1.append(str(bin(arr1[x])[2:]))
        answer1[x]=answer1[x].zfill(n)
    for x in range(len(arr2)):
        answer2.append(str(bin(arr2[x])[2:]))
        answer2[x]=answer2[x].zfill(n)
    for x in range(n):
        for y in range(n):
            if answer1[x][y]=="1"or answer2[x][y]=="1" :
                answer3.append("1")
            else:
                answer3.append("0")
    answer3=answer3.replace("1","#")
    print(answer3)
    


    return answer1,answer2
"""
def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        tmp = bin(arr1[i] | arr2[i])
        # tmp결과 ex) '0b1101' #비트연산
        tmp = tmp[2:].zfill(n)
        # tmp결과 ex) '01101'  #zfill함수
        tmp = tmp.replace('1','#').replace('0',' ')
        # tmp결과 ex) ' ## #'  #replace함수
        answer.append(tmp)
    
    return answer
print(solution(5,[9,20,28,18,11],[30,1,21,17,28]))
