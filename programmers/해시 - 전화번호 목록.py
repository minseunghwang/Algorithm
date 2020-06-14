def solution(phone_book):
    answer = True
    phone_book.sort(key=len)
    print(phone_book)
    for i in range(len(phone_book)):
        l = len(phone_book[i])
        for j in range(i+1,len(phone_book)):
            if phone_book[i] == phone_book[j][:l]:
                print(phone_book[i], phone_book[j])
                return False


    return answer

phone_book = ['119', '97674223', '1195524421']
# phone_book = ['123','456','789']
phone_book = ['12','123','1235','567','88']
print(solution(phone_book))
