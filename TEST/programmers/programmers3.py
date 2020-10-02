def solution(numbers, k):
    answer = 0

    def solv(q):
        while q:
            print(q)
            p = q.pop(0)
            for i in range(l-1):
                if abs(p[i]-p[i+1]) > k:
                    break

    l = len(numbers)
    q = [numbers]

    while True:
        solv(q)
        for i in range(l-1):
            pp = p.copy()
            pp[i+1], pp[i] = p[i], p[i+1]
            q.append(pp)



    return answer


numbers = [10, 40, 30, 20]
k = 20
print(solution(numbers, k))