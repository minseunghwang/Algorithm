def compareTriplets(a, b):
    cnta, cntb = 0,0
    for i,j in zip(a,b):
        if i > j:
            cnta += 1
        elif j > i:
            cntb += 1
    return (cnta,cntb)
