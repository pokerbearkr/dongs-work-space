def solution(nums):
    tem=set(nums)
    if len(tem)<(len(nums)/2):
        return len(tem)
    else:
        return int(len(nums)/2)


print(solution([3,1,2,3]))
print(solution([3,3,3,2,2,4]))