def solution(N, coffee_times):
    answer = []
    tmp = coffee_times[:N]
    idx = [i for i in range(N)]
    while tmp:
        mn = min(tmp)
        for i in range(len(tmp)):
            tmp[i] -= mn
            if tmp[i] == 0:
                answer.append(idx[i])
                tmp[i] = coffee_times[N]
                idx[i] = N
                N += 1
            if N >= len(coffee_times):
                while tmp:
                    iid = tmp.index(min(tmp))
                    tmp.pop(iid)
                    answer.append(idx.pop(iid))
                for i in range(len(answer)):
                    answer[i] += 1
                return answer
    return answer
N = 3
coffee_times = [4, 2, 2, 5, 3]
# coffee_times = [100, 1, 50, 1, 1]
print(solution(N,coffee_times))
