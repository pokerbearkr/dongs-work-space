"""def solution(n, left, right):
    arr=[[0]*n]*n
    arr1=[]
    for x in range(n):
        for y in range(n):
            arr[x][y]=max(x,y)+1
            arr1.append(arr[x][y])
            print(arr[x][y],end=" ")
        print()
    
    return arr1[left:right+1]
""" # 시간초과 획기적으로 줄여야함

def solution(n, left, right):
    arr=[[0]*n]*n
    arr1=[]
    count=0
    for x in range(n):
        for y in range(n):
            
            count+=1
            if count>left:
                arr[x][y]=max(x,y)+1
                arr1.append(arr[x][y])
            if count>right:
                break
    
    return arr1[:]
print(solution(3,2,5))
print(solution(4,7,14))
