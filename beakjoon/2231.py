n = str(input())
ans = 0
for i in range(1,int(n),1):
    tem = 0
    a=str(i)
    for j in range(len(str(i))):
        tem += int(a[j])
    if int(n) == i + tem:
        ans = i
        print(i)
        break
if ans == 0:
    print('0')
