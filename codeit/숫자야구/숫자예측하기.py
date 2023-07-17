def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")
    
    new_guess = []
    # 여기에 코드를 작성하세요
    tem=input("1번째 숫자를 입력하세요:")
    new_guess.append(tem)
    while len(new_guess)<2:
        tem=input("2번쨰 숫자를 입력하세요:")
        if int(tem)>10 or int(tem)<0:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
        elif tem not in new_guess:
            new_guess.append(tem)
        else:
            print("중복되는 숫자입니다. 다시 입력하세요.")
            
    while len(new_guess)<3:
        tem=input("3번쨰 숫자를 입력하세요:")
        if int(tem)>10 and int(tem)<0:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
        elif tem not in new_guess:
            new_guess.append(tem)
        else:
            print("중복되는 숫자입니다. 다시 입력하세요.")
            
    return new_guess
    
    
# 테스트 코드
print(take_guess())