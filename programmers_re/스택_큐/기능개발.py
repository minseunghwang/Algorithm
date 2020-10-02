def solution(progresses, speeds):
    import math
    answer = []
    p = [math.ceil((100-i)/j) for i,j in zip(progresses,speeds)]
    print(p)
    i = 0
    for idx in range(1,len(p)):
        if p[i] < p[idx]:
            answer.append(idx-i)
            i = idx
    answer.append(len(p)-i)
    return answer

progresses = [93,30,55]
progresses = [95, 90, 99, 99, 80, 99]
speeds = [1,50,1]
speeds = [1, 1, 1, 1, 1, 1]
print(solution(progresses, speeds))