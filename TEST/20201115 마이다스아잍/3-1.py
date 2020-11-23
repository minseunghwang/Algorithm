def cookies_root(now, b):
    print(now,b)
    if not b:
        return now
    if b[0] > now[-1]:
        now.append(b.pop(0))
        cookies_root(now,b)
    else:
        b.pop(0)
        cookies_root(now, b)
    return now

def solution(cookies,k):
    answer = []
    q = []
    for i in range(len(cookies)):
        q.append([[cookies[i]], cookies[i+1:]])
    print(q)
    while q:
        now, b = q.pop(0)
        answer.append(cookies_root(now, b))
    return answer


cookies = [1,4,2,6,5,3]
k = 2

print(solution(cookies,k))