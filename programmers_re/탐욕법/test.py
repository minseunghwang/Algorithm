def solution(triangle):
    answer = 0
    for i in range(len(triangle)):
        for j in range(i):
            print(j)

    return answer


triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(triangle))