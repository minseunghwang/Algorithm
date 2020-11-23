def minX(arr):
    tmp = []
    s = 0
    for i in range(len(arr)):
        s += arr[i]
        tmp.append(s)
    print(tmp)
    return min(tmp)

arr = [-5,4,-2,3,1,-1,-6,-1,5]
print(minX(arr))