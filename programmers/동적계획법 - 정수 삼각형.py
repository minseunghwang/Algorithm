def solution(triangle):
    l = len(triangle)
    triangle.append([0]*(l+1))
    for i in range(0,l):
        temp = []
        for cnt,j in enumerate(triangle[i]):
            if len(temp) != 0:
                if temp[-1] < triangle[i+1][cnt] + j:
                    temp.pop()
                    temp.append(triangle[i+1][cnt] + j)
            else:
                temp.append(triangle[i+1][cnt] + j)
            temp.append(triangle[i+1][cnt+1] + j)
        triangle[i+1] = temp

    return max(triangle[l-1])



triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(triangle))