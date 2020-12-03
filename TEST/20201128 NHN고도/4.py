def solution(self, cardNumber):
    lst = list(cardNumber)


    if len(cardNumber) % 2 == 1:
        for i in range(len(cardNumber)):
            if i % 2 == 1:
                lst[i] = str(int(lst[i]) * 2)
    else:
        for i in range(len(cardNumber)):
            if i % 2 == 0:
                lst[i] = str(int(lst[i]) * 2)
    answer = 0
    for i in range(len(lst)):
        answer += sum(map(int, list(lst[i])))
    if answer % 10 == 0:
        return 'VALID'
    return 'INVALID'

cardNumber = "21378"
# cardNumber = "11111101"
print(solution(cardNumber))
