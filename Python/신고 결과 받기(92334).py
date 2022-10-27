def solution(id_list, report, k):
    report_count=[0]*len(id_list)
    reported_count=[0]*len(id_list)
    overlap=[]
    for x in report:
        if x in overlap:
            pass
        else:
            overlap.append(x)
            n=x.split()
            report_count[id_list.index(n[0])]+=1
            reported_count[id_list.index(n[1])]+=1
            print(n)

    answer = []
    return answer

print(solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2))