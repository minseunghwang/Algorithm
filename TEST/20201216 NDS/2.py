import copy
from collections import defaultdict
import operator
def solution(K, user_scores):
    answer = 0
    ranking = defaultdict(int)
    for user_socre in user_scores:
        temp = copy.deepcopy(ranking)
        a, b = user_socre.split(" ")
        if ranking[a]:
            ranking[a] = max(int(b), ranking[a])
        else:
            ranking[a] = int(b)
        ranking = defaultdict(int, sorted(ranking.items(), key=operator.itemgetter(1), reverse=True))
        if len(ranking) > K:
            ranking.pop(list(ranking.keys())[-1])
        if list(ranking.keys()) != list(temp.keys()):
            answer += 1
        print(answer, ranking)
    return answer

K = 3
user_scores = ["alex111 100", "cheries2 200", "coco 150", "luna 100", "alex111 120", "coco 300", "cheries2 110"]
# user_scores = ["alex111 100", "cheries2 200", "alex111 200", "cheries2 150", "coco 50", "coco 200"]
# user_scores = ["cheries2 200", "alex111 100", "coco 150", "puyo 120"]
print(solution(K, user_scores))