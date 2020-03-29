def solution(N):
    ms = [1, 1]
    if N >= 3:
        for i in range(N - 2):
            ms.append(ms[-1] + ms[-2])

    return ms[-1] * 2 + (ms[-2] + ms[-1]) * 2


N = 5 # 26
N = 6 # 42
print(solution(N))



