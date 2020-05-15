def twoStrings(s1, s2):
    di = {}
    for i in s1:
        if i not in di:
            di[i] = 1
    for i in s2:
        if i in di:
            return 'YES'
    return 'NO'

q = int(input())

for q_itr in range(q):
    s1 = input()

    s2 = input()

    print(twoStrings(s1, s2))
