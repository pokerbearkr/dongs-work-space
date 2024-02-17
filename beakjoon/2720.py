n = int(input())
for _ in range(n):
    quarter, dime, nickel, penny = 0, 0, 0, 0
    change = int(input())
    if change >= 25:
        quarter = change // 25
        change = change % 25
    if change >= 10:
        dime = change // 10
        change = change % 10
    if change >= 5:
        nickel = change // 5
        change = change % 5
    penny = change
    print(quarter, dime, nickel, penny)
