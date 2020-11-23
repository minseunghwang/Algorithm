def balancedSum(arr):
    answer = 0
    index = len(arr) // 2
    tmp1 = sum(arr[:index])
    tmp2 = sum(arr[index + 1:])

    while True:
        print(tmp1, tmp2)
        if tmp1 == tmp2:
            break
        if tmp1 < tmp2:
            tmp2 -= arr[index + 1]
            tmp1 += arr[index + 1]
        else:
            tmp1 -= arr[index + 1]
            tmp2 += arr[index + 1]
        index += 1

    return index


arr = [1,2,3,3]
print(balancedSum(arr))