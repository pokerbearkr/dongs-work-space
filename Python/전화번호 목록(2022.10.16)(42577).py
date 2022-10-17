def solution(phone_book):
    
    phone_book.sort()
    for x in range(len(phone_book)):
        try:
            for y in range(x+1,x+2):
                if phone_book[x]==phone_book[y][0:len(phone_book[x])]:
                    return False
        except:
            1

    return True


print(solution(["123","456","789"]))
print(solution(["119", "97674223", "1195524421"]))