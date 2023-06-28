def solution(name, yearning, photo):
    answer = [0]
    for x in range(len(photo)-1):
        answer.append(0)
    for x in range(len(photo)):
        for y in name:
            if y in photo[x]:
                answer[x]+=yearning[name.index(y)]

    return answer

print(solution(["may", "kein", "kain", "radi"],[5, 10, 1, 3],[["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]))