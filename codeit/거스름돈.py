def calculate_change(payment, cost):
    change=payment-cost
    if change>=50000:
        print("50000원 지폐: {0}장",(change//50000))
    return 0
    


# 테스트 코드
calculate_change(100000, 33000)
print()
calculate_change(500000, 378000)