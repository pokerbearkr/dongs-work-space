def solution(want, number, discount):
    count=0
    for x in range(len(want)):
        tem=discount[x:x+10]
        try:
            for x in range(len(want)):
                for y in range(number[x]):
                    tem.remove(want[x])
            count+=1
        except:
            continue   


    return count

print(solution(["banana", "apple", "rice", "pork", "pot"],[3, 2, 2, 2, 1],["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))