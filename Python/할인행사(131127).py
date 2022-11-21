def solution(want, number, discount):
    count=0
    for x in range(len(discount)): 
        tem=discount[x:x+10]    # 10일동안 판매하는 목록
        try:
            for x in range(len(want)):
                for y in range(number[x]):
                    tem.remove(want[x])
            count+=1
        except: # 안팔면 넘어가기
            continue   


    return count

#  print(solution(["banana", "apple", "rice", "pork", "pot"],[3, 2, 2, 2, 1],["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))