"""def solution(participant, completion):
    par=participant
    for x in completion:
        if x in participant:
            par.remove(x)
        else:
            1

    return par[0]

print(solution(["leo", "kiki", "eden"]  ,["eden", "kiki"]))
""" # 효율성테스트 0점

def solution(participant, completion):
    participant.sort()
    completion.sort()
    for x,y in zip(participant,completion):
        if x!=y:
            return x

    return participant.pop()
print(solution(["leo", "kiki", "eden"]  ,["eden", "kiki"]))