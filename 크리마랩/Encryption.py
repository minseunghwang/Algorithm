import math
def encryption(s):
    a = len(s) ** 0.5
    answer = [[] for i in range(math.ceil(a))]

    for cnt, i in enumerate(s):
        answer[cnt % math.ceil(a)].append(i)
    ans = []
    for i in answer:
        ans.append(''.join(i))
    return ' '.join(ans)

s = 'chillout'
print(encryption(s))