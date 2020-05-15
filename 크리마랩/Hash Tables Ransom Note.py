def checkMagazine(magazine, note):
    di = {}
    for i in magazine:
        if i in di:
            di[i] += 1
        else:
            di[i] = 1
    for j in note:
        if j not in di or di[j] == 0:
            return 'No'
        di[j] -= 1
    return 'Yes'

mn = input().split()
m = int(mn[0])
n = int(mn[1])
magazine = input().rstrip().split()
note = input().rstrip().split()
print(checkMagazine(magazine, note))
'''
7 4
ive got a lovely bunch of coconuts
ive got some coconuts
'''