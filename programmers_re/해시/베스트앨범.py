from collections import defaultdict
import operator
def solution(genres, plays):
    answer = []

    d = defaultdict(int)
    for i in range(len(genres)):
        d[genres[i]] += plays[i]

    d = sorted(d.items(), key=operator.itemgetter(1),reverse=True)
    print(d)
    for i in d:
        temp = []
        for cnt in range(len(genres)):
            if i[0] == genres[cnt]:
                temp.append([plays[cnt],cnt])
        print(temp)
        temp.sort(reverse=True, key=operator.itemgetter(0))
        print(temp)
        for j in range(len(temp[:2])):
            answer.append(temp[j][1])

    return answer


genres = ['classic', 'pop', 'classic', 'classic', 'pop', 'tory']
plays = [500, 600, 150, 800, 2500, 300]
print(solution(genres,plays))