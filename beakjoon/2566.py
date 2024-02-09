arr = [[0 for col in range(9)] for row in range(9)]
for x in range(9):
    arr[x] = (list(map(int, input().split())))
max_num, max_col, max_row = 0, 0, 0
for x in range(9):
    for y in range(9):
        if arr[x][y] >= max_num:
            max_num = arr[x][y]
            max_col = x + 1
            max_row = y + 1
print(max_num)
print(max_col, max_row)
