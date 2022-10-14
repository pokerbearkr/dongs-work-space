def solution(s):
    answer=[]
    for x in range(len(s)):
        if s[x]!=" ":
            if x%2==1:
                if ord(s[x])>=ord("a") and ord(s[x])<=ord("z"):
                    answer.append(s[x])
                else:
                    answer.append(chr(int(ord(s[x])+int(32))))

            else:
                if ord(s[x])>=ord("A") and ord(s[x])<=ord("Z"):
                    answer.append(s[x])
                else:
                    answer.append(chr(int(ord(s[x])-int(32))))
        else:
            answer.append(" ")
    return "".join(answer)
    

print(solution("try  hello world"))