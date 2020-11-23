def solution(openA, closeB):
    answer = 0
    now = 0
    while openA:
        a = openA.pop(0)
        while a < now and len(openA) > 0:
            a = openA.pop(0)
        if len(openA) == 0 and a < now:
            return answer
        b = closeB.pop(0)
        while a > b:
            b = closeB.pop(0)
        answer  += b-a
        now = b
    return answer



openA = [4, 7, 9, 16]
openA = [3, 5, 7]
closeB = [2, 5, 12, 14, 20]
closeB = [4, 10, 12]
print(solution(openA,closeB))