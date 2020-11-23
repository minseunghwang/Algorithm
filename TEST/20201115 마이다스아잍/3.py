def solution(cookies,k):
    answer = []
    queue = []
    for i in range(len(cookies)):
        queue.append([[cookies[i]], cookies[i+1:]])

    while queue:
        n = queue.pop()

        if n[1] == []:
            answer.append(n[0])
            continue

        e = n[1].pop(0)
        if e > n[0][-1]:
            queue.append([n[0][:] + [e], n[1][:]])
        queue.append([n[0][:], n[1][:]])

    max_ = max(len(x) for x in answer)
    maxcookies = sorted(list(x for x in answer if len(x) == max_))
    return maxcookies[k-1]


cookies = [1,4,2,6,5,3]
k = 2

print(solution(cookies,k))