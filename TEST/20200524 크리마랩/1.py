from collections import defaultdict
def numPlayers(k, scores):
    d = defaultdict(int)
    scores.sort(reverse=True)
    now = scores[0]
    rank = 1
    for i in range(len(scores)):
        if now != scores[i]:
            rank += 1
            now = scores[i]
        d[rank] += 1
    answer = 0
    rank = 1
    while k > 0:
        k -= d[rank]
        answer += d[rank]
        rank += 1
    print(answer)
    return answer

'''
2
5
10
10
10
10
10
'''



if __name__ == '__main__':
    k = int(input().strip())
    scores_count = int(input().strip())
    scores = []
    for _ in range(scores_count):
        scores_item = int(input().strip())
        scores.append(scores_item)
    result = numPlayers(k, scores)