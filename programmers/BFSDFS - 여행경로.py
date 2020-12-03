from collections import defaultdict

from collections import defaultdict
import operator


def solution(tickets):
    answer = ["ICN"]

    d = defaultdict(list)

    for i in range(len(tickets)):
        d[tickets[i][0]].append(tickets[i][1])
    for i in d:
        d[i].sort()
    cnt = len(d)

    while cnt:
        top = answer[-1]
        answer.append(d[top].pop(0))
        if len(d[top]) == 0:
            cnt -= 1


    return answer

# tickets = [['ICN', 'JFK'], ['HND', 'IAD'], ['JFK', 'HND']]
tickets = [['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL','SFO']]

print(solution(tickets))