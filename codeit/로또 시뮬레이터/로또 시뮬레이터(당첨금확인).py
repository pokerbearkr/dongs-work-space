def count_matching_numbers(numbers, winning_numbers):
    # 지난 실습의 코드를 여기에 붙여 넣으세요
    count=0
    for x in numbers:
        if x in winning_numbers:
            count+=1
            
    return count

def check(numbers, winning_numbers):
    # 여기에 코드를 작성하세요
    tem=count_matching_numbers(numbers,winning_numbers[:-1])
    answer = 0
    if tem ==6:
        return 1000000000
    elif tem ==5:
        if winning_numbers[-1] in numbers:
            return 50000000
        else:
            return 1000000
    elif tem==4:
        return 50000
    elif tem==3:
        return 5000
    else:
        return 0
    

# 테스트 코드
print(check([2, 4, 11, 14, 25, 40], [4, 12, 14, 28, 40, 41, 6]))
print(check([2, 4, 11, 14, 25, 40], [2, 4, 10, 11, 14, 40, 25]))