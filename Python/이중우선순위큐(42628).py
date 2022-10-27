from re import I


def solution(operations):
    que=[]
    for x in operations:
        tem=x.split()
        if tem[0]=='I':
            que.append(int(tem[1]))
        elif x=="D 1":
            if len(que)==0:
                pass
            else:
                n=int(max(que))
                que.remove(n)
        elif x=="D -1":
            if len(que)==0:
                pass
            else:
                n=int(min(que))
                que.remove(n)
    if len(que)==0:
        return [0,0]

    return [max(que),min(que)]

print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]	))

# 작동은 하지만 출제자가 의도한 정답은 아님 heapq 자료구죠 사용해야함