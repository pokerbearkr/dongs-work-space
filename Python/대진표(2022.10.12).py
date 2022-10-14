import math
def solution(n,a,b):
    count=1
    while True:
        if math.ceil(a/2)==math.ceil(b/2):
            return count
        else:
            a=math.ceil(a/2)
            b=math.ceil(b/2)
            count+=1

print(solution(8,4,7))