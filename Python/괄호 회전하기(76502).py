"""def solution(s):
    if len(s)%2==1:
        return 0
    count=0
    t=list(map(str,s))
    t1=t
    while len(t)>0:
        x=0
        if ord(t[x])==91:
            for y in range(x+1,len(t)):
                if ord(t[y])==93:
                    del[t[x]]
                    del[t[y-1]]
                    break
        elif ord(t[x])==40:
            for y in range(x+1,len(t)):
                if ord(t[y])==41:
                    del[t[x]]
                    del[t[y-1]]
                    
                    break
        elif ord(t[x])==123:
            for y in range(x+1,len(t)):
                if ord(t[y])==125:
                    del[t[x]]
                    del[t[y-1]]
                    
                    break
        else:
            if count==len(t):
                return 0
            count+=1
            
            t1.append(t1[0])
            del(t1[0])
            t=t1
    return count

print(solution("[](){}"))
print(solution("])[({}"))

""" # 문제 잘못봐서 잘못만듬 왼쪽으로 몇번 돌아야 괄호가 완성되는지 문제로 만듬

def solution(s):
    answer = 0
    temp = list(s)
    
    for _ in range(len(s)):
 
        st = []
        for i in range(len(temp)):
            if len(st) > 0:
                if st[-1] == '[' and temp[i] == ']':
                    st.pop()
                elif st[-1] == '(' and temp[i] == ')':
                    st.pop()
                elif st[-1] == '{' and temp[i] == '}':
                    st.pop()
                else:
                    st.append(temp[i])
            else:
                st.append(temp[i])
        if len(st) == 0:
            answer += 1
        temp.append(temp.pop(0))
 
    return answer