import copy
def maxMin(k, arr):
    answer = []
    mn = 1000000
    arr.sort()
    temp = arr[:k]
    for i in range(1,n-k):
        print(temp,mn,answer)
        if temp[-1]-temp[0] < mn:
            print(i)
            mn = temp[-1]-temp[0]
            answer = copy.deepcopy(temp)
        temp.pop(0)
        temp.append(arr[k+i])

    return mn


if __name__ == '__main__':
    n = int(input())
    k = int(input())
    arr = []
    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)
    print(maxMin(k, arr))

