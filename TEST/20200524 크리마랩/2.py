from collections import defaultdict
def getMostVisited(n, sprints):
    d = defaultdict(int)
    for i in range(len(sprints) - 1):
        if sprints[i] < sprints[i+1]:
            for j in range(sprints[i],sprints[i+1]+1):
                d[j] += 1
        else:
            for j in range(sprints[i+1], sprints[i]+1):
                d[j] += 1
    kl = list(d.keys())
    vl = list(d.values())

    # print(d[kl.index(max(vl))])
    # print(kl)
    # print(vl)
    di = list(d.items())
    di.sort(key=lambda x:(x[1]))
    print(di[-1][0])

    # k = [0] * (n+1)
    # for i in range(len(sprints)-1):
    #     if sprints[i] < sprints[i+1]:
    #         for j in range(sprints[i], sprints[i+1]+1):
    #             k[j] += 1
    #     else:
    #         for j in range(sprints[i+1], sprints[i]+1):
    #             k[j] += 1
    # return k.index(max(k))
'''
9
4
9
7
3
1
'''

if __name__ == '__main__':
    n = int(input().strip())
    sprints_count = int(input().strip())
    sprints = []
    for _ in range(sprints_count):
        sprints_item = int(input().strip())
        sprints.append(sprints_item)

    result = getMostVisited(n, sprints)

