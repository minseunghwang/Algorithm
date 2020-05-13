import math
def encryption(s):
    answer = []
    a = len(s) ** 0.5

    for cnt,i in enumerate(s):
        if cnt != 0 and cnt%math.floor(a) == 0:
            answer += ' '
        answer += i

    return ''.join(answer)


s = 'haveaniceday'
print(encryption(s))