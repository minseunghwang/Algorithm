from collections import defaultdict

def solution(tickets):
    answer = []

    table = defaultdict(list)

    for f,t in tickets:
        table[f].append(t)
    print(table)
    print(table['ICN'])
    print(table['SFO'])


    # visit = [0 for _ in tickets]
    #
    # q = []
    # for i in range(len(tickets)-1,-1,-1):
    #     if tickets[i][0] == 'ICN':
    #         q += [tickets[i]]
    #
    # print(q)
    # print(tickets)
    #
    # while q:
    #     print(q,visit)
    #     a,vi = q.pop(0)
    #     for i in range(len(tickets)):
    #         if tickets[i][0] == a[-1] and vi[i] != 1:
    #             visit[i] = 1
    #             q.append([a+[tickets[i][1]],visit])

    return answer

# tickets = [['ICN', 'JFK'], ['HND', 'IAD'], ['JFK', 'HND']]
tickets = [['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL','SFO']]

print(solution(tickets))