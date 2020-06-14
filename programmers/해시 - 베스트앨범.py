from collections import defaultdict
import operator
def solution(genres, plays):
    answer = []

    d1 = defaultdict(int)
    for i,j in zip(genres,plays):
        d1[i] += j
    ms = sorted(d1.items(),key = operator.itemgetter(1),reverse=True)
    for i in ms:
        t = []
        for cnt,j in enumerate(genres):
            if i[0] == j:
                t.append([plays[cnt],cnt])
        temp = sorted(t, key = lambda x:x[0], reverse=True)
        for j in temp[:2]:
            answer.append(j[1])

    return answer


genres = ['classic', 'pop', 'classic', 'classic', 'pop','jazz']
plays = [500, 600, 150, 800, 2500, 5000]
print(solution(genres,plays))