def appendAndDelete(s, t, k):
    if s == t:
        return 'YES'
    ls = len(s)
    lt = len(t)

    cnt = 0
    for i in range(min(ls,lt)):
        if s[i] == t[i]:
            cnt += 1
        else:
            break

    if k >= (ls - cnt) + (lt - cnt):
        if (ls + lt - 2*cnt) % 2 == 0 or ls + lt == k:
            return 'Yes'
    return 'No'

s = 'abcd'
t = 'abcdert'
k = 10
print(appendAndDelete(s,t,k))