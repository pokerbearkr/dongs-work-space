def solution(n, arr1, arr2):
    answer1=[]
    answer2=[]
    answer3=[]
    for x in range(len(arr1)):
        answer1.append(str(bin(arr1[x])[2:]))
    for x in range(len(arr2)):
        answer2.append(str(bin(arr2[x])[2:]))

    


    return answer1,answer2

print(solution(5,[9,20,28,18,11],[30,1,21,17,28]))
