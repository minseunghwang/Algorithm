def pickingNumbers(a):
    maxx = 0
    for i in range(len(a)):
        cnt1,cnt2 = 0,0
        for j in range(len(a)):
            if (a[i]==a[j] or a[i] == a[j]+1):
                cnt1 += 1
            elif (a[i]==a[j] or a[i] == a[j]-1):
                cnt2 += 1
        maxx = max(cnt1,cnt2,maxx)
    return maxx

# s = [1, 2, 2, 3, 1, 2]
s = [10,10,10,10,10,10]
print(pickingNumbers(s))