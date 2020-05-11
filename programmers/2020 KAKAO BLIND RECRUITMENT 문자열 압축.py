def solution(s):
    answer = ''

    for i in range(1,len(s)//2+1):
        temp = s[:i]
        cnt = 1
        for j in range(i,len(s),i):
            if temp == s[i:j]:
                cnt += 1
            else:
                if cnt != 1:
                    answer += (str(cnt) + temp)
                    temp = s[i:j]
                    cnt = 1
        print(answer)

    return answer


# s = 'aabbaccc' # 7
s = 'ababcdcdababcdcd' # 9
# s = 'abcabcdede' # 8
# s = 'abcabcabcabcdededededede' # 14

print(solution(s))