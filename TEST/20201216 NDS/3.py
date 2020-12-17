def solution(s):
    answer = 0
    l = len(s)
    max_ = 0
    for i in range(2, (len(s)//2) + 1):
        if l%i == 0:
            max_ = max(max_, i)

    for i in range(max_,0,-1):
        temp = s[:i]
        for j in range(i,l,i):
             if temp != s[j:j+j]:
                 break
        else:
            answer = l // i
            return answer
    return answer


# s  = "abcabcabc"
s  = "abababab"
print(solution(s))