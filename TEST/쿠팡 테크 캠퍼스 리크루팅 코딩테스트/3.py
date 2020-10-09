import collections
def solution(k,score):
    d = collections.defaultdict(list)
    for i in range(1,len(score)):
        n = score[i-1]-score[i]
        d[n].append([i-1,i])
    s = []
    for i in list(d.values()):
        if k <= len(i):
            for j in i:
                s += j

    s = list(set(s))
    for i in s[::-1]:
        score.pop(i)

    return len(score)

k = 3
k = 2
score = [24,22,20,10,5,3,2,1]
score = [1300000000,700000000,668239490,618239490,568239490,568239486,518239486,157658638,157658634,100000000,100]

print(solution(k,score))


