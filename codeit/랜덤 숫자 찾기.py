import random

answer=random.randint(1,20)
yours=int(input("기회가 4번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요:"))
if answer==yours:
    print("축하합니다. 1번만에 숫자를 맞히셨습니다.")
elif answer>yours:
    print("Up")
else:
    print("Down")
yours=int(input("기회가 3번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요:"))
if answer==yours:
    print("축하합니다. 2번만에 숫자를 맞히셨습니다.")
elif answer>yours:
    print("Up")
else:
    print("Down")
yours=int(input("기회가 2번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요:"))
if answer==yours:
    print("축하합니다. 3번만에 숫자를 맞히셨습니다.")
elif answer>yours:
    print("Up")
else:
    print("Down")
yours=int(input("기회가 1번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요:"))
if answer==yours:
    print("축하합니다. 4번만에 숫자를 맞히셨습니다.")
else:
    print("아쉽습니다. 정답은 {}였습니다".format(answer))