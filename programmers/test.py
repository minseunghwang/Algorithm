def solution(n):
    answer = [0]
    for _ in range(n-1):
        ans = reversed(answer)
        answer.append(0)
        for i in ans:
            if i == 1:
                answer.append(0)
            else:
                answer.append(1)


    return answer

def solution2(n):
    answer = [0]
    for _ in range(n-1):
        answer.append(0)
        answer += [i^1 for i in reversed(answer)]

    return answer


n = 3
# print(solution(n))
print(solution2(n))

# 0
# 0, 0, 1
# 0,0,1, 0, 0,1,1
# 0,0,1,0,0,1,1, 0, 0,0,1,1,0,1,1


