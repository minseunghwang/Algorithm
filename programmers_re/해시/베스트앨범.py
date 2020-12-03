from collections import defaultdict
import operator
def solution(genres, plays):
    answer = []

    d = defaultdict(int)
    for i in range(len(genres)):
        d[genres[i]] += plays[i]
    print(d)
    d = sorted(d.items(), key=operator.itemgetter(1))
    print(d)



    return answer


genres = ['sexy', 'classic', 'pop', 'classic', 'classic', 'pop']
plays = [5000, 500, 600, 150, 800, 2500]
print(solution(genres,plays))