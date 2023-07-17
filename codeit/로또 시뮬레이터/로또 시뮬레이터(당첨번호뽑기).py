from random import randint


def generate_numbers(n):
    # 지난 실습의 코드를 여기에 붙여 넣으세요
    answer=[]
    answer.append(randint(1,45))
    for x in range(1,n):
        while True:
            tem=randint(1,45)
            if tem not in answer:
                answer.append(tem)
                break
    return answer

def draw_winning_numbers():
    # 여기에 코드를 작성하세요
    answer=[]
    answer.append(randint(1,45))
    for x in range(1,6):
        while True:
            tem=randint(1,45)
            if tem not in answer:
                answer.append(tem)
                break
    answer.sort()
    while True:
        tem=randint(1,45)
        if tem not in answer:
            answer.append(tem)
            break
    return answer

# 테스트 코드
print(draw_winning_numbers())