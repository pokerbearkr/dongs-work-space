def solution(sizes):
    arr1=[]
    arr2=[]
    for x in sizes:
        arr1.append(min(x))
        arr2.append(max(x))
    return max(arr1)*max(arr2)

#Test Case # print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))