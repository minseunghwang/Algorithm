def solution(budgets, M):
    answer = 0
    low = 0
    high = max(budgets)

    while high >= low:
        mid = (low + high) // 2
        temp = 0
        for i in budgets:
            if i > mid:
                temp += mid
            else:
                temp += i
        print(low, high, mid, temp)
        if temp > M:
            high = mid - 1
        else:
            low = mid + 1
            answer = mid

    return answer


budgets = [120, 110, 140, 150]
M = 485
print(solution(budgets, M))