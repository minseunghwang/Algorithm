from collections import defaultdict
def solution(votes):
    if len(votes) == 1:
        return 0
    answer = 0
    while True:
        if max(votes) == votes[0] and votes.count(votes[0]) == 1:
            break
        vote = sorted(votes[1:])
        vote[-1] -= 1
        votes[0] += 1
        votes[1:] = vote
        answer += 1
        print(votes)
    return answer

votes = [5,10,7,3,8]
print(solution(votes))
