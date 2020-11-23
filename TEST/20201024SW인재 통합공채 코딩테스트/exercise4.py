def countPerms(n):
    tmp = [1,1,1,1,1]
    for _ in range(n - 1):
        # a = e + i + u
        a = tmp[1] + tmp[2] + tmp[4]
        # e = a + i
        e = tmp[0] + tmp[2]
        # i = a + e + o + u
        i = tmp[1] + tmp[3]
        # o = i
        o = tmp[2]
        # u = i + o
        u = tmp[2] + tmp[3]
        tmp = [a,e,i,o,u]
        print(tmp)
    return sum(tmp)

n = 3
print(countPerms(n))