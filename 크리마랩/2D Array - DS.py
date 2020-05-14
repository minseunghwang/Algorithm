def hourglassSum(arr):
    print(arr)
    maxx = -10000
    for i in range(len(arr)-2):
        for j in range(len(arr)-2):
            maxx = max(maxx,(arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]))

    return maxx

# arr = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0,2,4, 4, 0], [0, 0, 0, 2, 0, 0] ,[0, 0, 1 ,2 ,4,0]]

arr = []
for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))

print(hourglassSum(arr))