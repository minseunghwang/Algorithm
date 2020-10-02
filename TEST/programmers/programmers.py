def solution(p,s):
    answer = 0

    for i,j in zip(p,s):
        ans = abs(int(i)-int(j))
        if ans <= 5:
            answer += ans
        else:
            answer += 10 - ans

    return answer


# p = '82195'
p = '00000000000000000000'
# s = '64723'
s = '91919191919191919191'
print('답',solution(p,s))
