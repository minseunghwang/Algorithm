from collections import defaultdict
def solution(movie):
    answer = []
    d = defaultdict(int)
    for i in movie:
        d[i] += 1
    x = sorted(d.items(), key=lambda x:(-x[1],x[0]))
    for i in x:
        answer.append(i[0])

    return answer