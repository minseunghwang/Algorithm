from collections import defaultdict


def solution(v):

    dictx = defaultdict(int)
    dicty = defaultdict(int)
    for i in range(len(v)):
        dictx[v[i][0]] += 1
        dicty[v[i][1]] += 1
    for i in zip(dicty.items(),dictx.items()):
        if i[0][1] == 1:
            y = i[0][0]
        if i[1][1] == 1:
            x = i[1][0]
    return [x,y]




# v = [[1, 4], [3, 4], [3, 10]]
v = [[1, 1], [2, 2], [1, 2]]
print(solution(v))