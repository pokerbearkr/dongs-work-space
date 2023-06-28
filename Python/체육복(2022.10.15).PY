"""def solution(n, lost, reserve):
    result=n-len(lost)
    for x in reserve:
        if x+1 in lost or x-1 in lost:
            result+=1
        if x+1 in lost and x-1 in lost:
            result-=1

    return result
"""
#???????????
def solution(n, lost, reserve):
    reserve_set = set(reserve)-set(lost) 
    lost_set = set(lost)-set(reserve) 
    
    for reserve_person in reserve_set: 
        if reserve_person-1 in lost_set: 
            lost_set.remove(reserve_person-1) 
        elif reserve_person+1 in lost_set: 
            lost_set.remove(reserve_person+1) 
    
    return n-len(lost_set)

print(solution(5,[2,4],[3]))
