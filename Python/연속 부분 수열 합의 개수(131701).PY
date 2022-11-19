def solution(elements):
    answer=set()
    work=elements+elements
    for x in range(len(elements)):
        for y in range(len(elements)):
            tem=sum(work[y:x+y+1])
            answer.add(tem)
    return len(answer)


print(solution([7,9,1,1,4]))