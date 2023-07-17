def count_matching_numbers(numbers, winning_numbers):
    # 여기에 코드를 작성하세요
    count=0
    for x in numbers:
        if x in winning_numbers:
            count+=1
            
    return count

# 테스트 코드
print(count_matching_numbers([2, 7, 11, 14, 25, 40], [2, 11, 13, 14, 30, 35]))
print(count_matching_numbers([2, 7, 11, 14, 25, 40], [14])) 