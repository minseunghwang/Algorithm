from copy import deepcopy
n = int(input())
m = int(input())
q = []
nam = []
for i in range(m):
    a,b = list(map(int,input().split()))
    if a == 1 and b not in q:
        q.append(b)
    elif b == 1 and a not in q:
        q.append(a)
    else:
        nam.append([a,b])

second = deepcopy(q)
for i in nam:
    if i[0] in q and i[1] not in second:
        print(i[0], i[1])
        second.append(i[1])
print(len(second))




