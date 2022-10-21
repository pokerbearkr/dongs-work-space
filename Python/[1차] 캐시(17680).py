def solution(cacheSize, cities):
    tem=[]
    count=0
    test=[]
    for x in cities:
        test.append(x.lower())
    if cacheSize ==0:
        return len(cities)*5
    for x in test:
        if x in tem:
            count+=1
            del tem[tem.index(x)]
            tem.append(x)
        else:
            count+=5
            if len(tem)==cacheSize:
                del tem[0]
            tem.append(x)
        
    
    return count


# print(solution(3,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
# print(solution(3,["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
# print(solution(0,["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))