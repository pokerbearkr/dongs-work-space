def solution(s, n):
    answer=[]
    for x in range(len(s)):
        if s[x]==" ":
            answer.append(" ")
        else:
            if ord(s[x])>=ord("a") and ord(s[x])<=ord("z"):
                if ord(s[x])+int(n)>ord("z"):
                    answer.append(chr(int(ord(s[x])+int(n)-26)))
                else:
                    answer.append(chr(int(ord(s[x])+int(n))))
            else:
                if ord(s[x])+int(n)>ord("Z"):
                    answer.append(chr(int(ord(s[x])+int(n)-26)))
                else:
                    answer.append(chr(int(ord(s[x])+int(n))))
    return "".join(answer)

#Test Case # print(solution("AB"))