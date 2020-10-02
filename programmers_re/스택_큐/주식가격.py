def solution(prices):
    answer = []
    q = [0 for i in range(len(prices))]

    for i in range(0,len(prices)):
        for j in range(i+1,len(prices)):
            if prices[i] <= prices[j]:
                q[i] += 1
            else:
                q[i] += 1
                break
    print(q)

    return answer

prices = [1, 2, 3, 2, 3]

solution(prices)