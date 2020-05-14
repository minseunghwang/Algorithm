def minimumSwaps(arr):
    answer = 0
    for i in range(len(arr)):
        while arr[i] != i+1:
            temp = arr[i]
            arr[i] = arr[temp-1]
            arr[temp-1] = temp
            answer += 1
    return answer

n = int(input())
arr = list(map(int, input().rstrip().split()))
print(minimumSwaps(arr))