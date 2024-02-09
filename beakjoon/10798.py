arr = [[-1 for col in range(15)] for row in range(5)]
for x in range(5):
    arr[x] = input()
for x in range(5):
    for y in range(15):
        try:
            if arr[y][x]==-1:
                continue
            else:
                print(arr[y][x],end='')
        except:
            pass

