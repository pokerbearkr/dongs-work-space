from random import randint


def generate_numbers(n):
    # 여기에 코드를 작성하세요
    answer=[]
    answer.append(randint(1,45))
    for x in range(1,n):
        while True:
            tem=randint(1,45)
            if tem not in answer:
                answer.append(tem)
                break
    return answer
        

# 테스트 코드
print(generate_numbers(6))