def solution(s):
    answer = ''
    l = len(s)

    for i in range(1,l//2+1):
        temp = s[:i]
        cnt = 0
        for j in range(1,l-1+i):
            if temp == s[j:j+i]:
                cnt += 1
            else:
                temp = s[j:j+i]







    return answer


s = 'aabbaccc' # 7
# s = 'ababcdcdababcdcd' # 9
# s = 'abcabcdede' # 8
# s = 'abcabcabcabcdededededede' # 14

print(solution(s))