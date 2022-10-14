def solution(dirs):
    answer=0
    now=[0,0]
    arr=[]
    for r in range(0,len(dirs)):
        if dirs[r]=="U":
            arr.append([now,[x+y for x,y in zip(now, [0,1])]])
            now=[x+y for x,y in zip(now, [0,1])]
            if now[1]>5:
                arr.pop()
                now=[x+y for x,y in zip(now, [0,-1])]
        elif dirs[r]=="D":
            arr.append([now,[x+y for x,y in zip(now, [0,-1])]])
            now=[x+y for x,y in zip(now, [0,-1])]
            if now[1]<-5:
                arr.pop()
                now=[x+y for x,y in zip(now, [0,1])]
        elif dirs[r]=="R":
            arr.append([now,[x+y for x,y in zip(now, [1,0])]])
            now=[x+y for x,y in zip(now, [1,0])]
            if now[0]>5:
                arr.pop()
                now=[x+y for x,y in zip(now, [-1,0])]
        else:
            arr.append([now,[x+y for x,y in zip(now, [-1,0])]])
            now=[x+y for x,y in zip(now, [-1,0])]
            if now[0]<-5:
                arr.pop()
                now=[x+y for x,y in zip(now, [1,0])]
    arr1=[]
    for x in arr:
        if x not in arr1:
            arr1.append(x)
            answer+=1
    return answer

print(solution("ULURRDLLU"))