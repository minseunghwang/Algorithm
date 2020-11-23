import math

def isPrime(n):
    if n == 1:
        return 1

    num = int(math.sqrt(n))
    answer = []
    for i in range(2, num + 1):
        if n % i == 0:
            answer.append(i)
    print(answer)
    if len(answer) != 0:
        return answer[-1]
    return 1


n = 4
print(isPrime(n))