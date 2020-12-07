def solution(numbers):


    num = list(map(str,numbers))
    num.sort(key=lambda x:x*3, reverse=True)
    print(''.join(num))
    return int(''.join(num))

numbers = [6, 10, 2]
# numbers = [3, 30, 34, 5, 9, 31]
print(solution(numbers))