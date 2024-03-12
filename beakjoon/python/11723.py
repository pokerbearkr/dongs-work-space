import sys
input = sys.stdin.readline

m = int(input())
arr = set()
for x in range(m):
    order = list(input().split())
    if order[0] == 'add':
        arr.add(order[1])
    elif order[0] == 'remove':
        try:
            arr.remove(order[1])
        except:
            pass
    elif order[0] == 'check':
        if order[1] in arr:
            print('1')
        else:
            print('0')
    elif order[0] == 'toggle':
        if order[1] in arr:
            arr.remove(order[1])
        else:
            arr.add(order[1])
    elif order[0] == 'all':
        arr.update(
            ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
             '20'])
    elif order[0] == 'empty':
        arr.clear()
