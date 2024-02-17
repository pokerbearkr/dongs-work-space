num = int(input())
if num == 4 or num == 7:
    print('-1')
else:
    answer = (num // 5) + (num % 5) // 3
    num = (num % 5) % 3

    if num == 0:
        print(answer)
    elif num == 1:
        print(answer + 1)
    else:
        print(answer + 2)
