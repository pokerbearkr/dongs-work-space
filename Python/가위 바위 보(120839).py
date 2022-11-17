def solution(rsp):
    answer =[]
    for x in range(len(rsp)):
        if rsp[x]=="2":
            answer.append("0")
        elif rsp[x]=="0":
            answer.append("5")
        else:
            answer.append("2")
    return "".join(answer)

print(solution("205"))