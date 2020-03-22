

arr = [0,1]
def pibo(n,cnt):
    if n == 0 or n == 1:
        return arr[n]
    arr.append(arr[cnt-2] + arr[cnt-1])
    if n != cnt:
        cnt += 1
        pibo(n,cnt)
    return arr[n]

print(pibo(int(input()),2))
