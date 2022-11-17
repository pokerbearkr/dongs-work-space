def solution(A, B):
    tem=list(A)
    tem2=list(B)
    count=0
    if tem==tem2: #A==B일때 바로 출력
        return 0
    for x in range(len(tem)):
        if tem==tem2:
            return len(tem)-count
        else:  # deque을 써서 retate함수를 쓰면 편하게 회전 가능하다
            tem.append(tem[0])
            tem.remove(tem[0])
            count+=1

    return -1


print(solution("hello","ohell"))