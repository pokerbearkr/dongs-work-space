list=[0 for i in range(30)]
for x in range(28):
    list[int(input())-1]=1
for x in range(30):
    if list[x]==0:
        print(x+1)
