def minimumAbsoluteDifference(arr):
    arr.sort()
    ms = 1000000
    for i in range(1,len(arr)):
        print('1',i-1, i)
        mn = abs(arr[i-1]-arr[i])
        if mn < ms:
            ms = mn
    return ms



if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    print(minimumAbsoluteDifference(arr))
