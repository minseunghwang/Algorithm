def solution(phone_book):
    l = len(phone_book)
    phone_book.sort()
    print(phone_book)
    for i in range(l-1):
        for j in range(i+1,l):
            print(phone_book[i], phone_book[j])
            if len(phone_book[i]) <= len(phone_book[j][:len(phone_book[i])]):
                if phone_book[i] == phone_book[j][:len(phone_book[i])]:
                    return False
    return True

phone_book = ['12','123','1235','567','88']
phone_book = ['123','456','789','78','45']
# phone_book = ['12','123','1235','567','88']

print(solution(phone_book))