from random import randint


def generate_numbers():
    numbers = []
    while True:
        tem=randint(0,9)
        if tem not in numbers:
            numbers.append(tem)
        if len(numbers)==3:
            print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
            return numbers

def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")
    
    new_guess = []
    tem=int(input("1번째 숫자를 입력하세요:"))
    new_guess.append(tem)
    while len(new_guess)<2:
        tem=int(input("2번쨰 숫자를 입력하세요:"))
        if int(tem)>10 or int(tem)<0:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
        elif tem not in new_guess:
            new_guess.append(tem)
        else:
            print("중복되는 숫자입니다. 다시 입력하세요.")
            
    while len(new_guess)<3:
        tem=int(input("3번쨰 숫자를 입력하세요:"))
        if int(tem)>10 and int(tem)<0:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
        elif tem not in new_guess:
            new_guess.append(tem)
        else:
            print("중복되는 숫자입니다. 다시 입력하세요.")
            
    return new_guess

def get_score(guesses, solution):
    strike_count = 0
    ball_count = 0
    for x in range(3):
        if guesses[x]==solution[x]:
            strike_count+=1
        if guesses[x] in solution:
            ball_count+=1
    return strike_count, ball_count-strike_count

# 여기서부터 게임 시작!
ANSWER = generate_numbers()
tries = 0
count_s=0
count_b=0
while True:
    tries+=1
    guess=take_guess()
    count_s,count_b=get_score(guess,ANSWER)
    if count_s==3:
        print("축하합니다. {}번 만에 숫자 3개의 값과 위치를 모두 맞히셨습니다.".format(tries))
        break
    print("{}S {}B".format(count_s,count_b))
        
# 여기에 코드를 작성하세요

print("축하합니다. {}번 만에 숫자 3개의 값과 위치를 모두 맞히셨습니다.".format(tries))