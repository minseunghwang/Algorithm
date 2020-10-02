def solution(N, coffee_times):
    answer = []
    tmp = coffee_times[:N]
    j = 0
    while tmp:
        print(tmp)
        mn = min(tmp)
        if mn == 0:
            tmp.remove(0)
        for i in range(len(tmp)):
            tmp[i] -= mn
            if tmp[i] == 0 and j < len(coffee_times) - N:
                tmp[i] = coffee_times[N+j]
                j += 1
                answer.append(i)



    return answer

N = 3
coffee_times = [4, 2, 2, 5, 3]
print(solution(N,coffee_times))