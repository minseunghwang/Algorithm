def solution(bridge_length, weight, truck_weights):
    answer = 0

    now = [0 for _ in range(bridge_length)]

    while truck_weights:
        answer += 1
        print(truck_weights)
        if sum(now) + truck_weights[0] <= weight:
            now.append(truck_weights.pop(0))
        else:
            now.append(0)
        now.pop(0)

    return answer

bridge_length = 100
weight = 100
truck_weights = [10]
print(solution(bridge_length, weight, truck_weights))