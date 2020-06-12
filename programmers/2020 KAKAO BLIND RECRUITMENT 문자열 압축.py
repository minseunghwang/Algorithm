def solution(s):
    answer = ''
    l = len(s)

    temp = 0
    for i in range(1,l//2+1):
        count = 1
        tempStr = s[:i]
        for j in range(i,l,i):
            if s[j:j+i] == tempStr:
                count += 1


    return answer


# s = 'aabbaccc' # 7
s = 'ababcdcdababcdcd' # 9
# s = 'abcabcdede' # 8
# s = 'abcabcabcabcdededededede' # 14

print(solution(s))