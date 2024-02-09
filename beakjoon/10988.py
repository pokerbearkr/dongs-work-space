word = input()
t = 0
for x in range(len(word)):
    if word[x] != word[-x - 1]:
        print('0')
        t += 1
        break
    else:
        continue
if t==0:
    print('1')
