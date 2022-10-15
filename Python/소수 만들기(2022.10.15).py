from itertools import combinations
def solution(nums):
    result=0
    t=list(combinations(nums,3))
    for x in range(len(t)):
        count=0
        for y in range(1,sum(t[x])):
            if sum(t[x])%y==0:
                count+=1
        if count==1:
            result+=1

# Test Case # print(solution([1,2,3,4]))