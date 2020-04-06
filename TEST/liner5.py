import operator
def solution(dataSource, tags):
    answer = []
    dict = {}
    for data in dataSource:
        cnt = 0
        for i in data[1:]:
            if i in tags:
                cnt += 1
        if cnt != 0:
            dict[data[0]] = cnt

    sdict = sorted(dict.items(), key = operator.itemgetter(1), reverse=True)
    for i in sdict[:10]:
        answer.append(i[0])
    return answer



dataSource = [
    ["doc1", "t1", "t2", "t3"],
    ["doc2", "t0", "t2", "t3"],
    ["doc3", "t1", "t6", "t7"],
    ["doc4", "t1", "t2", "t4"],
    ["doc5", "t6", "t100", "t8"]
]

tags = ["t1", "t2", "t3"]
print(solution(dataSource, tags))