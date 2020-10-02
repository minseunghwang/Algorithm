

m1, m2 = 0, 0
a = [4,2,3,5,1]
for i in range(len(a)):
    print("꺼져",i,m1,m2)
    if a[m1] > a[i]:
        m1 = i
    if a[m2] < a[i]:
        m2 = i
    print(i,m1,m2)
print(a[m1], a[m2])