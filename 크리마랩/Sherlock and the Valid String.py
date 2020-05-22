from collections import defaultdict
def isValid(s):
    d = defaultdict(int)

    for i in s:
        d[i] += 1
    print(d)
    dval = list(d.values())
    print(dval)
    sdval = list(set(dval))
    print(sdval)
    mx, mn = max(sdval),min(sdval)


    if len(sdval) > 2:
        return 'NO'
    elif len(sdval) == 2 and abs(sdval[0] - sdval[1]) > 1 and 1 not in sdval:
        return 'NO'

    if (dval.count(mx) > 1 and dval.count(mn) > 1):
        return 'NO'
    return 'YES'

if __name__ == '__main__':
    s = input()

    print(isValid(s))
