def solution(strings, n):
    answer=[]
    for x in range(len(strings)):
        strings[x]=strings[x][n]+strings[x]

    strings.sort()
    for x in range(len(strings)):
        answer.append(strings[x][1:])
         
    return answer

# Test Case # print(solution(["sun","bed","car"],1))